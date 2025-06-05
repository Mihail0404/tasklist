from tasklist import repos

    
def delete_task(id):
    return repos.task.delete_task(id).dto()