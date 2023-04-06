import pytest
from src.chains.base_chain import BaseChain
from src.llm_api.llm_api import LLMAPI
from unittest.mock import MagicMock

@pytest.fixture
def mock_llm_api():
    llm_api = MagicMock(spec=LLMAPI)
    llm_api.generate_response.return_value = "Mocked LLM response"
    return llm_api


def test_base_chain_initialization():
    chain = BaseChain("Test Chain")
    assert chain.name == "Test Chain"


def test_base_chain_run(mock_llm_api):
    chain = BaseChain("Test Chain", llm_api=mock_llm_api)
    result = chain.run("Test Input")
    mock_llm_api.generate_response.assert_called_once_with("Test Input", context=None)
    assert result == "Mocked LLM response"


def test_qa_chain_initialization():
    from src.chains.qa_chain import QAChain
    chain = QAChain("QA Test Chain")
    assert chain.name == "QA Test Chain"