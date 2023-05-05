import os
from dotenv import load_dotenv

class ConfigLoader:
    def __init__(self, env_file=".env"):
        load_dotenv(dotenv_path=env_file)
        self.config = os.environ

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value