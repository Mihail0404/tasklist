from tasklist import use_cases
import fastapi


def check_user_cookie(request: fastapi.Request, owner_id):
    try:
        jwt_with_userdata = request.cookies.get('userdata')
        decoded_userdata = use_cases.get_decoded_userdata_by_jwt(jwt_with_userdata)
        if owner_id == decoded_userdata['id']:
            return True
        else:
            return False
    except:
        return False
    
def check_delete_permission(request: fastapi.Request, task_id):
    try:
        jwt_with_userdata = request.cookies.get('userdata')
        decoded_userdata = use_cases.get_decoded_userdata_by_jwt(jwt_with_userdata)
        task = use_cases.get_task_by_id(task_id)
        if task.owner_id == decoded_userdata['id']:
            return True
        else:
            return False
    except:
        return False