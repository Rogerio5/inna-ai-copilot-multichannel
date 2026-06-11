def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def eh_saudacao(texto):
    saudacoes = ["oi", "olÃ¡", "ola", "bom dia", "boa tarde", "boa noite", "hello", "hi"]
    return texto.lower().strip() in saudacoes

