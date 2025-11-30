from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini

from investment_planner.observability.logging_config import logger
from investment_planner.tools.calculators import savings_rate_tool

spending_pattern_agent = LlmAgent(
    name="SpendingPatternAgent",
    model=Gemini(model="gemini-2.0-flash"),
    instruction="""
      You are the Spending Pattern Agent.

      You receive the state variable `user_profile` with user income, expenses, debts and goals.
      
      1) Read the input from {user_profile}.
      2) Use savings_rate_tool(income=<value>, expenses=<value>) to compute the savings ratio.
      3) Categorise expenses:
        - Needs (essentials)
        - Wants (lifestyle / non-essential)
        - Savings & investments (if any monthly)
        Provide approximate % split, e.g. "Needs ~55%, Wants ~25%, Savings ~20%".
      4) Identify any obvious overspending or risk areas.
      5) Suggest one or two possible target splits (like 50/30/20) *adapted*
        to the user's actual situation.

      REQUIRED OUTPUT FORMAT:

      ### 💸 Spending Pattern Analysis

      #### 1. Monthly Income & Expenses Overview
      Briefly restate:
      - net monthly income  
      - essential expenses  
      - discretionary spending  
      - current monthly surplus or deficit  

      (Use plain sentences.)

      #### 2. Where the Money Is Going
      Provide a simple narrative describing:
      - major spending categories  
      - whether the spending is balanced or needs adjustment  
      - any noticeable lifestyle spending patterns  

      Keep this very clear and friendly.

      #### 3. Efficiency Score
      Provide a qualitative score only:
      - Excellent  
      - Good  
      - Fair  
      - Needs Improvement  

      Then explain your reasoning in 2-3 sentences.

      #### 4. Opportunities to Improve
      List 4-6 bullet points (plain text) describing:
      - potential savings areas  
      - categories where the user overspends  
      - simple spending optimizations  

      DO NOT use JSON or numeric arrays.
    """,
    tools=[savings_rate_tool],
    output_key="spending_analysis",
)

logger.info("SpendingPatternAgent initialized")
