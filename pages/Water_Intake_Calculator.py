import streamlit as st

def calculate_water_intake(weight, physical_activity, climate_condition, pregnancy=False, breastfeeding=False):
    base_water_intake = weight * 30  # Recommended water intake per kg of body weight

    # Adjustments based on physical activity level
    if physical_activity == "Sedentary":
        activity_factor = 1.0
    elif physical_activity == "Lightly Active":
        activity_factor = 1.3
    elif physical_activity == "Moderately Active":
        activity_factor = 1.6
    elif physical_activity == "Very Active":
        activity_factor = 1.9
    else:
        activity_factor = 1.0

    water_intake = base_water_intake * activity_factor

    # Adjustments based on climate conditions
    if climate_condition == "Hot":
        water_intake *= 1.2
    elif climate_condition == "Cold":
        water_intake *= 1.1

    # Adjustments for special conditions
    if pregnancy:
        water_intake += 300  # Additional 300ml/day during pregnancy
    if breastfeeding:
        water_intake += 500  # Additional 500ml/day during breastfeeding

    return water_intake

z,x,c=st.columns([1,10,1])
x.image('THealthzoo.png')
st.title("Water Intake Calculator")

weight = st.number_input("Weight (in kg)", min_value=1.0)
physical_activity = st.selectbox("Physical Activity Level", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"])
climate_condition = st.selectbox("Climate Conditions", ["Normal", "Hot", "Cold"])
pregnancy = st.checkbox("Pregnant")
breastfeeding = st.checkbox("Breastfeeding")

water_intake = calculate_water_intake(weight, physical_activity, climate_condition, pregnancy, breastfeeding)

st.subheader("Recommended Daily Water Intake")
st.write(f"{water_intake:.2f} ml")
st.write("Base Water Intake")
st.caption("The calculation starts with a base water intake of weight * 30 ml per kilogram of body weight. This is a common guideline used to estimate water intake requirements.")
st.write("Physical Activity Adjustment:")
st.caption("The base water intake is adjusted based on the selected physical activity level. The activity factors used in the code (1.0, 1.3, 1.6, and 1.9) are typical values used to account for increased water needs during physical activity. However, these factors can vary depending on different sources and recommendations.")
st.write("Climate Condition Adjustment:") 

st.caption("The base water intake is further adjusted based on the selected climate conditions. The factors used in the code (1.0, 1.2, and 1.1) are general approximations to account for increased water needs in hot or cold environments. These factors can also vary depending on specific climate conditions and individual circumstances.")
st.write("Special Conditions Adjustment:") 
st.caption("The code includes additional adjustments for pregnancy and breastfeeding. The values used in the code (300 ml/day during pregnancy and 500 ml/day during breastfeeding) are commonly suggested increments to accommodate increased water needs during these periods. However, it's important to note that individual circumstances may vary, and specific recommendations should be obtained from healthcare professionals.")

st.caption("It's important to keep in mind that these calculations are approximate estimations based on general guidelines. Actual water intake requirements can vary depending on various factors such as individual differences, health conditions, physical activity levels, climate conditions, and more. For personalized and precise recommendations, it's always advisable to consult with a healthcare professional or registered dietitian.")