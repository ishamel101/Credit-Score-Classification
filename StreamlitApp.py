import streamlit as st
import numpy as np
from joblib import load

# Load the saved model
model = load('RandomForestClassifier.joblib')  # Replace with your model file path

# Mapping of occupation numeric values to labels
occupation_mapping = {
    0: 'Scientist', 1: 'Teacher', 2: 'Engineer', 3: 'Entrepreneur', 4: 'Developer',
    5: 'Lawyer', 6: 'Media Manager', 7: 'Doctor', 8: 'Journalist', 9: 'Manager',
    10: 'Accountant', 11: 'Musician', 12: 'Mechanic', 13: 'Writer', 14: 'Architect'
}

# Function to predict credit score
def predict_credit_score(features):
    # Prepare the input features in the same order as your model expects
    input_features = np.array(features).reshape(1, -1)  # Reshape to match model input shape
    prediction = model.predict(input_features)
    return prediction

# Streamlit app
def main():
    st.title('Credit Score Prediction App')
    st.write('Enter values for the following features to predict the credit score:')

    # Create two columns for side-by-side input fields
    col1, col2,col3 = st.columns(3)

    # Column 1 inputs
    with col1:
        outstanding_debt = st.number_input('Outstanding Debt')
        interest_rate = st.number_input('Interest Rate')
        delay_from_due_date = st.number_input('Delay from Due Date')
        changed_credit_limit = st.number_input('Changed Credit Limit')
        credit_mix = st.number_input('Credit Mix')
        credit_history_by_months = st.number_input('Credit History by Months')
        monthly_balance = st.number_input('Monthly Balance')


    # Column 2 inputs
    with col2:
        annual_income = st.number_input('Annual Income')
        total_emi_per_month = st.number_input('Total EMI per Month')
        monthly_inhand_salary = st.number_input('Monthly Inhand Salary')
        credit_utilization_ratio = st.number_input('Credit Utilization Ratio')
        num_of_delayed_payment = st.number_input('Number of Delayed Payments')
        num_credit_card = st.number_input('Number of Credit Cards')
        num_credit_inquiries = st.number_input('Number of Credit Inquiries')

    # Column 3 inputs
    with col3:
        amount_invested_monthly = st.number_input('Amount Invested Monthly')
        age = st.number_input('Age')
        num_bank_accounts = st.number_input('Number of Bank Accounts')
        month = st.number_input('Month')
        payment_of_min_amount = st.number_input('Payment of Minimum Amount')
        num_of_loan = st.number_input('Number of Loans')

    # Select occupation from predefined list
    occupation = st.selectbox('Occupation', list(occupation_mapping.values()))

    # Convert occupation label to numeric value
    occupation_value = list(occupation_mapping.keys())[list(occupation_mapping.values()).index(occupation)]

    # Append occupation value to features list
    features = [
        outstanding_debt, interest_rate, delay_from_due_date, changed_credit_limit, credit_mix,
        credit_history_by_months, num_credit_inquiries, monthly_balance, num_credit_card,
        amount_invested_monthly, annual_income, total_emi_per_month, monthly_inhand_salary,
        credit_utilization_ratio, num_of_delayed_payment, age, num_bank_accounts, month,
        payment_of_min_amount, num_of_loan, occupation_value
    ]

    # When all features are filled, predict the credit score
    if st.button('Predict Credit Score'):
        prediction = predict_credit_score(features)

        if prediction == 0:
            st.success('Predicted Credit Score is: Good')

        elif prediction == 1:
            st.warning('Predicted Credit Score is: Standard')

        else:
            st.error('Predicted Credit Score is: Poor')


# Run the app
if __name__ == '__main__':
    main()
