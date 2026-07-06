from pydantic import BaseModel
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from database import engine, get_session
from sqlmodel import SQLModel, Session, select
import models
from routers import tasks, moves


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Booting up: Instructing Supabase to build tables...")
    SQLModel.metadata.create_all(engine)
    yield



app = FastAPI(lifespan=lifespan)
app.include_router(tasks.router)
app.include_router(moves.router)


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Logisync engine is running"}









