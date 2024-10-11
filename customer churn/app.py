import streamlit as st
from churn_prediction import predict

# Define the page layout
st.title('Customer Churn Predictor')

categorical_options = {
    'State': ['KS', 'OH', 'NJ', 'OK'],  # Adjust based on your dataset
    'International Plan': ['Yes', 'No'],
    'Voice Mail Plan': ['Yes', 'No'],
    'Customer Service Calls Binned': ['0-2', '3-4', '5+']
}

# Create four rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assign inputs to the grid
with row1[0]:
    state = st.selectbox('State', categorical_options['State'])
with row1[1]:
    account_length = st.number_input('Account Length', min_value=0, step=1, max_value=200)
with row1[2]:
    area_code = st.number_input('Area Code', step=1, min_value=100, max_value=999)

with row2[0]:
    international_plan = st.selectbox('International Plan', categorical_options['International Plan'])
with row2[1]:
    voice_mail_plan = st.selectbox('Voice Mail Plan', categorical_options['Voice Mail Plan'])
with row2[2]:
    total_day_minutes = st.number_input('Total Day Minutes', min_value=0.0, step=0.1)

with row3[0]:
    total_eve_minutes = st.number_input('Total Evening Minutes', min_value=0.0, step=0.1)
with row3[1]:
    total_intl_minutes = st.number_input('Total International Minutes', min_value=0.0, step=0.1)
with row3[2]:
    customer_service_calls_binned = st.selectbox('Customer Service Calls Binned', categorical_options['Customer Service Calls Binned'])

with row4[0]:
    log_total_intl_calls = st.number_input('Log of Total International Calls', min_value=0.0, step=0.01)

# Create a dictionary for input values
input_dict = {
    'State': state,
    'Account Length': account_length,
    'Area Code': area_code,
    'International Plan': international_plan,
    'Voice Mail Plan': voice_mail_plan,
    'Total Day Minutes': total_day_minutes,
    'Total Evening Minutes': total_eve_minutes,
    'Total International Minutes': total_intl_minutes,
    'Customer Service Calls Binned': customer_service_calls_binned,
    'Log of Total International Calls': log_total_intl_calls
}

# Button to make prediction
if st.button('Predict'):
    st.snow()
    prediction = predict(input_dict)
    st.success(f'Churn Prediction: {"Yes" if prediction else "No"}')

