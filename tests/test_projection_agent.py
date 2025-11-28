from investment_planner.agents.projection_agent import projection_loop_agent


def test_projection_agent(sample_profile):
    result = projection_loop_agent.run_async(sample_profile)
    assert "projection" in result.lower()
