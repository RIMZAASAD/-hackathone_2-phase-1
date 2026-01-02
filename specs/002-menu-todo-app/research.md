# Research: Menu-Driven In-Memory Todo Console App

**Feature**: Menu-Driven In-Memory Todo Console App
**Created**: 2026-01-02
**Research for**: [specs/002-menu-todo-app/plan.md](./plan.md)

## Decision: Color Library Selection
**Rationale**: Need to add color support to the console application for visual feedback. Python's standard library doesn't provide color formatting for terminals, so a third-party library is needed.
**Alternatives considered**:
- colorama (most popular, cross-platform, simple API)
- termcolor (lightweight, but less features)
- rich (feature-rich but potentially overkill for simple color needs)
- ANSI escape codes directly (no dependencies but more complex)
**Chosen**: colorama as it provides reliable cross-platform color support with a simple API

## Decision: Menu Navigation Approach
**Rationale**: Need to implement a numbered menu system that's intuitive for users.
**Alternatives considered**:
- Text-based commands (like the existing app) vs numbered menu options
- Single character input vs full numeric input
- Continuous loop vs screen clearing after each operation
**Chosen**: Numbered menu options 1-7 with screen clearing after each operation for clean UI

## Decision: Screen Clearing Method
**Rationale**: Need to clear the screen between operations to maintain clean UI as specified.
**Alternatives considered**:
- os.system('clear') for Unix, os.system('cls') for Windows
- ANSI escape codes for cross-platform clearing
- Third-party libraries for terminal control
**Chosen**: os.system('cls' if os.name == 'nt' else 'clear') for reliable cross-platform clearing

## Decision: Input Validation Strategy
**Rationale**: Need to handle invalid user input gracefully with clear error messages.
**Alternatives considered**:
- Try/except blocks around input processing
- Input validation functions with clear error messages
- Type conversion with fallback values
**Chosen**: Input validation functions with specific error handling and color-coded feedback

## Decision: Task ID Management
**Rationale**: Need to maintain consistent task IDs even after deletion operations.
**Alternatives considered**:
- Re-numbering IDs after deletion (simpler for users but can be confusing)
- Keeping original IDs (consistent but may create gaps)
- Using separate display IDs vs internal IDs
**Chosen**: Keeping original IDs with gaps after deletion to maintain consistency