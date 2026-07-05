from pydantic import BaseModel
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from database import engine, get_session
from sqlmodel import SQLModel, Session, select
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
def get_tasks(session: Session = Depends(get_session)):
    tasks = session.exec(select(models.Task)).all()
    return tasks

@app.post("/tasks")
def create_task(task: models.Task, session: Session = Depends(get_session)):
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@app.post("/moves")
def create_move(move: models.Move, session: Session = Depends(get_session)):
    session.add(move)
    session.commit()
    session.refresh(move)
    return move

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(models.Task, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    session.delete(task)
    session.commit()
    return {"message": f"Task {task_id} deleted successfully from the cloud"}

class TaskUpdate(BaseModel):
    status: str

@app.patch("/tasks/{task_id}")
def update_task(task_id: int, update_data: TaskUpdate, session: Session = Depends(get_session)):
    
    task = session.get(models.Task, task_id)

    if not task:
        raise HTTPException(status_code = 404, detail="Task not found")
    
    task.status = update_data.status

    session.add(task)
    session.commit()    
    session.refresh(task)
    return task

    
    


