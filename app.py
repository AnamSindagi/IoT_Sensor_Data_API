from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

DB = "database.db"

def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL,
            humidity REAL,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route('/sensor', methods=['POST'])
def receive_data():
    data = request.json
    temperature = data.get("temperature")
    humidity = data.get("humidity")

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO sensor_data (temperature, humidity, timestamp)
        VALUES (?, ?, ?)
    """, (temperature, humidity, str(datetime.now())))
    conn.commit()
    conn.close()

    return jsonify({"message": "Data stored successfully"}), 201

@app.route('/sensor', methods=['GET'])
def get_data():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sensor_data")
    rows = cursor.fetchall()
    conn.close()

    data = []
    for row in rows:
        data.append({
            "id": row[0],
            "temperature": row[1],
            "humidity": row[2],
            "timestamp": row[3]
        })

    return jsonify(data)

@app.route('/average', methods=['GET'])
def get_average():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(temperature), AVG(humidity) FROM sensor_data")
    avg = cursor.fetchone()
    conn.close()

    return jsonify({
        "avg_temperature": avg[0],
        "avg_humidity": avg[1]
    })

if __name__ == '__main__':
    init_db()
    app.run(debug=True)