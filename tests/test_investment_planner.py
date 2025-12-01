import pathlib
import pytest

from dotenv import load_dotenv
from google.adk.evaluation.agent_evaluator import AgentEvaluator


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.mark.asyncio
async def test_agent():
    eval_path = (
        pathlib.Path(__file__).parent.parent
        / "tests/integration/evaluation/"
    )

    assert eval_path.exists()
    await AgentEvaluator.evaluate(
        agent_module="investment_planner.agent",
        eval_dataset_file_path_or_dir=str(eval_path),
        num_runs=1
    )
