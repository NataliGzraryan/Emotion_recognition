Emotion Detection Using Textual Data

Overview
This project aims to perform emotion detection using textual data. The goal is to build machine learning models that can accurately classify the emotion expressed in text. The project utilizes a dataset sourced from Kaggle, prepared by Hugging Face.

Files and Directories

templates/: Directory containing templates for the web application.
DT.pkl: Decision Tree model file.
RF.pkl: Random Forest model file.
SVM.pkl: Support Vector Machine (SVM) model file.
log_reg.pkl: Logistic Regression model file.
application.py: Main application file. (Flask)
final model for deployment.ipynb: Jupyter notebook with the final model for deployment.
models.py: Python script defining and loading machine learning models.
preprocessing.py: Python script for data preprocessing.
requirements.txt: File containing Python dependencies for the project.

Problem Definition

The main problem addressed in this project is emotion detection using textual data. The models are trained to classify text into different emotion categories- 'joy, sadness, anger, fear, love, surprise'. The project focuses on achieving high accuracy in emotion classification.

Data Source

The dataset used in this project is sourced from Kaggle and prepared by Hugging Face. It serves as the foundation for training and evaluating the machine learning models.

Machine Learning Models and Accuracies

Feel free to explore the Jupyter notebook (`final model for deployment.ipynb`) for a detailed walkthrough of the model development and deployment process.

Deployment

The models are deployed using Flask and Streamlit, and can be accessed through different platforms, including AWS and Streamlit Cloud. 
The web applications allow users to input text and receive predictions about the expressed emotion.


Deployment(AWS): http://16.16.201.46:8000/
Deployment(Streamlit): https://emotionrecognition-xyhwgrmovnjnxs3pfteso2.streamlit.app/

**Note:** Ensure that you have the necessary permissions and dependencies installed before running the application.
