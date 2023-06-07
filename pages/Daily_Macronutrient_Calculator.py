import streamlit as st

def calculate_daily_calorie_needs(weight, height, age, gender, activity_level, goal):
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_levels = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725,
        "Extra Active": 1.9
    }
    calorie_intake = bmr * activity_levels[activity_level]

    if goal == "Weight Loss":
        calorie_intake -= 500
    elif goal == "Muscle Gain":
        calorie_intake += 250

    return calorie_intake

def calculate_macronutrients(calorie_intake, protein_ratio, fat_ratio, carb_ratio):
    protein = (protein_ratio / 100) * calorie_intake / 4
    fat = (fat_ratio / 100) * calorie_intake / 9
    carb = (carb_ratio / 100) * calorie_intake / 4

    return protein, fat, carb

z,x,c=st.columns([1,10,1])
x.image('THealthzoo.png')
st.title("Daily Macronutrient Calculator")

weight = st.number_input("Weight (in kg)", min_value=1.0)
height = st.number_input("Height (in cm)", min_value=1.0)
age = st.number_input("Age (in years)", min_value=1.0)
gender = st.selectbox("Gender", ["Male", "Female"])
activity_level = st.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active"])
goal = st.selectbox("Goal", ["Weight Loss", "Maintenance", "Muscle Gain"])
protein_ratio = st.number_input("Protein Ratio (%)", min_value=0.0, max_value=100.0)
fat_ratio = st.number_input("Fat Ratio (%)", min_value=0.0, max_value=100.0)
carb_ratio = 100.0 - protein_ratio - fat_ratio

calorie_intake = calculate_daily_calorie_needs(weight, height, age, gender, activity_level, goal)
protein, fat, carb = calculate_macronutrients(calorie_intake, protein_ratio, fat_ratio, carb_ratio)

st.subheader("Daily Calorie Intake")
st.write(f"{calorie_intake:.2f} calories")

st.subheader("Daily Macronutrient Breakdown")
st.write(f"Protein: {protein:.2f} grams")
st.write(f"Fat: {fat:.2f} grams")
st.write(f"Carbohydrate: {carb:.2f} grams")
