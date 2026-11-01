"""Task helpers for Lantern."""

_tasks = []


def add_task(title):
    task = {"title":title.strip()}
    _tasks.append(task)
    return task


def list_tasks():
    return _tasks

