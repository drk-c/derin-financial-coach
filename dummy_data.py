#!/usr/bin/env python3
"""
Data management and sample data for Derin Financial Coach
"""

def get_sample_transactions():
    """Get sample transaction data for demo purposes"""
    return [
        {
            'id': 'demo_1',
            'amount': -15.99,
            'date': '2025-01-15',
            'merchant_name': 'Netflix',
            'name': 'Netflix Monthly Subscription',
            'account_id': 'demo_account'
        },
        {
            'id': 'demo_2',
            'amount': -15.99,
            'date': '2025-02-15',
            'merchant_name': 'Netflix',
            'name': 'Netflix Monthly Subscription',
            'account_id': 'demo_account'
        },
        {
            'id': 'demo_3',
            'amount': -15.99,
            'date': '2025-03-15',
            'merchant_name': 'Netflix',
            'name': 'Netflix Monthly Subscription',
            'account_id': 'demo_account'
        },
        {
            'id': 'demo_4',
            'amount': -1200.00,
            'date': '2025-01-01',
            'merchant_name': 'Rent Payment',
            'name': 'Monthly Rent Payment',
            'account_id': 'demo_account'
        },
        {
            'id': 'demo_5',
            'amount': -1200.00,
            'date': '2025-02-01',
            'merchant_name': 'Rent Payment',
            'name': 'Monthly Rent Payment',
            'account_id': 'demo_account'
        },
        {
            'id': 'demo_6',
            'amount': -1200.00,
            'date': '2025-03-01',
            'merchant_name': 'Rent Payment',
            'name': 'Monthly Rent Payment',
            'account_id': 'demo_account'
        },
        {
            'id': 'demo_7',
            'amount': -89.99,
            'date': '2025-01-10',
            'merchant_name': 'Electric Company',
            'name': 'Electric Bill',
            'account_id': 'demo_account'
        },
        {
            'id': 'demo_8',
            'amount': -95.50,
            'date': '2025-02-10',
            'merchant_name': 'Electric Company',
            'name': 'Electric Bill',
            'account_id': 'demo_account'
        },
        {
            'id': 'demo_9',
            'amount': -105.00,
            'date': '2025-03-10',
            'merchant_name': 'Electric Company',
            'name': 'Electric Bill',
            'account_id': 'demo_account'
        },
        {
            'id': 'demo_10',
            'amount': -9.99,
            'date': '2025-01-20',
            'merchant_name': 'Spotify',
            'name': 'Spotify Premium',
            'account_id': 'demo_account'
        },
        {
            'id': 'demo_11',
            'amount': -9.99,
            'date': '2025-02-20',
            'merchant_name': 'Spotify',
            'name': 'Spotify Premium',
            'account_id': 'demo_account'
        },
        {
            'id': 'demo_12',
            'amount': -9.99,
            'date': '2025-03-20',
            'merchant_name': 'Spotify',
            'name': 'Spotify Premium',
            'account_id': 'demo_account'
        }
    ]

def get_default_user_data():
    """Get default user data structure"""
    return {
        "bills": [],
        "transactions": [],
        "user_profile": {
            "name": "Derek",
            "connected_accounts": [],
            "bill_streaks": {},
            "preferences": {
                "alert_days_before": 3,
                "enable_ai_coaching": True
            }
        }
    }
