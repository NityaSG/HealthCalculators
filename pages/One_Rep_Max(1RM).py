import streamlit as st

# One Rep Max (1RM) calculation
def calculate_1rm(weight_lifted, repetitions, body_weight, age):
    epley_coefficient = 1 + (repetitions / 30)
    one_rep_max = weight_lifted * epley_coefficient
    adjusted_one_rep_max = one_rep_max * (1 + 0.0333 * age)
    relative_one_rep_max = adjusted_one_rep_max / body_weight
    return round(relative_one_rep_max, 2)

# Streamlit UI
st.set_page_config(page_title="1RM Calculator", page_icon="💪")
st.title("One Rep Max (1RM) Calculator")
st.caption("Calculate your estimated one rep max based on weight lifted, number of repetitions, body weight, and age.")
st.write("Enter your information to calculate your estimated 1RM.")

weight_lifted = st.number_input("Weight Lifted (in pounds):")
repetitions = st.number_input("Number of Repetitions:")
body_weight = st.number_input("Body Weight (in pounds):")
age = st.number_input("Age:")

if st.button("Calculate 1RM"):
    if weight_lifted <= 0 or repetitions <= 0 or body_weight <= 0 or age <= 0:
        st.error("Please enter valid values for weight lifted, repetitions, body weight, and age.")
    else:
        one_rep_max = calculate_1rm(weight_lifted, repetitions, body_weight, age)
        st.success(f"Your estimated One Rep Max (1RM) relative to body weight is {one_rep_max}.")
