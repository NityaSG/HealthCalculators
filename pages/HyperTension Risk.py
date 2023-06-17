import streamlit as st

def calculate_hypertension_risk(age, weight, family_history, lifestyle_habits, existing_conditions):
    hypertension_risk = 0

    # Calculate hypertension risk based on factors
    if age >= 40:
        hypertension_risk += 1

    if weight >= 90:
        hypertension_risk += 1

    if family_history == "Yes":
        hypertension_risk += 1

    if lifestyle_habits == "Sedentary":
        hypertension_risk += 1

    if existing_conditions == "Yes":
        hypertension_risk += 1

    return hypertension_risk

def main():
    z,x,c=st.columns([1,10,1])
    x.image('THealthzoo.png')
    st.title("Hypertension Risk Calculator")
    st.write("Assess your risk of developing high blood pressure.")

    # User input
    age = st.number_input("Age", min_value=1, max_value=120, value=40, step=1)
    weight = st.number_input("Weight (kg)", min_value=1, value=70, step=1)
    family_history = st.selectbox("Family History of Hypertension", ["No", "Yes"])
    lifestyle_habits = st.selectbox("Lifestyle Habits", ["Active", "Moderately Active", "Sedentary"])
    existing_conditions = st.selectbox("Existing Health Conditions", ["No", "Yes"])

    # Calculate hypertension risk
    if st.button("Calculate"):
        hypertension_risk = calculate_hypertension_risk(age, weight, family_history, lifestyle_habits, existing_conditions)

        # Display result
        if hypertension_risk >= 3:
            st.write("High Risk of Hypertension")
        else:
            st.write("Low Risk of Hypertension")

if __name__ == "__main__":
    main()
