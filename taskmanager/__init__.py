"""
Консольный менеджер задач
"""

__version__ = "1.0.0"
__author__ = "Anton"

from .models import Task
from .storage import Json
from .commands import Command, setup_parser
