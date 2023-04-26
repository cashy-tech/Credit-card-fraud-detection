import joblib
import pandas as pd
import io
from flask import Flask, jsonify, request
from flask_cors import CORS

# Load the trained model from the joblib file
model = joblib.load('../Model/trained_model.joblib')

# Create the Flask app
app = Flask(__name__)
CORS(app)  # enable CORS for all routes

# Define the API endpoint for receiving prediction requests
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    input_data = request.data.decode('utf-8').strip()

    # Convert the input CSV data to a pandas DataFrame
    input_df = pd.read_csv(io.StringIO(input_data), header=None)

    # Make a prediction using the loaded model
    prediction = model.predict(input_df)[0]

    # Convert prediction to a Python int
    prediction = int(prediction)

    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction})

# Run the app on localhost:5000
if __name__ == '__main__':
    app.run()
