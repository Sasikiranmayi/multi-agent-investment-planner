import math
from google.adk.tools import FunctionTool
from investment_planner.observability.logging_config import logger

# ------------------------------
# COMPOUND INTEREST
# ------------------------------


def compound_interest(principal: float, rate: float, years: float) -> float:
    logger.debug(
        f"compound_interest(principal={principal}, rate={rate}, years={years})")
    return round(principal * (1 + rate) ** years, 2)


# ------------------------------
# MONTHLY SIP GROWTH
# ------------------------------
def sip_growth(monthly_invest: float, rate: float, years: float) -> float:
    logger.debug(
        f"sip_growth(monthly_invest={monthly_invest}, rate={rate}, years={years})")
    months = years * 12
    monthly_rate = rate / 12
    future_value = monthly_invest * \
        (((1 + monthly_rate) ** months - 1) / monthly_rate)
    return round(future_value, 2)


# ------------------------------
# GOAL PROJECTION
# ------------------------------
def project_goal(target_amount: float, years: float, expected_return: float, inflation: float = 0.05):
    logger.debug(f"project_goal(target_amount={target_amount}, years={years}, "
                 f"expected_return={expected_return}, inflation={inflation})")

    future_cost = target_amount * ((1 + inflation) ** years)
    monthly_sip_needed = future_cost / \
        (((1 + expected_return/12) ** (years*12) - 1) / (expected_return/12))

    return {
        "future_cost": round(future_cost, 2),
        "monthly_sip_required": round(monthly_sip_needed, 2),
    }


# ------------------------------
# EMERGENCY FUND
# ------------------------------
def calculate_emergency_fund(monthly_expenses: float, months: int = 6):
    logger.debug(
        f"calculate_emergency_fund(monthly_expenses={monthly_expenses}, months={months})")
    return round(monthly_expenses * months, 2)


# ------------------------------
# PORTFOLIO ALLOCATION
# ------------------------------
def allocate_portfolio(risk_profile: str, age: int, income: float):
    logger.debug(
        f"allocate_portfolio(risk_profile={risk_profile}, age={age}, income={income})")

    if risk_profile.lower() == "conservative":
        return {"equity": 20, "debt": 60, "gold": 20}

    if risk_profile.lower() == "moderate":
        return {"equity": 50, "debt": 40, "gold": 10}

    if risk_profile.lower() == "aggressive":
        return {"equity": 70, "debt": 20, "gold": 10}

    return {"equity": 40, "debt": 40, "gold": 20}  # fallback


# ------------------------------
# SAVINGS RATE
# ------------------------------
def savings_rate(income: float, expenses: float):
    logger.debug(f"savings_rate(income={income}, expenses={expenses})")

    if income <= 0:
        return 0.0
    return round((income - expenses) / income, 2)


compound_interest_tool = FunctionTool(compound_interest)
sip_growth_tool = FunctionTool(sip_growth)
project_goal_tool = FunctionTool(project_goal)
emergency_fund_tool = FunctionTool(calculate_emergency_fund)
portfolio_tool = FunctionTool(allocate_portfolio)
savings_rate_tool = FunctionTool(savings_rate)
