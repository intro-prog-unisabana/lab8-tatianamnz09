"""Laboratorio 8 - CLI del gestor de tareas."""

import sys
from todo_manager import read_todo_file, write_todo_file

HELP_MESSAGE = """Usage: python main.py <file_path> <command> [arguments]...

Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.

Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view"""

try:
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print(HELP_MESSAGE)
        sys.exit(0)

    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")

    file_path = sys.argv[1]
    args = sys.argv[2:] 


    tasks = read_todo_file(file_path)


    if not args:
        sys.exit(0)

    i = 0
    while i < len(args):
        command = args[i]

        if command == "view":
            print("Tasks:")
            for task in tasks:
                print(task)
            i += 1

        elif command == "add":
            if i + 1 >= len(args):
                raise IndexError('Task description required for "add".')
            task_desc = args[i + 1]
            tasks.append(task_desc)
            print(f'Task "{task_desc}" added.')
            i += 2

        elif command == "remove":
            if i + 1 >= len(args):
                raise IndexError('Task description required for "remove".')
            task_desc = args[i + 1]
            try:
                tasks.remove(task_desc)
                print(f'Task "{task_desc}" removed.')
            except ValueError:
                print(f'Task "{task_desc}" not found.')
            i += 2

        else:
            raise ValueError("Command not found!")

    write_todo_file(file_path, tasks)

except IndexError as e:
    print(e)
except ValueError as e:
    print(e)
