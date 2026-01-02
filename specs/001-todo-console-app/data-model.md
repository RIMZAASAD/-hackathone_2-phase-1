# Data Model: Todo In-Memory Python Console Application

## Domain Entities

### Todo Entity
Represents a single todo item in the system

**Attributes:**
- `id`: Unique identifier (integer or UUID)
- `title`: Task description (string)
- `completed`: Completion status (boolean)
- `created_at`: Timestamp when the task was created (datetime)

**Business Rules:**
- ID must be unique within the system
- Title must not be empty or whitespace only
- Completed status can be toggled between true/false
- Created timestamp is set when the todo is first created

## Data Relationships

### Todo Collection
- A collection of Todo entities stored in memory
- Maintains order of creation (or can be sorted by user preference)
- Provides unique IDs for each new todo

## Storage Model

### In-Memory Implementation
- Uses Python list or dictionary for storage
- Data exists only during runtime
- No persistence to external storage
- Data is lost when application terminates

**Structure Options:**
1. List of Todo objects: `List[Todo]`
2. Dictionary with ID as key: `Dict[int, Todo]`

**Recommended**: Dictionary with ID as key for efficient lookup operations

## API Contracts

### Todo Operations
- `add_todo(title: str) -> Todo`: Creates a new todo with unique ID
- `get_todo(todo_id: int) -> Todo`: Retrieves a specific todo by ID
- `list_todos() -> List[Todo]`: Returns all todos in the system
- `update_todo(todo_id: int, title: str) -> Todo`: Updates todo title
- `complete_todo(todo_id: int) -> Todo`: Marks todo as completed
- `incomplete_todo(todo_id: int) -> Todo`: Marks todo as incomplete
- `delete_todo(todo_id: int) -> bool`: Removes todo from system

## Validation Rules

### Input Validation
- Todo title must be provided and not empty
- Todo ID must exist for update/delete operations
- Title updates must provide a non-empty value

### Business Validation
- Cannot mark already completed todo as completed
- Cannot mark already incomplete todo as incomplete
- Cannot update or delete non-existent todos