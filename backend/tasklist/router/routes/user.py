from fastapi import APIRouter

from tasklist.router.requests.user import User, Auth
from tasklist.repos.user import add_user, check_password

router = APIRouter()

@router.post("/api/sign-up")
def read_user(user: User):
    result = add_user(user.name, user.login, user.password)
    return result

@router.post("/api/sign-in")
def check_user_password(auth: Auth):
    result = check_password(auth.login, auth.password)
    return result
