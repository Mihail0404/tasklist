import fastapi

import typing
import tasklist.router.requests as requests
import tasklist.router.responses as responses 
from tasklist.use_cases import add_task, get_tasks_by_owner_id, delete_task, update_task, check_user_cookie


router = fastapi.APIRouter()

@router.post("/api/tasks", response_model= responses.Task)
def create_task(task: requests.Task):
    result = add_task.add_task(task.owner_id, task.name, task.description, task.completed_at)
    return result

@router.get("/api/tasks" ,response_model= list[responses.Task])
def read_user_task_by_id(owner_id: typing.Annotated[int, fastapi.Query(alias='ownerId')], request: fastapi.Request):
        if check_user_cookie.check_user_cookie(request, owner_id):
            result = get_tasks_by_owner_id.get_tasks_by_owner_id(owner_id)
            return result
        else:
            raise fastapi.HTTPException(status_code=fastapi.status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

@router.patch("/api/update-task")
def refresh_task(id:int, name:str, description:str, completed_at:str):
    result = update_task.update_task(id, name, description, completed_at)
    return result

@router.delete("/api/tasks/{id}", response_model= responses.Task)
def remove_task(id: int, request: fastapi.Request):
    if check_user_cookie.check_delete_permission(request, id):
        result = delete_task.delete_task(id)
        return result
    else:
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")