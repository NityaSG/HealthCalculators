import streamlit as st

def calculate_one_rep_max(weight_lifted, reps):
    one_rep_max = weight_lifted * (1 + (reps / 30))
    return one_rep_max

def calculate_training_intensity(one_rep_max):
    intensity_ranges = {
        "Endurance": (0.6, 0.69),
        "Hypertrophy": (0.7, 0.79),
        "Strength": (0.8, 0.89),
        "Power": (0.9, 1.0)
    }
    training_intensity = {}
    for intensity, (lower, upper) in intensity_ranges.items():
        training_intensity[intensity] = (lower * one_rep_max, upper * one_rep_max)
    return training_intensity

z,x,c=st.columns([1,10,1])
x.image('THealthzoo.png')
st.title("One-Rep Max (1RM) Calculator")

weight_lifted = st.number_input("Weight Lifted (in kg)", min_value=1.0)
reps = st.number_input("Number of Repetitions", min_value=1.0)

one_rep_max = calculate_one_rep_max(weight_lifted, reps)
training_intensity = calculate_training_intensity(one_rep_max)

st.subheader("Estimated One-Rep Max (1RM)")
st.write(f"{one_rep_max:.2f} kg")

st.subheader("Training Intensity Ranges")
for intensity, (lower, upper) in training_intensity.items():
    st.write(f"{intensity}: {lower:.2f} kg - {upper:.2f} kg")
