# Fluxo Telegram - BankPy AI Copilot

## Objetivo

Permitir que o usuÃ¡rio converse com o agente financeiro pelo Telegram.

## Passo a passo

### 1. Criar bot no Telegram

1. Abra o Telegram.
2. Procure por BotFather.
3. Envie o comando:

/newbot

4. Escolha o nome do bot.
5. Copie o token gerado.

### 2. Configurar no n8n

Crie um workflow com os nodes:

Telegram Trigger
â†“
HTTP Request
â†“
Telegram Send Message

### 3. Telegram Trigger

Use o token do BotFather.

Evento:

Message

### 4. HTTP Request

MÃ©todo:

POST

URL:

http://host.docker.internal:8000/ask

Se estiver rodando n8n fora do Docker, use:

http://localhost:8000/ask

Body JSON:

{
  "pergunta": "{{$json.message.text}}",
  "canal": "telegram"
}

### 5. Telegram Send Message

Chat ID:

{{$json.message.chat.id}}

Texto:

{{$node["HTTP Request"].json["resposta"]}}

## Resultado esperado

O usuÃ¡rio envia:

O que Ã© CDI?

O bot responde com uma explicaÃ§Ã£o financeira gerada pelo BankPy AI Copilot.

