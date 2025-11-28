from investment_planner.agents.spending_pattern_agent import spending_pattern_agent


def test_spending_pattern(sample_profile):
    result = spending_pattern_agent.run_async(sample_profile)
    assert "📊 Spending Pattern Summary" in result.lower() or "spending" in result.lower()
