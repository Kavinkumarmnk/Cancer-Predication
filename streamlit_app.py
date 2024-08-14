
import streamlit as st
import joblib
import pandas as pd

# Load the models
model_recurrence = joblib.load('model_recurrence.pkl')
model_metastasis = joblib.load('model_metastasis.pkl')

# Title of the web app
st.title('Breast Cancer Recurrence and Metastasis Prediction')

# User inputs
age = st.number_input('Age', min_value=18, max_value=100, value=50)
tumor_size = st.number_input('Tumor Size (cm)', min_value=0.1, max_value=10.0, value=2.0)
lymph_node_involvement = st.number_input('Lymph Node Involvement', min_value=0, max_value=50, value=0)
histological_grade = st.selectbox('Histological Grade', [1, 2, 3])
er_status = st.selectbox('ER Status', ['Positive', 'Negative'])
pr_status = st.selectbox('PR Status', ['Positive', 'Negative'])
her2_status = st.selectbox('HER2 Status', ['Positive', 'Negative'])
ki67_index = st.number_input('Ki-67 Index (%)', min_value=0, max_value=100, value=20)

# Convert user inputs into a DataFrame
input_data = pd.DataFrame({
    'Age': [age],
    'Tumor Size': [tumor_size],
    'Lymph Node Involvement': [lymph_node_involvement],
    'Histological Grade': [histological_grade],
    'ER Status': [1 if er_status == 'Positive' else 0],
    'PR Status': [1 if pr_status == 'Positive' else 0],
    'HER2 Status': [1 if her2_status == 'Positive' else 0],
    'Ki-67 Index (%)': [ki67_index]
})

# Prediction button
if st.button('Predict'):
    recurrence_prediction = model_recurrence.predict(input_data)
    metastasis_prediction = model_metastasis.predict(input_data)

    # Display the predictions
    st.write(f"Recurrence Prediction: {'Yes' if recurrence_prediction[0] == 1 else 'No'}")
    st.write(f"Metastasis Prediction: {'Yes' if metastasis_prediction[0] == 1 else 'No'}")
