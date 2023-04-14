from src.agents.base_agent import BaseAgent
from src.llm_api.llm_api import LLMApi

class ReactAgent(BaseAgent):
    def __init__(self, llm: LLMApi, tools: list, max_iterations: int = 5):
        super().__init__(llm)
        self.tools = tools
        self.max_iterations = max_iterations

    def run(self, task: str):
        """Runs the ReAct agent to complete the given task."""
        i = 0
        thought = f"I need to solve {task}."

        while i < self.max_iterations:
            i += 1
            print(f"Iteration: {i}")
            print(f"Thought: {thought}")

            # 1. Determine the next action
            action, action_input = self.plan_next_action(thought)

            print(f"Action: {action}\nAction Input: {action_input}")

            # 2. Execute the action and observe the result
            observation = self.execute_action(action, action_input)

            print(f"Observation: {observation}")

            # 3. Formulate the next thought based on the observation
            thought = self.formulate_next_thought(thought, action, action_input, observation)

        return thought  # Return the final thought as the result

    def plan_next_action(self, thought: str) -> tuple[str, str]:
        """Plans the next action based on the current thought.
        This involves using the LLM to decide which tool to use and what input to provide.
        """

        # Construct the prompt for the LLM
        prompt = f"""I am a ReAct agent. My current thought is:
        {thought}
        I have access to the following tools:
        {[tool.name for tool in self.tools]}
        What is my next action? Respond the tool name and necessary input, separated by a colon. For example: Search:what is the capital of France"""

        # Call the LLM to get the action and input
        response = self.llm.generate_text(prompt)
        action, action_input = response.split(':', 1)  # Split into tool and input
        action = action.strip()
        action_input = action_input.strip()

        return action, action_input

    def execute_action(self, action: str, action_input: str) -> str:
        """Executes the given action with the given input and returns the observation.
        If the action is not found in the available tools, it returns an error message.
        """
        for tool in self.tools:
            if tool.name == action:
                return tool.use(action_input)
        return f"Tool '{action}' not found."

    def formulate_next_thought(self, thought: str, action: str, action_input: str, observation: str) -> str:
        """Formulates the next thought based on the current thought, the action taken, the input provided, and the observation received.
        This involves using the LLM to generate the next thought.
        """

        # Construct the prompt for the LLM
        prompt = f"""I am a ReAct agent. My current thought is:
        {thought}
        I took the following action: {action} with input {action_input}
        The observation was: {observation}
        What is my next thought?"""

        # Call the LLM to get the next thought
        next_thought = self.llm.generate_text(prompt)

        return next_thought