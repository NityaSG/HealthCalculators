import streamlit as st

def calculate_meld_score(bilirubin, creatinine, inr):
    meld_score = 0

    # Calculate MELD score
    meld_score = 3.78 * float(np.log(bilirubin)) + 11.2 * float(np.log(creatinine)) + 9.57 * float(np.log(inr)) + 6.43

    return meld_score

def main():
    z,x,c=st.columns([1,10,1])
    x.image('THealthzoo.png')
    st.title("MELD Score Calculator")
    st.write("Calculate the Model for End-Stage Liver Disease (MELD) score.")

    # User input
    bilirubin = st.number_input("Total Bilirubin (mg/dL)", min_value=0.1, step=0.1)
    creatinine = st.number_input("Serum Creatinine (mg/dL)", min_value=0.1, step=0.1)
    inr = st.number_input("INR (International Normalized Ratio)", min_value=0.1, step=0.1)

    # Calculate MELD score
    if st.button("Calculate"):
        meld_score = calculate_meld_score(bilirubin, creatinine, inr)

        # Display result
        st.write("MELD Score:", meld_score)

if __name__ == "__main__":
    main()
