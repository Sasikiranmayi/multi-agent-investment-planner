import asyncio
import os

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService

from investment_planner.agent import root_agent
from investment_planner.sessions.session_manager import session_service
from investment_planner.observability.logging_config import logger

load_dotenv()


async def main():

    runner = Runner(
        agent=root_agent,
        session_service=session_service,
    )

    logger.info("🚀 Starting Multi-Agent Investment Planner (Runner mode)")
    logger.info(
        "Type your first message (e.g., 'Hi, I want to plan my investments').")

    # run_debug opens an interactive REPL in the terminal
    await runner.run_debug()


if __name__ == "__main__":
    asyncio.run(main())
