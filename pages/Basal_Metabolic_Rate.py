import streamlit as st

# Basal Metabolic Rate (BMR) calculation
def calculate_bmr(weight, height, age, gender, metric):
    if metric == 'FPS (Foot Pound Second)':
        weight = weight * 0.45359237  # Convert pounds to kg
        height = height * 0.3048  # Convert feet to meters
    
    if gender == 'Male':
        bmr = 4.184 * weight * height - 5 * age + 5
    else:
        bmr = 4.184 * weight * height - 5 * age - 161
    return round(bmr, 2)

# Streamlit UI
z,x,c=st.columns([1,10,1])
x.image('THealthzoo.png')
st.title("Basal Metabolic Rate (BMR) Calculator")
st.caption("BMR is the number of calories your body needs to maintain basic bodily functions at rest.")
st.write("Enter your information to calculate your BMR.")

metric_options = ['FPS (Foot Pound Second)', 'SI (International System of Units)']
selected_metric = st.radio("Select Metric", metric_options)

weight = st.number_input("Weight:")
height = st.number_input("Height:")
age = st.number_input("Age:")
gender = st.radio("Gender", ['Male', 'Female'])

if st.button("Calculate BMR"):
    if weight <= 0 or height <= 0 or age <= 0:
        st.error("Please enter valid weight, height, and age.")
    else:
        bmr = calculate_bmr(weight, height, age, gender, selected_metric)
        st.success(f"Your Basal Metabolic Rate (BMR) is {bmr} calories per day.")
