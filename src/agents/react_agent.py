from src.agents.base_agent import BaseAgent


class ReactAgent(BaseAgent):
    """
    Agent that uses the ReAct framework for reasoning and acting.
    """
    def __init__(self):
        """
        Initializes the ReactAgent.
        """
        super().__init__()

    def run(self, task: str) -> str:
        """
        Executes the ReAct agent with a given task.

        Args:
            task (str): The task to be executed.

        Returns:
            str: The result of the task execution.
        """
        return f"ReactAgent executing task: {task}"