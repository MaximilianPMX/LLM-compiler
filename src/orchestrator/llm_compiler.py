from src.llm_api.llm_api import LLMAPI
from src.agents.base_agent import BaseAgent
from src.chains.base_chain import BaseChain
from src.tools.search_tool import SearchTool
from typing import Dict, List, Optional

class LLMCompiler:
    def __init__(
        self,
        llm_api: LLMAPI,
        agents: Dict[str, BaseAgent],
        chains: Dict[str, BaseChain],
        tools: Dict[str, SearchTool],
        max_iterations: int = 5
    ):
        self.llm_api = llm_api
        self.agents = agents
        self.chains = chains
        self.tools = tools
        self.max_iterations = max_iterations

    def execute(self, question: str) -> str:
        """Executes the LLM orchestration logic."""
        context = {}
        current_input = question
        for i in range(self.max_iterations):
            # 1. Query LLM to determine the next action
            prompt = self._build_prompt(current_input, context)
            action = self.llm_api.generate_response(prompt)

            # 2. Parse the action
            action_type, action_name, action_input = self._parse_action(action)

            # 3. Execute the action
            if action_type == "agent":
                if action_name not in self.agents:
                    return f"Error: Agent '{action_name}' not found."
                agent_response = self.agents[action_name].run(action_input)
                context[f'agent_{action_name}_{i}'] = agent_response #Store response in context
                current_input = agent_response #Consider setting current_input to agent_response
            elif action_type == "chain":
                if action_name not in self.chains:
                    return f"Error: Chain '{action_name}' not found."
                chain_response = self.chains[action_name].run(action_input)
                context[f'chain_{action_name}_{i}'] = chain_response #Store response in context
                current_input = chain_response #Consider setting current_input to chain_response
            elif action_type == "tool":
                if action_name not in self.tools:
                    return f"Error: Tool '{action_name}' not found."
                tool_response = self.tools[action_name].use(action_input)
                context[f'tool_{action_name}_{i}'] = tool_response #Store response in context
                current_input = tool_response #Consider setting current_input to tool_response
            elif action_type == "final_answer":
                return action_input
            else:
                return f"Error: Invalid action type: {action_type}"

        return "Error: Maximum iterations reached."

    def _build_prompt(self, current_input: str, context: Dict) -> str:
        """Builds the prompt for the LLM."""
        prompt = f"You are an intelligent agent that orchestrates other agents, chains and tools to answer the user's question. Here is the question: {current_input}\n"
        prompt += "Available Agents: " + ", ".join(self.agents.keys()) + "\n"
        prompt += "Available Chains: " + ", ".join(self.chains.keys()) + "\n"
        prompt += "Available Tools: " + ", ".join(self.tools.keys()) + "\n"
        prompt += "Previous Context: " + str(context) + "\n"
        prompt += "What do you want to do next? You can use an agent, a chain, a tool, or provide a final answer. Return your answer in the format: <action_type>:<action_name>:<action_input>\n"
        prompt += "Example: agent:ResearcherAgent:Find information about the topic\n" 
        prompt += "If you know the answer, use final_answer:Answer:The final answer\n" 

        return prompt

    def _parse_action(self, action_string: str) -> tuple[str, str, str]:
        """Parses the action string returned by the LLM."""
        try:
            action_type, action_name, action_input = action_string.split(":", 2)
            return action_type.strip(), action_name.strip(), action_input.strip()
        except ValueError:
            return "", "", ""
