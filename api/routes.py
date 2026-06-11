import sys
import time
from pathlib import Path

from fastapi import APIRouter

from api.schemas import PerguntaRequest, PerguntaResponse

BASE_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = BASE_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

from agente import perguntar_ao_agente
from logger_interacoes import salvar_interacao

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "online",
        "service": "Inna API",
        "agente": "Inna",
        "descricao": "Educadora Financeira Inteligente"
    }


@router.post("/ask", response_model=PerguntaResponse)
def perguntar(request: PerguntaRequest):
    inicio = time.time()

    canal = request.canal or "api"
    usuario = getattr(request, "usuario", None) or "usuario_desconhecido"
    usuario_id = getattr(request, "usuario_id", None)
    pergunta_usuario = request.pergunta

    try:
        resposta = perguntar_ao_agente(pergunta_usuario)
        status = "success"

    except Exception as erro:
        resposta = (
            "Ocorreu um erro ao processar sua pergunta. "
            f"Detalhes técnicos: {erro}"
        )
        status = "error"

    tempo_resposta = time.time() - inicio

    salvar_interacao(
        canal=canal,
        usuario_id=usuario_id,
        usuario=usuario,
        pergunta=pergunta_usuario,
        resposta=resposta,
        status=status,
        tempo_resposta_segundos=tempo_resposta
    )

    return PerguntaResponse(
        resposta=resposta,
        canal=canal,
        status=status
    )