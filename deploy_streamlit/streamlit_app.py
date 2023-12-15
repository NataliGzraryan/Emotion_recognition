#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Import necessary libraries
import streamlit as st
import joblib
from models import predict_emotion  # Assuming this function is compatible with Streamlit
from preprocessing import preprocess_text

# Define your models dictionary
models = {
    'Logistic Regression': 'log_reg.pkl',
    'Decision Tree': 'DT.pkl',
    'Support Vector Machine': 'SVM.pkl',
    'Random Forest': 'RF.pkl'
}

# Title of the Streamlit app
st.title('Emotion Prediction App')

# Create text input for user
text = st.text_input("Enter your text here:")

# Dropdown for model selection
selected_model_name = st.selectbox("Choose a Model", list(models.keys()))

if st.button('Predict Emotion'):
    model_name_key = models[selected_model_name]  # Ensure this matches a key in your dictionary
    processed_text = preprocess_text(text)
    emotion = predict_emotion(processed_text,model_name_key)
    st.write(f'Predicted Emotion: {emotion}')


# In[3]:


models.keys()


# In[ ]:




