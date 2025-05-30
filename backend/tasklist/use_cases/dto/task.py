import pydantic

class Task(pydantic.BaseModel):
    id: int
    owner_id: int 
    name: str
    description: str
    completed_at: str | None
    created_at: str
