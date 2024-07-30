import streamlit as st
import pandas as pd

def csv_analytics_app():
    st.title('CSV Analytics Application')
    
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("Dataframe Preview:")
            st.dataframe(df)
            
            st.write("Summary Statistics:")
            st.write(df.describe())
            
            st.write("Dataframe Shape:")
            st.write(df.shape)
            
            st.write("Column Data Types:")
            st.write(df.dtypes)
            
        except Exception as e:
            st.error(f"Error reading CSV file: {e}")

# Function to verify access code
def verify_access_code(code):
    # Simulate checking against a list of valid access codes
    # In a real application, you might check against a database or other storage
    valid_codes = {"ACCESSCODE123", "ACCESSCODE456"}  # Example valid codes
    return code in valid_codes

# Payoneer payment instructions
payoneer_payment_instructions = """
To make a payment, please send the amount to our Payoneer account using the following details:
- **Account Holder Name:** Your Name
- **Account Holder Email:** your-email@example.com
- **Amount:** $10.00

After making the payment, please send the payment receipt to our email: verify@example.com.
Once we verify your payment, we will provide you with an access code.
"""

# Define the Streamlit app
def main():
    st.title('Exclusive Content Access')

    # User enters access code to verify payment
    st.header('Enter Access Code')
    access_code = st.text_input('Access Code')

    if st.button('Verify'):
        if verify_access_code(access_code):
            st.success('Access code verified! Redirecting to the main application...')
            csv_analytics_app()  # Call the main application function
        else:
            st.error('Invalid access code. Please ensure you have received the correct code after payment verification.')

    # Display Payoneer payment instructions
    st.header('Payment Instructions')
    st.markdown(payoneer_payment_instructions)

if __name__ == '__main__':
    main()
