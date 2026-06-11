# Inna AI Copilot Multichannel
Educadora Financeira Inteligente com IA Generativa, FastAPI, Streamlit, n8n, Telegram, Gmail e Webhook API

A **Inna** é uma assistente financeira inteligente multicanal desenvolvida para explicar conceitos de finanças pessoais de forma simples, segura e contextualizada.

O projeto combina IA Generativa, Prompt Engineering, FastAPI, Streamlit, n8n, Telegram Bot, Gmail Bot, Webhook API, logs unificados e analytics para demonstrar uma solução prática de IA Conversacional aplicada à educação financeira.

---

![Capa do Projeto](Inna_bot_ruiva.png)

---

## 🏅 Badges
- 📦 Tamanho do repositório  
  ![GitHub repo size](https://img.shields.io/github/repo-size/Rogerio5/inna-ai-copilot-multichannel)
- 📄 Licença do projeto  
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
Ela explica conceitos como CDI, Selic, reserva de emergência, organização de gastos, metas financeiras, renda fixa, perfil financeiro e planejamento pessoal.  
⚠️ **Importante:** A Inna não faz recomendação de investimentos, apenas explica conceitos de forma educativa.

---

## 🎯 Problema Resolvido
- Dificuldade das pessoas em entender finanças pessoais.  
- Chatbots financeiros genéricos, sem contexto ou métricas.  

Este projeto resolve criando uma assistente que:  
- Explica conceitos com linguagem simples.  
- Usa dados fictícios de cliente demo.  
- Atende por múltiplos canais.  
- Registra logs e gera analytics.  

---

## 💡 Solução
Fluxo principal:  
Usuário → Streamlit / Telegram / Gmail / Webhook → n8n → FastAPI → Agente Inna → Gemini ou Mock Mode → Logs e Analytics  

Integra:  
- Backend Python  
- IA Generativa  
- Automação low-code  
- Canais conversacionais  
- Logs e métricas  

---

## 🚧 Status
✅ MVP funcional em desenvolvimento avançado  

| Módulo | Status |
|--------|--------|
| Web Chat Streamlit | ✅ |
| FastAPI /ask | ✅ |
| Gemini API | ✅ |
| Mock Mode | ✅ |
| Telegram Bot via n8n | ✅ |
| Gmail Bot via n8n | ✅ |
| Webhook API via n8n | ✅ |
| Logs unificados | ✅ |
| Analytics inicial | ✅ |
| RAG | 🧪 Estrutura inicial |
| PostgreSQL | 🔜 Roadmap |
| WhatsApp | 🔜 Roadmap |
| Power BI | 🔜 Roadmap |
| Deploy em Cloud | 🔜 Roadmap |

---

## 🧩 Funcionalidades
- 💬 Chat com IA (Streamlit)  
- 📊 Panorama financeiro (reserva, saldo, perfil, gastos)  
- 🤖 Gemini API para respostas reais  
- 🧪 Mock Mode para testes  
- ⚡ FastAPI endpoint `/ask`  
- 🔁 n8n para orquestração  
- 📲 Telegram Bot  
- 📧 Gmail Bot  
- 🌐 Webhook API  
- 🧾 Logs unificados  
- 📈 Analytics iniciais  
- ⭐ Feedbacks dos usuários  
- 🔐 Segurança contra recomendações financeiras  
- 🧠 Estrutura inicial de RAG  

---

## 🖼️ Demonstração Visual
- Interface Web (Streamlit)  
- Painel financeiro com dados fictícios  
- Workflows no n8n (Telegram, Gmail, Webhook)  
- Fluxo de mensagens integrado  

---

## 🏗️ Arquitetura
Usuário → Canais (Web, Telegram, Gmail, Webhook) → n8n → FastAPI → Agente Inna → Gemini/Mock → Logs + Analytics  

---

## 🧰 Tecnologias
- **Linguagem:** Python  
- **Interface:** Streamlit  
- **API:** FastAPI  
- **IA Generativa:** Gemini API  
- **Automação:** n8n  
- **Canais:** Telegram, Gmail, Webhook  
- **Dados:** CSV, JSON  
- **Analytics:** Pandas, Plotly  
- **Testes:** Pytest  
- **Configuração:** dotenv  
- **Versionamento:** Git/GitHub  
- **Roadmap:** PostgreSQL, RAG, Power BI, OCI Cloud  

---

## 📂 Estrutura do Projeto
