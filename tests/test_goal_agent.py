from investment_planner.agents.goal_collection_agent import goal_collection_agent


def test_goal_agent(sample_profile):
    output = goal_collection_agent.run_async(sample_profile)
    assert "short-term goal" in output.lower()
