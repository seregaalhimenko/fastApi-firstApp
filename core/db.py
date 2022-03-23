from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ

# берем параметры БД из переменных окружения
DB_USER = environ.get("DB_USER", "user")
DB_PASSWORD = environ.get("DB_PASSWORD", "password")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_NAME = "quizDb"

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)


engine = create_engine(
    SQLALCHEMY_DATABASE_URL #, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()