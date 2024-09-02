import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('motionsensorlogging.db')
cursor = conn.cursor()

# Query the database
cursor.execute('SELECT * FROM motion_events')

# Fetch all results
records = cursor.fetchall()

# Print the results
for record in records:
    print(record)

# Close the connection
conn.close()
