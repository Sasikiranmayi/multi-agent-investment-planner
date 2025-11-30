from google.adk.agents import LlmAgent, LoopAgent
from google.adk.models.google_llm import Gemini

from investment_planner.observability.logging_config import logger
from investment_planner.tools.calculators import (
    project_goal_tool,
    sip_growth_tool,
    compound_interest_tool,
)

projection_core_agent = LlmAgent(
    name="ProjectionCoreAgent",
    model=Gemini(model="gemini-2.0-flash"),
    instruction="""
        You are the Projection & Portfolio Agent.

        Inputs available in state:
        - user_profile: {user_profile}
        - spending_analysis: {spending_analysis}
        - savings_plan: {savings_plan}
        - investment_goals: {investment_goals}
        - risk_profile: {risk_profile}
        - market_insights: {market_insights}

        Your tasks:
        1) Propose a simple asset allocation based on risk profile:
        e.g. equity %, debt %, cash %, alternatives (if any).
        2) Call project_goal_tool(target_amount=<>, years=<>, expected_return=<>, inflation=<>)
        3) Call sip_growth_tool(monthly_invest=<>, rate=<>, years=<>)
        4) Call compound_interest_tool(principal=<>, rate=<>, times_compounded=<>, years=<>)
        5) Refine the plan over iterations (you may assume previous iteration
        feedback is in the conversation, but keep each response self-contained).

        REQUIRED OUTPUT FORMAT (strict):

        ### 🔮 Financial Projection Summary

        #### 1. Current Position
        Describe the user's current financial state in 2-3 sentences
        (income, surplus, savings).

        #### 2. Short-Term Projection (1-3 Years)
        Provide a forecast of savings or investment growth based on the surplus
        and market_insights (1-2 paragraphs).

        #### 3. Medium-Term Projection (3-10 Years)
        Explain growth patterns, compounding, and expected ranges.
        Reference interest-rate and inflation notes from market_insights.

        #### 4. Long-Term Projection (10+ Years)
        Give a long-term wealth outlook, assuming consistent saving/investing habits.
        Include 1-2 scenarios:
        - stable economic climate  
        - mildly volatile climate  

        #### 5. Key Risks & Considerations
        A simple bullet list of 4-6 items, plain text only.

        IMPORTANT:
        - The tone should feel like a financial advisor.
        - NEVER mention formulas or calculations.
        - Make it realistic, not overly optimistic.
    """,
    tools=[project_goal_tool, sip_growth_tool, compound_interest_tool],
    output_key="investment_projection",
)

projection_loop_agent = LoopAgent(
    name="ProjectionLoopAgent",
    description=(
        "Runs the ProjectionCoreAgent up to 3 times to refine the "
        "investment projection and asset allocation."
    ),
    sub_agents=[projection_core_agent],
    max_iterations=3,
)

logger.info("ProjectionLoopAgent initialized")
