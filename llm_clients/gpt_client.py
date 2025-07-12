import os
from openai import OpenAI
from llm_clients.base import LLMClient

class GPTClient(LLMClient):
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not set in .env")
        self.client = OpenAI(api_key=self.api_key)

    def ask(self, prompt : str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

