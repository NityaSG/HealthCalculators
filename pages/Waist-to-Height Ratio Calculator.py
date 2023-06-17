import streamlit as st

def calculate_whtr(height, waist):
    whtr = waist / (height / 100)  # Convert height to meters
    return whtr

def interpret_whtr(whtr):
    if whtr < 0.35:
        interpretation = "Underweight"
    elif 0.35 <= whtr < 0.42:
        interpretation = "Healthy weight"
    elif 0.42 <= whtr < 0.48:
        interpretation = "Overweight"
    else:
        interpretation = "Obese"
    return interpretation

def main():
    z,x,c=st.columns([1,10,1])
    x.image('THealthzoo.png')
    st.title("Waist-to-Height Ratio Calculator")
    st.write("Enter your height and waist measurements to calculate your WHtR.")

    # User input
    height = st.number_input("Height (in centimeters):")
    waist = st.number_input("Waist circumference (in centimeters):")

    # Calculate WHtR
    if st.button("Calculate"):
        whtr = calculate_whtr(height, waist)
        interpretation = interpret_whtr(whtr)

        # Display results
        st.write("Your Waist-to-Height Ratio (WHtR) is:", round(whtr, 2))
        st.write("Interpretation:", interpretation)

if __name__ == "__main__":
    main()
