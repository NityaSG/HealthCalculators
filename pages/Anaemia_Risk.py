import streamlit as st

def calculate_anemia_risk(age, gender, dietary_habits, medical_history, fatigue, weakness):
    anemia_risk = 0

    # Calculate anemia risk based on factors
    if age > 50:
        anemia_risk += 2

    if gender == "Female":
        anemia_risk += 1

    if dietary_habits == "Vegetarian":
        anemia_risk += 1

    if medical_history == "Yes":
        anemia_risk += 2

    if fatigue == "Yes":
        anemia_risk += 1

    if weakness == "Yes":
        anemia_risk += 1

    return anemia_risk

def main():
    st.title("Anemia Risk Calculator")
    st.write("Assess your risk of anemia based on various factors.")

    # User input
    age = st.number_input("Age", min_value=1, max_value=120, value=30, step=1)
    gender = st.selectbox("Gender", ["Male", "Female"])
    dietary_habits = st.selectbox("Dietary Habits", ["Non-vegetarian", "Vegetarian"])
    medical_history = st.selectbox("Medical History", ["No", "Yes"])
    fatigue = st.selectbox("Experience Fatigue", ["No", "Yes"])
    weakness = st.selectbox("Experience Weakness", ["No", "Yes"])

    # Calculate anemia risk
    if st.button("Calculate"):
        anemia_risk = calculate_anemia_risk(age, gender, dietary_habits, medical_history, fatigue, weakness)

        # Display result
        st.write("Anemia Risk:", anemia_risk)

if __name__ == "__main__":
    main()
