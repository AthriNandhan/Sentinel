import google.generativeai as genai
from app.core.config import settings

class LLMService:
    def __init__(self):
        settings.validate()
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(settings.MODEL_NAME)

    def generate_text(self, prompt: str) -> str:
        """
        Generates text using the configured LLM.
        """
        try:
            response = self.model.generate_content(prompt)
            if not response.text:
                 raise ValueError("Empty response from LLM")
            return response.text
        except Exception as e:
            print(f"Error generating text: {e}")
            raise e

llm_service = LLMService()
