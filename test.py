from inference import run_inference   

data = {
    'arus': 2.15,
    'voltase': 230.5,
    'daya': 643.60,
    'frekuensi': 49.95,
    'suhu_dalam': 36.5,
    'suhu_luar': 35.0,
    'prakiraan_suhu_luar': 12.0
}

# print sample
print("Contoh Sampel:")
for k, v in data.items():
    print(f"{k}: {v}")



pred = run_inference(data)
status = "Anomali" if pred == 1 else "Normal"
print({
    "prediction": int(pred),
    "status": status
})