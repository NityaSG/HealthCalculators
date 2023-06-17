import streamlit as st

def calculate_psi(age, gender, temperature, heart_rate, respiratory_rate, systolic_bp, presence_of_neoplastic_disease):
    points = 0

    # Age points
    if age >= 50 and age <= 64:
        points += 5
    elif age >= 65 and age <= 79:
        points += 10
    elif age >= 80:
        points += 20

    # Gender points
    if gender == "Male":
        points += 10

    # Temperature points
    if temperature < 35:
        points += 20
    elif temperature >= 35 and temperature <= 38.9:
        points += 0
    elif temperature >= 39 and temperature <= 41.9:
        points += 15
    elif temperature >= 42:
        points += 20

    # Heart rate points
    if heart_rate >= 125:
        points += 20
    elif heart_rate >= 110 and heart_rate <= 124:
        points += 10
    elif heart_rate >= 100 and heart_rate <= 109:
        points += 5

    # Respiratory rate points
    if respiratory_rate >= 30:
        points += 20
    elif respiratory_rate >= 24 and respiratory_rate <= 29:
        points += 10

    # Systolic blood pressure points
    if systolic_bp < 90:
        points += 20
    elif systolic_bp >= 90 and systolic_bp <= 99:
        points += 10

    # Presence of neoplastic disease points
    if presence_of_neoplastic_disease:
        points += 30

    return points

def interpret_psi(points):
    if points <= 70:
        interpretation = "Risk Class I - Low risk"
    elif points >= 71 and points <= 90:
        interpretation = "Risk Class II - Low risk"
    elif points >= 91 and points <= 130:
        interpretation = "Risk Class III - Low risk"
    elif points >= 131 and points <= 170:
        interpretation = "Risk Class IV - High risk"
    else:
        interpretation = "Risk Class V - High risk"

    return interpretation

def main():
    z,x,c=st.columns([1,10,1])
    x.image('THealthzoo.png')
    st.title("Pneumonia Severity Index (PSI) Calculator")
    st.write("Enter the required information to calculate your PSI.")

    # User input
    age = st.number_input("Age:", min_value=1, max_value=120, value=30, step=1)
    gender = st.selectbox("Gender:", ["Male", "Female"])
    temperature = st.number_input("Temperature (°C):", min_value=34, max_value=43, value=37, step=0.1)
    heart_rate = st.number_input("Heart Rate (beats per minute):", min_value=1, value=70, step=1)
    respiratory_rate = st.number_input("Respiratory Rate (breaths per minute):", min_value=1, value=20, step=1)
    systolic_bp = st.number_input("Systolic Blood Pressure (mmHg):", min_value=1, value=120, step=1)
    presence_of_neoplastic_disease = st.checkbox("Presence of Neoplastic Disease", value=False)

    # Calculate PSI
    if st.button("Calculate"):
        points = calculate_psi(age, gender, temperature, heart_rate, respiratory_rate, systolic_bp, presence_of_neoplastic_disease)
