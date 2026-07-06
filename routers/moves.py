from fastapi import APIRouter, Depends
from sqlmodel import Session
import models
from database import get_session

router = APIRouter(prefix = "/moves", tags = ["moves"])

@router.post("/")
def create_move(move: models.Move, session:Session = Depends(get_session)):
    session.add(move)
    session.commit()
    session.refresh(move)
    return move


