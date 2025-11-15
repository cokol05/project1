"""Существующие команды для main.py:
usage: main.py [-h] {add,list,done,delete,view} ...

positional arguments:
  {add,list,done,delete,view}
                        Команды
    add                 Добавить новую задачу
    list                Показать список задач
    done                Отметить задачу как выполненную
    delete              Удалить задачу
    view                Просмотреть детали задачи

options:
  -h, --help            show this help message and exit


Подробное описание команды add:
usage: main.py add [-h] [--description DESCRIPTION] [--priority {low,medium,high}] [--due-date DUE_DATE] title

positional arguments:
  title                 Название задачи

options:
  -h, --help            show this help message and exit
  --description, -d DESCRIPTION
                        Описание задачи
  --priority, -p {low,medium,high}
                        Приоритет задачи
  --due-date DUE_DATE   Дата выполнения (YYYY-MM-DD)


Подробное описание команды list:
usage: main.py list [-h] [--status {Ожидание,Выполнено}] [--priority {low,medium,high}] [--hide-completed]

options:
  -h, --help            show this help message and exit
  --status {Ожидание,Выполнено}
                        Фильтр по статусу
  --priority {low,medium,high}
                        Фильтр по приоритету
  --hide-completed      Скрыть выполненные задачи


Подробное описание команды done:
usage: main.py done [-h] task_id

positional arguments:
  task_id     ID задачи

options:
  -h, --help  show this help message and exit



Подробное описание команды delete:
usage: main.py delete [-h] task_id

positional arguments:
  task_id     ID задачи

options:
  -h, --help  show this help message and exit


Подробное описание команды view:
usage: main.py view [-h] task_id

positional arguments:
  task_id     ID задачи

options:
  -h, --help  show this help message and exit
"""

__version__ = "1.0.0"
__author__ = "Anton"

from .models import Task
from .storage import Json
from .commands import Command, setup_parser
