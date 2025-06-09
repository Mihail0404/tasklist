import sqlalchemy as sa
from tasklist.helper import hash
from tasklist.db.entities.user import User
from tasklist.db.database import get_session

def add_user(name, login, pwd):
    # try:
    hash_password = hash.get_hash(pwd)

    session = get_session()
    user = User(
        name = name,
        login = login,
        password = hash_password,
    )
    session.add(user)
    session.commit()

    return user.dto()


def get_user_by_login_and_password(login: str, password: str):
    session = get_session()
    return session.scalars(sa.select(User).filter_by(login=login, password=password)).one_or_none()

def get_user_by_login(login: str):
    session = get_session()
    user = session.scalars(sa.select(User).filter_by(login=login)).one_or_none()
    return user