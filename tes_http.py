import requests
import random
import time

URL = "http://192.168.200.118:1880/sensor"  # ganti sesuai endpoint kamu

while True:
    data_dummy = {
        "current": round(random.uniform(20.0, 35.0), 2),
        "power": round(random.uniform(20.0, 35.0), 2),
        "voltage": round(random.uniform(20.0, 35.0), 2),
        "frequency": round(random.uniform(20.0, 35.0), 2),
    }

    try:
        response = requests.post(URL, json=data_dummy)
        print("Sent:", data_dummy, "Status:", response.status_code)
    except Exception as e:
        print("Error:", e)

    print("-----------------------")
    time.sleep(1)  # kirim tiap 5 detik
