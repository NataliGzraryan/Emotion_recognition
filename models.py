import joblib
import pickle
# Dictionary to hold the models
models = {
    'log_reg': 'log_reg.pkl',
    'decision_tree': 'DT.pkl',
    'svm': 'SVM.pkl',
    'random_forest': 'RF.pkl'
}

# Function to load models
def load_model(model_name):
    """
    Load the model from the disk.

    Parameters:
    model_name (str): The name of the model to load.

    Returns:
    The loaded model.
    """
    model_path = models.get(model_name)
    if model_path:
        return pickle.load(open(model_path, 'rb'))

    else:
        raise ValueError("Model name not recognized.")

# Function to predict emotion
def predict_emotion(text, model_name):
    """
    Predict the emotion of the given text using the specified model.

    Parameters:
    text (str): The text to predict emotion for.
    model_name (str): The name of the model to use.

    Returns:
    str: The predicted emotion.
    """
    model = load_model(model_name)
    prediction = model.predict([text])
    return prediction[0]  
