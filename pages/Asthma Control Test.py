import streamlit as st

def calculate_act_score(q1, q2, q3, q4, q5):
    score = q1 + q2 + q3 + q4 + q5
    return score

def interpret_act_score(score):
    if score >= 20:
        interpretation = "Well controlled"
    elif score >= 16 and score <= 19:
        interpretation = "Not well controlled"
    else:
        interpretation = "Very poorly controlled"

    return interpretation

def main():
    st.title("Asthma Control Test (ACT) Calculator")
    st.write("Answer the following questions to assess your asthma control.")

    # User input
    q1 = st.slider("During the past 4 weeks, how often did your asthma prevent you from getting as much done at work, school, or home?", min_value=1, max_value=5, value=3, step=1)
    q2 = st.slider("During the past 4 weeks, how often have you had shortness of breath?", min_value=1, max_value=5, value=3, step=1)
    q3 = st.slider("During the past 4 weeks, how often did your asthma symptoms (wheezing, coughing, chest tightness, shortness of breath) wake you up at night or earlier than usual in the morning?", min_value=1, max_value=5, value=3, step=1)
    q4 = st.slider("During the past 4 weeks, how often have you used your rescue inhaler or nebulizer medication (such as albuterol)?", min_value=1, max_value=5, value=3, step=1)
    q5 = st.slider("How would you rate your asthma control during the past 4 weeks?", min_value=1, max_value=5, value=3, step=1)

    # Calculate ACT score
    if st.button("Calculate"):
        score = calculate_act_score(q1, q2, q3, q4, q5)
        interpretation = interpret_act_score(score)

        # Display results
        st.write("Your ACT score is:", score)
        st.write("Your asthma control is:", interpretation)

if __name__ == "__main__":
    main()
