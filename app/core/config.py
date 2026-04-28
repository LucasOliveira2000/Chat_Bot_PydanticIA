from pydantic_settings import BaseSettings

class Config(BaseSettings):
    """Application configuration."""

    APP_NAME: str = "Chat Bot IA"
    APP_ENV: str = "local"
    GEMINI_API_KEY: str = ""
    PYDANTIC_IA_MODEL: str = "gemini-2.5-flash-lite"

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }
    
    
config = Config()