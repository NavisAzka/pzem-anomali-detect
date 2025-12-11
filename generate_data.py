import pandas as pd
import random
from datetime import datetime, timedelta

def generate_ac_data(n=100, start_time=None):
    if not start_time:
        start_time = datetime.now()

    rows = []
    for i in range(n):
        ts = start_time + timedelta(minutes=i * random.randint(1, 5))

        arus = round(random.uniform(0.0, 7.5), 2)
        voltase = round(random.uniform(210.0, 240.0), 1)
        daya = round(arus * voltase * random.uniform(0.8, 1.0), 1)
        frekuensi = round(random.uniform(49.5, 50.5), 2)

        suhu_dalam = round(random.uniform(18.0, 35.0), 1)
        suhu_luar = round(random.uniform(20.0, 40.0), 1)
        prakiraan = suhu_luar + random.uniform(-5, 10)
        prakiraan_suhu_luar = round(max(min(prakiraan, 60.0), 5.0), 1)

        # Anomaly logic
        if frekuensi < 45 or frekuensi > 55:
            label = 1
        elif arus > 30 and daya < 1000:
            label = 1
        elif arus > 0.2 and suhu_dalam < 20 and prakiraan_suhu_luar < 28:
            label = 1
        elif arus <= 0.2 and suhu_dalam > 28 and prakiraan_suhu_luar > 30:
            label = 1
        elif arus <= 0.2 and suhu_dalam < 23 and prakiraan_suhu_luar > 45:
            label = 1
        elif arus > 0.2 and suhu_dalam < 23 and suhu_luar < 25 and prakiraan_suhu_luar < 28:
            label = 1
        else:
            label = 0

        rows.append([
            ts.isoformat(), arus, voltase, daya, frekuensi,
            suhu_dalam, suhu_luar, prakiraan_suhu_luar, label
        ])

    df = pd.DataFrame(rows, columns=[
        'timestamp', 'arus', 'voltase', 'daya', 'frekuensi',
        'suhu_dalam', 'suhu_luar', 'prakiraan_suhu_luar', 'label_anomali'])

    return df

# Example usage
if __name__ == "__main__":
    df = generate_ac_data(100)
    df.to_csv("synthetic_ac_data.csv", index=False)
    print("Data generated and saved to synthetic_ac_data.csv")
