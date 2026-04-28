from app.core.config import config
from pydantic_ai.providers.google import GoogleProvider
from pydantic_ai.models.google import GoogleModel
from pydantic_ai import Agent


class AgentServiceGoogle:

    def __init__(self, instructions: str):
        provider = GoogleProvider(api_key=config.GEMINI_API_KEY)
        model = GoogleModel(
            config.PYDANTIC_IA_MODEL, 
            provider=provider
        )
        self._agent = Agent(
            model=model, 
            instructions=instructions
        )

    async def run(self, mensagem: str) -> str:
        result = await self._agent.run(mensagem)
        return result.output