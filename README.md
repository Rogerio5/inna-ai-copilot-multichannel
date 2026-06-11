# inna-ai-copilot-multichannel
Educadora Financeira Inteligente com IA Generativa, FastAPI, Streamlit, n8n, Telegram, Gmail e Webhook API

A Inna é uma assistente financeira inteligente multicanal desenvolvida para explicar conceitos de finanças pessoais de forma simples, segura e contextualizada.

O projeto combina IA Generativa, Prompt Engineering, FastAPI, Streamlit, n8n, Telegram Bot, Gmail Bot, Webhook API, logs unificados e analytics para demonstrar uma solução prática de IA Conversacional aplicada à educação financeira.


 ---

![Capa do Projeto](Inna_bot_ruiva.png)

---

## 🏅 Badges

- 📦 Tamanho do repositório / Repository Size:  
  ![GitHub repo size](https://img.shields.io/github/repo-size/Rogerio5/inna-ai-copilot-multichannel)

- 📄 Licença do projeto / Project License:  
  ![GitHub license](https://img.shields.io/github/license/Rogerio5/inna-ai-copilot-multichannel)

  ---

## 📋 Índice

📖 Descrição
🎯 Problema Resolvido
💡 Solução
🚧 Status
🧩 Funcionalidades
🖼️ Demonstração Visual
🏗️ Arquitetura
🧰 Tecnologias
📂 Estrutura do Projeto
📊 Dados Utilizados
🔐 Segurança e Limitações
⚙️ Configuração
▶️ Como Rodar
🔄 Integração com n8n
📈 Logs e Analytics
🧪 Testes
📚 Documentação Técnica
🚀 Roadmap
👨‍💻 Autor
📜 Licença
🏁 Conclusão

---

## 📖 Descrição

A Inna AI Copilot Multichannel é um MVP funcional de agente conversacional financeiro.

Ela foi criada para atuar como uma educadora financeira inteligente, explicando temas como:

CDI;
Selic;
Reserva de emergência;
Organização de gastos;
Metas financeiras;
Renda fixa;
Perfil financeiro;
Planejamento financeiro pessoal.

A Inna não faz recomendação de investimentos. Ela explica conceitos de forma educativa, segura e acessível.

---

## 🎯 Problema Resolvido

Muitas pessoas têm dificuldade para entender conceitos básicos de finanças pessoais.

Além disso, muitos chatbots financeiros são genéricos, sem contexto, sem histórico, sem integração real com canais externos e sem métricas de atendimento.

Este projeto resolve esse problema criando uma assistente capaz de:

Explicar conceitos financeiros com linguagem simples;
Usar dados fictícios de um cliente demo como exemplo;
Atender por múltiplos canais;
Registrar logs das interações;
Gerar base para analytics e evolução futura.

---

## 💡 Solução

A Inna conecta diferentes canais de atendimento a uma API central.

Fluxo principal:

Usuário → Streamlit / Telegram / Gmail / Webhook
        → n8n
        → FastAPI /ask
        → Agente Inna
        → Gemini ou Mock Mode
        → Logs e Analytics

O projeto mostra na prática a integração entre:

Backend Python;
IA Generativa;
Automação low-code;
Canais conversacionais;
Dados estruturados;
Logs de atendimento;
Métricas operacionais

---

## 🚧 Status

✅ MVP funcional em desenvolvimento avançado

Status atual:

Módulo	Status
Web Chat Streamlit	✅ Implementado
FastAPI /ask	✅ Implementado
Gemini API	✅ Implementado
Mock Mode	✅ Implementado
Telegram Bot via n8n	✅ Implementado
Gmail Bot via n8n	✅ Implementado
Webhook API via n8n	✅ Implementado
Logs unificados	✅ Implementado
Analytics inicial	✅ Implementado
RAG	🧪 Estrutura inicial
PostgreSQL	🔜 Roadmap
WhatsApp	🔜 Roadmap
Power BI	🔜 Roadmap
Deploy em Cloud	🔜 Roadmap

---

## Funcionalidades

Funcionalidade	Descrição
💬 Chat com IA	Conversa com a Inna por interface Streamlit
📊 Panorama financeiro	Exibe reserva, meta, saldo, perfil e gastos
🤖 Gemini API	Usa IA Generativa para respostas reais
🧪 Mock Mode	Permite testar sem consumir API Gemini
⚡ FastAPI	Disponibiliza endpoint /ask
🔁 n8n	Orquestra canais externos
📲 Telegram Bot	Atendimento automatizado via Telegram
📧 Gmail Bot	Atendimento automatizado por e-mail
🌐 Webhook API	Integração com sistemas externos
🧾 Logs unificados	Registra interações por canal
📈 Analytics	Exibe métricas da sessão, feedbacks e interações
⭐ Feedbacks	Usuário pode avaliar a experiência
🔐 Segurança	Regras para evitar recomendação financeira
🧠 RAG inicial	Estrutura preparada para evolução futura

---

## 🖼️ Demonstração Visual

Interface Web — Streamlit

Painel financeiro com dados do cliente demo, reserva de emergência, saldo estimado, perfil e gastos por categoria 

--
Demonstração do Agente

Conversa com a Inna respondendo perguntas sobre CDI, reserva de emergência e análise de gastos

--
Workflows Publicados no n8n

Visão geral dos workflows publicados para Telegram, Gmail e Webhook API.

--
Fluxo Telegram

Workflow responsável por receber mensagens do Telegram, enviar para a API FastAPI e retornar a resposta ao usuário.

--
Fluxo Gmail

Workflow responsável por receber e-mails, enviar a dúvida para a API da Inna e responder automaticamente pelo Gmail.

--
Fluxo Webhook API

Workflow que permite integração com sistemas externos por meio de Webhook.

---

## 🏗️ Arquitetura

A arquitetura atual foi pensada para ser simples, funcional e preparada para evolução.

Usuário
│
├── Web Chat Streamlit
├── Telegram Bot
├── Gmail Bot
└── Webhook API
        │
        ▼
      n8n
        │
        ▼
   FastAPI /ask
        │
        ▼
   Agente Inna
        │
        ├── Gemini API
        ├── Mock Mode
        ├── CSV/JSON
        ├── Prompt Engineering
        └── Regras de Segurança
        │
        ▼
 Logs Unificados + Analytics

 ---

 ## 🧰 Tecnologias
 
Categoria	Tecnologias
Linguagem	Python
Interface	Streamlit
API	FastAPI
IA Generativa	Gemini API
Automação	n8n
Canais	Telegram, Gmail, Webhook API
Dados	CSV, JSON
Analytics	Streamlit, Pandas, Plotly
Testes	Pytest
Configuração	dotenv
Versionamento	Git e GitHub
Roadmap	PostgreSQL, RAG, Power BI, OCI Cloud

---

## 📂 Estrutura do Projeto
inna-ai-copilot/
├── api/
│   ├── main.py
│   ├── routes.py
│   └── schemas.py
│
├── assets/
│   ├── arquitetura-inna-ai-copilot.png
│   ├── demo-agente.png
│   ├── fluxo-gmail.png
│   ├── fluxo-telegram.png
│   ├── fluxo-webhook-api.png
│   ├── print-n8n.png
│   └── print-streamlit.png
│
├── data/
│   ├── perfil_usuario.json
│   ├── transacoes.csv
│   ├── interacoes_inna.csv
│   └── feedbacks.csv
│
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   ├── 05-pitch.md
│   └── arquitetura.md
│
├── rag/
│   ├── embeddings.py
│   ├── retriever.py
│   ├── vector_store.py
│   └── README.md
│
├── src/
│   ├── app.py
│   ├── agente.py
│   ├── config.py
│   ├── data_loader.py
│   ├── gemini_client.py
│   └── logger_interacoes.py
│
├── tests/
│   ├── test_agente.py
│   ├── test_api.py
│   └── test_data_loader.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

---

## 📊 Dados Utilizados

O projeto utiliza dados fictícios para demonstração.

Arquivo	Finalidade
perfil_usuario.json	Perfil fictício principal do cliente demo João Silva
transacoes.csv	Transações simuladas para análise financeira
interacoes_inna.csv	Logs de atendimento por canal
feedbacks.csv	Avaliações dos usuários
base_conhecimento.md	Base inicial para evolução com RAG

---

## 🔐 Segurança e Limitações

A Inna foi projetada para atuar como educadora financeira, não como consultora de investimentos.

A assistente:

Não recomenda compra ou venda de ativos;
Não promete rentabilidade;
Não acessa dados bancários reais;
Não solicita senhas;
Não substitui profissional certificado;
Utiliza dados fictícios para demonstração;
Explica conceitos financeiros de forma educativa;
Informa limitações quando não possui contexto suficiente.

---

## ⚙️ Configuração

O projeto utiliza .env para variáveis locais e .env.example como modelo seguro para o GitHub.

Exemplo:

APP_NAME=inna-ai-copilot-multichannel
APP_VERSION=1.0.0
APP_ENV=development

INNA_APP_NAME=Inna - Educadora Financeira Inteligente
INNA_NOME=Inna
INNA_TITULO=Educadora Financeira Inteligente
INNA_MOCK_MODE=true

GEMINI_API_KEY=coloque_sua_chave_gemini_aqui
GEMINI_MODEL=gemini-2.5-flash-lite

API_HOST=127.0.0.1
API_PORT=8000
API_BASE_URL=http://127.0.0.1:8000

O arquivo .env real não deve ser enviado para o GitHub.

---

## ▶️ Como Rodar
1. Clonar o repositório
git clone https://github.com/Ronaldo94-GITHUB/inna-ai-copilot-multichannel.git
cd inna-ai-copilot-multichannel
2. Criar ambiente virtual
python -m venv .venv
3. Ativar ambiente virtual

Windows PowerShell:

.\.venv\Scripts\Activate.ps1
4. Instalar dependências
pip install -r requirements.txt
5. Configurar .env
copy .env.example .env

Depois, preencha as variáveis necessárias.

6. Rodar a API FastAPI
python -m uvicorn api.main:app --reload --port 8000

A API ficará disponível em:

http://127.0.0.1:8000
7. Rodar o Streamlit

Em outro terminal:

streamlit run src/app.py --server.port 8501

A interface ficará disponível em:

http://localhost:8501

---

## 🔄 Integração com n8n

O projeto utiliza n8n para orquestrar os canais externos.

Workflows:

Inna - Telegram Bot;
Inna - Gmail Bot;
Inna - Webhook API.

Fluxo geral:

Canal externo → n8n → FastAPI /ask → Agente Inna → n8n → resposta ao usuário

Durante o desenvolvimento local, o ngrok pode ser usado para expor o n8n:

ngrok http 5678

---

## 📈 Logs e Analytics

As interações são registradas em:

data/interacoes_inna.csv

Campos principais:

data_hora
canal
usuario_id
usuario
assistente
pergunta
resposta
status
tempo_resposta_segundos

Esses dados permitem acompanhar:

Total de interações;
Canais utilizados;
Tempo médio de resposta;
Taxa de sucesso;
Erros;
Usuários atendidos;
Perguntas frequentes;
Temas mais buscados;
Base futura para Power BI.

---

## 🧪 Testes

O projeto possui estrutura inicial de testes com Pytest.

Arquivos:

tests/
├── test_agente.py
├── test_api.py
└── test_data_loader.py

Executar testes:

pytest

---

## 📚 Documentação Técnica

A documentação detalhada está na pasta docs/.

Arquivo	Conteúdo
01-documentacao-agente.md	Caso de uso, persona, tom de voz e segurança
02-base-conhecimento.md	Dados utilizados e contexto do agente
03-prompts.md	System Prompt, exemplos e edge cases
04-metricas.md	Métricas de avaliação e testes
05-pitch.md	Roteiro executivo de apresentação
arquitetura.md	Arquitetura atual e evolução futura

--- 

## 🚀 Roadmap — Projeto 2

A evolução planejada será:

Inna Cloud AI Platform

Uma plataforma multicanal de IA Conversacional com memória, cloud, automação e analytics.

Evoluções futuras:

Deploy em OCI;
n8n rodando 24/7;
PostgreSQL para logs, usuários, feedbacks e transações;
Memória persistente por usuario_id;
WhatsApp como canal oficial;
RAG com base documental financeira;
Power BI conectado ao banco;
Dashboards executivos;
Observabilidade e monitoramento;
Possível integração com OCI Generative AI;
Arquitetura escalável para múltiplos usuários.

--- 

## 👨‍💻 Desenvolvedor / Developer

- [Rogerio](https://github.com/Rogerio5)

---

## ## 📜 Licença / License

Este projeto está sob licença MIT. Para mais detalhes, veja o arquivo LICENSE.

This project is under the MIT license. For more details, see the LICENSE file.

---

## 🏁 Conclusão

A Inna AI Copilot Multichannel demonstra como aplicar IA Generativa em um caso realista de educação financeira, integrando interface web, API, automação low-code, canais externos, logs e analytics.

Mais do que um chatbot simples, a Inna funciona como um MVP de IA Conversacional Multicanal, com arquitetura preparada para evoluir para uma plataforma cloud com PostgreSQL, RAG, Power BI, WhatsApp e memória persistente por usuário.
