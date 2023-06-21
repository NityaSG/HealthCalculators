import streamlit as st

def calculate_osteoporosis_risk(age, gender, weight, smoking, alcohol, calcium_intake):
    osteoporosis_risk = 0

    # Calculate osteoporosis risk based on factors
    if age >= 50:
        osteoporosis_risk += 1

    if gender == "Female":
        osteoporosis_risk += 1

    if weight < 60:
        osteoporosis_risk += 1

    if smoking == "Yes":
        osteoporosis_risk += 1

    if alcohol == "Yes":
        osteoporosis_risk += 1

    if calcium_intake < 1000:
        osteoporosis_risk += 1

    return osteoporosis_risk

def main():
    z,x,c=st.columns([1,10,1])
    x.image('THealthzoo.png')
    st.title("Osteoporosis Risk Calculator")
    st.write("Assess your risk of developing osteoporosis.")

    # User input
    age = st.number_input("Age", min_value=1, max_value=120, value=50, step=1)
    gender = st.selectbox("Gender", ["Male", "Female"])
    weight = st.number_input("Weight (Pounds)", min_value=1, value=70, step=1)
    weight*=2.205
    smoking = st.selectbox("Smoking", ["No", "Yes"])
    alcohol = st.selectbox("Alcohol Consumption", ["No", "Yes"])
    calcium_intake = st.number_input("Calcium Intake (mg/day)", min_value=1, value=1000, step=1)

    # Calculate osteoporosis risk
    if st.button("Calculate"):
        osteoporosis_risk = calculate_osteoporosis_risk(age, gender, weight, smoking, alcohol, calcium_intake)

        # Display result
        if osteoporosis_risk >= 3:
            st.write("High Risk of Osteoporosis")
        else:
            st.write("Low Risk of Osteoporosis")

if __name__ == "__main__":
    main()
