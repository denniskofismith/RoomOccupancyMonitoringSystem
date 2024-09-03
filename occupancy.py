from flask import Flask, render_template

app = Flask(__name__)

# Hard-coded room data
room_data = {
    'Room 101': {'occupied': True, 'people_count': 3},
    'Room 102': {'occupied': False, 'people_count': 0},
    'Room 103': {'occupied': True, 'people_count': 5},
}

@app.route('/')
def index():
    return render_template('roomocupancy.html', rooms=room_data)

if __name__ == '__main__':
    app.run(debug=True)
























# from flask import Flask, render_template, jsonify

# app = Flask(__name__)

# # Sample data to simulate room occupancy
# room_data = {
#     'room1': {'occupied': False, 'people_count': 0},
#     'room2': {'occupied': True, 'people_count': 3},
# }

# @app.route('/')
# def index():
#     return render_template('index.html', rooms=room_data)

# @app.route('/api/rooms/<room_id>', methods=['GET'])
# def get_room_status(room_id):
#     if room_id in room_data:
#         return jsonify(room_data[room_id])
#     return jsonify({"error": "Room not found"}), 404

# if __name__ == '__main__':
#     app.run(debug=True)
