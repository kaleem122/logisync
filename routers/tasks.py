from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from pydantic import BaseModel 
import models
from database import get_session

router = APIRouter(prefix = "/tasks", tags = ["tasks"])

@router.get("/")
def get_tasks(session: Session = Depends(get_session)):
    tasks = session.exec(select(models.Task)).all()
    return tasks


@router.post("/")
def create_task(task: models.Task, session: Session = Depends(get_session)):
    session.add(task) 
    session.commit()
    session.refresh(task)
    return task

@router.delete("/{task_id}")
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(models.Task, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    session.delete(task)
    session.commit()
    return {"message": f"Task {task_id} deleted successfully from the cloud"}

class TaskUpdate(BaseModel):
    status: str

@router.patch("/{task_id}")
def update_task(task_id: int, update_data: TaskUpdate, session: Session = Depends(get_session)):
    task = session.get(models.Task, task_id)
    if not task: 
        raise HTTPException(status_code=404, detail = "Task not found")
    task.status = update_data.status
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


    

