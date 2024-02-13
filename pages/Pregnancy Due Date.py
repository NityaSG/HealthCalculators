import streamlit as st
from datetime import datetime, timedelta

# Title and description
st.title('Pregnancy Due Date Calculator')
st.write('Estimate the due date for a pregnant woman based on her last menstrual period (LMP) or the conception date if known.')

# Input method selection
calc_method = st.radio("Calculate by:", ("Last Menstrual Period (LMP)", "Conception Date"))

# Input field for date
if calc_method == "Last Menstrual Period (LMP)":
    input_date = st.date_input("Enter the date of the last menstrual period (LMP):")
    calculation_base = "LMP"
else:
    input_date = st.date_input("Enter the conception date:")
    calculation_base = "Conception"

# Button to calculate the due date
if st.button("Calculate Due Date"):
    # Convert input date to datetime object
    input_date = datetime.strptime(str(input_date), '%Y-%m-%d')
    
    # Calculate due date based on selected method
    if calculation_base == "LMP":
        due_date = input_date + timedelta(days=280)  # Add 280 days for LMP
    else:
        due_date = input_date + timedelta(days=266)  # Add 266 days for conception date
    
    # Display the result
    st.success(f"Estimated Due Date: {due_date.strftime('%Y-%m-%d')}")
