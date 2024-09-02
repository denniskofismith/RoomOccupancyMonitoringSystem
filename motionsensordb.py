import sqlite3
import datetime
import time
from gpiozero import MotionSensor

# Set up the MotionSensor (replace GPIO pin number with your setup)
pir = MotionSensor(17)  # Example GPIO pin

# Connect to SQLite database
conn = sqlite3.connect('motionsensorlogging.db')
cursor = conn.cursor()

# Create the table if it does not exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS motion_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

def log_event(event):
    """Insert a motion event into the database."""
    cursor.execute('''
    INSERT INTO motion_events (event) VALUES (?)
    ''', (event,))
    conn.commit()

try:
    while True:
        print("Scanning Motion")
        pir.wait_for_active()

        print("Motion detected")
        log_event('Motion Detected')

        pir.wait_for_inactive()

        print("Motion Stopped")
        log_event('Motion Stopped')

        # Optional: sleep to avoid excessive CPU usage
        time.sleep(1)
except KeyboardInterrupt:
    print("Program interrupted. Closing database connection.")
finally:
    # Close the connection when the program is interrupted
    conn.close()
