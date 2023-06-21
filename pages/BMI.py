import streamlit as st

def calculate_bmi(height, weight):
    bmi = weight / ((height/100) ** 2)
    return round(bmi, 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Streamlit UI
st.title("BMI Calculator")
st.caption("BMI (Body Mass Index) is a commonly used measurement to assess the relationship between a person's weight and height. It provides a general indication of whether an individual's weight is within a healthy range for their height.")
st.write("Enter your height and weight to calculate your BMI.")

metric_options = ["FPS (Frames Per Second)", "SI (International System of Units)"]
selected_metric = st.radio("Select Metric", metric_options)

height = st.number_input("Height:",step=0.1)
weight = st.number_input("Weight:")

if st.button("Calculate BMI"):
    if height <= 0 or weight <= 0:
        st.error("Please enter valid height and weight values.")
    else:
        if selected_metric == "FPS (Frames Per Second)":
            height *= 30.48  # Convert feet to cm
            weight *= 0.45359237  # Convert pounds to kg
        bmi = calculate_bmi(height, weight)
        category = interpret_bmi(bmi)
        st.success(f"Your BMI is {bmi}. You are {category}.")
