import csv
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
LOG_FILE = DATA_DIR / "interacoes_inna.csv"


CAMPOS = [
    "data_hora",
    "canal",
    "usuario_id",
    "usuario",
    "assistente",
    "pergunta",
    "resposta",
    "status",
    "tempo_resposta_segundos"
]


def garantir_arquivo_log():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not LOG_FILE.exists():
        with open(LOG_FILE, mode="w", newline="", encoding="utf-8") as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=CAMPOS)
            writer.writeheader()
        return

    # Se o arquivo já existe com cabeçalho antigo, faz uma migração simples
    with open(LOG_FILE, mode="r", encoding="utf-8") as arquivo:
        reader = csv.DictReader(arquivo)
        campos_atuais = reader.fieldnames or []
        linhas_antigas = list(reader)

    if campos_atuais != CAMPOS:
        linhas_migradas = []

        for linha in linhas_antigas:
            linhas_migradas.append({
                "data_hora": linha.get("data_hora", ""),
                "canal": linha.get("canal", "desconhecido"),
                "usuario_id": linha.get("usuario_id", ""),
                "usuario": linha.get("usuario", "usuario_desconhecido"),
                "assistente": linha.get("assistente", "Inna"),
                "pergunta": linha.get("pergunta", ""),
                "resposta": linha.get("resposta", ""),
                "status": linha.get("status", "success"),
                "tempo_resposta_segundos": linha.get(
                    "tempo_resposta_segundos",
                    "0.0"
                )
            })

        with open(LOG_FILE, mode="w", newline="", encoding="utf-8") as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=CAMPOS)
            writer.writeheader()
            writer.writerows(linhas_migradas)


def salvar_interacao(
    canal: str,
    usuario: str,
    pergunta: str,
    resposta: str,
    status: str = "success",
    tempo_resposta_segundos: float = 0.0,
    usuario_id: str | None = None,
    assistente: str = "Inna"
):
    garantir_arquivo_log()

    registro = {
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "canal": canal or "desconhecido",
        "usuario_id": usuario_id or "",
        "usuario": usuario or "usuario_desconhecido",
        "assistente": assistente or "Inna",
        "pergunta": pergunta or "",
        "resposta": resposta or "",
        "status": status or "success",
        "tempo_resposta_segundos": round(float(tempo_resposta_segundos), 3)
    }

    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        writer.writerow(registro)


def carregar_interacoes():
    garantir_arquivo_log()

    with open(LOG_FILE, mode="r", encoding="utf-8") as arquivo:
        reader = csv.DictReader(arquivo)
        return list(reader)