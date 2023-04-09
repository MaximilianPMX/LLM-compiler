import json
import os


class ConfigLoader:
    """
    A class for loading configurations from JSON files.
    """

    def __init__(self):
        """
        Initializes the ConfigLoader.
        """
        pass

    def load_config(self, config_path: str) -> dict:
        """
        Loads a configuration from a JSON file.

        Args:
            config_path (str): The path to the configuration file.

        Returns:
            dict: The configuration loaded from the file, or an empty dictionary if loading fails.
        """
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
            return config
        except FileNotFoundError:
            print(f"Error: Config file not found at {config_path}")
            return {}
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {config_path}")
            return {}