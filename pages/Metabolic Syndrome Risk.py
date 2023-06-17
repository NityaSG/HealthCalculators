import streamlit as st

def calculate_metabolic_syndrome_risk(waist_circumference, blood_pressure, blood_sugar, cholesterol, triglycerides):
    metabolic_syndrome_risk = 0

    # Calculate metabolic syndrome risk based on factors
    if waist_circumference >= 102:
        metabolic_syndrome_risk += 1

    if blood_pressure >= 130/85:
        metabolic_syndrome_risk += 1

    if blood_sugar >= 100:
        metabolic_syndrome_risk += 1

    if cholesterol >= 150:
        metabolic_syndrome_risk += 1

    if triglycerides >= 150:
        metabolic_syndrome_risk += 1

    return metabolic_syndrome_risk

def main():
    z,x,c=st.columns([1,10,1])
    x.image('THealthzoo.png')
    st.title("Metabolic Syndrome Calculator")
    st.write("Determine your risk of metabolic syndrome.")

    # User input
    waist_circumference = st.number_input("Waist Circumference (cm)", min_value=1, value=80, step=1)
    blood_pressure = st.number_input("Blood Pressure (mmHg)", min_value=1, value=120, step=1)
    blood_sugar = st.number_input("Blood Sugar (mg/dL)", min_value=1, value=90, step=1)
    cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=1, value=200, step=1)
    triglycerides = st.number_input("Triglycerides (mg/dL)", min_value=1, value=150, step=1)

    # Calculate metabolic syndrome risk
    if st.button("Calculate"):
        metabolic_syndrome_risk = calculate_metabolic_syndrome_risk(waist_circumference, blood_pressure, blood_sugar, cholesterol, triglycerides)

        # Display result
        if metabolic_syndrome_risk >= 3:
            st.write("High Risk of Metabolic Syndrome")
        else:
            st.write("Low Risk of Metabolic Syndrome")

if __name__ == "__main__":
    main()
