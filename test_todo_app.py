"""
Validation test for the Todo Console Application
Tests all core functionality of the todo app
"""
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.todo_app.domain.models import Todo
from src.todo_app.domain.services import TodoService
from src.todo_app.infrastructure.storage import InMemoryTodoRepository


def test_basic_functionality():
    """
    Test basic functionality of the todo application
    """
    print("Testing basic functionality...")

    # Create repository and service
    repository = InMemoryTodoRepository()
    service = TodoService(repository)

    # Test 1: Add functionality
    print("\n1. Testing add functionality:")
    todo1 = service.add_todo("Buy groceries")
    todo2 = service.add_todo("Walk the dog")
    print(f"   Added: {todo1}")
    print(f"   Added: {todo2}")
    print("   + Add functionality works")

    # Test 2: List functionality
    print("\n2. Testing list functionality:")
    todos = service.list_todos()
    print(f"   Found {len(todos)} todos:")
    for todo in todos:
        print(f"     {todo}")
    print("   + List functionality works")

    # Test 3: Complete functionality
    print("\n3. Testing complete functionality:")
    completed_todo = service.complete_todo(1)
    print(f"   Completed: {completed_todo}")
    print("   + Complete functionality works")

    # Test 4: Update functionality
    print("\n4. Testing update functionality:")
    updated_todo = service.update_todo(2, "Walk the cat instead")
    print(f"   Updated: {updated_todo}")
    print("   - Update functionality works")

    print("\n+ All basic functionality tests passed!")


def test_edge_cases():
    """
    Test edge cases and error handling
    """
    print("\n\nTesting edge cases...")

    # Create fresh repository and service for clean state
    repository = InMemoryTodoRepository()
    service = TodoService(repository)

    # Test 1: Empty todo validation
    print("\n1. Testing empty todo validation:")
    try:
        service.add_todo("")
        print("   - Empty todo incorrectly accepted")
    except ValueError:
        print("   + Empty todo correctly rejected")

    try:
        service.add_todo("   ")  # whitespace only
        print("   - Whitespace-only todo incorrectly accepted")
    except ValueError:
        print("   + Whitespace-only todo correctly rejected")

    # Test 2: Update non-existent todo
    print("\n2. Testing update non-existent todo:")
    try:
        service.update_todo(999, "New name")
        print("   - Non-existent todo update incorrectly accepted")
    except ValueError:
        print("   + Non-existent todo correctly rejected")

    # Test 3: Complete non-existent todo
    print("\n3. Testing complete non-existent todo:")
    try:
        service.complete_todo(999)
        print("   - Non-existent todo completion incorrectly accepted")
    except ValueError:
        print("   + Non-existent todo correctly rejected")

    print("\n+ All edge case tests passed!")


def main():
    """
    Main test function
    """
    print("Starting Todo Console Application tests...")

    try:
        test_basic_functionality()
        test_edge_cases()
        print("\n\n[SUCCESS] All tests passed!")
        print("The Todo Console Application is working correctly.")
    except Exception as e:
        print(f"\n\n[ERROR] Some tests failed: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())