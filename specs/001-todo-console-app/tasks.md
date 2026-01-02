---
description: "Task list for Todo In-Memory Python Console Application"
---

# Tasks: Todo In-Memory Python Console Application

**Input**: Design documents from `/specs/001-todo-console-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, quickstart.md

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions
- Follow memory-first, incremental evolution, and separation of concerns principles from constitution

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are the actual implementation tasks for the Todo In-Memory Python Console Application based on the design documents.

  The tasks are organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan in src/
- [x] T002 [P] Create directory structure: src/todo_app/, src/todo_app/domain/, src/todo_app/infrastructure/, src/todo_app/presentation/
- [x] T003 [P] Create __init__.py files in all directories
- [x] T004 Create main.py file in root directory
- [x] T005 Create requirements.txt file with Python version specification

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [x] T006 Create Todo data model in src/todo_app/domain/models.py
- [x] T007 Create in-memory storage implementation in src/todo_app/infrastructure/storage.py
- [x] T008 Create Todo service with business logic in src/todo_app/domain/services.py
- [x] T009 Create console interface framework in src/todo_app/presentation/console.py
- [x] T010 Create basic application entry point in src/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---
## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Users can add new tasks and view all their current tasks

**Independent Test**: The application can be fully tested by adding multiple tasks and viewing them. This delivers the basic value proposition of a todo app.

### Implementation for User Story 1

- [x] T011 [P] [US1] Implement Todo class with id, title, completed, created_at attributes in src/todo_app/domain/models.py
- [x] T012 [P] [US1] Implement InMemoryTodoRepository with add_todo and list_todos methods in src/todo_app/infrastructure/storage.py
- [x] T013 [US1] Implement TodoService with add_todo and list_todos methods in src/todo_app/domain/services.py
- [x] T014 [US1] Implement console command parsing for 'add' and 'list' commands in src/todo_app/presentation/console.py
- [x] T015 [US1] Connect console interface to TodoService for add/list operations in src/main.py
- [x] T016 [US1] Add validation for non-empty todo titles in src/todo_app/domain/services.py
- [x] T017 [US1] Add unique ID generation for new todos in src/todo_app/infrastructure/storage.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - Update and Complete Tasks (Priority: P2)

**Goal**: Users can update their tasks and mark them as complete when finished

**Independent Test**: The application can be tested by adding tasks, marking them complete, and viewing the updated status. This delivers the core task management functionality.

### Implementation for User Story 2

- [x] T018 [P] [US2] Extend TodoService with update_todo, complete_todo, and incomplete_todo methods in src/todo_app/domain/services.py
- [x] T019 [P] [US2] Extend InMemoryTodoRepository with get_todo method in src/todo_app/infrastructure/storage.py
- [x] T020 [US2] Extend InMemoryTodoRepository with update_todo, complete_todo, and incomplete_todo methods in src/todo_app/infrastructure/storage.py
- [x] T021 [US2] Implement console command parsing for 'update', 'complete', and 'incomplete' commands in src/todo_app/presentation/console.py
- [x] T022 [US2] Connect console interface to TodoService for update/complete operations in src/main.py
- [x] T023 [US2] Add validation for existing todo IDs in update/complete operations in src/todo_app/domain/services.py
- [x] T024 [US2] Add business validation to prevent marking already completed/incomplete todos in src/todo_app/domain/services.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 - Delete Tasks (Priority: P3)

**Goal**: Users can remove tasks that are no longer relevant

**Independent Test**: The application can be tested by adding tasks, deleting them, and confirming they no longer appear in the list. This delivers the complete task lifecycle.

### Implementation for User Story 3

- [x] T025 [P] [US3] Extend TodoService with delete_todo method in src/todo_app/domain/services.py
- [x] T026 [P] [US3] Extend InMemoryTodoRepository with delete_todo method in src/todo_app/infrastructure/storage.py
- [x] T027 [US3] Implement console command parsing for 'delete' command in src/todo_app/presentation/console.py
- [x] T028 [US3] Connect console interface to TodoService for delete operations in src/main.py
- [x] T029 [US3] Add validation for existing todo IDs in delete operations in src/todo_app/domain/services.py
- [x] T030 [US3] Add proper ID renumbering or maintain ID consistency after deletion in src/todo_app/infrastructure/storage.py

**Checkpoint**: All user stories should now be independently functional

---
## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T031 [P] Add comprehensive error handling and user-friendly messages across all operations
- [x] T032 [P] Add input validation for all user commands and proper error messages
- [x] T033 Add help command implementation in src/todo_app/presentation/console.py
- [x] T034 Add quit/exit command implementation in src/todo_app/presentation/console.py
- [x] T035 [P] Add proper application loop in src/main.py to handle continuous command input
- [x] T036 Add timestamp functionality for created_at in src/todo_app/domain/models.py
- [x] T037 Add edge case handling for invalid commands, empty inputs, and non-existent todo IDs
- [x] T038 [P] Add documentation to all implemented methods and classes
- [x] T039 Update quickstart guide based on implemented functionality in docs/quickstart.md
- [x] T040 Run application validation to ensure all 5 basic todo features work correctly

---
## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Models before services
- Services before console interface
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---
## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---
## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence