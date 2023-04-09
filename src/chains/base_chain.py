class BaseChain:
    """
    Base class for all chains.
    """

    def __init__(self):
        """
        Initializes the BaseChain.
        """
        pass

    def run(self, query: str) -> str:
        """
        Executes the chain's main logic.

        Args:
            query (str): The input query.

        Returns:
            str: The result of the chain execution.
        """
        raise NotImplementedError