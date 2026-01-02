# Quickstart Guide: Menu-Driven In-Memory Todo Console App

**Feature**: Menu-Driven In-Memory Todo Console App
**Created**: 2026-01-01
**Input**: Feature specification and implementation plan

## Prerequisites

- Python 3.13 or higher
- UV package manager (optional but recommended)

## Setup

### 1. Clone or Download the Project
```bash
git clone [repository-url]
cd [project-directory]
```

### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

If no requirements.txt exists, install colorama for color support:
```bash
pip install colorama
```

## Running the Application

### Execute the Application
```bash
python main.py
```

## Using the Application

### Main Menu
The application presents a colorful menu with 7 options:

```
=====================================
    TODO CONSOLE APPLICATION
=====================================
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit
=====================================
Enter your choice (1-7):
```

### Menu Options

#### 1. Add Task
- Prompts for task description
- Creates new task with unique ID
- Sets completion status to incomplete
- Returns to main menu after adding

#### 2. View All Tasks
- Displays all tasks with color-coded status
- Green for completed tasks
- Red for incomplete tasks
- Shows task ID, description, and creation time

#### 3. Update Task
- Prompts for task ID to update
- Prompts for new task description
- Updates the task if ID exists
- Returns to main menu

#### 4. Delete Task
- Prompts for task ID to delete
- Removes task if ID exists
- Returns to main menu

#### 5. Mark Task Complete
- Prompts for task ID to mark complete
- Changes status to completed
- Shows success/error message
- Returns to main menu

#### 6. Mark Task Incomplete
- Prompts for task ID to mark incomplete
- Changes status to incomplete
- Shows success/error message
- Returns to main menu

#### 7. Exit
- Closes the application
- All in-memory data is lost

## Example Usage

```
=====================================
    TODO CONSOLE APPLICATION
=====================================
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit
=====================================
Enter your choice (1-7): 1
Enter task description: Buy groceries
Task added successfully!
=====================================
    TODO CONSOLE APPLICATION
=====================================
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit
=====================================
Enter your choice (1-7): 2
Tasks:
1. [INCOMPLETE] Buy groceries (Created: 2026-01-02 15:30:00)
=====================================
    TODO CONSOLE APPLICATION
=====================================
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit
=====================================
Enter your choice (1-7): 5
Enter task ID to mark complete: 1
Task marked as complete successfully!
```

## Error Handling

- Invalid menu choices show error message and return to menu
- Non-existent task IDs show appropriate error message
- Empty task descriptions are rejected
- Invalid input is handled gracefully with clear messages

## Development

### File Structure
```
src/
├── todo_app/
│   ├── domain/
│   │   ├── models.py        # Todo data structure
│   │   └── services.py      # Business logic
│   ├── infrastructure/
│   │   └── storage.py       # In-memory storage
│   └── presentation/
│       └── menu_cli.py      # Menu-driven interface
├── main.py                  # Application entry point
└── requirements.txt         # Dependencies
```

### Adding New Features
1. Update the data model if new entities are needed
2. Extend services with new business logic
3. Add new menu options to the CLI interface
4. Update validation as needed