import sqlite3 

# Function to establish a connection to the SQLite database
def openConnection():
    return sqlite3.connect("../database/sqlite3.db")

# Function to create a cursor object to execute SQL commands
def createCursor(connection):
    return connection.cursor()

# Function to close the cursor and connection
def endConnection(connection, cursor):
    cursor.close()
    connection.close()

# Function to log errors to a log file
def logError(message):
    try:
        log = open('../logs/logs.txt', 'w')  # Open the log file in write mode
        log.write(message)  # Write the error message to the log file
        log.close()  # Close the log file
        return True 
    except Exception as error:
        return False

# Function to handle errors by printing a message and logging the error
def handleError(error):
    print("Something went wrong, please try again later..")
    logError("ERROR: " + str(error))
    return False

# Function to fetch tasks based on their status
def myTasks(status='pending'):
    try:
        connection = openConnection()  # Open a connection to the database
        cursor = createCursor(connection)  # Create a cursor for executing SQL commands
        cursor.execute("SELECT * FROM tasks WHERE status=?", (status,))  # Execute the SELECT query with a parameterized status value
        tasks = cursor.fetchall()  # Fetch all rows returned by the query
        endConnection(connection, cursor)  # Close the cursor and connection
        return tasks  # Return the fetched tasks
    except sqlite3.Error as error:
        return handleError(error)  # Handle SQLite database errors and log them
    except Exception as error:
        return handleError(error)  # Handle other unexpected errors and log them

# Function to search tasks based on a search term in description or due_date
def searchTask(search):
    try:
        connection = openConnection()  # Open a connection to the database
        cursor = createCursor(connection)  # Create a cursor for executing SQL commands
        query = "SELECT * FROM tasks WHERE description LIKE ? OR due_date LIKE ?"  # SQL query to search for tasks
        search_term = f'%{search}%'  # Format the search term with wildcard characters
        tasks = cursor.execute(query, (search_term, search_term)).fetchall()  # Execute the query and fetch all matching tasks
        cursor.close()  # Close the cursor
        connection.close()  # Close the connection
        return tasks  # Return the fetched tasks
    except sqlite3.Error as error:
        return handleError(error)  # Handle SQLite database errors and log them
    except Exception as error:
        return handleError(error)  # Handle other unexpected errors and log them

# Function to create a new task
def createTask(description, date, status='pending'):
    try:
        connection = openConnection()  # Open a connection to the database
        cursor = createCursor(connection)  # Create a cursor for executing SQL commands
        cursor.execute("INSERT INTO tasks (description, due_date, status) VALUES (?, ?, ?)", (description, date, status))  # Insert a new task into the database
        connection.commit()  # Commit changes to the database
        endConnection(connection, cursor)  # Close the cursor and connection
    except sqlite3.Error as error:
        return handleError(error)  # Handle SQLite database errors and log them
    except Exception as error:
        return handleError(error)  # Handle other unexpected errors and log them

# Function to update an existing task
def updateTask(taskID, description=None, date=None, status=None):
    try:
        connection = openConnection()  # Open a connection to the database
        cursor = createCursor(connection)  # Create a cursor for executing SQL commands

        # Update the task based on provided information
        if description is not None:
            cursor.execute("UPDATE tasks SET description=? WHERE id=?", (description, taskID))
        if date is not None:
            cursor.execute("UPDATE tasks SET due_date=? WHERE id=?", (date, taskID))
        if status is not None:
            cursor.execute("UPDATE tasks SET status=? WHERE id=?", (status, taskID))

        connection.commit()  # Commit changes to the database
        endConnection(connection, cursor)  # Close the cursor and connection
        return True  # Return True indicating successful update
    except sqlite3.Error as error:
        return handleError(error)  # Handle SQLite database errors and log them
    except Exception as error:
        return handleError(error)  # Handle other unexpected errors and log them

# Function to delete a task
def deleteTask(taskID):
    try:
        connection = openConnection()  # Open a connection to the database
        cursor = createCursor(connection)  # Create a cursor for executing SQL commands
        cursor.execute("DELETE FROM tasks WHERE id=?", (taskID,))  # Delete a task from the database based on taskID
        connection.commit()  # Commit changes to the database
        endConnection(connection, cursor)  # Close the cursor and connection
        return True  # Return True indicating successful deletion
    except sqlite3.Error as error:
        return handleError(error)  # Handle SQLite database errors and log them
    except Exception as error:
        return handleError(error)  # Handle other unexpected errors and log them
