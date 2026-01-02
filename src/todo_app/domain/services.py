from typing import List, Optional
from src.todo_app.domain.models import Todo
from src.todo_app.infrastructure.storage import InMemoryTodoRepository


class TodoService:
    """Business logic service for todo operations"""

    def __init__(self, repository: InMemoryTodoRepository):
        self.repository = repository

    def add_todo(self, description: str) -> Optional[Todo]:
        """Add a new todo with validation"""
        if not description or not description.strip():
            raise ValueError("Todo description cannot be empty")

        todo = Todo(id=0, description=description.strip())  # ID will be set by repository
        return self.repository.add_todo(todo)

    def list_todos(self) -> List[Todo]:
        """Get all todos"""
        return self.repository.list_todos()

    def get_todo(self, todo_id: int) -> Optional[Todo]:
        """Get a specific todo by ID"""
        return self.repository.get_todo(todo_id)

    def update_todo(self, todo_id: int, description: str) -> Optional[Todo]:
        """Update a todo's description with validation"""
        if not description or not description.strip():
            raise ValueError("Todo description cannot be empty")

        if not self.repository.get_todo(todo_id):
            raise ValueError(f"Todo with ID {todo_id} does not exist")

        return self.repository.update_todo(todo_id, description.strip())

    def complete_todo(self, todo_id: int) -> Optional[Todo]:
        """Mark a todo as complete"""
        if not self.repository.get_todo(todo_id):
            raise ValueError(f"Todo with ID {todo_id} does not exist")

        return self.repository.complete_todo(todo_id)

    def incomplete_todo(self, todo_id: int) -> Optional[Todo]:
        """Mark a todo as incomplete"""
        if not self.repository.get_todo(todo_id):
            raise ValueError(f"Todo with ID {todo_id} does not exist")

        return self.repository.incomplete_todo(todo_id)

    def delete_todo(self, todo_id: int) -> bool:
        """Delete a todo by ID"""
        if not self.repository.get_todo(todo_id):
            raise ValueError(f"Todo with ID {todo_id} does not exist")

        return self.repository.delete_todo(todo_id)