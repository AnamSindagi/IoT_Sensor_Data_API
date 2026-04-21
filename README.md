# 🚀 IoT Sensor Data API

## 📌 Overview
This project is a Python-based REST API that simulates an IoT system where an embedded device sends real-time sensor data (temperature and humidity) to a backend server. The backend processes, stores, and provides access to this data through API endpoints.

---

## 🎯 Features
- 📡 Receive sensor data via REST API (`POST /sensor`)
- 📊 Retrieve all stored data (`GET /sensor`)
- 📈 Compute average values (`GET /average`)
- 🗄 Store data using SQLite database
- 🔁 Simulated embedded device sending real-time data

---

## 🧠 Tech Stack
- Python  
- Flask (REST API)  
- SQLite (Database)  
- Requests (Device simulation)  
- Git & GitHub  

---

## 📁 Project Structure

iot-sensor-api/
│── app.py
│── device_simulator.py
│── database.db
│── requirements.txt
│── README.md
│── .gitignore


---

## ⚙️ How It Works
1. The simulated device generates sensor data (temperature & humidity).
2. It sends data to the Flask API using HTTP POST requests.
3. The backend stores the data in an SQLite database.
4. Users can retrieve and analyze the data via API endpoints.

---

## ▶️ Getting Started

### 1️⃣ Clone the repository

git clone https://github.com/your-username/iot-sensor-api.git

cd iot-sensor-api


### 2️⃣ Install dependencies

pip install -r requirements.txt


### 3️⃣ Run the backend server

python app.py


### 4️⃣ Run the device simulator (in a new terminal)

python device_simulator.py


---

## 🔌 API Endpoints

### 📥 POST /sensor
Send sensor data
```json
{
  "temperature": 28.5,
  "humidity": 65.2
}

📤 GET /sensor

Retrieve all sensor data

📊 GET /average

Get average temperature and humidity

📸 Sample Output

[
  {
    "id": 1,
    "temperature": 27.3,
    "humidity": 60.5,
    "timestamp": "2026-04-21 10:30:00"
  }
]


💡 Key Learnings
Designed and built RESTful APIs using Flask
Implemented real-time data flow simulation (IoT concept)
Integrated Python backend with SQLite database
Practiced API testing and debugging


🚀 Future Improvements
Add frontend dashboard for visualization
Deploy API to cloud (Render/Railway)
Integrate real hardware (ESP32/Arduino)
Add authentication & security



🧑‍💻 Author

[Your Name]
GitHub: https://github.com/your-username



---

## ⭐ Support
If you like this project, give it a star ⭐