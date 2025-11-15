"""
В этом файле размещены функции, отвечающие за действия над задачами.
"""


import json
import os

from .models import Task


class Json:
    """Класс служит для взаимодействия программы с json-файлом.

    Atributes:
        filename (str): Путь к json-файлу.

    Позволяет:
        создавать,
        записывать,
        сохранять изменения в этот файл,

        читать,
        выводить список задач из файла,

        создавать новый ID,
        удалять задачу, перезаписывая json-файл.

    """

    def __init__(self, filename):
        """Метод инициализирует атрибут класса.

        Args:
            filename (str): Путь к json-файлу.
        """
        self.filename = filename
        self.create_a_file_if_it_does_not_exist()

    def create_a_file_if_it_does_not_exist(self):
        """Метод создаст json-файл с пустым списком, если он не существует."""
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8-sig') as f:
                json.dump(list(), f)

    def load_tasks(self):
        """Метод считывает информацию о существующих задачах из json-файла.

        Returns:
            list: Список словарей с информацией о задачах из json-файла ИЛИ пустой список в случае ошибки.
        """
        try:
            with open(self.filename, 'r', encoding='utf-8-sig') as f:
                return json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            print("Возникла ошибка при попытки чтения файла! Возможно, файл был перемещён или повреждён.")
            return []

    def write_tasks(self, tasks):
        """Запись изменений в json-файл.

        Args:
            tasks (list): Список задач для записи их в json-файл.
        """
        with open(self.filename, 'w', encoding='utf-8-sig') as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)

    def save_tasks(self, task):
        """Метод записывает или обновляет информацию о текущей задачи в json-файл.
        Если задача существует, то производит обновление данных об этой задаче.

        Args:
            task (Task): Объект задачи для сохранения.

        Returns:
            Task: Сохраненная задача с обновлёнными данными. Новые задачи вернутся с присвоенным ID.
        """
        load_tasks = self.load_tasks()

        if task.id is None:
            task.id = self.creating_a_new_id(load_tasks)
            load_tasks.append(task.to_dict())
        else:
            for i, cur_task in enumerate(load_tasks):
                if cur_task["id"] == task.id:
                    load_tasks[i] = task.to_dict()
                    break

        self.write_tasks(load_tasks)
        return task

    def getting_all_tasks(self):
        """Метод отображает все задачи.

        Returns:
            list: Список объектов Task, преобразованных из json-файла.
        """
        load_tasks = self.load_tasks()
        return [Task.from_dict(task) for task in load_tasks]  # проверить

    def creating_a_new_id(self, tasks):
        """Метод создает следующее значение идентификатора.

        Args:
            tasks (list): Список существующих задач.

        Returns:
            int: Новый уникальный идентификатор для новой задачи ИЛИ 1, если это первая задача.
        """
        if not tasks:
            return 1
        return max(task["id"] for task in tasks) + 1

    def delete_task(self, task_id):
        """Метод удаляет задачи.

        Args:
            task_id (int): Идентификатор задачи.

        Returns:
            bool: True, если задача успешно удалена.

        Raises:
            ValueError: Если задача не найдена по идентификатору.
        """
        task_r = self.load_tasks()
        for i, cur_task in enumerate(task_r):
            if cur_task["id"] == task_id:
                del task_r[i]
                self.write_tasks(task_r)
                return True

        raise ValueError(f"Задача с идентификатором task_id {task_id} не найдена.")
