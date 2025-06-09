from tasklist import repos


def add_task(owner_id, name, description, completed_at):
    return repos.task.add_task(owner_id, name, description, completed_at)