import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
            
            # Plotting section
            st.write("### Data Visualization")

            # Select columns for plotting
            numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
            if len(numeric_columns) > 1:
                x_axis = st.selectbox('Select X-axis column', options=numeric_columns)
                y_axis = st.selectbox('Select Y-axis column', options=numeric_columns, index=1)

                # Scatter plot
                st.write("#### Scatter Plot")
                fig, ax = plt.subplots()
                ax.scatter(df[x_axis], df[y_axis])
                ax.set_xlabel(x_axis)
                ax.set_ylabel(y_axis)
                st.pyplot(fig)

                # Histogram
                st.write("#### Histogram")
                column = st.selectbox('Select column for histogram', options=numeric_columns)
                fig, ax = plt.subplots()
                ax.hist(df[column], bins=20)
                ax.set_xlabel(column)
                ax.set_ylabel('Frequency')
                st.pyplot(fig)

                # Pairplot
                st.write("#### Pairplot")
                sns.pairplot(df[numeric_columns])
                st.pyplot(plt)

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
