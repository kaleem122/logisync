from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import engine
from sqlmodel import SQLModel
import models

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Booting up: Instructing Supabase to build tables...")
    SQLModel.metadata.create_all(engine)
    yield



app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Logisync engine is running"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": [
            {"id": 1, "action": "Book loading zone in Haymarket", "status" : "running"},
            {"id": 2, "action": "Procure functional dishwasher", "status" : "in_progress"}
            ]
    }
    
