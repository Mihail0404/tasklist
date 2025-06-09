from tasklist.db import entities
from tasklist.db.database import get_session
from tasklist.use_cases.dto import task
import sqlalchemy as sa
from tasklist.db.entities.task import Task
from datetime import datetime


def add_task(owner_id, name, description, completed_at):
    session = get_session()
    task = entities.Task(
        owner_id = owner_id,
        name = name,
        description = description,
        completed_at = completed_at,
        created_at = datetime.now()
    )
    session.add(task)
    session.commit()

    return task.dto()
    

def delete_task(id):
    session = get_session()

    current_task = sa.select(Task).where(Task.id ==  id)
    task = session.scalars(current_task).one()
    session.delete(task)
    session.commit()
    return task
    

def get_tasks_by_owner_id(owner_id):
    session = get_session()
    result = sa.select(Task).where(Task.owner_id == owner_id)
    tasks_from_db = list(session.scalars(result))
    tasks = []
    for task_from_db in tasks_from_db:
        tasks.append(task.Task(id=task_from_db.id,
                            owner_id=task_from_db.owner_id,
                            name=task_from_db.name,
                            description=task_from_db.description,
                            completed_at=task_from_db.completed_at,
                            created_at=task_from_db.created_at))
    return tasks