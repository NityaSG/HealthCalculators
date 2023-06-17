import streamlit as st

def calculate_preterm_birth_risk(age, bmi, prior_preterm, gestational_age, cervical_length):
    risk = 0

    # Age risk factor
    if age < 18 or age > 35:
        risk += 1

    # BMI risk factor
    if bmi < 18.5 or bmi > 24.9:
        risk += 1

    # Prior preterm birth risk factor
    if prior_preterm:
        risk += 1

    # Gestational age risk factor
    if gestational_age < 37:
        risk += 1

    # Cervical length risk factor
    if cervical_length < 25:
        risk += 1

    return risk

def interpret_preterm_birth_risk(risk):
    if risk == 0:
        interpretation = "Low risk of preterm birth"
    elif risk == 1:
        interpretation = "Moderate risk of preterm birth"
    elif risk == 2:
        interpretation = "High risk of preterm birth"
    else:
        interpretation = "Very high risk of preterm birth"

    return interpretation

def main():
    z,x,c=st.columns([1,10,1])
    x.image('THealthzoo.png')
    st.title("Preterm Birth Risk Calculator")
    st.write("Enter the required information to calculate your preterm birth risk.")

    # User input
    age = st.number_input("Age:", min_value=1, max_value=120, value=25, step=1)
    bmi = st.number_input("BMI:", min_value=10, max_value=100, value=22, step=0.1)
    prior_preterm = st.checkbox("Prior Preterm Birth", value=False)
    gestational_age = st.number_input("Gestational Age (weeks):", min_value=1, max_value=50, value=40, step=1)
    cervical_length = st.number_input("Cervical Length (mm):", min_value=1, max_value=100, value=35, step=1)

    # Calculate preterm birth risk
    if st.button("Calculate"):
        risk = calculate_preterm_birth_risk(age, bmi, prior_preterm, gestational_age, cervical_length)
        interpretation = interpret_preterm_birth_risk(risk)

        # Display results
        st.write("Your preterm birth risk is:", interpretation)

if __name__ == "__main__":
    main()
