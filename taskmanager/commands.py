"""
В этом файле содержатся обработчики команд для командной строки main.py.
"""


import  argparse

from .models import Task
from .storage import Json


class Command:

    def __init__(self, storage: Json = None):
        self.storage = storage or Json()

    def add_task(self, title, description, priority, due_date):
        """Метод добавляет новую задачу."""
        task = Task(title, description, priority, due_date)
        return self.storage.save(task)

    def filter_task(self, status, priority, due_date, filter_flag):
        """Метод возвращает отфильтрованный список."""
        tasks = self.storage.getting_all_tasks()
        if status:
            tasks = list(filter(lambda task: task.status == status, tasks))

        if priority:
            tasks = list(filter(lambda task: task.priority == priority, tasks))

        if due_date:
            tasks = list(filter(lambda task: task.due_date == due_date, tasks))

        if not filter_flag:
            tasks = list(filter(lambda task: task.status == "Выполнено", tasks))

        return tasks

    def complete_task(self, task_id):
        """Метод отмечает задачу, как выполненную."""
        task = self.storage.getting_all_tasks(task_id)
        if task:
            task.change_task_execution_status()
            self.storage.save_tasks(task)
            return True

        raise ValueError(f'Невозможно изменить статус задачи с идентификатором {task_id} на "Выполнено".')

    def delete_task(self, task_id):
        """Метод удаляет задачу"""
        return self.storage.delete_tasks(task_id)

    def get_task(self, task_id):
        """Метод возвращает информацию о задаче по её идентификатору."""
