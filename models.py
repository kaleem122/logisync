from typing import Optional
from sqlmodel import SQLModel, Field

class Task(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    action: str
    status: str = Field(default = "pending")
        
    