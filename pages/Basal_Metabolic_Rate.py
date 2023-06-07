import streamlit as st

def calculate_bmr(weight, height, age, gender):
    if gender == "Male":
        bmr = 66 + (13.75 * weight) + (5 * height) - (6.75 * age)
    else:
        bmr = 655 + (9.56 * weight) + (1.85 * height) - (4.68 * age)
    return bmr

def main():
    z,x,c=st.columns([1,10,1])
    x.image('THealthzoo.png')
    st.title("Basal Metabolic Rate (BMR) Calculator")
    st.write("This calculator estimates your Basal Metabolic Rate (BMR), which represents the number of calories you burn at rest.")

    weight = st.number_input("Weight (in kg)", min_value=1.0, step=0.1)
    height = st.number_input("Height (in cm)", min_value=1.0, step=0.1)
    age = st.number_input("Age", min_value=1, step=1)
    gender = st.selectbox("Gender", ("Male", "Female"))

    if st.button("Calculate BMR"):
        bmr = calculate_bmr(weight, height, age, gender)
        st.success(f"Your Basal Metabolic Rate (BMR) is {bmr} calories/day.")

if __name__ == "__main__":
    main()
