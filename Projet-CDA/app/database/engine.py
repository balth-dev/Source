import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Récupérer les infos de connexion depuis .env ou utiliser un fallback
DB_USER = os.getenv("DB_USER") or os.getenv("DB_user") or "root"
DB_PASSWORD = os.getenv("DB_PASSWORD") or os.getenv("DB_password") or ""
DB_HOST = os.getenv("DB_HOST") or os.getenv("DB_host") or "localhost"
DB_PORT = os.getenv("DB_PORT") or os.getenv("DB_port") or "3306"
DB_NAME = os.getenv("DB_NAME") or os.getenv("DB_name") or "resa_salles"
DB_DRIVER = os.getenv("DB_DRIVER") or os.getenv("DB_driver") or "mysql+pymysql"
if DB_DRIVER == "mysql":
    DB_DRIVER = "mysql+pymysql"

if DB_PASSWORD:
    auth = f"{DB_USER}:{DB_PASSWORD}"
else:
    auth = DB_USER

DATABASE_URL = f"{DB_DRIVER}://{auth}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)
