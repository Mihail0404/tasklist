from tasklist import repos


def get_tasks_by_owner_id(owner_id):
    return repos.task.get_tasks_by_owner_id(owner_id)