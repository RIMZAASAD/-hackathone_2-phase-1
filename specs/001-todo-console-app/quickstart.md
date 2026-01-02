# Quickstart: Todo In-Memory Python Console Application

## Prerequisites

- Python 3.13+ installed
- UV package manager installed (for environment management)

## Setup

1. Clone or navigate to the project directory
2. Create and activate a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies (if any beyond standard library):
   ```bash
   uv pip install -r requirements.txt
   ```

## Running the Application

1. Navigate to the project root directory
2. Run the main application:
   ```bash
   python src/main.py
   ```
3. The console application will start and display available commands

## Using the Application

### Available Commands

- `add "task description"` - Add a new todo
  Example: `add "Buy groceries"`

- `list` - View all todos with their status
  Example: `list`

- `complete <id>` - Mark a todo as complete
  Example: `complete 1`

- `incomplete <id>` - Mark a todo as incomplete
  Example: `incomplete 1`

- `update <id> "new description"` - Update a todo's description
  Example: `update 1 "Buy weekly groceries"`

- `delete <id>` - Delete a todo
  Example: `delete 1`

- `help` - Show available commands
  Example: `help`

- `quit` or `exit` - Exit the application
  Example: `quit`

## Example Session

```
Welcome to the Todo Console Application!
Type 'help' for available commands.

> add "Buy groceries"
Added todo: Buy groceries (ID: 1)

> add "Walk the dog"
Added todo: Walk the dog (ID: 2)

> list
Todos:
1. [ ] Buy groceries
2. [ ] Walk the dog

> complete 1
Todo 1 marked as complete: Buy groceries

> list
Todos:
1. [x] Buy groceries
2. [ ] Walk the dog

> quit
Goodbye!
```

## Development

To modify the application:

1. Domain logic is in `src/todo_app/domain/`
2. Storage implementation is in `src/todo_app/infrastructure/`
3. Console interface is in `src/todo_app/presentation/`
4. Main application entry point is `src/main.py`

## Memory-Only Behavior

- All data is stored in memory only
- Data is lost when the application exits
- Each session starts with an empty todo list
- Maximum recommended number of todos: 1000 (for performance)