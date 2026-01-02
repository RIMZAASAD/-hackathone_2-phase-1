from src.todo_app.domain.services import TodoService
from src.todo_app.infrastructure.storage import InMemoryTodoRepository


class TodoConsoleApp:
    """Console interface for the todo application"""

    def __init__(self):
        self.repository = InMemoryTodoRepository()
        self.service = TodoService(self.repository)

    def run(self):
        """Main application loop"""
        print("Welcome to the Todo Console Application!")
        print("Available commands: add, list, update, complete, incomplete, delete, help, quit")
        print("Type 'help' for more information or 'quit' to exit.\n")

        while True:
            try:
                command = input("Enter command: ").strip().lower()

                if command == "quit" or command == "exit":
                    print("Goodbye!")
                    break
                elif command == "help":
                    self._show_help()
                elif command.startswith("add "):
                    self._handle_add(command[4:].strip())
                elif command == "list" or command == "view":
                    self._handle_list()
                elif command.startswith("update "):
                    self._handle_update(command[7:].strip())
                elif command.startswith("complete "):
                    self._handle_complete(command[9:].strip())
                elif command.startswith("incomplete "):
                    self._handle_incomplete(command[11:].strip())
                elif command.startswith("delete "):
                    self._handle_delete(command[7:].strip())
                else:
                    print(f"Unknown command: {command}")
                    print("Type 'help' for available commands.\n")

            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}\n")

    def _show_help(self):
        """Display help information"""
        help_text = """
Available commands:
  add <task>           - Add a new task
  list (or view)       - View all tasks
  update <id> <task>   - Update a task (e.g., 'update 1 Buy milk')
  complete <id>        - Mark task as complete (e.g., 'complete 1')
  incomplete <id>      - Mark task as incomplete (e.g., 'incomplete 1')
  delete <id>          - Delete a task (e.g., 'delete 1')
  help                 - Show this help message
  quit (or exit)       - Exit the application

Examples:
  add Buy groceries
  list
  complete 1
  update 2 Buy weekly groceries
  delete 3
        """
        print(help_text)

    def _handle_add(self, task_description: str):
        """Handle add command"""
        if not task_description:
            print("Please provide a task description.\n")
            return

        try:
            todo = self.service.add_todo(task_description)
            print(f"Added task: {todo}\n")
        except ValueError as e:
            print(f"Error adding task: {e}\n")

    def _handle_list(self):
        """Handle list command"""
        todos = self.service.list_todos()

        if not todos:
            print("No tasks found.\n")
        else:
            print("Your tasks:")
            for todo in todos:
                print(f"  {todo}")
            print()

    def _handle_update(self, args: str):
        """Handle update command"""
        try:
            parts = args.split(' ', 1)
            if len(parts) != 2:
                print("Usage: update <id> <new task description>\n")
                return

            todo_id = int(parts[0])
            new_description = parts[1]
            todo = self.service.update_todo(todo_id, new_description)
            print(f"Updated task: {todo}\n")
        except ValueError as e:
            print(f"Error updating task: {e}\n")
        except Exception:
            print("Usage: update <id> <new task description>\n")

    def _handle_complete(self, args: str):
        """Handle complete command"""
        try:
            todo_id = int(args)
            todo = self.service.complete_todo(todo_id)
            if todo:
                print(f"Marked task as complete: {todo}\n")
            else:
                print(f"Task with ID {todo_id} not found.\n")
        except ValueError as e:
            print(f"Error completing task: {e}\n")
        except Exception:
            print("Usage: complete <id>\n")

    def _handle_incomplete(self, args: str):
        """Handle incomplete command"""
        try:
            todo_id = int(args)
            todo = self.service.incomplete_todo(todo_id)
            if todo:
                print(f"Marked task as incomplete: {todo}\n")
            else:
                print(f"Task with ID {todo_id} not found.\n")
        except ValueError as e:
            print(f"Error marking task as incomplete: {e}\n")
        except Exception:
            print("Usage: incomplete <id>\n")

    def _handle_delete(self, args: str):
        """Handle delete command"""
        try:
            todo_id = int(args)
            success = self.service.delete_todo(todo_id)
            if success:
                print(f"Deleted task with ID {todo_id}.\n")
            else:
                print(f"Task with ID {todo_id} not found.\n")
        except ValueError as e:
            print(f"Error deleting task: {e}\n")
        except Exception:
            print("Usage: delete <id>\n")