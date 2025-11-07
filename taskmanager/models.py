"""
Этот файл содержит класс Task, который описывает структуру одной задачи.
Здесь определяются, какие данные хранятся в каждой задаче.
"""


from datetime import datetime


class Task():

    def __init__(self, title, description, priority, due_date=None, id = None, status=None, created_date=None, completed_date=None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status or "Ожидание"
        self.priority = priority
        self.created_date = created_date or datetime.now().isoformat()
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

    @classmethod
    def from_dict(cls, data):
        """Метод для создания объекта из словаря."""
        return cls(
            id=data['id'],
            title=data['title'],
            description=data['description'],
            status=data['status'],
            priority=data['priority'],
            created_date=data['created_date'],
            due_date=data['due_date'],
            completed_date=data['completed_date']
        )

    def change_task_execution_status(self):
        self.status = "Выполнено"
        self.completed_date = datetime.now().isoformat()

    def __str__(self):
        """Метод отображает информацию о задачах."""
        status_icon = "✅" if self.status == "Выполнено" else "⏳"
        priority_icons = {
            "low": "🔽",
            "medium": "🔼",
            "high": "🔴"
        }
        priority_icon = priority_icons.get(self.priority, "🔼")

        due_info = ""
        if self.due_date:
            due_info = f" | 📅 {self.due_date}"

        return f"{status_icon} #{self.id} {priority_icon} {self.title}{due_info}"
