import streamlit as st
#st.set_page_config(page_title="Calorie Intake",layout='wide')
def calculate_calorie_intake(age, gender, weight, height, activity_level):
    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() == 'female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        return "Invalid gender. Please enter 'male' or 'female'."

    activity_levels = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725,
        'extra active': 1.9
    }

    if activity_level.lower() in activity_levels:
        calorie_intake = bmr * activity_levels[activity_level.lower()]
        return int(calorie_intake)
    else:
        return "Invalid activity level. Please choose from 'sedentary', 'lightly active', 'moderately active', 'very active', 'extra active'."


# Example usage
z,x,c=st.columns([1,10,1])
x.image('THealthzoo.png')
x.header("Calorie Intake Calculator")
c,e,d=st.columns([2,1,2])
age =x.number_input("age",step=1)
weight = x.number_input("weight")
height = x.number_input("Height")
gender=x.radio('Gender', ['male', 'female'])
activity_level = x.select_slider('Select Activity level', ['sedentary', 'lightly active', 'moderately active', 'very active', 'extra active'])
if x.button("Submit"):
    result = calculate_calorie_intake(age, gender, weight, height, activity_level)
    if isinstance(result, int):
        x.subheader("Your daily calorie intake should be: "+str(result)+" calories.")
    else:
        x.caption(result)
