from os import environ

DB_USER = environ.get("DB_USER", "user")
DB_PASSWORD = environ.get("DB_PASSWORD", "password")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_NAME = "quizDb"
DB_PORT= environ.get("DB_PORT", "5432")
