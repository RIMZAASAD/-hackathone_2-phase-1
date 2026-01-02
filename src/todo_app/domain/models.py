from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Todo:
    """
    Represents a single todo item with properties for identification,
    content, status, and creation timestamp.
    """
    id: int
    description: str
    completed: bool = False
    created_at: datetime = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

    def __str__(self) -> str:
        status = "X" if self.completed else "O"
        return f"[{status}] {self.id}: {self.description} (Created: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')})"