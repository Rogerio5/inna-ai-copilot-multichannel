import csv
import time
from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st

from agente import perguntar_ao_agente
from config import (
    INNA_APP_NAME,
    INNA_DEMO_EMAIL,
    INNA_DEMO_PASSWORD,
    INNA_ADMIN_EMAIL,
    INNA_ADMIN_PASSWORD,
    INNA_NOME,
    INNA_TITULO
)
from data_loader import (
    carregar_perfil,
    carregar_transacoes,
    calcular_resumo_financeiro
)
from logger_interacoes import salvar_interacao, carregar_interacoes


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
FEEDBACKS_FILE = DATA_DIR / "feedbacks.csv"


st.set_page_config(
    page_title=INNA_APP_NAME,
    page_icon="💰",
    layout="wide"
)


perfil = carregar_perfil()
transacoes = carregar_transacoes()
resumo = calcular_resumo_financeiro(
    transacoes,
    perfil.get("renda_mensal", 0)
)


def moeda(valor):
    return (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def formatar_texto_streamlit(texto: str) -> str:
    """
    Evita que o Streamlit/Markdown interprete o símbolo $ como fórmula.
    Assim valores como R$ 10.000,00 aparecem corretamente.
    """
    if not texto:
        return ""

    return str(texto).replace("R$", "R\\$")


def salvar_feedback(nota, comentario, usuario):
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    arquivo_existe = FEEDBACKS_FILE.exists()

    with open(FEEDBACKS_FILE, "a", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)

        if not arquivo_existe:
            writer.writerow(["data_hora", "usuario", "nota", "comentario"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            usuario,
            nota,
            comentario
        ])


def tela_login():
    col1, col2, col3 = st.columns([1, 1.4, 1])

    with col2:
        st.title("💰 Inna")
        st.subheader("Educadora Financeira Inteligente")
        st.caption(
            "Aprenda sobre finanças pessoais de forma simples, prática "
            "e baseada nos seus dados."
        )

        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")

        if st.checkbox("Mostrar credenciais demo"):
            st.info(
                f"Cliente: {INNA_DEMO_EMAIL} | Senha: {INNA_DEMO_PASSWORD}\n\n"
                f"Admin: {INNA_ADMIN_EMAIL} | Senha: {INNA_ADMIN_PASSWORD}"
            )

        entrar = st.button("Entrar", use_container_width=True)

        if entrar:
            if email == INNA_DEMO_EMAIL and senha == INNA_DEMO_PASSWORD:
                st.session_state.logado = True
                st.session_state.usuario = email
                st.session_state.perfil_usuario = "cliente"
                st.rerun()

            elif email == INNA_ADMIN_EMAIL and senha == INNA_ADMIN_PASSWORD:
                st.session_state.logado = True
                st.session_state.usuario = email
                st.session_state.perfil_usuario = "admin"
                st.rerun()

            else:
                st.error("E-mail ou senha inválidos.")


def dashboard():
    st.title("📊 Meu Panorama Financeiro")
    st.caption("Resumo educativo baseado nos dados disponíveis do cliente.")

    reserva_atual = perfil["reserva_emergencia_atual"]
    meta_reserva = 15000.0
    faltante = max(0, meta_reserva - reserva_atual)
    progresso = min(reserva_atual / meta_reserva, 1.0)

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("Reserva atual", moeda(reserva_atual))
    c2.metric("Meta reserva", moeda(meta_reserva))
    c3.metric("Faltante", moeda(faltante))
    c4.metric("Saldo estimado", moeda(resumo["saldo_estimado"]))
    c5.metric("Perfil", perfil["perfil_investidor"].capitalize())

    st.divider()

    left, right = st.columns([1, 1])

    with left:
        st.subheader("💡 Insight do mês")
        st.info(
            f"Sua maior despesa é **{resumo['maior_categoria']}** "
            f"({moeda(resumo['maior_valor'])}), representando "
            f"**{resumo['percentual_maior_categoria_sobre_renda']}%** "
            f"da renda mensal."
        )

        st.subheader("🎯 Progresso da reserva")
        st.progress(progresso)
        st.write(f"Você concluiu **{progresso * 100:.1f}%** da sua meta.")
        st.write(f"Faltam **{moeda(faltante)}** para concluir sua reserva.")

    with right:
        st.subheader("📊 Gastos por categoria")
        df_gastos = pd.DataFrame(resumo["gastos_por_categoria"])

        if not df_gastos.empty:
            st.bar_chart(df_gastos.set_index("categoria"))
        else:
            st.info("Não há gastos disponíveis para exibir.")


def chat_inna():
    st.title(f"💬 Conversar com {INNA_NOME}")
    st.caption(
        "Educadora financeira baseada em IA, contexto do cliente "
        "e dados estruturados."
    )

    b1, b2, b3, b4 = st.columns(4)

    if b1.button("O que é CDI?"):
        st.session_state.pergunta_rapida = "O que é CDI?"

    if b2.button("Minha reserva"):
        st.session_state.pergunta_rapida = (
            "Como está minha reserva de emergência?"
        )

    if b3.button("Meus gastos"):
        st.session_state.pergunta_rapida = (
            "Onde estou gastando mais dinheiro?"
        )

    if b4.button("Minhas metas"):
        st.session_state.pergunta_rapida = (
            "Quais são minhas metas financeiras?"
        )

    st.divider()

    if "mensagens" not in st.session_state:
        st.session_state.mensagens = [
            {
                "role": "assistant",
                "content": (
                    "Olá! Sou a Inna, sua educadora financeira inteligente. "
                    "Como posso ajudar?"
                )
            }
        ]

    for mensagem in st.session_state.mensagens:
        with st.chat_message(mensagem["role"]):
            st.markdown(formatar_texto_streamlit(mensagem["content"]))

    pergunta_digitada = st.chat_input("Digite sua dúvida financeira...")
    pergunta_rapida = st.session_state.pop("pergunta_rapida", None)
    pergunta = pergunta_digitada or pergunta_rapida

    if pergunta:
        st.session_state.mensagens.append(
            {"role": "user", "content": pergunta}
        )

        with st.chat_message("user"):
            st.markdown(formatar_texto_streamlit(pergunta))

        with st.chat_message("assistant"):
            with st.spinner("Analisando..."):
                inicio = time.time()

                try:
                    resposta = perguntar_ao_agente(pergunta)
                    status = "success"

                except Exception as erro:
                    resposta = (
                        "Ocorreu um erro ao processar sua pergunta. "
                        f"Detalhes técnicos: {erro}"
                    )
                    status = "error"

                tempo_resposta = time.time() - inicio

                usuario_logado = st.session_state.get(
                    "usuario",
                    "usuario_webchat"
                )

                salvar_interacao(
                    canal="webchat",
                    usuario_id=usuario_logado,
                    usuario=usuario_logado,
                    pergunta=pergunta,
                    resposta=resposta,
                    status=status,
                    tempo_resposta_segundos=tempo_resposta
                )

                st.markdown(formatar_texto_streamlit(resposta))

        st.session_state.mensagens.append(
            {"role": "assistant", "content": resposta}
        )


def historico():
    st.title("📜 Histórico de Conversas")
    st.caption("Área administrativa para pesquisar, exportar ou excluir mensagens.")

    mensagens = st.session_state.get("mensagens", [])

    if not mensagens:
        st.info("Nenhuma conversa registrada ainda.")
        return

    termo_busca = st.text_input(
        "🔍 Pesquisar no histórico",
        placeholder="Digite uma palavra ou assunto..."
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("🗑️ Limpar Histórico", use_container_width=True):
            st.session_state.mensagens = [
                {
                    "role": "assistant",
                    "content": (
                        "Olá! Sou a Inna, sua educadora financeira inteligente. "
                        "Como posso ajudar?"
                    )
                }
            ]
            st.success("Histórico limpo com sucesso.")
            st.rerun()

    with col2:
        texto_exportacao = ""

        for mensagem in mensagens:
            papel = INNA_NOME if mensagem["role"] == "assistant" else "Usuário"
            texto_exportacao += f"{papel}: {mensagem['content']}\n\n"

        st.download_button(
            label="📥 Exportar Histórico",
            data=texto_exportacao,
            file_name="historico_inna.txt",
            mime="text/plain",
            use_container_width=True
        )

    st.divider()

    for indice, mensagem in enumerate(mensagens):
        conteudo = mensagem["content"]

        if termo_busca and termo_busca.lower() not in conteudo.lower():
            continue

        papel = INNA_NOME if mensagem["role"] == "assistant" else "Usuário"
        icone = "👩" if mensagem["role"] == "assistant" else "👤"

        with st.container(border=True):
            col_msg, col_del = st.columns([10, 1])

            with col_msg:
                st.markdown(f"**{icone} {papel}:**")
                st.markdown(formatar_texto_streamlit(conteudo))

            with col_del:
                if st.button("❌", key=f"deletar_msg_{indice}"):
                    st.session_state.mensagens.pop(indice)
                    st.success("Mensagem excluída.")
                    st.rerun()


def feedback():
    st.title("⭐ Avaliar a Inna")
    st.caption("Seu feedback ajuda a melhorar a experiência da educadora financeira.")

    nota = st.slider(
        "Como você avalia sua experiência com a Inna?",
        1,
        5,
        5
    )

    comentario = st.text_area("Comentário")

    if st.button("Enviar feedback", use_container_width=True):
        salvar_feedback(
            nota=nota,
            comentario=comentario,
            usuario=st.session_state.get("usuario")
        )

        st.success("Obrigado! Seu feedback foi registrado com sucesso.")
        st.session_state.feedback = {
            "nota": nota,
            "comentario": comentario
        }


def identificar_temas(texto):
    temas = {
        "CDI": 0,
        "Selic": 0,
        "Liquidez": 0,
        "Reserva de emergência": 0,
        "Gastos": 0,
        "Metas financeiras": 0,
        "CDB": 0,
        "Tesouro Selic": 0,
        "LCI/LCA": 0,
        "Fundo Imobiliário": 0,
        "Fundo de Ações": 0
    }

    texto = texto.lower()

    for tema in temas:
        if tema.lower() in texto:
            temas[tema] = texto.count(tema.lower())

    return {
        tema: qtd
        for tema, qtd in temas.items()
        if qtd > 0
    }


def analytics():
    st.title("📈 Analytics da Inna")
    st.caption("Área administrativa com métricas da experiência da educadora financeira.")

    mensagens = st.session_state.get("mensagens", [])

    total_mensagens = len(mensagens)
    total_perguntas = len([m for m in mensagens if m["role"] == "user"])
    total_respostas = len([m for m in mensagens if m["role"] == "assistant"])

    perguntas_usuario = [
        m["content"]
        for m in mensagens
        if m["role"] == "user"
    ]

    st.subheader("💬 Métricas da Sessão Atual")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Mensagens na sessão", total_mensagens)
    col2.metric("Perguntas do usuário", total_perguntas)
    col3.metric("Respostas da Inna", total_respostas)

    if total_perguntas > 0:
        media_respostas = round(total_respostas / total_perguntas, 2)
    else:
        media_respostas = 0

    col4.metric("Respostas por pergunta", media_respostas)

    st.divider()

    st.subheader("🌐 Interações Unificadas por Canal")

    try:
        interacoes = carregar_interacoes()
        df_interacoes = pd.DataFrame(interacoes)

        if not df_interacoes.empty:
            total_interacoes = len(df_interacoes)
            canais_unicos = df_interacoes["canal"].nunique()
            total_success = len(df_interacoes[df_interacoes["status"] == "success"])
            total_error = len(df_interacoes[df_interacoes["status"] == "error"])

            if "tempo_resposta_segundos" in df_interacoes.columns:
                df_interacoes["tempo_resposta_segundos"] = pd.to_numeric(
                    df_interacoes["tempo_resposta_segundos"],
                    errors="coerce"
                )
                tempo_medio = df_interacoes["tempo_resposta_segundos"].mean()
            else:
                tempo_medio = 0

            c1, c2, c3, c4, c5 = st.columns(5)

            c1.metric("Total de interações", total_interacoes)
            c2.metric("Canais usados", canais_unicos)
            c3.metric("Sucessos", total_success)
            c4.metric("Erros", total_error)
            c5.metric("Tempo médio", f"{tempo_medio:.3f}s")

            st.markdown("#### 📊 Interações por canal")

            df_canais = (
                df_interacoes["canal"]
                .value_counts()
                .reset_index()
            )
            df_canais.columns = ["canal", "quantidade"]

            st.bar_chart(df_canais.set_index("canal"))

            st.markdown("#### 📋 Últimas interações registradas")

            colunas_exibir = [
                "data_hora",
                "canal",
                "usuario_id",
                "usuario",
                "pergunta",
                "status",
                "tempo_resposta_segundos"
            ]

            colunas_existentes = [
                coluna
                for coluna in colunas_exibir
                if coluna in df_interacoes.columns
            ]

            st.dataframe(
                df_interacoes[colunas_existentes].tail(20),
                use_container_width=True,
                hide_index=True
            )

            texto_logs = " ".join(
                df_interacoes["pergunta"].fillna("").astype(str).str.lower()
            )
            temas_logs = identificar_temas(texto_logs)

            st.markdown("#### 🏷️ Temas identificados nos logs")

            if temas_logs:
                df_temas_logs = pd.DataFrame(
                    list(temas_logs.items()),
                    columns=["Tema", "Quantidade"]
                )

                st.bar_chart(df_temas_logs.set_index("Tema"))

                st.dataframe(
                    df_temas_logs,
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.info("Ainda não há temas suficientes nos logs unificados.")

        else:
            st.info(
                "Ainda não há interações registradas no arquivo "
                "`data/interacoes_inna.csv`."
            )

    except Exception as erro:
        st.warning(f"Não foi possível carregar os logs unificados: {erro}")

    st.divider()

    st.subheader("⭐ Métricas de Feedback")

    if FEEDBACKS_FILE.exists():
        df_feedbacks = pd.read_csv(FEEDBACKS_FILE)

        total_feedbacks = len(df_feedbacks)
        media_nota = df_feedbacks["nota"].mean()
        ultima_nota = df_feedbacks["nota"].iloc[-1]
        ultimo_usuario = df_feedbacks["usuario"].iloc[-1]
        ultimo_comentario = df_feedbacks["comentario"].iloc[-1]

        feedbacks_positivos = df_feedbacks[df_feedbacks["nota"] >= 4]
        taxa_satisfacao = round(
            (len(feedbacks_positivos) / total_feedbacks) * 100,
            1
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Total de feedbacks", total_feedbacks)
        c2.metric("Média das avaliações", f"{media_nota:.1f}/5")
        c3.metric("Última nota", f"{ultima_nota}/5")
        c4.metric("Satisfação", f"{taxa_satisfacao}%")

        st.info(
            f"Último feedback recebido de **{ultimo_usuario}**: "
            f"_{ultimo_comentario}_"
        )

        st.markdown("#### 📋 Feedbacks registrados")

        st.dataframe(
            df_feedbacks,
            use_container_width=True,
            hide_index=True
        )

    else:
        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Total de feedbacks", 0)
        c2.metric("Média das avaliações", "Sem dados")
        c3.metric("Última nota", "Sem dados")
        c4.metric("Satisfação", "Sem dados")

        st.info("Nenhum feedback registrado ainda.")

    st.divider()

    st.subheader("🧠 Últimas Perguntas da Sessão")

    if perguntas_usuario:
        for pergunta in perguntas_usuario[-5:]:
            st.markdown(f"- {formatar_texto_streamlit(pergunta)}")
    else:
        st.info("Nenhuma pergunta registrada nesta sessão.")

    st.divider()

    st.subheader("🏷️ Temas Identificados na Sessão")

    texto_conversa = " ".join(
        [m["content"].lower() for m in mensagens]
    )

    temas_encontrados = identificar_temas(texto_conversa)

    if temas_encontrados:
        df_temas = pd.DataFrame(
            list(temas_encontrados.items()),
            columns=["Tema", "Quantidade"]
        )

        st.bar_chart(df_temas.set_index("Tema"))

        st.dataframe(
            df_temas,
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info("Ainda não há temas suficientes identificados na conversa.")

    st.divider()

    st.subheader("🩺 Diagnóstico da Sessão")

    if total_perguntas == 0:
        st.warning("O usuário ainda não fez perguntas nesta sessão.")

    elif total_perguntas <= 2:
        st.info(
            "A sessão ainda está no início. Poucas interações foram registradas."
        )

    else:
        st.success(
            "A sessão já possui interações suficientes para análise básica."
        )

    if FEEDBACKS_FILE.exists():
        if media_nota >= 4:
            st.success(
                "A média de feedback indica boa percepção da experiência com a Inna."
            )
        elif media_nota >= 3:
            st.warning(
                "A média de feedback está intermediária. Pode valer revisar respostas e fluxo."
            )
        else:
            st.error(
                "A média de feedback está baixa. Recomenda-se revisar a experiência da Inna."
            )


if "logado" not in st.session_state:
    st.session_state.logado = False


if not st.session_state.logado:
    tela_login()

else:
    st.sidebar.title("💰 Inna")
    st.sidebar.caption(INNA_TITULO)

    if st.session_state.get("perfil_usuario") == "admin":
        paginas = [
            "Meu Panorama Financeiro",
            "Conversar com Inna",
            "Histórico de Conversas",
            "Analytics da Inna",
            "Avaliar a Inna",
            "Sair"
        ]
    else:
        paginas = [
            "Meu Panorama Financeiro",
            "Conversar com Inna",
            "Avaliar a Inna",
            "Sair"
        ]

    pagina = st.sidebar.radio("Menu", paginas)

    st.sidebar.divider()
    st.sidebar.caption(f"Usuário: {st.session_state.get('usuario')}")
    st.sidebar.caption(f"Perfil: {st.session_state.get('perfil_usuario')}")

    if pagina == "Meu Panorama Financeiro":
        dashboard()

    elif pagina == "Conversar com Inna":
        chat_inna()

    elif pagina == "Histórico de Conversas":
        historico()

    elif pagina == "Analytics da Inna":
        analytics()

    elif pagina == "Avaliar a Inna":
        feedback()

    elif pagina == "Sair":
        st.session_state.logado = False
        st.session_state.usuario = None
        st.session_state.perfil_usuario = None
        st.rerun()
