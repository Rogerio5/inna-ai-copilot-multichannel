from data_loader import montar_contexto
from gemini_client import gerar_resposta
from prompts import SYSTEM_PROMPT
from utils import eh_saudacao

# Memória simples da conversa na sessão atual
HISTORICO_CONVERSA = []


def montar_historico():
    if not HISTORICO_CONVERSA:
        return "Nenhuma conversa anterior."

    ultimas_mensagens = HISTORICO_CONVERSA[-10:]

    historico_formatado = ""

    for mensagem in ultimas_mensagens:
        papel = mensagem["role"]
        conteudo = mensagem["content"]
        historico_formatado += f"{papel}: {conteudo}\n"

    return historico_formatado


def pergunta_curta_de_continuacao(pergunta: str) -> bool:
    pergunta_normalizada = pergunta.strip().lower()

    respostas_curtas = [
        "sim",
        "s",
        "quero",
        "sim quero",
        "pode",
        "pode mostrar",
        "me mostre",
        "mostre",
        "gostaria",
        "eu gostaria",
        "quero sim",
        "claro",
        "ok",
        "vamos",
        "continue",
        "pode continuar"
    ]

    return pergunta_normalizada in respostas_curtas


def tratar_erro_gemini(erro):
    texto_erro = str(erro)

    if "429" in texto_erro or "RESOURCE_EXHAUSTED" in texto_erro:
        return (
            "João, o limite gratuito diário da IA foi atingido no momento.\n"
            "Tente novamente mais tarde ou reduza a quantidade de testes.\n"
            "Posso continuar depois com a mesma linha de raciocínio."
        )

    if "503" in texto_erro or "UNAVAILABLE" in texto_erro:
        return (
            "João, o serviço de IA está com alta demanda agora.\n"
            "Tente novamente em alguns instantes.\n"
            "Sua conversa continua salva nesta sessão."
        )

    return f"Erro ao consultar Gemini: {erro}"


def registrar_no_historico(pergunta: str, resposta: str):
    HISTORICO_CONVERSA.append(
        {
            "role": "user",
            "content": pergunta
        }
    )

    HISTORICO_CONVERSA.append(
        {
            "role": "assistant",
            "content": resposta
        }
    )


def perguntar_ao_agente(pergunta: str) -> str:
    if eh_saudacao(pergunta):
        return (
            "Olá! Sou a Inna, sua educadora financeira inteligente. "
            "Como posso ajudar?"
        )

    contexto = montar_contexto()
    historico = montar_historico()
    eh_continuacao = pergunta_curta_de_continuacao(pergunta)

    instrucao_continuacao = ""

    if eh_continuacao:
        instrucao_continuacao = """
ATENÇÃO:
O usuário respondeu com uma continuação curta, como "sim", "quero" ou "pode mostrar".

Nesse caso:
1. Identifique a última pergunta feita pela Inna no histórico recente.
2. Responda diretamente ao que foi oferecido.
3. Não repita a explicação anterior.
4. Não reinicie o assunto.
5. Aprofunde o tema atual usando apenas os dados disponíveis no contexto.
6. Se a última pergunta da Inna foi sobre exemplo, comparação ou explicação, entregue exatamente esse conteúdo.
"""

    prompt_final = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

HISTÓRICO RECENTE DA CONVERSA:
{historico}

PERGUNTA ATUAL DO USUÁRIO:
{pergunta}

{instrucao_continuacao}

INSTRUÇÃO FINAL:
Responda usando somente as informações disponíveis no contexto, no histórico recente e nas regras do sistema.

Se o usuário disser apenas "sim", "quero", "pode mostrar", "me mostre", "gostaria" ou algo semelhante:
- use o histórico recente para entender o assunto;
- responda diretamente ao que foi oferecido;
- não repita a explicação anterior;
- não reinicie a conversa;
- aprofunde o tema atual.

Se o assunto for CDI e o usuário pedir exemplo:
- use produtos da base relacionados ao CDI, como CDB Liquidez Diária ou LCI/LCA;
- não invente taxas além das que já existem no contexto;
- explique de forma curta como o CDI aparece nesses produtos.

Se o assunto for Selic:
- use o Tesouro Selic presente na base;
- não invente taxa atual da Selic;
- explique apenas o que consta no contexto.

Se o assunto for comparação:
- compare apenas características disponíveis na base;
- não conclua qual produto é melhor;
- não faça recomendação de investimento.

Não invente taxas, percentuais, prazos, datas, rentabilidades ou valores que não estejam no contexto.
Evite repetir "Olá" em respostas subsequentes.
Responda de forma curta, educativa e conectada ao assunto atual.
"""

    try:
        resposta = gerar_resposta(prompt_final)

        registrar_no_historico(
            pergunta=pergunta,
            resposta=resposta
        )

        return resposta

    except Exception as erro:
        return tratar_erro_gemini(erro)