class BaseAgent:
    """
    Base class for all agents.
    """
    def __init__(self):
        """
        Initializes the BaseAgent.
        """
        pass

    def run(self, task: str) -> str:
        """
        Executes the agent's main logic.

        Args:
            task (str): The task to be executed.

        Returns:
            str: The result of the task execution.
        """
        raise NotImplementedError