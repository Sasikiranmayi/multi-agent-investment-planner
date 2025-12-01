import asyncio

from dotenv import load_dotenv

from google.adk.runners import Runner
from google.genai import types

from investment_planner.agent import root_agent
from investment_planner.sessions.session_manager import session_service
from investment_planner.observability.logging_config import logger

load_dotenv()

USER_ID = "default_user"
SESSION_ID = "default_session"
APP_NAME = "investment_planner"

session = session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
)


async def main():

    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    logger.info("🚀 Starting Multi-Agent Investment Planner (Runner mode)")
    logger.info(
        "Type your first message (e.g., 'Hi, I want to plan my investments').")
    replies = []
    user_input = input("You: ")
    user_msg = types.Content(role="user", parts=[types.Part(text=user_input)])
    # Run the agent with the runner
    for event in runner.run(
            user_id=USER_ID,
            session_id=SESSION_ID,
            new_message=user_msg
    ):
        if event.content:
            replies.append(event.content.parts[0].text)
            print("Agent:", event.content.parts[0].text)


if __name__ == "__main__":
    asyncio.run(main())
