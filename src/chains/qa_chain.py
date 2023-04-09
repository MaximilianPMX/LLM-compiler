from src.chains.base_chain import BaseChain


class QAChain(BaseChain):
    """
    Chain for Question Answering tasks.
    """

    def __init__(self):
        """
        Initializes the QAChain.
        """
        super().__init__()

    def run(self, query: str) -> str:
        """
        Executes the QA chain with a given query.

        Args:
            query (str): The input query.

        Returns:
            str: The answer to the query.
        """
        return f"Answering question: {query}"