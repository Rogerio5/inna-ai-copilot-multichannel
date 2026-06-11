import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# INFORMAÇÕES DA APLICAÇÃO
# ==========================================

INNA_APP_NAME = os.getenv(
    "INNA_APP_NAME",
    "Inna - Educadora Financeira Inteligente"
)

APP_VERSION = os.getenv(
    "APP_VERSION",
    "1.0.0"
)

# ==========================================
# USUÁRIO CLIENTE DEMONSTRAÇÃO
# ==========================================

INNA_DEMO_EMAIL = os.getenv(
    "INNA_DEMO_EMAIL",
    "joao@inna.ai"
)

INNA_DEMO_PASSWORD = os.getenv(
    "INNA_DEMO_PASSWORD",
    "123456"
)

# ==========================================
# USUÁRIO ADMINISTRADOR
# ==========================================

INNA_ADMIN_EMAIL = os.getenv(
    "INNA_ADMIN_EMAIL",
    "admin@inna.ai"
)

INNA_ADMIN_PASSWORD = os.getenv(
    "INNA_ADMIN_PASSWORD",
    "admin123"
)

# ==========================================
# GEMINI
# ==========================================

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash-lite"
)

# ==========================================
# CONFIGURAÇÕES DA INNA
# ==========================================

INNA_NOME = os.getenv(
    "INNA_NOME",
    "Inna"
)

INNA_TITULO = os.getenv(
    "INNA_TITULO",
    "Educadora Financeira Inteligente"
)

# ==========================================
# SIMULAÇÃO DA INNA
# ==========================================
INNA_MOCK_MODE = os.getenv(
    "INNA_MOCK_MODE",
    "false"
).lower() == "true"