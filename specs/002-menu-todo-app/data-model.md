# Data Model: Menu-Driven In-Memory Todo Console App

**Feature**: Menu-Driven In-Memory Todo Console App
**Created**: 2026-01-02
**Input**: Feature specification from `/specs/002-menu-todo-app/spec.md`

## Entities

### Todo Task

**Description**: Represents a single todo item with properties for identification, content, status, and creation timestamp.

**Fields**:
- `id` (int): Unique identifier assigned when task is created (primary key)
- `description` (str): Text content describing the task
- `completed` (bool): Status indicator showing whether task is completed (default: False)
- `created_at` (datetime): Timestamp when task was created

**Validation Rules**:
- `id` must be a positive integer
- `description` must not be empty or contain only whitespace
- `completed` must be a boolean value
- `created_at` must be a valid datetime object

**State Transitions**:
- `completed` can transition from False to True (mark complete)
- `completed` can transition from True to False (mark incomplete)
- `description` can be updated while maintaining the same `id`

**Relationships**:
- No direct relationships with other entities
- Belongs to the in-memory collection of tasks

## Data Flow

### Creation
1. User provides description through menu option
2. System assigns next available ID
3. System sets completion status to False
4. System records creation timestamp
5. Task is added to in-memory collection

### Reading
1. System retrieves all tasks from in-memory collection
2. Tasks are displayed with color-coded status indicators
3. IDs are shown for reference in other operations

### Update
1. User provides task ID and new description
2. System validates ID exists
3. System updates description field
4. Other fields remain unchanged

### Deletion
1. User provides task ID
2. System validates ID exists
3. System removes task from collection
4. Original ID is not reused (creates gap in sequence)

### Status Changes
1. User provides task ID
2. System validates ID exists
3. System toggles completed status
4. Other fields remain unchanged

## Storage Structure

### In-Memory Collection
- **Type**: Dictionary mapping ID (int) to Todo object
- **Key**: Unique task ID
- **Value**: Todo object instance
- **Access Pattern**: Direct lookup by ID for O(1) retrieval
- **Iteration**: Sequential access for display operations

### ID Generation
- **Starting Point**: 1
- **Increment**: Sequential (1, 2, 3, ...)
- **Reuse Policy**: IDs are not reused after deletion
- **Collision Handling**: Not applicable (sequential generation)