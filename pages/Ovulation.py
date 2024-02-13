import streamlit as st
from datetime import datetime, timedelta

# Title and description
st.title('Ovulation Calculator')
st.write('Predict ovulation dates and fertile windows for planning or avoiding pregnancy.')

# Input fields for LMP and cycle length
lmp = st.date_input("Enter the first day of the last menstrual period (LMP):")
cycle_length = st.number_input("Enter the average length of the menstrual cycle:", min_value=1)

# Button to calculate the ovulation day and fertile window
if st.button("Calculate Ovulation and Fertile Window"):
    # Convert LMP to datetime object
    lmp_date = datetime.strptime(str(lmp), '%Y-%m-%d')
    
    # Calculate ovulation (14 days before the next period)
    ovulation_day = lmp_date + timedelta(days=(cycle_length - 14))
    
    # Calculate fertile window start (5 days before ovulation)
    fertile_start = ovulation_day - timedelta(days=5)
    
    # Display the results
    st.success(f"Estimated Ovulation Day: {ovulation_day.strftime('%Y-%m-%d')}")
    st.success(f"Fertile Window: {fertile_start.strftime('%Y-%m-%d')} to {ovulation_day.strftime('%Y-%m-%d')}")
