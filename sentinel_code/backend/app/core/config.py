import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    
    # Provider selection: 'gemini' or 'groq'
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "groq")

    @property
    def MODEL_NAME(self) -> str:
        if self.LLM_PROVIDER == "groq":
            return "llama-3.3-70b-versatile"
        return "gemini-2.0-flash"
    
    def validate(self):
        if self.LLM_PROVIDER == "gemini" and not self.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is not set in environment variables or .env file.")
        if self.LLM_PROVIDER == "groq" and not self.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is not set in environment variables or .env file.")

settings = Settings()
