from investment_planner.agents.summary_agent import summary_agent


def test_summary(sample_profile):
    result = summary_agent.run_async(sample_profile)
    assert "final summary" in result.lower() or "summary" in result.lower()
