import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


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




def csv_analytics_app():
    st.title('CSV Analytics Application')
    
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            
            st.write("### Dataframe Preview:")
            st.dataframe(df)
            
            st.write("### Summary Statistics:")
            st.write(df.describe())
            
            st.write("### Dataframe Shape:")
            st.write(df.shape)
            
            st.write("### Column Data Types:")
            st.write(df.dtypes)

            # Check if DataFrame has numeric columns
            numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
            if numeric_columns:
                # Correlation Heatmap
                st.write("### Correlation Heatmap")
                fig, ax = plt.subplots()
                sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
                st.pyplot(fig)
                
                # Pairplot
                st.write("### Pairplot")
                if len(numeric_columns) > 1:
                    sns.pairplot(df[numeric_columns])
                    st.pyplot(plt)
                
                # Interactive Scatter Plot with Plotly
                st.write("### Interactive Scatter Plot")
                x_axis = st.selectbox('Select X-axis column', options=numeric_columns)
                y_axis = st.selectbox('Select Y-axis column', options=numeric_columns, index=1)
                fig = px.scatter(df, x=x_axis, y=y_axis, title=f'Scatter Plot of {x_axis} vs {y_axis}')
                st.plotly_chart(fig)
                
                # Histogram with Plotly
                st.write("### Interactive Histogram")
                column = st.selectbox('Select column for histogram', options=numeric_columns)
                fig = px.histogram(df, x=column, nbins=20, title=f'Histogram of {column}')
                st.plotly_chart(fig)
                
                # Box Plot with Plotly
                st.write("### Interactive Box Plot")
                fig = px.box(df, y=numeric_columns, title='Box Plot of Numeric Columns')
                st.plotly_chart(fig)

        except Exception as e:
            st.error(f"Error reading CSV file: {e}")




# Function to verify access code
def verify_access_code(code):
    # Simulate checking against a list of valid access codes
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
    # Check if the user has already been verified
    if st.session_state.get('verified', False):
        csv_analytics_app()
    else:
        st.title('Exclusive Content Access')

        # Display Payoneer payment instructions
        st.header('Payment Instructions')
        st.markdown(payoneer_payment_instructions)

        # User enters access code to verify payment
        st.header('Enter Access Code')
        access_code = st.text_input('Access Code')

        if st.button('Verify'):
            if verify_access_code(access_code):
                st.success('Access code verified! You now have access to the application.')
                st.session_state['verified'] = True  # Set verification state to True
                try:
                    st.experimental_rerun()  # Refresh the page to load the CSV analytics app
                except:
                    st.markdown('click verify again')

            else:
                st.error('Invalid access code. Please ensure you have received the correct code after payment verification.')

if __name__ == '__main__':
    main()
