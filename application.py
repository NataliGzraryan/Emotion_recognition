# Import necessary libraries
from flask import Flask, request, render_template, redirect, url_for
from models import predict_emotion
from preprocessing import preprocess_text

# Initialize the Flask app
app = Flask(__name__)

# Define a route for the main page
@app.route("/", methods=["GET"])
def read_root():
    # Serve the index.html template
    return render_template("index.html")

# Define a route to handle the prediction request
@app.route("/predict/", methods=["POST"])
def predict():
    # Extract data from form
    text = request.form.get("text")
    model_name = request.form.get("model_name")

    # Preprocess the text using the function from preprocessing.py
    processed_text = preprocess_text(text)

    # Get the emotion prediction by calling predict_emotion function from models.py
    # This function should accept the processed text and model name, and return the predicted emotion
    emotion = predict_emotion(processed_text, model_name)

    # Return the prediction result along with the original data to the user
    # This data is displayed in the HTML template
    return render_template("index.html", emotion=emotion, text=text, model_name=model_name)

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
