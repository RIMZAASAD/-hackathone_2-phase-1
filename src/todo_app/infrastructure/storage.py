from typing import Dict, List, Optional
from src.todo_app.domain.models import Todo


class InMemoryTodoRepository:
    """In-memory storage implementation for Todo items"""

    def __init__(self):
        self._todos: Dict[int, Todo] = {}
        self._next_id = 1

    def add_todo(self, todo: Todo) -> Todo:
        """Add a new todo to the repository"""
        # Set the ID to the next available ID
        todo.id = self._next_id
        self._todos[todo.id] = todo
        self._next_id += 1
        return todo

    def list_todos(self) -> List[Todo]:
        """Get all todos"""
        return list(self._todos.values())

    def get_todo(self, todo_id: int) -> Optional[Todo]:
        """Get a specific todo by ID"""
        return self._todos.get(todo_id)

    def update_todo(self, todo_id: int, description: str) -> Optional[Todo]:
        """Update a todo's description"""
        if todo_id not in self._todos:
            return None

        todo = self._todos[todo_id]
        todo.description = description
        return todo

    def complete_todo(self, todo_id: int) -> Optional[Todo]:
        """Mark a todo as complete"""
        if todo_id not in self._todos:
            return None

        todo = self._todos[todo_id]
        todo.completed = True
        return todo

    def incomplete_todo(self, todo_id: int) -> Optional[Todo]:
        """Mark a todo as incomplete"""
        if todo_id not in self._todos:
            return None

        todo = self._todos[todo_id]
        todo.completed = False
        return todo

    def delete_todo(self, todo_id: int) -> bool:
        """Delete a todo by ID"""
        if todo_id not in self._todos:
            return False

        del self._todos[todo_id]
        return True