from tasklist import repos


def get_task_by_id(id):
    return repos.task.get_task_by_id(id)