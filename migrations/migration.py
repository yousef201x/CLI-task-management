import sqlite3

# Connection to the SQLite database
connection = sqlite3.connect("../database/sqlite3.db")

# Cursor to interact with the database
cursor = connection.cursor()

# Create tasks table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        due_date DATE NOT NULL,
        status TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'completed'))
    );
''')

# Close the cursor (not needed if using a context manager like "with")
cursor.close()

# Close the database connection
connection.close()
