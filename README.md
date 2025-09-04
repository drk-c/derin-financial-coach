# Meet Derin, an AI Financial Coach

A simple CLI tool that detects recurring bills from transaction data and provides financial insights.

## Features

- **Bill Detection**: Automatically identifies recurring bills from transaction patterns
- **Bill Classification**: Categorizes bills as rent, utilities, subscriptions, etc.
- **Smart Alerts**: Shows upcoming bills and amount changes
- **Financial Insights**: Provides basic analysis of your spending patterns

## Installation

1. Clone the repository:
```bash
git clone https://github.com/drk-c/derin-financial-coach.git
cd derin-financial-coach
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Quick Start

```bash
# Load sample data to see how it works
python main.py demo

# View detected recurring bills
python main.py bills

# Get insight from Derin
python main.py ask

# Check bill alerts and insights
python main.py alerts
```

### Available Commands

- `python main.py demo` - Load sample transaction data
- `python main.py bills` - View detected recurring bills
- `python main.py ask` - Get insight from Derin
- `python main.py alerts` - Show bill alerts and insights

### Example Output

```
Your Recurring Bills:
------------------------------------------------------------------------------------------
Merchant                            Amount       Type            Last Paid    Next Due
------------------------------------------------------------------------------------------
Netflix Monthly Subscription        $15.99       Subscription    08/15/25     09/15/25
Monthly Rent Payment                $1200.00     Rent/Mortgage   08/01/25     09/01/25
Electric Bill                       $96.83       Utilities       08/10/25     09/10/25
Spotify Premium                     $9.99        Subscription    08/20/25     09/20/25
------------------------------------------------------------------------------------------
Total Monthly Bills: $1322.81
```

## How It Works

1. **Pattern Recognition**: Analyzes transaction data to find recurring payments
2. **Bill Classification**: Uses simple rules to categorize bills by type
3. **Trend Analysis**: Detects increasing or decreasing bill amounts
4. **Alert System**: Identifies upcoming bills and unusual changes

## Project Structure

- `main.py` - CLI interface and commands
- `utils.py` - Core business logic and algorithms
- `dummy_data.py` - Sample data for testing
- `requirements.txt` - Python dependencies

## Data Storage

All data is stored locally in `~/.derin_bills.json` including:
- Detected recurring bills
- Transaction history
- User preferences

## Requirements

- Python 3.7+
- click
- python-dateutil

## Deliverables

- **Video Presentation**: (https://www.youtube.com/your-demo-link)
- **Design Documentation**: (https://docs.google.com/document/d/1aREIXDmk6iFUWbsFzlbiXnPFn_ROIHCmHs7-f5GLrIA/edit?usp=sharing)
