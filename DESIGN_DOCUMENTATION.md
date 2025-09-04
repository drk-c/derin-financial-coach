# Design Documentation: Derin Financial Coach

## Project Overview
Derin is a CLI-based AI financial companion that helps users track and analyze their recurring bills using pattern recognition and statistical anomaly detection.

## Core Features
- **Bill Detection**: Automatically identifies recurring bills from transaction data
- **Smart Alerts**: Detects unusual price increases using robust statistical analysis
- **Subscription Analysis**: Identifies and categorizes subscription services
- **Due Date Tracking**: Monitors upcoming bill payments
- **Conversational Interface**: Interactive Q&A about financial health

## Tech Stack
- **Language**: Python 3.x
- **CLI Framework**: Click
- **Data Storage**: Local JSON files (`~/.derin_bills.json`)
- **Date Handling**: `python-dateutil`
- **Statistics**: Built-in `statistics` module for anomaly detection

## Architecture
- **`main.py`**: CLI interface and command definitions
- **`utils.py`**: Core business logic, bill detection, and anomaly analysis
- **`dummy_data.py`**: Sample data for demonstration

## How do we determine a bill?
### Rule based checks
- **Grouped by transaction names**: Bills are identified by matching exact transaction names
- **Payments spaced around 25-35 days apart monthly**: Recurring pattern detection
- **Keyword matching**: Bill type classification using merchant name keywords
- **30% variance**: Allow up to 30% amount variation between payments

## Key Algorithms
- **Bill Detection**: Pattern matching on transaction names and date intervals (25-35 days)
- **Anomaly Detection**: Robust z-score using Median Absolute Deviation (MAD)
- **Bill Classification**: Rule-based categorization using merchant name keywords

## Data Structure
```json
{
  "bills": [
    {
      "merchant": "Electric Bill",
      "amount": 113.50,
      "type": "Utilities",
      "amount_history": [89.99, 95.50, 155.00],
      "anomaly": {"is_anomaly": true, "score": 7.28}
    }
  ],
  "transactions": [...],
  "user_profile": {...}
}
```

## Future Enhancements

### Merchant Normalization with Vector Embeddings
Right now, recurring bill detection groups by the exact transaction name. This can miss the same merchant when banks report it with small variations (e.g., "NETFLIX.COM", "Netflix", "Netflix Subscriptions").

To solve this, I plan to use embeddings: pre-trained AI models that turn text into numerical vectors that capture meaning. By comparing similarity between merchant names in this vector space, we can group together different strings that actually refer to the same company.

### Additional Future Implementations
- **Bank Integration**: Plaid API for real transaction data
- **AI-Powered Insights**: OpenAI integration for personalized financial advice
- **Web Interface**: Modern UI for better user experience
- **Mobile App**: Cross-platform mobile application
- **Advanced Analytics**: Machine learning for spending pattern prediction
- **Bill Negotiation**: Automated price comparison and negotiation suggestions
