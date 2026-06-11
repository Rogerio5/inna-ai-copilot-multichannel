# Fluxo Gmail - BankPy AI Copilot

## Objetivo

Ler e-mails recebidos, interpretar dÃºvidas financeiras e responder automaticamente usando IA Generativa.

## Fluxo

Gmail Trigger
â†“
HTTP Request para FastAPI
â†“
Gmail Send Reply

## Gmail Trigger

Evento:

New Email

Filtro sugerido:

subject contains "DÃºvida financeira"

## HTTP Request

MÃ©todo:

POST

URL:

http://host.docker.internal:8000/ask

Se estiver rodando n8n fora do Docker, use:

http://localhost:8000/ask

Body JSON:

{
  "pergunta": "{{$json.textPlain}}",
  "canal": "gmail"
}

## Gmail Send

Para:

{{$json.from.email}}

Assunto:

Resposta do BankPy AI Copilot

Corpo:

{{$node["HTTP Request"].json["resposta"]}}

## ObservaÃ§Ã£o

Para usar Gmail no n8n, serÃ¡ necessÃ¡rio configurar credenciais OAuth no Google Cloud Console.

