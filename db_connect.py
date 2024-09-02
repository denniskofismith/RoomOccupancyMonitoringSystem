



import sqlite3
import datetime

# Connect to (or create) a SQLite database
conn = sqlite3.connect('motionsensorlogging.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS my_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT NOT NULL,
    time_slot TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

# # Insert a new record
# message = 'Hello, World!'
# time_slot = 'Morning'
# cursor.execute('''
# INSERT INTO my_table (message, time_slot) VALUES (?, ?)
# ''', (message, time_slot))
# conn.commit()

# # Query records
# cursor.execute('SELECT * FROM my_table')
# records = cursor.fetchall()
# for record in records:
#     print(record)

# # Update a record
# new_message = 'Updated Message'
# record_id = 1
# cursor.execute('''
# UPDATE my_table
# SET message = ?
# WHERE id = ?
# ''', (new_message, record_id))
# conn.commit()

# # Delete a record
# record_id = 1
# cursor.execute('''
# DELETE FROM my_table
# WHERE id = ?
# ''', (record_id,))
# conn.commit()

# Close the connection
conn.close()
