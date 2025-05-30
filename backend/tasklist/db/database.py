from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass

def get_session():
    engine = create_engine('sqlite:///tasklist.db')
    return Session(engine)
