---
description: "Task list for Menu-Driven In-Memory Todo Console App"
---

# Tasks: Menu-Driven In-Memory Todo Console App

**Input**: Design documents from `/specs/002-menu-todo-app/`
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
  IMPORTANT: The tasks below are the actual implementation tasks for the Menu-Driven In-Memory Todo Console App based on the design documents.

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
- [x] T005 Create requirements.txt file with Python version specification and colorama dependency

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Create Todo data model in src/todo_app/domain/models.py
- [x] T007 Create in-memory storage implementation in src/todo_app/infrastructure/storage.py
- [x] T008 Create Todo service with business logic in src/todo_app/domain/services.py
- [x] T009 Create screen clearing utility function in src/todo_app/presentation/utils.py
- [x] T010 Create color formatting utility functions in src/todo_app/presentation/utils.py
- [x] T011 Create basic application entry point in src/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Menu Navigation (Priority: P1) 🎯 MVP

**Goal**: Users can navigate through a colorful menu with numbered options and perform basic operations

**Independent Test**: The application can be fully tested by navigating through all menu options and seeing the colorful interface. This delivers the core user experience of the menu-driven interface.

### Implementation for User Story 1

- [x] T012 [P] [US1] Implement colorful menu display function in src/todo_app/presentation/menu_cli.py
- [x] T013 [P] [US1] Implement menu navigation loop with input validation in src/todo_app/presentation/menu_cli.py
- [x] T014 [US1] Create MenuCLIApp class to manage menu flow in src/todo_app/presentation/menu_cli.py
- [x] T015 [US1] Implement screen clearing functionality after each menu operation in src/todo_app/presentation/menu_cli.py
- [x] T016 [US1] Add error handling for invalid menu choices in src/todo_app/presentation/menu_cli.py
- [x] T017 [US1] Connect menu interface to TodoService for basic operations in src/main.py
- [x] T018 [US1] Add color-coded status display for menu options in src/todo_app/presentation/menu_cli.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Core Todo Operations (Priority: P2)

**Goal**: Users can perform all basic todo operations (add, view, update, delete, mark complete/incomplete) through the menu-driven interface with visual feedback

**Independent Test**: The application can be tested by using menu options to add tasks, view them with color coding, update them, mark them complete, and delete them. This delivers the complete todo management experience.

### Implementation for User Story 2

- [x] T019 [P] [US2] Implement Add Task functionality in src/todo_app/presentation/menu_cli.py
- [x] T020 [P] [US2] Implement View All Tasks functionality with color-coded status in src/todo_app/presentation/menu_cli.py
- [x] T021 [US2] Implement Update Task functionality in src/todo_app/presentation/menu_cli.py
- [x] T022 [US2] Implement Delete Task functionality in src/todo_app/presentation/menu_cli.py
- [x] T023 [US2] Implement Mark Task Complete functionality in src/todo_app/presentation/menu_cli.py
- [x] T024 [US2] Implement Mark Task Incomplete functionality in src/todo_app/presentation/menu_cli.py
- [x] T025 [US2] Add validation for task IDs in update/delete operations in src/todo_app/presentation/menu_cli.py
- [x] T026 [US2] Add validation for task descriptions in add/update operations in src/todo_app/presentation/menu_cli.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Enhanced UI Experience (Priority: P3)

**Goal**: Users experience visual feedback with colors, clear screen management, and professional error handling that makes the console application feel polished

**Independent Test**: The application can be tested by using all features and observing the color output, screen clearing, and error handling. This delivers the enhanced UI experience.

### Implementation for User Story 3

- [x] T027 [P] [US3] Enhance color feedback for success messages in src/todo_app/presentation/menu_cli.py
- [x] T028 [P] [US3] Enhance color feedback for error messages in src/todo_app/presentation/menu_cli.py
- [x] T029 [US3] Implement color-coded task status indicators (green for complete, red for incomplete) in src/todo_app/presentation/menu_cli.py
- [x] T030 [US3] Add visual formatting for task display in src/todo_app/presentation/menu_cli.py
- [x] T031 [US3] Implement graceful error handling with clear messages in src/todo_app/presentation/menu_cli.py
- [x] T032 [US3] Add input validation with user-friendly error messages in src/todo_app/presentation/menu_cli.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T033 [P] Add comprehensive error handling and user-friendly messages across all operations
- [x] T034 [P] Add input validation for all user inputs and proper error messages
- [x] T035 Add exit functionality implementation in src/todo_app/presentation/menu_cli.py
- [x] T036 [P] Add proper application loop in src/main.py to handle continuous menu navigation
- [x] T037 Add edge case handling for invalid choices, empty inputs, and non-existent task IDs
- [x] T038 [P] Add documentation to all implemented methods and classes
- [x] T039 Update quickstart guide based on implemented functionality in docs/quickstart.md
- [x] T040 Run application validation to ensure all 7 menu options work correctly

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
- Services before menu interface
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all parallel tasks for User Story 1 together:
Task: "Implement colorful menu display function in src/todo_app/presentation/menu_cli.py"
Task: "Implement menu navigation loop with input validation in src/todo_app/presentation/menu_cli.py"
```

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