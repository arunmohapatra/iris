from flask import Flask, request, jsonify
import pickle
import joblib
import os

app = Flask(__name__)

# Print the current working directory for debuggingg
print("Current Working Directory:", os.getcwd())
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")

# Load the model
model = joblib.load(model_path)
print("Model loaded successfully.")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Print the received data for debugging
        print("Received data:", request.json)

        # Parse input JSON
        input_data = request.json["data"]
        prediction = model.predict(input_data)
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
