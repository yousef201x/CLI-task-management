import sqlite3 

def openConnection():
    # Establishes a connection to the SQLite database
    return sqlite3.connect("../database/sqlite3.db")

def createCursor(connection):
    # Creates a cursor object to execute SQL commands
    return connection.cursor()

def endConnection(connection, cursor):
    # Closes the cursor and connection
    cursor.close()
    connection.close()

def logError(message):
    try:
        # Opens the log file in write mode ('w')
        log = open('../logs/logs.txt', 'w')
        # Writes the error message to the log file
        log.write(message)
        # Closes the log file
        log.close()
        return True 
    except Exception as error:
        return False

def handleError(error) :
    print("Something went wrong, please try again later..")
    logError("ERROR: " + str(error))
    return False


def myTasks(status='pending'):
    try:
        # Open a connection to the database
        connection = openConnection()

        # Create a cursor for executing SQL commands
        cursor = createCursor(connection)

        # Execute the SELECT query with a parameterized status value
        cursor.execute("SELECT * FROM tasks WHERE status=?", (status,))

        # Fetch all rows returned by the query
        tasks = cursor.fetchall()

        # Close the cursor and connection
        endConnection(connection, cursor)

        # Return the fetched tasks
        return tasks
    
    except sqlite3.Error as error:
        # Handle SQLite database errors and log them
        print(handleError(error))
    
    except Exception as error:
        # Handle other unexpected errors and log them
        print(handleError(error))

def createTask(description, date, status='pending'):
    try:
        # Open a connection to the database
        connection = openConnection()

        # Create a cursor for executing SQL commands
        cursor = createCursor(connection)

        # Insert a new task into the database
        cursor.execute("INSERT INTO tasks (description, due_date, status) VALUES (?, ?, ?)", (description, date, status))

        # Commit changes to the database
        connection.commit()

        # Close the cursor and connection
        endConnection(connection, cursor)

    except sqlite3.Error as error:
        # Handle SQLite database errors and log them
        print(handleError(error))
    
    except Exception as error:
        # Handle other unexpected errors and log them
        print(handleError(error))

def updateTask(taskID, description=None, date=None, status=None):
    try:
        # Open a connection to the database
        connection = openConnection()

        # Create a cursor for executing SQL commands
        cursor = createCursor(connection)

        # Check if description is provided and update the task's description
        if description is not None:
            cursor.execute("UPDATE tasks SET description=? WHERE id=?", (description, taskID))

        # Check if date is provided and update the task's due date
        if date is not None:
            cursor.execute("UPDATE tasks SET due_date=? WHERE id=?", (date, taskID))

        # Check if status is provided and update the task's status
        if status is not None:
            cursor.execute("UPDATE tasks SET status=? WHERE id=?", (status, taskID))
        
        # Commit changes to the database
        connection.commit()

        # Close the cursor and connection
        endConnection(connection, cursor)

        return True  # Return True indicating successful update

    except sqlite3.Error as error:
        print(handleError(error))

    except Exception as error:
        # Handle other unexpected errors and log them
        print(handleError(error))

def deleteTask(taskID):
    try:
        # Open a connection to the database
        connection = openConnection()

        # Create a cursor for executing SQL commands
        cursor = createCursor(connection)

        # Delete a task from the database based on taskID
        cursor.execute("DELETE FROM tasks WHERE id=?", (taskID,))

        # Commit changes to the database
        connection.commit()

        # Close the cursor and connection
        endConnection(connection, cursor)

        return True  # Return True indicating successful deletion

    except sqlite3.Error as error:
        # Handle SQLite database errors and log them
        print(handleError(error))

    except Exception as error:
        # Handle other unexpected errors and log them
        print(handleError(error))
