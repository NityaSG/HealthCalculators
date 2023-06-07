import streamlit as st

def calculate_bac(weight, gender, drinks, alcohol_percentage, duration, metabolism_rate):
    if gender == "Male":
        r = 0.68
    else:
        r = 0.55

    bac = (drinks * alcohol_percentage * 5.14) / (weight * r) - metabolism_rate * duration
    return max(bac, 0)
z,x,c=st.columns([1,10,1])
x.image('THealthzoo.png')
st.title("Blood Alcohol Content (BAC) Calculator")

weight = st.number_input("Weight (in kg)", min_value=1.0)
gender = st.selectbox("Gender", ["Male", "Female"])
drinks = st.number_input("Number of Standard Drinks", min_value=1)
alcohol_percentage = st.number_input("Alcohol Percentage per Drink", min_value=0.1, max_value=100.0, step=0.1)
duration = st.number_input("Drinking Duration (in hours)", min_value=0.1)
metabolism_rate = st.number_input("Metabolism Rate (0.015 for average)", min_value=0.0)

bac = calculate_bac(weight, gender, drinks, alcohol_percentage, duration, metabolism_rate)

st.subheader("Blood Alcohol Content (BAC)")
st.write(f"{bac:.4f}%")

if bac >= 0.08:
    st.warning("You are likely over the legal driving limit.")
else:
    st.success("You are likely below the legal driving limit.")


st.caption("Please note that this calculator provides an estimate and should be used as a guideline. Individual variations, tolerance, and other factors can affect BAC. It is always important to drink responsibly and never drink and drive.")