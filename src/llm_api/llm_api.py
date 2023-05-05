import os
import openai
from src.config.config_loader import ConfigLoader

class LLMApi:
    def __init__(self, config: ConfigLoader):
        self.api_key = config.get('OPENAI_API_KEY')
        openai.api_key = self.api_key

    def generate_text(self, prompt, model="gpt-3.5-turbo", max_tokens=150):
        try:
            completion = openai.Completion.create(
                engine=model,
                prompt=prompt,
                max_tokens=max_tokens,
                n=1,
                stop=None,
                temperature=0.7,
            )
            message = completion.choices[0].text
            return message
        except Exception as e:
            print(f"Error during LLM API call: {e}")
            return None

    def generate_text_chat(self, messages, model="gpt-3.5-turbo", max_tokens=150):
        try:
            completion = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens
            )
            return completion.choices[0].message.content
        except Exception as e:
            print(f"Error during LLM API call: {e}")
            return None