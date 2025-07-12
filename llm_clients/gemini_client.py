import os
import google.generativeai as genai
from llm_clients.base import LLMClient

class GeminiClient(LLMClient):
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not set in .env")

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name="gemini-2.5-flash")

    def ask(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text