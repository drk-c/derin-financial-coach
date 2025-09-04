#!/usr/bin/env python3
"""
Derin - AI Financial Companion for Recurring Bills
"""

import click
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Import utility functions
from utils import load_data, save_data, detect_recurring_bills, get_insight
from dummy_data import get_sample_transactions

@click.group()
def cli():
    """Derin - AI Financial Companion for Recurring Bills"""
    pass

@cli.command()
def bills():
    """Show all detected recurring bills"""
    data = load_data()
    bills = data.get('bills', [])
    
    if not bills:
        print("No recurring bills detected yet. Run 'python main.py demo' to load sample data.")
        return
    
    print("\nYour Recurring Bills:")
    print("-" * 90)
    print(f"{'Merchant':<35} {'Amount':<12} {'Type':<15} {'Last Paid':<12} {'Next Due':<12}")
    print("-" * 90)
    
    for bill in bills:
        last_paid = datetime.fromisoformat(bill['last_paid']).strftime('%m/%d/%y')
        next_due = (datetime.fromisoformat(bill['last_paid']) + relativedelta(months=1)).strftime('%m/%d/%y')
        
        # Shorten long names
        merchant_name = bill['merchant'][:32] + "..." if len(bill['merchant']) > 35 else bill['merchant']
        
        print(f"{merchant_name:<35} ${bill['amount']:<11.2f} {bill['type']:<15} {last_paid:<12} {next_due:<12}")
    
    # Show total
    total = sum(bill['amount'] for bill in bills)
    print("-" * 90)
    print(f"Total Monthly Bills: ${total:.2f}")

@cli.command()
def ask():
    """Ask Derin about your bills and financial health"""
    data = load_data()
    
    if not data.get('bills'):
        print("No bills detected yet. Run 'python main.py demo' first.")
        return
    
    print("Ask Derin anything about your bills!")
    
    while True:
        question = click.prompt("\nYour question (or 'quit' to exit)")
        if question.lower() in ['quit', 'exit', 'q']:
            break
        
        if question:
            insight = get_insight(data, question)
            print(f"\nDerin's Response: {insight}")

@cli.command()
def alerts():
    """Show smart alerts and subscription insights"""
    data = load_data()
    bills = data.get('bills', [])
    
    if not bills:
        print("No bills to show alerts for.")
        return
    
    print("Smart Alerts & Subscription Insights")
    print("-" * 50)
    
    # Check for amount changes
    print("\nAmount Change Alerts:")
    for bill in bills:
        if bill.get('amount_trend') == 'increasing':
            recent_amount = bill['amount_history'][-1] if bill['amount_history'] else bill['amount']
            avg_amount = sum(bill['amount_history'][:-1]) / len(bill['amount_history'][:-1]) if len(bill['amount_history']) > 1 else bill['amount']
            increase = recent_amount - avg_amount
            print(f"WARNING: {bill['merchant']}: Usually ${avg_amount:.2f}, but last payment was ${recent_amount:.2f} (+${increase:.2f})")
    
    # Check for upcoming bills
    print("\nUpcoming Bills:")
    today = datetime.now()
    alerts = []
    
    for bill in bills:
        last_paid = datetime.fromisoformat(bill['last_paid'])
        next_due = last_paid + relativedelta(months=1)
        days_until_due = (next_due - today).days
        
        if days_until_due <= 7:  # Due within a week
            alerts.append({
                'bill': bill,
                'days_until_due': days_until_due,
                'next_due': next_due
            })
    
    if alerts:
        for alert in alerts:
            bill = alert['bill']
            days = alert['days_until_due']
            
            if days <= 0:
                status = "OVERDUE"
            elif days <= 3:
                status = "DUE SOON"
            else:
                status = "UPCOMING"
            
            print(f"BILL: {bill['merchant']} - ${bill['amount']:.2f} - {status} ({days} days)")
    
    # Subscription & Gray Charge Detection
    print("\nSubscription & Gray Charge Analysis:")
    subscriptions = [bill for bill in bills if bill['type'] in ['Subscription', 'Other'] and bill['amount'] < 50]
    
    if subscriptions:
        total_subscriptions = sum(bill['amount'] for bill in subscriptions)
        print(f"Found {len(subscriptions)} potential subscriptions totaling ${total_subscriptions:.2f}/month:")
        
        for sub in subscriptions:
            print(f"  - {sub['merchant']}: ${sub['amount']:.2f}/month")
        
        print(f"\nTIP: Consider reviewing these services - you could save ${total_subscriptions:.2f}/month if you cancel unused ones!")
    
    # Get insights
    if bills:
        insight = get_insight(data, "Show smart alerts about bill changes and subscription optimization")
        print(f"\nDerin's Insights: {insight}")

@cli.command()
def demo():
    """Load demo data to showcase the AI companion features"""
    print("Loading Demo Data")
    
    # Get sample transactions from data module
    sample_transactions = get_sample_transactions()
    
    # Load data and add sample transactions
    data = load_data()
    data['transactions'] = sample_transactions
    
    # Detect recurring bills
    print("AI is analyzing your transactions for recurring bills...")
    detected_bills = detect_recurring_bills(data['transactions'])
    data['bills'] = detected_bills
    
    save_data(data)
    
    print(f"Loaded {len(sample_transactions)} sample transactions!")
    print(f"Found {len(detected_bills)} recurring bills!")
    
    # Show detected bills
    if detected_bills:
        print("\nDetected Recurring Bills:")
        print("-" * 60)
        print(f"{'Merchant':<35} {'Amount':<12} {'Type':<15}")
        print("-" * 60)
        for bill in detected_bills:
            # Truncate long merchant names to fit in column
            merchant_name = bill['merchant'][:32] + "..." if len(bill['merchant']) > 35 else bill['merchant']
            print(f"{merchant_name:<35} ${bill['amount']:<11.2f} {bill['type']:<15}")
    
    print("\nDemo data loaded! Try these commands:")
    print("  • python main.py bills - View your bills")
    print("  • python main.py ask - Chat with Derin")
    print("  • python main.py alerts - See bill alerts")

if __name__ == "__main__":
    cli()