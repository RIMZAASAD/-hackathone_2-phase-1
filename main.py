#!/usr/bin/env python3
"""
Menu-Driven In-Memory Todo Console App
Entry point for the application
"""

from src.todo_app.presentation.menu_cli import MenuCLIApp


def main():
    """Application entry point"""
    app = MenuCLIApp()
    app.run()


if __name__ == "__main__":
    main()