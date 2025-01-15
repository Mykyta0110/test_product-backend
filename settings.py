from envparse import Env


env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://postgres_user:rk1vDwkXLJGgl7cPE8nxt2nXyyxDyoBE@dpg-cu3pjid6l47c73a962eg-a.oregon-postgres.render.com/products_ntit"
)

APP_PORT = env.int("APP_PORT", default=8000)