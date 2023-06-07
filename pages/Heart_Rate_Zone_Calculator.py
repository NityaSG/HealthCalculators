import streamlit as st

def karvonen_formula(age, resting_heart_rate, intensity, gender, exercise_type):
    max_heart_rate = 220 - age if gender == "Male" else 226 - age
    if exercise_type == "General":
        intensity_factor = 0.5
    elif exercise_type == "Cardiovascular":
        intensity_factor = 0.6
    elif exercise_type == "High-intensity":
        intensity_factor = 0.7
    else:
        intensity_factor = 0.5
    heart_rate_reserve = max_heart_rate - resting_heart_rate
    target_heart_rate = (heart_rate_reserve * intensity * intensity_factor) + resting_heart_rate
    return target_heart_rate

z,x,c=st.columns([1,10,1])
x.image('THealthzoo.png')
st.title("Karvonen Formula Calculator")
st.caption("The Karvonen Formula, also known as the Karvonen method or Karvonen equation, is a mathematical formula used to calculate target heart rate during aerobic exercise. It takes into account an individual's age, resting heart rate, and exercise intensity level to determine the target heart rate zone.")
age = st.slider("Age", 1, 100, 30)
resting_heart_rate = st.slider("Resting Heart Rate", 1, 200, 70)
intensity = st.slider("Intensity (as a decimal)", 0.1, 1.0, 0.6, 0.05)
gender = st.selectbox("Gender", ["Male", "Female"])
exercise_type = st.selectbox("Exercise Type", ["General", "Cardiovascular", "High-intensity"])

target_heart_rate = karvonen_formula(age, resting_heart_rate, intensity, gender, exercise_type)

st.subheader("Target Heart Rate")
st.write(target_heart_rate)
