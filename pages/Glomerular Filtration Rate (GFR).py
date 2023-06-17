import streamlit as st

def calculate_gfr(age, gender, serum_creatinine, is_aa=False):
    if is_aa:
        k = 1.159 if gender == "Male" else 1
        gfr = 141 * min(serum_creatinine / k, 1) ** (-0.411) * max(serum_creatinine / k, 1) ** (-1.209) * 0.993 ** age
    else:
        k = 0.9 if gender == "Male" else 0.7
        gfr = 175 * (serum_creatinine ** -1.154) * (age ** -0.203) * k

    return gfr

def main():
    st.title("Glomerular Filtration Rate (GFR) Calculator")
    st.write("Enter the required information to calculate your GFR.")

    # User input
    age = st.number_input("Age:", min_value=1, max_value=120, value=30, step=1)
    gender = st.selectbox("Gender:", ["Male", "Female"])
    serum_creatinine = st.number_input("Serum Creatinine (mg/dL):", min_value=0.1, value=0.8, step=0.1)
    is_aa = st.checkbox("African American", value=False)

    # Calculate GFR
    if st.button("Calculate"):
        gfr = calculate_gfr(age, gender, serum_creatinine, is_aa)

        # Display results
        st.write("Your Glomerular Filtration Rate (GFR) is:", round(gfr, 2), "mL/min")

if __name__ == "__main__":
    main()
