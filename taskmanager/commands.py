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
        """Метод добавляет новую задачу"""
        task = Task(title, description, priority, due_date)
        return self.storage.save(task)

    def filter_task(self, status, priority, due_date):
        """Метод возвращает отфильтрованный список"""
        tasks = self.storage.getting_all_tasks()
        if status:
            tasks = list(filter(lambda task: task.status == status, tasks))

        if priority:
            tasks = list(filter(lambda task: task.priority == priority, tasks))

        if due_date:
            tasks = list(filter(lambda task: task.due_date == due_date, tasks))

        # Добавить сортировку только задач, ожидающих выполнение или выполненных

        return tasks
