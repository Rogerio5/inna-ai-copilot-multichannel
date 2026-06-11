# n8n - BankPy AI Copilot

Esta pasta contÃ©m a documentaÃ§Ã£o e os fluxos de automaÃ§Ã£o low-code do projeto BankPy AI Copilot.

## Objetivo

Integrar o agente financeiro com canais reais de atendimento, como:

- Telegram
- Gmail
- Webhooks
- APIs externas

## Arquitetura do fluxo

Mensagem do usuÃ¡rio
â†“
n8n
â†“
HTTP Request
â†“
FastAPI BankPy
â†“
Ollama / LLM local
â†“
Resposta automÃ¡tica

## Fluxos planejados

### Telegram

UsuÃ¡rio envia mensagem para um bot no Telegram.  
O n8n recebe a mensagem, envia para a API FastAPI e retorna a resposta gerada pelo agente.

### Gmail

UsuÃ¡rio envia e-mail para a conta configurada.  
O n8n lÃª o e-mail, envia o conteÃºdo para a API FastAPI e gera uma resposta automÃ¡tica.

## Endpoints usados

### Health check

GET http://localhost:8000/health

### Perguntar ao agente

POST http://localhost:8000/ask

Body:

{
  "pergunta": "Onde estou gastando mais?",
  "canal": "n8n"
}

