from pydantic import BaseModel
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from database import engine, get_session
from sqlmodel import SQLModel, Session, select
import models
from routers import tasks, moves
from fastapi.middleware.cors import CORSMiddleware



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Booting up: Instructing Supabase to build tables...")
    SQLModel.metadata.create_all(engine)
    yield



app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware, 
    allow_origins = ["http://localhost:5173"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
    )

app.include_router(tasks.router)
app.include_router(moves.router)


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Logisync engine is running"}









