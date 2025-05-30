from sqlalchemy import update
from tasklist.db.entities.task import Task
from tasklist.db.database import get_session


def update_task(id, name, description, completed_at):
    session = get_session()

    try:
        update(Task).where(Task.id == id).values(name=name, description=description, completed_at=completed_at)
        session.commit()
        return {"errors": False}
    except:
        return {"errors": True}