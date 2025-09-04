# Derin - AI Financial Companion for Recurring Bills

A simple CLI companion that uses AI to detect recurring bills from transaction data and provide personalized financial insights.

## 🚀 Features

### 🔹 1. Bill Detection & Tracking
- **Pattern Recognition**: AI scans transactions for repeated charges (same merchant, similar amount, monthly frequency)
- **Smart Classification**: Automatically labels bills as rent, utilities, phone, insurance, subscriptions, etc.
- **Confidence Scoring**: Shows how confident the AI is in each bill detection

### 🔹 2. AI Coaching Companion
- Conversational Q&A about your bills and spending
- Personalized insights and recommendations
- Behavioral coaching based on payment patterns
- Goal alignment and optimization suggestions

### 🔹 3. Proactive Alerts
- Shows upcoming bill due dates
- Identifies overdue payments
- Provides AI-generated insights about your financial health

## 🛠️ Installation

1. **Clone and setup**:
```bash
git clone <your-repo>
cd derin-financial-coach
pip install -r requirements.txt
```

2. **Configure environment** (optional):
Edit `.env` file with your OpenAI API key for AI insights:
```env
# OpenAI Configuration (optional - for AI insights)
OPENAI_API_KEY=your_openai_api_key

# User Configuration
USER_NAME=Derek
```

## 🤖 Usage

### Quick Start with Demo Data

```bash
# Load sample data to see how it works
python main.py demo

# View detected recurring bills
python main.py bills

# Ask Derin about your finances (requires OpenAI API key)
python main.py ask

# Check upcoming bill alerts
python main.py alerts
```

### Available Commands

```bash
python main.py demo    # Load sample transaction data
python main.py bills   # View detected recurring bills
python main.py ask     # Chat with AI about your bills
python main.py alerts  # Show bill alerts and insights
```

### Example Output

```
Your Recurring Bills:
----------------------------------------------------------------------
Merchant             Amount     Type            Last Paid    Next Due
----------------------------------------------------------------------
Netflix              $15.99     Other           03/15/25     04/15/25
Rent Payment         $1200.00   Other           03/01/25     04/01/25
Electric Company     $92.58     Other           03/10/25     04/10/25
Spotify              $9.99      Other           03/20/25     04/20/25
----------------------------------------------------------------------
Total Monthly Bills: $1318.56
```

### Example AI Conversation

```
Your question: How much do I spend on subscriptions each month?
Derin's Response: You're spending $25.98/month on subscriptions (Netflix $15.99 + Spotify $9.99). 
That's about 2% of your total monthly bills. Consider if you're using both services regularly!

Your question: When is my rent due?
Derin's Response: Your rent of $1,200 is due on the 1st of each month. 
It's your largest recurring expense at 91% of your total monthly bills.
```

## 🏗️ Architecture

- **AI Bill Detection**: Pattern recognition for recurring payments from transaction data
- **OpenAI Integration**: Conversational AI for insights and coaching (optional)
- **Simple CLI Interface**: Clean command-line interface
- **Local Data Storage**: JSON-based storage for bills and user data

## 📊 Data Structure

```json
{
  "bills": [
    {
      "merchant": "Netflix",
      "amount": 15.99,
      "type": "Other",
      "frequency": "monthly",
      "last_paid": "2025-03-15",
      "confidence": 1.0
    }
  ],
  "transactions": [...],
  "user_profile": {
    "name": "Derek",
    "connected_accounts": [],
    "bill_streaks": {},
    "preferences": {
      "alert_days_before": 3,
      "enable_ai_coaching": true
    }
  }
}
```

## 🎯 Hackathon Features

- **Quick Demo**: Get running in seconds with sample data
- **AI-Powered**: Intelligent bill detection and classification
- **Conversational**: Natural language interaction with AI
- **Simple Setup**: No complex configuration required
- **Extensible**: Easy to add real bank integration later

## 🚀 Future Enhancements

See `FUTURE_PLANS.md` for detailed roadmap including:
- Real bank integration via Plaid API
- Advanced AI features and predictive analytics
- Web interface and mobile app
- Enhanced gamification and reporting

## 📝 License

MIT License - feel free to use for your hackathon project!