import pandas as pd
import joblib


# ===============   
# UJI COBA
# ===============

sample = {
    'arus': 0.15,
    'voltase': 230.5,
    'daya': 0.60,
    'frekuensi': 49.95,
    'suhu_dalam': 18.5,
    'suhu_luar': 30.0,
    'prakiraan_suhu_luar': 55.0
}

clf = joblib.load('./model/model_rtos.pkl')

# print sample
print("\nContoh Sampel:")
for k, v in sample.items():
    print(f"{k}: {v}")


print("\nContoh Prediksi:")

df_sample = pd.DataFrame([sample])

pred = clf.predict(df_sample)[0]
print("Anomali" if pred == 1 else "Normal")
