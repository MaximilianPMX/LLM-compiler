import pytest
from src.agents.base_agent import BaseAgent
from src.chains.base_chain import BaseChain
from unittest.mock import MagicMock

@pytest.fixture
def mock_chain():
    chain = MagicMock(spec=BaseChain)
    chain.run.return_value = "Mocked chain response"
    return chain


def test_base_agent_initialization():
    agent = BaseAgent("Test Agent", [])
    assert agent.name == "Test Agent"
    assert agent.tools == []


def test_base_agent_run(mock_chain):
    agent = BaseAgent("Test Agent", [], chain=mock_chain)
    result = agent.run("Test Input")
    mock_chain.run.assert_called_once_with("Test Input")
    assert result == "Mocked chain response"


def test_react_agent_initialization():
    from src.agents.react_agent import ReactAgent
    agent = ReactAgent("React Test Agent", [])
    assert agent.name == "React Test Agent"
    assert agent.tools == []
