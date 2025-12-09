import requests
import pandas as pd
import datetime
import time
import sys
from collections import defaultdict

PROM_URL = "http://localhost:9090"
DATE = "2025-12-04"
STEP = 5
CHUNK_HOURS = 1

# Mapping label → kolom CSV
LABEL_MAP = {
    "label_current": "current",
    "label_freq": "freq",
    "label_power": "power",
    "label_voltage": "voltage"
}

# ================================
# SETUP TANGGAL
# ================================
start_day = datetime.datetime.strptime(DATE + " 00:00:00", "%Y-%m-%d %H:%M:%S")
end_day   = datetime.datetime.strptime(DATE + " 23:59:59", "%Y-%m-%d %H:%M:%S")

data_table = defaultdict(dict)
current_time = start_day

print(f"[INFO] Tanggal : {DATE}")
print("[INFO] Mode    : Multi-label merge")
print("======================================")

# ================================
# LOOP PER JAM
# ================================
while current_time < end_day:
    chunk_start = int(current_time.timestamp())
    chunk_end_dt = current_time + datetime.timedelta(hours=CHUNK_HOURS)
    if chunk_end_dt > end_day:
        chunk_end_dt = end_day

    chunk_end = int(chunk_end_dt.timestamp())

    print(f"[FETCH] {current_time} → {chunk_end_dt}")

    for prom_label, column_name in LABEL_MAP.items():
        query = f'metric_pzem{{{prom_label}!=""}}'

        r = requests.get(
            f"{PROM_URL}/api/v1/query_range",
            params={
                "query": query,
                "start": chunk_start,
                "end": chunk_end,
                "step": STEP
            },
            timeout=20
        )

        try:
            j = r.json()
        except Exception:
            print("[FATAL] Response bukan JSON")
            sys.exit(1)

        if j.get("status") != "success":
            print("[ERROR] Prometheus error:")
            print(j)
            sys.exit(1)

        for series in j["data"]["result"]:
            for ts, val in series["values"]:
                ts = int(float(ts))
                data_table[ts]["datetime"] = datetime.datetime.fromtimestamp(ts)
                data_table[ts]["timestamp"] = ts
                data_table[ts][column_name] = float(val)

        time.sleep(0.1)

    current_time = chunk_end_dt
    time.sleep(0.3)

# ================================
# BUILD DATAFRAME
# ================================
if not data_table:
    print("[FATAL] Data kosong total.")
    sys.exit(1)

df = pd.DataFrame(list(data_table.values()))
df = df.sort_values("timestamp")

filename = f"metric_pzem_multilabel_{DATE}.csv"
df.to_csv(filename, index=False)

print("======================================")
print(f"✅ Export selesai : {filename}")
print(f"✅ Total rows     : {len(df)}")
print("✅ Format siap AI training")
