
# import os
# from dotenv import load_dotenv
# from fastapi_mail import ConnectionConfig

# # .env faylni yuklash
# load_dotenv()

# # Database va JWT sozlamalari
# DATABASE_URL = os.getenv("DATABASE_URL")
# SECRET_KEY = os.getenv("SECRET_KEY")
# JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

# # Mail sozlamalari
# MAIL_USERNAME = os.getenv("MAIL_USERNAME")
# MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
# MAIL_FROM = os.getenv("MAIL_FROM")
# MAIL_SERVER = os.getenv("MAIL_SERVER")
# MAIL_PORT = int(os.getenv("MAIL_PORT") or 587)  # default port 587

# # Mail FROM bo'sh bo'lsa xatolik beradi
# if not MAIL_FROM:
#     raise ValueError("MAIL_FROM environment variable not set")

# # FastAPI Mail konfiguratsiyasi
# mail_conf = ConnectionConfig(
#     MAIL_USERNAME=MAIL_USERNAME or "",
#     MAIL_PASSWORD=MAIL_PASSWORD or "",
#     MAIL_FROM=MAIL_FROM,
#     MAIL_SERVER=MAIL_SERVER or "",
#     MAIL_PORT=MAIL_PORT,
#     MAIL_STARTTLS=True,
#     MAIL_SSL_TLS=False,
#     USE_CREDENTIALS=True,
#     VALIDATE_CERTS=True
# )

import os
from dotenv import load_dotenv
from fastapi_mail import ConnectionConfig

load_dotenv()

# JWT Settings
SECRET_KEY = os.getenv("SECRET_KEY", "secret_key")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database Settings
DATABASE_URL = os.getenv("DATABASE_URL")

# Email Settings
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_FROM = os.getenv("MAIL_FROM")
MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")

# Mail Configuration
mail_conf = ConnectionConfig(
    MAIL_USERNAME=MAIL_USERNAME,
    MAIL_PASSWORD=MAIL_PASSWORD,
    MAIL_FROM=MAIL_FROM,
    MAIL_PORT=MAIL_PORT,
    MAIL_SERVER=MAIL_SERVER,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)