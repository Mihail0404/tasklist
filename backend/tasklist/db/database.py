from sqlalchemy.orm import DeclarativeBase, Session
import sqlalchemy as sa
class Base(DeclarativeBase):
    pass

def get_session():
    engine = sa.create_engine('sqlite:///tasklist.db')
    return Session(engine)
