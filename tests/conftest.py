import pytest


@pytest.fixture
def sample_profile():
    return {
        "income": {
            "monthly_net": 5000,
            "bonus": 2000,
        },
        "expenses": {
            "fixed": 2800,
            "variable": 1200,
            "upcoming": 500,
        },
        "savings": {
            "cash": 700,
            "investments": [],
            "sip": 0,
        },
        "debt": {
            "home_loan": 0,
            "car_loan": 0,
            "personal_loan": 0,
            "credit_card": 0
        },
        "risk": "medium",
        "goals": [
            {"name": "House", "horizon": "long_term"},
            {"name": "Emergency Fund", "horizon": "short_term"},
        ]
    }
