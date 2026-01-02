import os
import sys
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)


def clear_screen():
    """Clear the screen using os.system command"""
    os.system('cls' if os.name == 'nt' else 'clear')


def format_success_message(message: str) -> str:
    """Format a success message with green color"""
    return f"{Fore.GREEN}{message}{Style.RESET_ALL}"


def format_error_message(message: str) -> str:
    """Format an error message with red color"""
    return f"{Fore.RED}{message}{Style.RESET_ALL}"


def format_warning_message(message: str) -> str:
    """Format a warning message with yellow color"""
    return f"{Fore.YELLOW}{message}{Style.RESET_ALL}"


def format_info_message(message: str) -> str:
    """Format an info message with blue color"""
    return f"{Fore.BLUE}{message}{Style.RESET_ALL}"


def format_completed_task(task_str: str) -> str:
    """Format a completed task with green color"""
    return f"{Fore.GREEN}{task_str}{Style.RESET_ALL}"


def format_incomplete_task(task_str: str) -> str:
    """Format an incomplete task with red color"""
    return f"{Fore.RED}{task_str}{Style.RESET_ALL}"


def format_menu_option(option: str) -> str:
    """Format a menu option with cyan color"""
    return f"{Fore.CYAN}{option}{Style.RESET_ALL}"


def format_task_with_icon(task_id: int, description: str, completed: bool) -> str:
    """Format a task with appropriate icon and color based on completion status"""
    if completed:
        icon = "✅"
        return f"{Fore.GREEN}{icon} [{task_id}] {description} [Complete]{Style.RESET_ALL}"
    else:
        icon = "⏳"
        return f"{Fore.YELLOW}{icon} [{task_id}] {description} [Incomplete]{Style.RESET_ALL}"


def format_task_added(task_id: int, description: str) -> str:
    """Format a task added message with icon"""
    return f"{Fore.GREEN}✅ Task added successfully!{Style.RESET_ALL}\n  [ID: {task_id}] [Description: {description}] [Status: Incomplete]"


def format_task_updated(task_id: int, description: str, completed: bool) -> str:
    """Format a task updated message with icon"""
    status = "Complete" if completed else "Incomplete"
    status_icon = "✅" if completed else "⏳"
    return f"{Fore.GREEN}🔄 Task updated successfully!{Style.RESET_ALL}\n  [ID: {task_id}] [Description: {description}] [Status: {status}]"


def format_task_deleted(task_id: int, description: str) -> str:
    """Format a task deleted message with icon"""
    return f"{Fore.RED}🗑️  Task deleted successfully!{Style.RESET_ALL}\n  [ID: {task_id}] [Description: {description}]"


def format_task_status_changed(task_id: int, description: str, completed: bool) -> str:
    """Format a task status changed message with icon"""
    if completed:
        return f"{Fore.GREEN}✅ Task status updated successfully!{Style.RESET_ALL}\n  [ID: {task_id}] [Description: {description}] [Status: Complete]"
    else:
        return f"{Fore.GREEN}⏳ Task status updated successfully!{Style.RESET_ALL}\n  [ID: {task_id}] [Description: {description}] [Status: Incomplete]"