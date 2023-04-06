from src.orchestrator.llm_compiler import LLMCompiler
from src.agents.base_agent import BaseAgent
from src.document_stores.simple_document_store import SimpleDocumentStore
from unittest.mock import MagicMock
import pytest

@pytest.fixture
def mock_agent():
    agent = MagicMock(spec=BaseAgent)
    agent.run.return_value = "Mocked Agent Response"
    return agent

@pytest.fixture
def mock_document_store():
    document_store = MagicMock(spec=SimpleDocumentStore)
    document_store.search.return_value = ["Mocked Document"]
    return document_store

def test_llm_compiler_initialization():
    compiler = LLMCompiler(agent_name="Test Agent", document_store_name="Test Store")
    assert compiler.agent_name == "Test Agent"
    assert compiler.document_store_name == "Test Store"


def test_llm_compiler_run(mock_agent, mock_document_store):
    compiler = LLMCompiler(agent=mock_agent, document_store=mock_document_store)
    result = compiler.run("Test Query")
    mock_agent.run.assert_called_once()


