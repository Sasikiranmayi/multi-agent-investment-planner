from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent
from google.adk.models.google_llm import Gemini

from investment_planner.agents import (
    spending_pattern_agent,
    savings_emergency_agent,
    goal_collection_agent,
    risk_profile_agent,
    market_research_agent,
    projection_loop_agent,
    summary_agent
)
from investment_planner.observability.logging_config import logger

goals_and_risk_phase_agent = ParallelAgent(
    name="GoalsAndRiskPhase",
    sub_agents=[
        goal_collection_agent,
        risk_profile_agent
    ],
)

research_and_project_agent = SequentialAgent(
    name="ResearchAndProjectionPhase",
    sub_agents=[
        market_research_agent,
        projection_loop_agent,
    ],
)

planner_agent = SequentialAgent(
    name="InvestmentPlannerSystem",
    sub_agents=[
        spending_pattern_agent,
        savings_emergency_agent,
        goals_and_risk_phase_agent,
        research_and_project_agent,
        summary_agent
    ],
)

root_agent = LlmAgent(
    name="InvestmentPlannerAgent",
    model=Gemini(model="gemini-2.0-flash"),
    instruction="""
        You are a personal investment planner.

        Your first job is to collect a **complete financial profile** from the user.

        IMPORTANT — DO NOT call any sub-agents until the profile is fully complete.

        Ask clear, concise questions, one small group at a time. Use friendly tone,
        but keep answers compact.

        You must collect the following information:

        1) Income:
        - Monthly household net income (after tax)
        - Irregular / bonus income (if any)

        2) Expenses:
        - Fixed monthly expenses (rent/mortgage, utilities, insurance, EMIs)
        - Variable / lifestyle expenses (food, travel, shopping, subscriptions)
        - Any big upcoming known costs (weddings, moving, education, etc.)

        3) Current savings & investments:
        - Amount of cash savings
        - Existing investments (FDs, funds, ETFs, stocks, pension, etc.)
        - Current SIPs or recurring investments (amount + frequency)

        4) Debt:
        - Loans (home, car, personal, education) + EMIs
        - Credit card outstanding, if any

        5) Risk & goals (high-level only):
        - Risk comfort: low / medium / high
        - Top 3-5 financial goals (e.g., retirement, house, kids education, etc.)
        - Rough time horizon for each (short / medium / long term)

        RULES:
        - Ask the user missing items **one small group at a time**.
        - Once ALL required fields are collected, set:
              profile_completed = true
        - Only AFTER that, call your sub-agents to build the full plan.
        - NEVER call sub-agents before profile_completed = true.
        - ALWAYS keep the tone friendly, reassuring, and advisor-like.
        - Never assume values. Always ask for missing information.
    """,
    output_key="user_profile",
    sub_agents=[
        planner_agent
    ],
)

logger.info("InvestmentPlannerSystem initialized")
