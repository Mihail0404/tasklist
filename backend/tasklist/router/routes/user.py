import fastapi

import tasklist.router.requests as requests
import tasklist.router.responses as responses
from tasklist.repos.user import add_user, get_user_by_login
import tasklist.use_cases as use_cases

router = fastapi.APIRouter()

@router.post("/api/sign-up")
def read_user(user: requests.User):
    result = add_user(user.name, user.login, user.password)

    return result

@router.post("/api/sign-in", response_model=responses.User)
def get_user_by_login_and_password(auth: requests.Auth, response: fastapi.Response):
    result = use_cases.autorize_user_by_login_and_password(auth.login, auth.password)
    user = get_user_by_login(auth.login)
    encoded_userdata = use_cases.get_encoded_user(user.id, user.login, user.name)
    response.set_cookie(key="userdata", value=encoded_userdata)

    return result

@router.get("/api/my-profile", response_model=responses.User)
def get_userdata_by_cookie(request: fastapi.Request):
    try:
        userdata = request.cookies.get('userdata')
        result = use_cases.get_decoded_userdata_by_jwt(userdata)

    except:
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    return result