"""
Этот файл содержит класс Task, который описывает структуру одной задачи.
Здесь определяются, какие данные хранятся в каждой задаче.
"""


from datetime import datetime


class Task():

    def __init__(self, id, title, description, status, priority, created_date, due_date, completed_date):
        self.id = id
        self.title = title
        self.description = description
        self.status = "Ожидание завершения выполнения задачи"
        self.priority = priority
        self.created_date = datetime.now().isoformat()
        self.due_date = due_date
        self.completed_date = completed_date

    def to_dict(self):
        """Метод для преобразования в словарь для сохранения."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'priority': self.priority,
            'created_date': self.created_date,
            'due_date': self.due_date,
            'completed_date': self.completed_date,
        }

    def from_dict(self, data):
        """Метод для создания объекта из словаря."""
        return (data['id'], data['title'], data['description'], data['status'], data['priority'], data['created_date'],
                data['due_date'], data['completed_date'])

    def change_the_task_execution_status(self):
        """Метод для изменения статуса выполнения задачи"""
        self.status = "Задача выполнена"
        self.completed_date = datetime.now().isoformat()

    def change_task_execution_status(self):
        self.status = "Выполнено"
        self.completed_date = datetime.now().isoformat()

    def __str__(self):
        pass
