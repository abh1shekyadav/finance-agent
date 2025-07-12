from abc import ABC, abstractmethod

class LLMClient(ABC):
    @abstractmethod
    def ask(self, prompt: str) -> str:
        """Send prompt to llm and get response."""
        pass