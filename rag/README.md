# RAG — Estrutura Inicial

Esta pasta contém a estrutura inicial para evolução da Inna com RAG  
(Retrieval-Augmented Generation).

No MVP atual, a Inna utiliza IA Generativa, Prompt Engineering, dados fictícios
em CSV/JSON e regras de segurança financeira.

A proposta futura do RAG é permitir que a Inna consulte uma base de conhecimento
antes de gerar respostas, usando documentos, FAQs, arquivos Markdown e dados
estruturados.

## Fluxo previsto

Usuário → Pergunta → Busca semântica → Contexto recuperado → Gemini → Resposta da Inna

## Arquivos

- `embeddings.py`: estrutura futura para geração de embeddings.
- `vector_store.py`: estrutura futura para armazenamento vetorial.
- `retriever.py`: estrutura futura para recuperação de contexto relevante.

## Status

🧪 Estrutura inicial criada para evolução futura.

## Possíveis tecnologias futuras

- FAISS
- ChromaDB
- PostgreSQL com pgvector
- OCI Cloud
- Base documental financeira
- RAG com documentos da pasta `docs/`