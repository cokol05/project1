"""
В этом файле содержатся обработчики команд для командной строки main.py.
"""


import  argparse

from .models import Task
from .storage import Json


class Command:

    def __init__(self, storage: Json = None):
        self.storage = storage or Json("tasks.json")

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


def setup_parser():
    """Метод создает команды для командной строки"""
    parser = argparse.ArgumentParser(description="Консольный менеджер задач")
    subparsers = parser.add_subparsers(dest="commands", help="Команды")

    add_parser = subparsers.add_parser("add", help="Добавить новую задачу")
    add_parser.add_argument("title", help="Название задачи")
    add_parser.add_argument("--description", "-d", help="Описание задачи", default="")
    add_parser.add_argument("--priority", "-p", choices=["low", "medium", "high"], default="medium", help="Приоритет задачи")
    add_parser.add_argument("--due-date", help="Дата выполнения (YYYY-MM-DD)")

    list_parser = subparsers.add_parser("list", help="Показать список задач")
    list_parser.add_argument("--status", choices=["pending", "completed"], help="Фильтр по статусу")
    list_parser.add_argument("--priority", choices=["low", "medium", "high"], help="Фильтр по приоритету")
    list_parser.add_argument("--hide-completed", action="store_true", help="Скрыть выполненные задачи")

    done_parser = subparsers.add_parser("done", help="Отметить задачу как выполненную")
    done_parser.add_argument("task_id", type=int, help="ID задачи")

    delete_parser = subparsers.add_parser("delete", help="Удалить задачу")
    delete_parser.add_argument("task_id", type=int, help="ID задачи")

    view_parser = subparsers.add_parser("view", help="Просмотреть детали задачи")
    view_parser.add_argument("task_id", type=int, help="ID задачи")

    return parser
