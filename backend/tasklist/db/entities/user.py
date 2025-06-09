import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from tasklist.db.database import Base
from tasklist.use_cases.dto import user

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(sa.String)
    login: Mapped[str] = mapped_column(sa.String)
    password: Mapped[str] = mapped_column(sa.String)

    def dto(self) -> user.User:
        return user.User(
            id=self.id,
            name=self.name,
            login=self.login,
            password=self.password,
        )