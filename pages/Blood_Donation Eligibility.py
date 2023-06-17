import streamlit as st

def check_eligibility(age, weight, medical_history, recent_travel, recent_medication):
    eligibility = True

    # Check eligibility based on factors
    if age < 18 or age > 65:
        eligibility = False

    if weight < 50:
        eligibility = False

    if medical_history == "Yes":
        eligibility = False

    if recent_travel == "Yes":
        eligibility = False

    if recent_medication == "Yes":
        eligibility = False

    return eligibility

def main():
    st.title("Blood Donation Eligibility Calculator")
    st.write("Check your eligibility to donate blood.")

    # User input
    age = st.number_input("Age", min_value=1, max_value=120, value=30, step=1)
    weight = st.number_input("Weight (kg)", min_value=1, value=60, step=1)
    medical_history = st.selectbox("Medical History", ["No", "Yes"])
    recent_travel = st.selectbox("Recent Travel", ["No", "Yes"])
    recent_medication = st.selectbox("Recent Medication", ["No", "Yes"])

    # Check eligibility
    if st.button("Check Eligibility"):
        eligibility = check_eligibility(age, weight, medical_history, recent_travel, recent_medication)

        # Display result
        if eligibility:
            st.write("You are eligible to donate blood.")
        else:
            st.write("You are not eligible to donate blood.")

if __name__ == "__main__":
    main()
