from flask import Flask, render_template, jsonify
import sqlite3
import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('motionsensorlogging.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM motion_events ORDER BY timestamp DESC LIMIT 1')
    latest_event = cursor.fetchone()
    conn.close()
    return render_template('index.html', latest_event=latest_event)

@app.route('/history')
def history():
    conn = get_db_connection()
    cursor = conn.cursor()
    one_week_ago = datetime.datetime.utcnow() - datetime.timedelta(days=7)
    cursor.execute('SELECT * FROM motion_events WHERE timestamp >= ?', (one_week_ago,))
    events = cursor.fetchall()
    conn.close()
    return render_template('history.html', events=events)

@app.route('/api/occupancy')
def occupancy_api():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM motion_events ORDER BY timestamp DESC LIMIT 1')
    latest_event = cursor.fetchone()
    conn.close()
    return jsonify({
        'event': latest_event['event'],
        'timestamp': latest_event['timestamp']
    })

if __name__ == '__main__':
    app.run(debug=True)
