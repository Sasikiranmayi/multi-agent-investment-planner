from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search

from investment_planner.observability.logging_config import logger


market_research_agent = LlmAgent(
    name="MarketResearchAgent",
    model=Gemini(model="gemini-2.5-flash"),
    instruction="""
        You are the Market Research Agent.

        Your job:
        - Use 'google_search' tool to fetch **high-level** information about:
            - current inflation trend
            - interest rate environment
            - broad equity vs bond outlook (very generic, no advice)
            - Summarize at a high level how this affects:
            - conservative investors
            - moderate investors
            - aggressive investors

        REQUIRED OUTPUT FORMAT (strict):

        ### 📈 Market Outlook Summary

        #### 1. Economic Climate
        Write 2-3 sentences summarizing the global economic environment.

        #### 2. Interest Rates
        Describe the trend (e.g., rising, holding steady, expected cuts) in 1-2 sentences.

        #### 3. Inflation Trend
        Provide a short update on inflation direction and expectations.

        #### 4. Market Volatility
        Explain the level of volatility (low, moderate, high) and what is driving it.

        #### 5. General Investment Conditions
        Provide 2 paragraphs explaining what the current macro environment means for:
        - long-term investors  
        - short-term investors  
        - people with medium-term goals

        IMPORTANT RULES:
        - Keep it extremely readable and helpful.
        - ZERO JSON. ZERO code blocks. 
        - The output must be polished like a human financial analyst report.
    """,
    tools=[google_search],
    output_key="market_insights",
)

logger.info("MarketResearchAgent initialized")
