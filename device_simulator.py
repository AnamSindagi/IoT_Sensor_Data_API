import requests
import random
import time

URL = "http://127.0.0.1:5000/sensor"

while True:
    data = {
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(40, 80), 2)
    }

    try:
        response = requests.post(URL, json=data)
        print("Sent:", data, "| Status:", response.status_code)
    except Exception as e:
        print("Error:", e)

    time.sleep(5)