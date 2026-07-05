from typing import Optional
from sqlmodel import SQLModel, Field



class Move(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    name: str           # e.g., "Haymarket Relocation"
    date: str           # e.g., "June 2026"


class Task(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    action: str           # e.g., "Load cargo"
    status: str = Field(default = "pending")
    move_id : Optional[int] = Field(default = None, foreign_key = "move.id")

class Asset(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    name: str           # e.g., "Pre-owned Dishwasher"
    price: float
    condition: str      # e.g., "Used"

    move_id: Optional[int] = Field(default = None, foreign_key = "move.id")
        
    