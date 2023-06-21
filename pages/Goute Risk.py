import streamlit as st

def calculate_gout_risk(age, gender, weight, blood_pressure, diet, alcohol_consumption, medical_history):
    gout_risk = 0

    # Calculate gout risk based on factors
    if age >= 40:
        gout_risk += 1

    if gender == "Male":
        gout_risk += 1

    if weight >= 100:
        gout_risk += 1

    if blood_pressure >= 140/90:
        gout_risk += 1

    if diet == "High in Purines":
        gout_risk += 1

    if alcohol_consumption == "High":
        gout_risk += 1

    if medical_history == "Yes":
        gout_risk += 1

    return gout_risk

def main():
    z,x,c=st.columns([1,10,1])
    x.image('THealthzoo.png')
    st.title("Gout Risk Calculator")
    st.write("Calculate your risk of developing gout.")

    # User input
    age = st.number_input("Age", min_value=1, max_value=120, value=40, step=1)
    gender = st.selectbox("Gender", ["Male", "Female"])
    weight = st.number_input("Weight (kg)", min_value=1, value=70, step=1)
    weight*=2.205
    blood_pressure = st.number_input("Blood Pressure (mmHg)", min_value=1, value=120, step=1)
    diet = st.selectbox("Diet", ["Low in Purines", "Moderate in Purines", "High in Purines"])
    alcohol_consumption = st.selectbox("Alcohol Consumption", ["Low", "Moderate", "High"])
    medical_history = st.selectbox("Medical History of Gout", ["No", "Yes"])

    # Calculate gout risk
    if st.button("Calculate"):
        gout_risk = calculate_gout_risk(age, gender, weight, blood_pressure, diet, alcohol_consumption, medical_history)

        # Display result
        if gout_risk >= 3:
            st.write("High Risk of Gout")
        else:
            st.write("Low Risk of Gout")

if __name__ == "__main__":
    main()
