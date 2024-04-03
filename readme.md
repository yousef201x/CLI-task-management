# Task Management System

## Introduction
The Task Management System is a command-line application designed to help users manage their tasks efficiently. It provides functionalities to create, update, delete, search, and view tasks. The system interacts with a SQLite database to store and retrieve task-related information.

## How to Use the System
1. Ensure you have Python installed on your system.
2. Clone the Task Management System repository to your local machine.
3. Navigate to the project directory and open a terminal or command prompt.
4. Run the command `python app.py` to launch the command-line interface.
5. Follow the on-screen prompts to perform various tasks such as viewing tasks, creating tasks, updating tasks, and deleting tasks.

That's it! You can now use the Task Management System to efficiently manage your tasks from the command line.

## System Components
1. **SQLite Database:** Stores task information such as ID, description, due date, and status.
2. **Logic Module (`logic/logic.py`):** Contains Python functions to interact with the database and perform CRUD (Create, Read, Update, Delete) operations on tasks.
3. **Command-Line Interface (`app.py`):** Provides a user-friendly interface to interact with the system functionalities.
## Database Schema
The database schema includes a single table named `tasks` with the following columns:
- `id`: Integer (Primary Key, Auto Increment)
- `description`: Text (Task description)
- `due_date`: Date (Task due date)
- `status`: Text (Task status, can be 'pending' or 'completed')

## Functions in `logic.py`

### `openConnection()`
- Description: Establishes a connection to the SQLite database.
- Returns: SQLite connection object.

### `createCursor(connection)`
- Description: Creates a cursor object to execute SQL commands.
- Parameters:
  - `connection`: SQLite connection object.
- Returns: Cursor object for executing SQL commands.

### `endConnection(connection, cursor)`
- Description: Closes the cursor and connection.
- Parameters:
  - `connection`: SQLite connection object.
  - `cursor`: Cursor object.

### `logError(message)`
- Description: Logs an error message to a log file.
- Parameters:
  - `message`: Error message to be logged.
- Returns: `True` if logging is successful, `False` otherwise.

### `handleError(error)`
- Description: Handles and logs errors during database operations.
- Parameters:
  - `error`: Exception object representing the error.
- Returns: `False` to indicate error handling.

### `myTasks(status='pending')`
- Description: Retrieves tasks based on their status.
- Parameters:
  - `status`: Status of tasks to retrieve (default is 'pending').
- Returns: List of tasks matching the specified status.

### `searchTask(search)`
- Description: Searches for tasks based on a search term.
- Parameters:
  - `search`: Search term to match against task descriptions or due dates.
- Returns: List of tasks matching the search term.

### `createTask(description, date, status='pending')`
- Description: Creates a new task and adds it to the database.
- Parameters:
  - `description`: Description of the task.
  - `date`: Due date of the task.
  - `status`: Status of the task (default is 'pending').

### `updateTask(taskID, description=None, date=None, status=None)`
- Description: Updates an existing task in the database.
- Parameters:
  - `taskID`: ID of the task to be updated.
  - `description`: New description for the task (optional).
  - `date`: New due date for the task (optional).
  - `status`: New status for the task (optional).

### `deleteTask(taskID)`
- Description: Deletes a task from the database.
- Parameters:
  - `taskID`: ID of the task to be deleted.

