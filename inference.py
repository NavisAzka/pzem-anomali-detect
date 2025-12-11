import pandas as pd
import joblib

# Load model sekali di awal
clf = joblib.load('./model/model_rtos_11-12-2025_12:19:03.pkl')

def run_inference(sample: dict):
    """Return 1 = anomali, 0 = normal"""
    df_sample = pd.DataFrame([sample])
    pred = clf.predict(df_sample)[0]
    return pred
