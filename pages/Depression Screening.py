import streamlit as st

def calculate_depression_likelihood(answers):
    depression_likelihood = 0

    # Calculate depression likelihood based on answers
    for answer in answers:
        depression_likelihood += answer

    return depression_likelihood

def main():
    st.title("Depression Screening Calculator")
    st.write("Assess the likelihood of depression based on a series of questions.")

    # Questions and answer choices
    questions = [
        "Little interest or pleasure in doing things?",
        "Feeling down, depressed, or hopeless?",
        "Trouble falling or staying asleep, or sleeping too much?",
        "Feeling tired or having little energy?",
        "Poor appetite or overeating?",
        "Feeling bad about yourself, or that you are a failure or have let yourself or your family down?",
        "Trouble concentrating on things, such as reading the newspaper or watching television?",
        "Moving or speaking so slowly that other people could have noticed, or the opposite - being so fidgety or restless that you have been moving around a lot more than usual?",
        "Thoughts that you would be better off dead, or of hurting yourself in some way?"
    ]

    # User input
    answers = []
    for i, question in enumerate(questions):
        answer = st.selectbox(question, [0, 1, 2, 3])
        answers.append(answer)

    # Calculate depression likelihood
    if st.button("Calculate"):
        depression_likelihood = calculate_depression_likelihood(answers)

        # Display result
        st.write("Depression Likelihood:", depression_likelihood)

if __name__ == "__main__":
    main()
