from sqlalchemy import  Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from tasklist.db.database import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    login: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)