# src/config/config_loader.py

import json

class ConfigLoader:
    def __init__(self, config_file):
        self.config_file = config_file

    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
            return config
        except FileNotFoundError:
            print(f"Error: Configuration file not found: {self.config_file}")
            return None