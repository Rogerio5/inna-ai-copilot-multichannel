# Exemplos de Webhook

## Exemplo de requisiÃ§Ã£o para a API

URL:

http://localhost:8000/ask

MÃ©todo:

POST

Body JSON:

{
  "pergunta": "O que Ã© CDI?",
  "canal": "webhook"
}

Resposta esperada:

{
  "resposta": "CDI significa Certificado de DepÃ³sito InterbancÃ¡rio...",
  "canal": "webhook",
  "status": "success"
}

## Exemplo com Telegram

Entrada recebida do Telegram:

{
  "message": {
    "chat": {
      "id": 123456789
    },
    "text": "Onde estou gastando mais?"
  }
}

Campo usado como pergunta:

{{$json["message"]["text"]}}

Campo usado como chat ID:

{{$json["message"]["chat"]["id"]}}

## Exemplo com Gmail

Assunto:

DÃºvida financeira

Corpo:

Quero entender onde estou gastando mais.

Campo enviado para a API:

{
  "pergunta": "Quero entender onde estou gastando mais.",
  "canal": "gmail"
}

