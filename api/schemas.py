from pydantic import BaseModel


class PerguntaRequest(BaseModel):
    pergunta: str
    usuario: str | None = "usuario_desconhecido"
    usuario_id: str | int | None = None
    canal: str | None = "api"


class PerguntaResponse(BaseModel):
    resposta: str
    canal: str
    status: str
