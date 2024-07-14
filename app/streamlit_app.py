import streamlit as st
import requests

st.title("Emotion Recognition")

text_input = st.text_area("Enter your text here:", height=150)

if st.button("Predict"):
    if text_input:  # Check if the input is not empty
        response = requests.post("http://localhost:8000/predict", json={"text": text_input})
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Error in prediction: " + response.text)  # Show error message from response
    else:
        st.warning("Please enter some text to analyze.")
