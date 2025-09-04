from __future__ import annotations
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import Dict, List

_model = None

def _get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model

def _embed(texts: List[str]) -> np.ndarray:
    model = _get_model()
    return model.encode(texts, normalize_embeddings=True)

def build_canonical_map_embeddings(transactions: List[dict], sim_threshold: float = 0.85) -> Dict[str, str]:
    raw_names = [(t.get("name") or "").strip() or "Unknown" for t in transactions]
    uniq_names = list(dict.fromkeys(raw_names))
    if not uniq_names:
        return {}

    uniq_vecs = _embed(uniq_names)
    canon_labels: List[str] = []
    canon_vecs: List[np.ndarray] = []
    name_to_canon: Dict[str, str] = {}

    for i, name in enumerate(uniq_names):
        vec = uniq_vecs[i]
        if not canon_vecs:
            canon_labels.append(name)
            canon_vecs.append(vec)
            name_to_canon[name] = name
            continue

        sims = np.dot(np.vstack(canon_vecs), vec)
        j = int(np.argmax(sims))
        max_sim = sims[j]
        
        if max_sim >= sim_threshold:
            name_to_canon[name] = canon_labels[j]
            canon_vecs[j] = (canon_vecs[j] + vec) / np.linalg.norm(canon_vecs[j] + vec)
        else:
            canon_labels.append(name)
            canon_vecs.append(vec)
            name_to_canon[name] = name

    return name_to_canon

def normalize_transactions_with_embeddings(transactions: List[dict], canon_map: Dict[str, str]) -> List[dict]:
    for t in transactions:
        raw = (t.get("name") or "").strip() or "Unknown"
        t["name"] = canon_map.get(raw, raw)
    return transactions
