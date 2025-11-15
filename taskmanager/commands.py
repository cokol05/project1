"""
В этом файле содержатся обработчики команд для командной строки main.py.
"""


import  argparse

from .models import Task
from .storage import Json


class Command:
    """Класс служит для управления задачами через командную строку.

    Attributes:
        storage: Объект для работы с хранилищем задач.
    """

    def __init__(self, storage: Json = None):
        """Метод инициализирует атрибут класса.

        Args:
            storage: Объект хранилища задач. Если не указан, используется Json("tasks.json").
        """
        self.storage = storage or Json("tasks.json")

    def add_task(self, title, description, priority, due_date):
        """Метод добавляет новую задачу.

        Args:
            title: Название задачи.
            description: Описание задачи.
            priority: Приоритет задачи (low, medium, high).
            due_date: Дата выполнения в формате YYYY-MM-DD.

        Returns:
            bool: Результат операции сохранения.
        """
        task = Task(
            title=title,
            description=description,
            priority=priority,
            due_date=due_date
        )
        return self.storage.save_tasks(task)

    def filter_task(self, status=None, priority=None, due_date=None, filter_flag=False):
        """Метод возвращает отфильтрованный список.

        Args:
            status: Статус задачи для фильтрации ("Ожидание", "Выполнено").
            priority: Приоритет задачи для фильтрации ("low", "medium", "high").
            due_date: Дата выполнения для фильтрации.
            filter_flag: Если True, скрывает выполненные задачи.

        Returns:
            list: Отфильтрованный список объектов Task.
        """
        tasks = self.storage.getting_all_tasks()

        if status:
            tasks = list(filter(lambda task: task.status == status, tasks))

        if priority:
            tasks = list(filter(lambda task: task.priority == priority, tasks))

        if due_date:
            tasks = list(filter(lambda task: task.due_date == due_date, tasks))

        if filter_flag:
            tasks = list(filter(lambda task: task.status != "Выполнено", tasks))

        return tasks

    def complete_task(self, task_id):
        """Метод отмечает задачу, как выполненную.

        Args:
            task_id: Идентификатор задачи для изменения статуса.

        Returns:
            bool: True если операция выполнена успешно.

        Raises:
            ValueError: Если задача с указанным ID не найдена.
        """
        tasks = self.storage.getting_all_tasks()

        for task in tasks:
            if task.id == task_id:
                task.change_task_execution_status()
                self.storage.save_tasks(task)
                return True

        raise ValueError(f'Невозможно изменить статус задачи с идентификатором {task_id} на "Выполнено".')

    def delete_task(self, task_id):
        """Метод удаляет задачу.

        Args:
            task_id: Идентификатор задачи для удаления.

        Returns:
            bool: Результат операции удаления.
        """
        return self.storage.delete_task(task_id)

    def get_task(self, task_id):
        """Метод возвращает информацию о задаче по её идентификатору.

        Args:
            task_id: Идентификатор задачи.

        Returns:
            Task: Если объект задачи найден.
            None: Если Объект задачи не найден.
        """
        tasks = self.storage.getting_all_tasks()
        for task in tasks:
            if task.id == task_id:
                return task

        return None


def setup_parser():
    """Метод создает команды для командной строки.

    Returns:
        argparse.ArgumentParser: Настроенный парсер аргументов.
    """
    parser = argparse.ArgumentParser(description="Консольный менеджер задач")
    subparsers = parser.add_subparsers(dest="command", help="Команды")

    add_parser = subparsers.add_parser("add", help="Добавить новую задачу")
    add_parser.add_argument("title", help="Название задачи")
    add_parser.add_argument("--description", "-d", help="Описание задачи", default="")
    add_parser.add_argument("--priority", "-p", choices=["low", "medium", "high"], default="medium", help="Приоритет задачи")
    add_parser.add_argument("--due-date", help="Дата выполнения (YYYY-MM-DD)")

    list_parser = subparsers.add_parser("list", help="Показать список задач")
    list_parser.add_argument("--status", choices=["Ожидание", "Выполнено"], help="Фильтр по статусу")
    list_parser.add_argument("--priority", choices=["low", "medium", "high"], help="Фильтр по приоритету")
    list_parser.add_argument("--hide-completed", action="store_true", help="Скрыть выполненные задачи")

    done_parser = subparsers.add_parser("done", help="Отметить задачу как выполненную")
    done_parser.add_argument("task_id", type=int, help="ID задачи")

    delete_parser = subparsers.add_parser("delete", help="Удалить задачу")
    delete_parser.add_argument("task_id", type=int, help="ID задачи")

    view_parser = subparsers.add_parser("view", help="Просмотреть детали задачи")
    view_parser.add_argument("task_id", type=int, help="ID задачи")

    return parser
