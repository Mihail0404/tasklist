import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from tasklist.db.database import Base
from tasklist.use_cases.dto import task
class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(sa.Integer)
    name: Mapped[str] = mapped_column(sa.String)
    description: Mapped[str] = mapped_column(sa.String)
    completed_at: Mapped[str] = mapped_column(sa.String, nullable=True)
    created_at: Mapped[str] = mapped_column(sa.String)
    
    def dto(self) -> task.Task:
        return task.Task(
            id=self.id,
            owner_id=self.owner_id,
            name=self.name,
            description=self.description,
            completed_at=self.completed_at,
            created_at=self.created_at,
        )