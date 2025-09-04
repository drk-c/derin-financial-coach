#!/usr/bin/env python3
"""
Utility functions
"""

import os
import json
from datetime import datetime
from collections import defaultdict
from dateutil.relativedelta import relativedelta
from statistics import median

# User configuration
USER_NAME = "Derek"

# Data file path
DATA_FILE = os.path.expanduser("~/.derin_bills.json")

# --- Robust anomaly check on amount history (MAD z-score) ---
def robust_anomaly_flag(amounts, z_thresh=3.5):
    """
    Returns (is_anomaly, score) for the LAST value in amounts using a robust z-score.
    Works with short histories (>=3) and is resistant to outliers.
    """
    if not amounts or len(amounts) < 3:
        return False, 0.0

    x = [float(amount) for amount in amounts]
    med = median(x)
    abs_dev = [abs(v - med) for v in x]
    mad = median(abs_dev) or 1e-6  # avoid divide-by-zero
    z_scores = [(0.6745 * (v - med) / mad) for v in x]
    last_z = z_scores[-1]
    return (abs(last_z) > z_thresh), float(last_z)

def load_data():
    """Load user data from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    
    from dummy_data import get_default_user_data
    return get_default_user_data()

def save_data(data):
    """Save user data to JSON file"""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def detect_recurring_bills(transactions):
    """AI-powered detection of recurring bills from transactions"""
    if not transactions:
        return []
    
    # Group transactions by transaction name
    transaction_groups = defaultdict(list)
    
    for transaction in transactions:
        # Use the full transaction name for grouping
        transaction_name = transaction.get('name', 'Unknown')
        amount = abs(float(transaction.get('amount', 0)))
        
        # Skip very small amounts (likely not bills)
        if amount < 5:
            continue
            
        transaction_groups[transaction_name].append({
            'amount': amount,
            'date': transaction.get('date'),
            'transaction': transaction
        })
    
    recurring_bills = []
    
    for transaction_name, transactions_list in transaction_groups.items():
        if len(transactions_list) < 2:
            continue
        
        # Sort by date
        transactions_list.sort(key=lambda x: x['date'])
        
        # Check for recurring date pattern
        dates = [datetime.fromisoformat(t['date']) for t in transactions_list]
        amounts = [t['amount'] for t in transactions_list]
        
        # Check if dates are about a month apart
        is_monthly = True
        if len(dates) >= 2:
            for i in range(1, len(dates)):
                days_diff = (dates[i] - dates[i-1]).days
                # 25-35 days between payments
                if not (25 <= days_diff <= 35):
                    is_monthly = False
                    break
        
        if is_monthly:
            # Calculate amount variance
            amount_variance = max(amounts) - min(amounts) if amounts else 0
            avg_amount = sum(amounts) / len(amounts)
            
            # More lenient variance check since we're using name matching
            if amount_variance / avg_amount < 0.8:  # Allow up to 80% variance
                # Bill type
                bill_type = classify_bill_type(transaction_name, avg_amount)
                
                # Calculate amount trend
                amount_trend = "stable"
                if len(amounts) >= 3:
                    recent_avg = sum(amounts[-2:]) / 2
                    older_avg = sum(amounts[:-2]) / len(amounts[:-2])
                    if recent_avg > older_avg * 1.1:  # 10% increase
                        amount_trend = "increasing"
                    elif recent_avg < older_avg * 0.9:  # 10% decrease
                        amount_trend = "decreasing"
                
                is_anom, anom_score = robust_anomaly_flag(amounts)
                
                recurring_bills.append({
                    'merchant': transaction_name,
                    'amount': avg_amount,
                    'frequency': 'monthly',
                    'type': bill_type,
                    'last_paid': max(t['date'] for t in transactions_list),
                    'transaction_count': len(transactions_list),
                    'amount_trend': amount_trend,
                    'amount_history': amounts,
                    'anomaly': {
                        'is_anomaly': is_anom,
                        'score': anom_score
                    }
                })
    
    return recurring_bills

def classify_bill_type(merchant, amount):
    """Classify bill type based on merchant and amount"""
    # Simple rule-based classification
    merchant_lower = merchant.lower()
    
    if any(word in merchant_lower for word in ['rent', 'apartment', 'housing']):
        return "Rent/Mortgage"
    elif any(word in merchant_lower for word in ['electric', 'gas', 'water', 'trash', 'disposal','utility']):
        return "Utilities"
    elif any(word in merchant_lower for word in ['internet', 'cable', 'wifi', 'ethernet']):
        return "Internet/Cable"
    elif any(word in merchant_lower for word in ['phone', 'mobile', 'cellular']):
        return "Phone/Mobile"
    elif any(word in merchant_lower for word in ['insurance', 'auto', 'health']):
        return "Insurance"
    elif any(word in merchant_lower for word in ['netflix', 'spotify', 'subscription', 'streaming']):
        return "Subscription"
    elif any(word in merchant_lower for word in ['credit', 'card', 'payment']):
        return "Credit Card"
    elif any(word in merchant_lower for word in ['loan', 'mortgage']):
        return "Loan Payment"
    else:
        return "Other"

def get_insight(user_data, context=""):
    """Get basic insights about bills and financial health"""
    bills = user_data.get('bills', [])
    transactions = user_data.get('transactions', [])
    
    total_monthly_bills = sum(bill['amount'] for bill in bills)
    bill_count = len(bills)
    
    insights = []
    insights.append(f"Hi {USER_NAME}! You have {bill_count} recurring bills totaling ${total_monthly_bills:.2f}/month.")
    
    if bills:
        # Highest bill
        highest_bill = max(bills, key=lambda x: x['amount'])
        insights.append(f"Your highest bill is {highest_bill['merchant']} at ${highest_bill['amount']:.2f}.")
        
        # Find subscriptions
        subscriptions = [bill for bill in bills if bill['amount'] < 50]
        if subscriptions:
            subscription_total = sum(sub['amount'] for sub in subscriptions)
            insights.append(f"You're spending ${subscription_total:.2f}/month on subscriptions. Consider reviewing these services.")
        
        # Check for unusual price increases (anomalies)
        anomaly_bills = [bill for bill in bills if bill.get('anomaly', {}).get('is_anomaly')]
        if anomaly_bills:
            for bill in anomaly_bills:
                insights.append(f"{bill['merchant']} has increased unusually. Please review the alerts for details.")
    
    insights.append("Tip: Set up autopay for consistent bills to avoid late fees!")
    
    return "\n".join(insights)
