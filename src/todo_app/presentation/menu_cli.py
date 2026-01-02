from src.todo_app.domain.services import TodoService
from src.todo_app.infrastructure.storage import InMemoryTodoRepository
from .utils import (
    clear_screen, format_success_message, format_error_message,
    format_info_message, format_menu_option, format_completed_task,
    format_incomplete_task, format_task_with_icon, format_task_added,
    format_task_updated, format_task_deleted, format_task_status_changed
)
import os


class MenuCLIApp:
    """Menu-driven console interface for the todo application with colorful output"""

    def __init__(self):
        self.repository = InMemoryTodoRepository()
        self.service = TodoService(self.repository)

    def display_menu(self):
        """Display the colorful menu with numbered options"""
        clear_screen()
        print("=" * 45)
        print(format_info_message("    TODO CONSOLE APPLICATION"))
        print("=" * 45)
        print(format_menu_option("1. Add Task"))
        print(format_menu_option("2. View All Tasks"))
        print(format_menu_option("3. Update Task"))
        print(format_menu_option("4. Delete Task"))
        print(format_menu_option("5. Mark Task Complete"))
        print(format_menu_option("6. Mark Task Incomplete"))
        print(format_menu_option("7. Exit"))
        print("=" * 45)

    def run(self):
        """Main application loop with menu navigation"""
        while True:
            try:
                self.display_menu()
                choice = input("Enter your choice (1-7): ").strip()

                if choice == "1":
                    self._handle_add_task()
                elif choice == "2":
                    self._handle_view_tasks()
                elif choice == "3":
                    self._handle_update_task()
                elif choice == "4":
                    self._handle_delete_task()
                elif choice == "5":
                    self._handle_complete_task()
                elif choice == "6":
                    self._handle_incomplete_task()
                elif choice == "7":
                    print(format_success_message("Goodbye!"))
                    break
                else:
                    print(format_error_message("Invalid choice. Please enter a number between 1 and 7."))
                    input("Press Enter to continue...")

            except KeyboardInterrupt:
                print(format_success_message("\nGoodbye!"))
                break
            except Exception as e:
                print(format_error_message(f"An error occurred: {e}"))
                input("Press Enter to continue...")

    def _handle_add_task(self):
        """Handle Add Task functionality with enhanced feedback and icons"""
        try:
            description = input("Enter task description: ").strip()
            if not description:
                print(format_error_message("Task description cannot be empty."))
                input("Press Enter to continue...")
                return

            todo = self.service.add_todo(description)
            print(format_task_added(todo.id, todo.description))
        except ValueError as e:
            print(format_error_message(f"Error adding task: {e}"))
        except Exception as e:
            print(format_error_message(f"Unexpected error: {e}"))

        input("Press Enter to continue...")

    def _handle_view_tasks(self):
        """Handle View All Tasks functionality with color-coded status and icons"""
        try:
            todos = self.service.list_todos()

            if not todos:
                print(format_info_message("No tasks found."))
            else:
                print(format_info_message("Tasks:"))
                for todo in todos:
                    print(format_task_with_icon(todo.id, todo.description, todo.completed))
        except Exception as e:
            print(format_error_message(f"Error viewing tasks: {e}"))

        input("Press Enter to continue...")

    def _handle_update_task(self):
        """Handle Update Task functionality with enhanced feedback and icons"""
        try:
            task_id_str = input("Enter task ID to update: ").strip()
            if not task_id_str.isdigit():
                print(format_error_message("Invalid task ID. Please enter a number."))
                input("Press Enter to continue...")
                return

            task_id = int(task_id_str)
            new_description = input("Enter new task description: ").strip()

            if not new_description:
                print(format_error_message("Task description cannot be empty."))
                input("Press Enter to continue...")
                return

            todo = self.service.update_todo(task_id, new_description)
            print(format_task_updated(todo.id, todo.description, todo.completed))
        except ValueError as e:
            print(format_error_message(f"Error updating task: {e}"))
        except Exception as e:
            print(format_error_message(f"Unexpected error: {e}"))

        input("Press Enter to continue...")

    def _handle_delete_task(self):
        """Handle Delete Task functionality with enhanced feedback and icons"""
        try:
            task_id_str = input("Enter task ID to delete: ").strip()
            if not task_id_str.isdigit():
                print(format_error_message("Invalid task ID. Please enter a number."))
                input("Press Enter to continue...")
                return

            task_id = int(task_id_str)
            # Get the task before deletion to show its details
            todo = self.service.get_todo(task_id)
            success = self.service.delete_todo(task_id)
            if success and todo:
                print(format_task_deleted(todo.id, todo.description))
            else:
                print(format_error_message(f"Task with ID {task_id} not found."))
        except ValueError as e:
            print(format_error_message(f"Error deleting task: {e}"))
        except Exception as e:
            print(format_error_message(f"Unexpected error: {e}"))

        input("Press Enter to continue...")

    def _handle_complete_task(self):
        """Handle Mark Task Complete functionality with enhanced feedback and icons"""
        try:
            task_id_str = input("Enter task ID to mark complete: ").strip()
            if not task_id_str.isdigit():
                print(format_error_message("Invalid task ID. Please enter a number."))
                input("Press Enter to continue...")
                return

            task_id = int(task_id_str)
            todo = self.service.complete_todo(task_id)
            print(format_task_status_changed(todo.id, todo.description, todo.completed))
        except ValueError as e:
            print(format_error_message(f"Error completing task: {e}"))
        except Exception as e:
            print(format_error_message(f"Unexpected error: {e}"))

        input("Press Enter to continue...")

    def _handle_incomplete_task(self):
        """Handle Mark Task Incomplete functionality with enhanced feedback and icons"""
        try:
            task_id_str = input("Enter task ID to mark incomplete: ").strip()
            if not task_id_str.isdigit():
                print(format_error_message("Invalid task ID. Please enter a number."))
                input("Press Enter to continue...")
                return

            task_id = int(task_id_str)
            todo = self.service.incomplete_todo(task_id)
            print(format_task_status_changed(todo.id, todo.description, todo.completed))
        except ValueError as e:
            print(format_error_message(f"Error marking task as incomplete: {e}"))
        except Exception as e:
            print(format_error_message(f"Unexpected error: {e}"))

        input("Press Enter to continue...")