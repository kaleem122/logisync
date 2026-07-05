import os
from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel, Session

load_dotenv(override = True)  # Load environment variables from .env file

DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is missing!")

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    """Yields a database session, ensuring it is automatically closed after use."""
    with Session(engine) as session:
        yield session


