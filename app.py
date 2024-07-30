import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def csv_analytics_app():
    st.title('Random Points Plot')

    # Clear other UI elements
    st.empty()

    # Generate random points
    num_points = 100
    x = np.random.rand(num_points)
    y = np.random.rand(num_points)

    # Plot random points
    fig, ax = plt.subplots()
    ax.scatter(x, y, alpha=0.6)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Scatter Plot of Random Points')

    st.pyplot(fig)

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

    # Display Payoneer payment instructions
    st.header('Payment Instructions')
    st.markdown(payoneer_payment_instructions)

    # User enters access code to verify payment
    st.header('Enter Access Code')
    access_code = st.text_input('Access Code')

    if st.button('Verify'):
        if verify_access_code(access_code):
            st.success('Access code verified! Redirecting to the main application...')
            st.session_state['uploaded_file'] = None  # Clear any previously uploaded file
            st.experimental_rerun()  # Refresh the page to load the CSV analytics app
        else:
            st.error('Invalid access code. Please ensure you have received the correct code after payment verification.')

if __name__ == '__main__':
    main()
