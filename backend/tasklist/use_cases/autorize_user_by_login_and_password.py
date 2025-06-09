from tasklist.repos.user import get_user_by_login_and_password
from tasklist.helper.hash import get_hash


def autorize_user_by_login_and_password(login, password):
    hash_password = get_hash(password)
    result = get_user_by_login_and_password(login, hash_password)
    if result is None:
        raise Exception

    return result.dto() 