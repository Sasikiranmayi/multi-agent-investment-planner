from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from investment_planner.observability.logging_config import logger


summary_agent = LlmAgent(
    name="SummaryAgent",
    model=Gemini(model="gemini-2.0-flash"),
    instruction="""
        You are the Summary Agent.

        You receive all prior state keys:
        - user_profile: {user_profile}
        - spending_analysis: {spending_analysis}
        - savings_plan: {savings_plan}
        - investment_goals: {investment_goals}
        - risk_profile: {risk_profile}
        - market_insights: {market_insights}
        - investment_projection: {investment_projection}

        Your job is to give the user a **human-friendly** but concise summary:

        Sections:
        1) Snapshot of their situation (income, surplus, risk level)
        2) Suggested savings & emergency fund plan
        3) High-level investment / asset allocation summary
        4) Goal-wise recommendation (1-2 lines per goal)
        5) 3-5 next action steps for the next 30 days

        You may use Markdown here for readability (headings, bullet points).
    """,
    output_key="final_recommendation",
)

logger.info("SummaryAgent initialized")
