import json
import os

class ConfigLoader:
    def __init__(self, config_dir='src/config'):
        self.dir = config_dir
        self.orchestrator_config = self._load_config('orchestrator_config.json')
        self.tools_config = self._load_config('tools_config.json')
        self.llm_config = self._load_config('llm_config.json')

    def _load_config(self, filename):
        filepath = os.path.join(self.dir, filename)
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Configuration file not found: {filename}")
            return {}
        except json.JSONDecodeError:
            print(f"Error decoding JSON in file: {filename}")
            return {}

    def get_orchestrator_config(self):
        return self.orchestrator_config

    def get_tools_config(self):
        return self.tools_config

    def get_llm_config(self):
        return self.llm_config


if __name__ == '__main__':
    # Example usage:
    config_loader = ConfigLoader()
    orchestrator = config_loader.get_orchestrator_config()
    tools = config_loader.get_tools_config()
    llm = config_loader.get_llm_config()

    print("Orchestrator Config:", orchestrator)
    print("Tools Config:", tools)
    print("LLM Config:", llm)
