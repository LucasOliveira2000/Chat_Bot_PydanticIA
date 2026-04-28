from fastapi import APIRouter
import app
from app.schemas.mensagem_schema import MensagemRequest, MensagemResponse
from app.services.agent_service_google import AgentServiceGoogle

router = APIRouter(
    prefix="/mensagem",
    tags=["mensagem"]
)

agente_construcao = AgentServiceGoogle(
    instructions="Você é um agente especializado em orçamentos de construção civil."
)

agente_juridico = AgentServiceGoogle(
    instructions="Você é um especialista em direito imobiliário."
)

@router.post(
    "/agente-construcao", 
    response_model=MensagemResponse,
    description="Envie uma mensagem para o agente especializado em orçamentos de construção civil."
)
async def enviar_mensagem_construcao(mensagem_request: MensagemRequest) -> MensagemResponse:
    result = await agente_construcao.run(mensagem_request.mensagem)
    return MensagemResponse(resposta=result)


@router.post(
    "/agente-juridico", 
    response_model=MensagemResponse,
    description="Envie uma mensagem para o agente especializado em direito imobiliário."
)
async def enviar_mensagem_juridica(mensagem_request: MensagemRequest) -> MensagemResponse:
    result = await agente_juridico.run(mensagem_request.mensagem)
    return MensagemResponse(resposta=result)