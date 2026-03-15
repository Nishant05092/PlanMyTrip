import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL

load_dotenv()


class Settings:
    # DATABASE_URL = URL.create(
    #     drivername="postgresql+psycopg2",
    #     username=os.getenv("POSTGRES_USER"),
    #     password=os.getenv("POSTGRES_PASSWORD"),
    #     host=os.getenv("POSTGRES_HOST"),
    #     port=int(os.getenv("POSTGRES_PORT")),
    #     database=os.getenv("POSTGRES_DB"),
    # )
    DATABASE_URL = os.getenv("DATABASE_URL")

    JWT_SECRET: str = os.getenv("JWT_SECRET")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")


settings = Settings()

