# churn_prediction_helper.py

def predict(input_data):
    """
    This is a mock churn prediction function based on simple heuristics.
    In a real-world case, this would use a trained machine learning model.
    """
    # Simulate churn prediction based on some simple conditions
    churn_risk = 0

    # Example conditions to estimate churn risk (these are arbitrary for demo)
    if input_data['Account Length'] < 50:
        churn_risk += 1
    if input_data['Total Day Minutes'] > 300:
        churn_risk += 1
    if input_data['International Plan'] == 'Yes':
        churn_risk += 1
    if input_data['Customer Service Calls Binned'] == '5+':
        churn_risk += 1
    if input_data['Voice Mail Plan'] == 'No':
        churn_risk += 0.5  # Slightly higher risk without voicemail
    if input_data['Log of Total International Calls'] > 1.5:
        churn_risk += 1

    # Threshold: If churn_risk exceeds a certain value, we predict churn
    return churn_risk > 2  # True means churn, False means no churn
