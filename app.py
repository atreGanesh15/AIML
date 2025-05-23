# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1I4yFhA0pfv3qy-kbG11JmG0c0aotQ2I0
"""

import streamlit as st
import pandas as pd

# Error handling for joblib import
try:
    from joblib import load
except ImportError as e:
    st.error("Error loading the joblib module. Please ensure it's installed.")
    raise e  # Exit if the import fails

# Try loading the model
try:
    model = load('best_model.joblib')
except Exception as e:
    st.error(f"Error loading the model: {e}")
    raise e

# The rest of your app code
st.title("Smog Level Prediction")
st.write("Enter vehicle details to predict smog levels.")

# Input fields for vehicle data (replace with your actual fields)
engine_size = st.number_input("Engine Size (L)", min_value=0.0, max_value=10.0, value=2.0)
cylinders = st.number_input("Cylinders", min_value=1, max_value=12, value=4)

# When the user presses the button, predict smog level
if st.button("Predict Smog Level"):
    input_data = pd.DataFrame({
        'Engine_Size': [engine_size],
        'Cylinders': [cylinders]
    })
    
    # Make the prediction
    prediction = model.predict(input_data)[0]
    
    if prediction == 0:
        st.success("The predicted smog level is LOW.")
    elif prediction == 1:
        st.warning("The predicted smog level is MEDIUM.")
    else:
        st.error("The predicted smog level is HIGH.")
