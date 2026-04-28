from pydantic import BaseModel

class MensagemRequest(BaseModel):
    mensagem: str
    
    
class MensagemResponse(BaseModel):
    resposta: str