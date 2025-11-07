import sys
from taskmanager.commands import Command, setup_parser


def main():
    parser = setup_parser()
    args = parser.parse_args()

    commands = Command()

    if not args.command:
        parser.print_help()
        return

    try:
        if args.command == "add":
            task = commands.add_task(
                title=args.title,
                description=args.description,
                priority=args.priority,
                due_date=args.due_date
            )
            print(f"✅ Задача добавлена (ID: {task.id}): {task.title}")

        elif args.command == "list":
            tasks = commands.filter_task(
                status=args.status,
                priority=args.priority,
                filter_flag=args.hide_completed
            )

            if not tasks:
                print("📝 Нет задач для отображения")
                return

            pending_tasks = [t for t in tasks if t.status == "Ожидание"]
            completed_tasks = [t for t in tasks if t.status == "Выполнено"]

            if pending_tasks:
                print("\n📋 Активные задачи:")
                for task in pending_tasks:
                    print(f"  {task}")

            if completed_tasks:
                print("\n✅ Выполненные задачи:")
                for task in completed_tasks:
                    print(f"  {task}")

            print(f"\n📊 Итого: {len(pending_tasks)} активных, {len(completed_tasks)} выполненных")

        elif args.command == "done":
            if commands.complete_task(args.task_id):
                print(f"✅ Задача #{args.task_id} отмечена как выполненная")
            else:
                print(f"❌ Задача #{args.task_id} не найдена")

        elif args.command == "delete":
            if commands.delete_task(args.task_id):
                print(f"🗑️ Задача #{args.task_id} удалена")
            else:
                print(f"❌ Задача #{args.task_id} не найдена")

        elif args.command == "view":
            task = commands.get_task(args.task_id)
            if task:
                print(f"\n📄 Детали задачи #{task.id}:")
                print(f"  Заголовок: {task.title}")
                print(f"  Описание: {task.description}")
                print(f"  Приоритет: {task.priority}")
                print(f"  Статус: {task.status}")
                print(f"  Создана: {task.created_date}")
                if task.due_date:
                    print(f"  Срок выполнения: {task.due_date}")
                if task.completed_date:
                    print(f"  Завершена: {task.completed_date}")
            else:
                print(f"❌ Задача #{args.task_id} не найдена")

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
