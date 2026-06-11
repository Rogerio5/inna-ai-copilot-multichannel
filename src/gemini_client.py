from google import genai

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    INNA_MOCK_MODE
)


def gerar_resposta_mock(prompt: str) -> str:
    return (
        "João, esta é uma resposta simulada da Inna para testar a integração "
        "com FastAPI, n8n e o fluxo conversacional. "
        "O modo de teste está ativo e nenhuma chamada ao Gemini foi realizada."
    )


def gerar_resposta(prompt: str) -> str:
    if INNA_MOCK_MODE:
        return gerar_resposta_mock(prompt)

    if not GEMINI_API_KEY:
        return (
            "A chave da API Gemini não foi encontrada. "
            "Verifique a variável GEMINI_API_KEY no arquivo .env."
        )

    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    if not response or not response.text:
        return (
            "Não consegui gerar uma resposta no momento. "
            "Tente novamente em alguns instantes."
        )

    return response.text