import streamlit as st

def calculate_kidney_stone_risk(age, gender, family_history, dietary_habits, fluid_intake):
    kidney_stone_risk = 0

    # Calculate kidney stone risk based on factors
    if age >= 40:
        kidney_stone_risk += 1

    if gender == "Male":
        kidney_stone_risk += 1

    if family_history == "Yes":
        kidney_stone_risk += 1

    if dietary_habits == "High in Oxalate":
        kidney_stone_risk += 1

    if fluid_intake < 2000:
        kidney_stone_risk += 1

    return kidney_stone_risk

def main():
    z,x,c=st.columns([1,10,1])
    x.image('THealthzoo.png')
    st.title("Kidney Stone Risk Calculator")
    st.write("Estimate your risk of developing kidney stones.")

    # User input
    age = st.number_input("Age", min_value=1, max_value=120, value=40, step=1)
    gender = st.selectbox("Gender", ["Male", "Female"])
    family_history = st.selectbox("Family History of Kidney Stones", ["No", "Yes"])
    dietary_habits = st.selectbox("Dietary Habits", ["Low in Oxalate", "Moderate in Oxalate", "High in Oxalate"])
    fluid_intake = st.number_input("Fluid Intake (mL/day)", min_value=1, value=2000, step=1)

    # Calculate kidney stone risk
    if st.button("Calculate"):
        kidney_stone_risk = calculate_kidney_stone_risk(age, gender, family_history, dietary_habits, fluid_intake)

        # Display result
        if kidney_stone_risk >= 3:
            st.write("High Risk of Kidney Stones")
        else:
            st.write("Low Risk of Kidney Stones")

if __name__ == "__main__":
    main()
