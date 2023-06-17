import streamlit as st

def calculate_melanoma_risk(age, gender, family_history, sunburn_history):
    risk = 0

    # Age risk factor
    if age >= 50:
        risk += 1

    # Gender risk factor
    if gender == "Male":
        risk += 1

    # Family history risk factor
    if family_history:
        risk += 1

    # Sunburn history risk factor
    if sunburn_history:
        risk += 1

    return risk

def interpret_melanoma_risk(risk):
    if risk == 0:
        interpretation = "Low risk of melanoma"
    elif risk == 1:
        interpretation = "Moderate risk of melanoma"
    elif risk == 2:
        interpretation = "High risk of melanoma"
    else:
        interpretation = "Very high risk of melanoma"

    return interpretation

def main():
    z,x,c=st.columns([1,10,1])
    x.image('THealthzoo.png')
    st.title("Melanoma Risk Calculator")
    st.write("Enter the required information to calculate your melanoma risk.")

    # User input
    age = st.number_input("Age:", min_value=1, max_value=120, value=30, step=1)
    gender = st.selectbox("Gender:", ["Male", "Female"])
    family_history = st.checkbox("Family History of Melanoma", value=False)
    sunburn_history = st.checkbox("History of Severe Sunburn", value=False)

    # Calculate melanoma risk
    if st.button("Calculate"):
        risk = calculate_melanoma_risk(age, gender, family_history, sunburn_history)
        interpretation = interpret_melanoma_risk(risk)

        # Display results
        st.write("Your melanoma risk is:", interpretation)

if __name__ == "__main__":
    main()
