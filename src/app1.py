from flask import Flask, request, jsonify
import numpy as np
from sklearn.ensemble import IsolationForest  # Example anomaly detection model
import requests

app = Flask(__name__)

# Load a pre-trained anomaly detection model
model = IsolationForest(contamination=0.05)  # Assuming a trained model is available

# Dummy threshold
THRESHOLD = 0.7

# Spinnaker rollback API details
SPINNAKER_API_URL = "http://spinnaker-api.example.com/pipelines/{app}/rollback"

def check_anomaly(metrics):
    """
    Detect anomalies using the trained AI model.
    """
    metrics_array = np.array(metrics).reshape(1, -1)
    anomaly_score = model.decision_function(metrics_array)[0]
    return anomaly_score < THRESHOLD  # Return True if an anomaly is detected

@app.route("/analyze", methods=["POST"])
def analyze_metrics():
    data = request.json
    api_metrics = data.get("metrics", [])
    
    if check_anomaly(api_metrics):
        # Trigger rollback if anomaly is detected
        response = requests.post(SPINNAKER_API_URL.format(app="your-app-name"))
        return jsonify({"rollback_triggered": True, "response": response.text})
    
    return jsonify({"rollback_triggered": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

