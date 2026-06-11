# Base de Conhecimento

## Dados Utilizados

A Inna utiliza uma base de conhecimento local com arquivos CSV e JSON para simular um contexto financeiro real de um cliente fictício.

Esses dados permitem que o agente responda de forma mais personalizada, usando exemplos práticos de perfil financeiro, transações, metas e histórico de interação.

---

## Arquivos da Base de Conhecimento

| Arquivo                     | Formato  | Finalidade                                                                         |
| --------------------------- | -------- | ---------------------------------------------------------------------------------- |
| `perfil_usuario.json`       | JSON     | Armazena o perfil fictício principal do cliente demo João Silva                    |
| `transacoes.csv`            | CSV      | Contém receitas, despesas, categorias e movimentações financeiras simuladas        |
| `interacoes_inna.csv`       | CSV      | Registra logs de interações com canal, usuário, pergunta, resposta, status e tempo |
| `feedbacks.csv`             | CSV      | Armazena avaliações dos usuários sobre as respostas da Inna                        |
| `exemplos_atendimento.json` | JSON     | Pode conter exemplos de perguntas e respostas para Few-Shot Prompting              |
| `produtos_financeiros.json` | JSON     | Pode conter produtos financeiros usados apenas para explicação educativa           |
| `base_conhecimento.md`      | Markdown | Pode armazenar conceitos financeiros, regras e explicações para evolução com RAG   |

---

## Perfil Fictício Principal

O Projeto 1 utiliza um perfil financeiro fictício principal:

```json
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false
}
```

Esse perfil é usado apenas para demonstração e não representa dados reais.

---

## Transações Simuladas

A base `transacoes.csv` representa movimentações financeiras fictícias do cliente demo.

Exemplo:

```csv
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-11,Aplicação Tesouro Selic,investimentos,500.00,saida
2025-10-18,Transferência para reserva,investimentos,700.00,saida
2025-10-25,Combustível,transporte,250.00,saida
```

Esses dados permitem que a Inna explique conceitos como:

* Receita;
* Despesa;
* Saldo mensal;
* Gastos por categoria;
* Reserva de emergência;
* Organização financeira;
* Metas financeiras;
* Educação sobre investimentos.

---

## Logs de Interação

O arquivo `interacoes_inna.csv` registra as interações dos canais conectados à Inna.

Campos principais:

| Campo                     | Descrição                                    |
| ------------------------- | -------------------------------------------- |
| `data_hora`               | Data e hora da interação                     |
| `canal`                   | Canal usado: webchat, telegram, gmail ou api |
| `usuario_id`              | Identificador do usuário ou remetente        |
| `usuario`                 | Nome ou identificação do usuário             |
| `assistente`              | Nome da assistente, Inna                     |
| `pergunta`                | Pergunta recebida                            |
| `resposta`                | Resposta gerada                              |
| `status`                  | success ou error                             |
| `tempo_resposta_segundos` | Tempo aproximado de resposta                 |

Essa base permite criar métricas de atendimento e dashboards executivos.

---

## Estratégia de Integração

### Como os dados são carregados?

Os dados são carregados por arquivos locais usando Python, CSV, JSON e funções auxiliares no projeto.

Exemplo:

```python
import pandas as pd
import json

transacoes = pd.read_csv("data/transacoes.csv")

with open("data/perfil_usuario.json", "r", encoding="utf-8") as arquivo:
    perfil = json.load(arquivo)
```

### Como os dados são usados pela Inna?

No Projeto 1, os dados são usados como contexto estruturado para a resposta da Inna.

A API recebe uma pergunta, consulta o agente, utiliza dados disponíveis no projeto e retorna uma resposta educativa.

A interação é registrada em log para análise posterior.

---

## Exemplo de Contexto Montado

```text
CLIENTE DEMO:
Nome: João Silva
Perfil: Moderado
Objetivo: Construir reserva de emergência
Renda mensal: R$ 5.000,00
Reserva atual: R$ 10.000,00
Meta de reserva: R$ 15.000,00

RESUMO FINANCEIRO:
Receitas simuladas
Despesas por categoria
Gastos recorrentes
Aplicações para reserva/investimentos

REGRAS:
Não recomendar investimentos
Não prometer rentabilidade
Explicar conceitos de forma educativa
Usar os dados apenas como exemplo
```

---

## Evolução com RAG

O projeto possui uma pasta `rag/` com estrutura inicial para evolução futura.

Essa estrutura pode permitir que a Inna consulte documentos internos antes de responder, como:

* FAQ financeiro;
* Regras de segurança;
* Política de não recomendação;
* Conceitos sobre CDI, Selic, CDB e reserva de emergência;
* Base documental para educação financeira.

No Projeto 1, o RAG pode ser tratado como módulo experimental.

No Projeto 2, ele pode se tornar um componente oficial da arquitetura cloud.
