import pandas as pd

sample = {
    'arus': 0.15,
    'voltase': 230.5,
    'daya': 20.0,
    'frekuensi': 49.95,
    'suhu_dalam': 20.5,
    'suhu_luar': 23.0,
    'prakiraan_suhu_luar': 35.0
}


df_sample = pd.DataFrame([sample])

pred = clf.predict(df_sample)[0]
print("Anomali" if pred == 1 else "Normal")
