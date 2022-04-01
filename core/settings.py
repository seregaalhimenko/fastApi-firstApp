from os import environ

DB_USER = environ.get("POSTGRES_USER", "postgres")
DB_PASSWORD = environ.get("POSTGRES_PASSWORD", "postgres")
DB_HOST = environ.get("POSTGRES_HOST", "localhost")
DB_NAME = environ.get("POSTGRES_NAME", "postgres")
DB_PORT = environ.get("POSTGRES_PORT", "5432")


SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
