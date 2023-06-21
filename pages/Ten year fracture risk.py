import streamlit as st

def calculate_fracture_risk(age, gender, weight, smoking, bmd):
    fracture_risk = 0

    # Calculate fracture risk based on factors
    if gender == "Male":
        fracture_risk += 1.06
    else:
        fracture_risk += 0.89

    if weight < 70:
        fracture_risk += 0.1
    else:
        fracture_risk += 0.2

    if smoking == "Yes":
        fracture_risk += 0.3

    if bmd < 0.8:
        fracture_risk += 0.4
    else:
        fracture_risk += 0.2

    # Calculate 10-year fracture risk
    fracture_risk *= (age / 10)

    return fracture_risk

def main():
    z,x,c=st.columns([1,10,1])
    x.image('THealthzoo.png')
    st.title("10-Year Fracture Risk Calculator")
    st.write("Estimate your 10-year risk of experiencing a fracture.")

    # User input
    age = st.number_input("Age", min_value=1, max_value=120, value=30, step=1)
    gender = st.selectbox("Gender", ["Male", "Female"])
    weight = st.number_input("Weight (pounds)", min_value=1, value=60, step=1)
    weight*=2.205
    smoking = st.selectbox("Smoking", ["No", "Yes"])
    bmd = st.number_input("Bone Mineral Density", min_value=0.1, value=1.0, step=0.1)

    # Calculate fracture risk
    if st.button("Calculate"):
        fracture_risk = calculate_fracture_risk(age, gender, weight, smoking, bmd)

        # Display result
        st.write("10-Year Fracture Risk:", fracture_risk)

if __name__ == "__main__":
    main()
