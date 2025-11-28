from investment_planner.agents.market_research_agent import market_research_agent


def test_market_research(sample_profile):
    result = market_research_agent.run_async(sample_profile)
    assert "market" in result.lower()
