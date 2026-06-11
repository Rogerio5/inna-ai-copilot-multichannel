from datetime import datetime


class HistoricoInteracao:
    def __init__(self, pergunta: str, resposta: str, canal: str):
        self.pergunta = pergunta
        self.resposta = resposta
        self.canal = canal
        self.data_hora = datetime.now().isoformat()

