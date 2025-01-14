from envparse import Env


env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://postgres:Admin@127.0.0.1:5432/products"
)

APP_PORT = env.int("APP_PORT", default=8000)