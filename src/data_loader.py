import json
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def carregar_json(nome_arquivo):
    caminho = DATA_DIR / nome_arquivo
    with open(caminho, "r", encoding="utf-8-sig") as arquivo:
        return json.load(arquivo)


def carregar_csv(nome_arquivo):
    caminho = DATA_DIR / nome_arquivo
    return pd.read_csv(caminho, encoding="utf-8-sig")


def carregar_perfil():
    return carregar_json("perfil_investidor.json")


def carregar_produtos():
    return carregar_json("produtos_financeiros.json")


def carregar_glossario():
    return carregar_json("glossario_financeiro.json")


def carregar_dicas():
    return carregar_json("dicas_financeiras.json")


def carregar_transacoes():
    return carregar_csv("transacoes.csv")


def carregar_historico():
    return carregar_csv("historico_atendimento.csv")


def calcular_resumo_financeiro(transacoes, renda_mensal):
    saidas = transacoes[transacoes["tipo"] == "saida"]
    entradas = transacoes[transacoes["tipo"] == "entrada"]

    total_entradas = entradas["valor"].sum()
    total_saidas = saidas["valor"].sum()
    saldo_estimado = total_entradas - total_saidas

    gastos_por_categoria = (
        saidas.groupby("categoria")["valor"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    maior_categoria = None
    maior_valor = 0
    percentual_renda = 0

    if not gastos_por_categoria.empty:
        maior_categoria = gastos_por_categoria.iloc[0]["categoria"]
        maior_valor = float(gastos_por_categoria.iloc[0]["valor"])

        if renda_mensal:
            percentual_renda = round((maior_valor / renda_mensal) * 100, 2)

    return {
        "total_entradas": float(total_entradas),
        "total_saidas": float(total_saidas),
        "saldo_estimado": float(saldo_estimado),
        "maior_categoria": maior_categoria,
        "maior_valor": maior_valor,
        "percentual_maior_categoria_sobre_renda": percentual_renda,
        "gastos_por_categoria": gastos_por_categoria.to_dict(orient="records")
    }


def montar_contexto():
    perfil = carregar_perfil()
    produtos = carregar_produtos()
    transacoes = carregar_transacoes()
    historico = carregar_historico()
    glossario = carregar_glossario()
    dicas = carregar_dicas()

    resumo_financeiro = calcular_resumo_financeiro(
        transacoes,
        perfil.get("renda_mensal", 0)
    )

    metas = perfil.get("metas", [])
    reserva_atual = perfil.get("reserva_emergencia_atual", 0)

    contexto = f"""
CLIENTE:
Nome: {perfil["nome"]}
Idade: {perfil["idade"]}
Profissão: {perfil["profissao"]}
Renda mensal: R$ {perfil["renda_mensal"]}
Perfil investidor: {perfil["perfil_investidor"]}
Objetivo principal: {perfil["objetivo_principal"]}
Patrimônio total: R$ {perfil["patrimonio_total"]}
Reserva de emergência atual: R$ {reserva_atual}

METAS FINANCEIRAS:
{json.dumps(metas, indent=2, ensure_ascii=False)}

RESUMO FINANCEIRO CALCULADO:
{json.dumps(resumo_financeiro, indent=2, ensure_ascii=False)}

TRANSAÇÕES:
{transacoes.to_string(index=False)}

HISTÓRICO DE ATENDIMENTO:
{historico.to_string(index=False)}

PRODUTOS FINANCEIROS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}

GLOSSÁRIO FINANCEIRO:
{json.dumps(glossario, indent=2, ensure_ascii=False)}

DICAS FINANCEIRAS:
{json.dumps(dicas, indent=2, ensure_ascii=False)}
"""
    return contexto

