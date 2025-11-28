from investment_planner.agents.risk_profile_agent import risk_profile_agent


def test_risk_agent(sample_profile):
    result = risk_profile_agent.run_async(sample_profile)
    assert "risk profile" in result.lower()
