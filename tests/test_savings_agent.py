from investment_planner.agents.savings_agent import savings_emergency_agent


def test_savings_agent(sample_profile):
    output = savings_emergency_agent.run_async(sample_profile)
    assert "emergency" in output.lower()
    assert "recommended" in output.lower()
