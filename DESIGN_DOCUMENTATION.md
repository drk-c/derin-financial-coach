# Derin Financial Coach - Design Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Tech Stack](#tech-stack)
4. [Core Features](#core-features)
5. [Data Flow](#data-flow)
6. [File Structure](#file-structure)
7. [Algorithm Design](#algorithm-design)
8. [User Interface](#user-interface)
9. [Data Storage](#data-storage)
10. [Future Enhancements](#future-enhancements)
11. [Technical Decisions](#technical-decisions)
12. [Performance Considerations](#performance-considerations)

---

## Project Overview

**Derin Financial Coach** is a command-line interface (CLI) application designed to help users track and analyze their recurring bills. The system automatically detects recurring payment patterns from transaction data and provides intelligent insights about spending habits.

### Key Objectives
- Automate recurring bill detection from transaction data
- Provide clear financial insights and alerts
- Offer a simple, user-friendly interface
- Enable proactive bill management

### Target Users
- Individuals seeking better bill management
- Users wanting to understand their spending patterns
- People looking for subscription optimization
- Financial planning enthusiasts

---

## System Architecture

### High-Level Architecture
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Input    │───▶│   CLI Interface │───▶│  Core Engine    │
│   (Commands)    │    │   (main.py)     │    │  (utils.py)     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
                       ┌─────────────────┐    ┌─────────────────┐
                       │  Data Storage   │    │  Sample Data    │
                       │  (JSON Files)   │    │ (dummy_data.py) │
                       └─────────────────┘    └─────────────────┘
```

### Component Interaction
1. **CLI Interface** receives user commands
2. **Core Engine** processes data and applies algorithms
3. **Data Storage** persists user data and bill information
4. **Sample Data** provides demo functionality

---

## Tech Stack

### Core Technologies
- **Python 3.7+** - Primary programming language
- **Click** - CLI framework for command handling
- **JSON** - Data serialization and storage
- **datetime/dateutil** - Date manipulation and calculations

### Dependencies
```
click==8.1.7              # CLI framework
python-dateutil==2.8.2    # Advanced date operations
```

### Development Tools
- **Git** - Version control
- **GitHub** - Repository hosting
- **VS Code/Cursor** - Development environment

---

## Core Features

### 1. Bill Detection Engine
- **Pattern Recognition**: Identifies recurring transactions based on:
  - Transaction name matching
  - Monthly frequency (25-35 day intervals)
  - Amount variance tolerance (up to 30%)
- **Smart Classification**: Categorizes bills into types:
  - Rent/Mortgage
  - Utilities (Electric, Gas, Water, Trash)
  - Internet/Cable
  - Phone/Mobile
  - Insurance
  - Subscriptions
  - Credit Card
  - Loan Payment
  - Other

### 2. Financial Insights
- **Spending Analysis**: Calculates total monthly bills
- **Trend Detection**: Identifies increasing/decreasing bill amounts
- **Subscription Analysis**: Highlights potential savings opportunities
- **Personalized Recommendations**: Provides actionable financial advice

### 3. Alert System
- **Amount Change Alerts**: Flags unusual bill increases
- **Upcoming Bills**: Shows bills due within 7 days
- **Overdue Detection**: Identifies past-due payments
- **Subscription Optimization**: Suggests potential cancellations

### 4. Interactive Interface
- **Command-based Navigation**: Simple CLI commands
- **Question-Answer System**: Natural language interaction
- **Formatted Output**: Clean, readable tables and reports

---

## Data Flow

### 1. Data Input
```
Sample Data → Transaction Processing → Pattern Analysis
```

### 2. Bill Detection Process
```
Transactions → Group by Name → Check Frequency → Validate Amounts → Classify Type → Store Results
```

### 3. User Interaction Flow
```
User Command → Data Retrieval → Processing → Formatted Output → User Response
```

---

## File Structure

```
derin-financial-coach/
├── main.py              # CLI interface and commands
├── utils.py             # Core business logic and algorithms
├── dummy_data.py        # Sample data for testing
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── .gitignore          # Git ignore rules
└── DESIGN_DOCUMENTATION.md  # This document
```

### File Responsibilities
- **main.py**: CLI commands, user interaction, output formatting
- **utils.py**: Bill detection algorithms, data processing, insights generation
- **dummy_data.py**: Sample transactions and default configurations
- **requirements.txt**: Project dependencies and versions

---

## Algorithm Design

### Bill Detection Algorithm
```python
def detect_recurring_bills(transactions):
    1. Group transactions by transaction name
    2. Filter out small amounts (< $5)
    3. For each group:
       a. Check if 2+ transactions exist
       b. Verify monthly frequency (25-35 days apart)
       c. Calculate amount variance (< 30% tolerance)
       d. Classify bill type using rule-based system
       e. Detect amount trends (increasing/decreasing/stable)
       f. Store bill information
```

### Classification Algorithm
```python
def classify_bill_type(merchant, amount):
    1. Convert merchant name to lowercase
    2. Check against keyword lists for each category
    3. Return appropriate category or "Other"
```

### Trend Analysis
```python
def analyze_trends(amounts):
    1. If 3+ transactions exist:
       a. Calculate recent average (last 2 transactions)
       b. Calculate older average (remaining transactions)
       c. Compare averages with 10% threshold
       d. Return trend classification
```

---

## User Interface

### Command Structure
```bash
python main.py <command> [options]
```

### Available Commands
- **demo**: Load sample data for testing
- **bills**: Display detected recurring bills
- **ask**: Interactive Q&A about finances
- **alerts**: Show bill alerts and insights

### Output Formatting
- **Tables**: Formatted columns for bill information
- **Alerts**: Clear warning messages for important events
- **Insights**: Multi-line formatted financial advice
- **Status Indicators**: Clear labels for bill status (OVERDUE, DUE SOON, etc.)

---

## Data Storage

### Storage Format
- **File**: `~/.derin_bills.json`
- **Format**: JSON with structured data
- **Location**: User's home directory

### Data Structure
```json
{
  "bills": [
    {
      "merchant": "Netflix Monthly Subscription",
      "amount": 15.99,
      "frequency": "monthly",
      "type": "Subscription",
      "last_paid": "2025-08-15",
      "transaction_count": 3,
      "amount_trend": "stable",
      "amount_history": [15.99, 15.99, 15.99]
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

---

## Future Enhancements

### Phase 1: Enhanced Data Integration
- **Bank API Integration**: Connect to real bank accounts via Plaid API
- **Transaction Import**: Automatic transaction fetching
- **Multi-Account Support**: Handle multiple bank accounts
- **Real-time Updates**: Live transaction monitoring

### Phase 2: Advanced Analytics
- **Machine Learning**: Improved bill detection using ML models
- **Predictive Analytics**: Forecast future bill amounts
- **Spending Categories**: Advanced expense categorization
- **Budget Tracking**: Set and monitor spending limits

### Phase 3: User Experience
- **Web Interface**: Browser-based dashboard
- **Mobile App**: iOS and Android applications
- **Email Notifications**: Automated bill reminders
- **Calendar Integration**: Bill due date synchronization

### Phase 4: Financial Intelligence
- **AI Chatbot**: Advanced conversational interface
- **Bill Negotiation**: Automated service provider communication
- **Savings Optimization**: AI-powered cost reduction suggestions
- **Investment Tracking**: Portfolio and investment monitoring

### Phase 5: Social Features
- **Family Accounts**: Shared bill management
- **Financial Coaching**: Professional advisor integration
- **Community Features**: User forums and tips sharing
- **Gamification**: Rewards and achievement systems

---

## Technical Decisions

### Why Python?
- **Rapid Development**: Quick prototyping and iteration
- **Rich Libraries**: Extensive ecosystem for data processing
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **CLI Support**: Excellent command-line interface libraries

### Why Click Framework?
- **Simple API**: Easy command definition and handling
- **Built-in Help**: Automatic help generation
- **Type Safety**: Input validation and type conversion
- **Extensibility**: Easy to add new commands

### Why JSON Storage?
- **Human Readable**: Easy to debug and modify
- **No Dependencies**: No database setup required
- **Portable**: Easy to backup and transfer
- **Simple**: Minimal complexity for MVP

### Why Rule-Based Classification?
- **Transparent**: Easy to understand and modify
- **Fast**: No training or model loading required
- **Reliable**: Consistent results
- **Extensible**: Easy to add new categories

---

## Performance Considerations

### Current Performance
- **Small Dataset**: Optimized for personal use (hundreds of transactions)
- **Fast Startup**: Minimal initialization time
- **Memory Efficient**: Low memory footprint
- **Quick Processing**: Sub-second bill detection

### Scalability Limitations
- **File I/O**: JSON file access becomes bottleneck with large datasets
- **Memory Usage**: All data loaded into memory
- **Processing Time**: O(n²) complexity for large transaction sets

### Optimization Strategies
- **Database Migration**: Move to SQLite or PostgreSQL for large datasets
- **Lazy Loading**: Load data on-demand
- **Caching**: Cache frequently accessed data
- **Batch Processing**: Process transactions in chunks
- **Indexing**: Add database indexes for faster queries

---

## Conclusion

Derin Financial Coach represents a solid foundation for personal finance management with a focus on simplicity and usability. The current implementation provides core functionality for bill detection and analysis, while the architecture supports future enhancements and scaling.

The modular design allows for easy extension and modification, making it an excellent starting point for more advanced financial management applications.

---

**Document Version**: 1.0  
**Last Updated**: September 2025  
**Author**: Development Team  
**Repository**: https://github.com/drk-c/derin-financial-coach
