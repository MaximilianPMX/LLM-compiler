class Agent:
    def __init__(self, name: str, description: str):
        """
        Base class for all agents.

        Args:
            name (str): The name of the agent.
            description (str): A brief description of the agent's purpose.
        """
        self.name = name
        self.description = description

    def __str__(self):
        return f"Agent(name='{self.name}', description='{self.description}')"