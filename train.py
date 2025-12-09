import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import joblib

# 1. Muat data
df = pd.read_csv('tes.csv')

# 2. Drop kolom timestamp
df = df.drop(columns=['timestamp'])

# 3. Pisahkan fitur dan label
X = df.drop(columns=['label_anomali'])
y = df['label_anomali']

# 4. Bagi data latih/tes (70%/30%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# 5. Latih model Random Forest
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 6. Evaluasi model
y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, zero_division=0)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Akurasi:", acc)
print("Presisi:", prec)
print("Recall:", rec)
print("F1-score:", f1)
print("Confusion Matrix:\n", cm)

# 7. Contoh prediksi
result = X_test.copy()
result['Label_Aktual'] = y_test.values
result['Prediksi'] = y_pred
# print(result.head())

joblib.dump(clf, 'model_rtos.pkl')

# saat runtime
# clf = joblib.load('model_rtos.pkl')


# ===============   
# UJI COBA
# ===============

sample = {
    'arus': 0.15,
    'voltase': 230.5,
    'daya': 20.0,
    'frekuensi': 49.95,
    'suhu_dalam': 20.5,
    'suhu_luar': 23.0,
    'prakiraan_suhu_luar': 55.0
}


# print sample
print("\nContoh Sampel:")
for k, v in sample.items():
    print(f"{k}: {v}")


print("\nContoh Prediksi:")

df_sample = pd.DataFrame([sample])

pred = clf.predict(df_sample)[0]
print("Anomali" if pred == 1 else "Normal")
