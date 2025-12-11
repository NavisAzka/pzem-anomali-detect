from flask import Flask, request, jsonify
from inference import run_inference   

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    required = [
        'arus', 'voltase', 'daya', 'frekuensi',
        'suhu_dalam', 'suhu_luar', 'prakiraan_suhu_luar'
    ]
    if not all(k in data for k in required):
        return jsonify({"error": "missing fields"}), 400

    pred = run_inference(data)
    status = "Anomali" if pred == 1 else "Normal"

    return jsonify({
        "prediction": int(pred),
        "status": status
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=49000, debug=True)
