import streamlit as st

# Daily Macronutrients Calculator
def calculate_macronutrients(weight, height, age, gender, activity_level):
    # Convert height to inches
    height_in = int(height * 12)

    # Calculate Basal Metabolic Rate (BMR)
    if gender == 'Male':
        bmr = 10 * weight + 6.25 * height_in - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height_in - 5 * age - 161

    # Apply activity level multiplier
    activity_multiplier = {
        'Sedentary': 1.2,
        'Lightly Active': 1.375,
        'Moderately Active': 1.55,
        'Very Active': 1.725,
        'Extra Active': 1.9
    }
    bmr *= activity_multiplier[activity_level]

    # Calculate macronutrient distribution
    protein = 0.8 * weight
    fat = 0.3 * bmr / 9
    carbs = (bmr - (protein * 4) - (fat * 9)) / 4

    return {
        'Protein': round(protein, 2),
        'Fat': round(fat, 2),
        'Carbohydrates': round(carbs, 2)
    }

# Streamlit UI
st.set_page_config(page_title="Macronutrients Calculator", page_icon="🥦")
st.title("Daily Macronutrients Calculator")
st.caption("Calculate your daily macronutrient needs based on weight, height, age, gender, and activity level.")
st.write("Enter your information to calculate your daily macronutrient needs.")

weight = st.number_input("Weight (in pounds):")
height = st.number_input("Height (in feet):")
age = st.number_input("Age:")
gender = st.radio("Gender", ['Male', 'Female'])
activity_level = st.selectbox("Activity Level", ['Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active', 'Extra Active'])

if st.button("Calculate"):
    if weight <= 0 or height <= 0 or age <= 0:
        st.error("Please enter valid values for weight, height, age.")
    else:
        macronutrients = calculate_macronutrients(weight, height, age, gender, activity_level)
        st.success("Your Daily Macronutrient Needs:")
        st.write(f"Protein: {macronutrients['Protein']} grams")
        st.write(f"Fat: {macronutrients['Fat']} grams")
        st.write(f"Carbohydrates: {macronutrients['Carbohydrates']} grams")
