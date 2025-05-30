from sqlalchemy import select
from tasklist.helper import hash
from tasklist.db.entities.user import User
from tasklist.db.database import get_session

def add_user(name, login, pwd):
    # try:
    hash_pwd = hash.get_hash(pwd)

    session = get_session()
    user = User(
        name = name,
        login = login,
        password = hash_pwd,
    )
    session.add(user)
    session.commit()

    return user
    # except: return {"error": True}


def check_password(login, pwd):
    hash_pwd = hash.get_hash(pwd)

    session = get_session()

    result = select(User).where(User.login == login).where(User.password == hash_pwd)
    if(len(list(session.scalars(result)))):
        return {"is_password_correct": True}
    else:
        return {"is_password_correct": False}