import streamlit as st

def identify_allergens(symptoms):
    allergens = []

    # Check symptoms and identify potential allergens
    if "sneezing" in symptoms:
        allergens.append("Pollen")
    if "itchy eyes" in symptoms:
        allergens.append("Dust mites")
    if "runny nose" in symptoms:
        allergens.append("Pet dander")
    if "skin rash" in symptoms:
        allergens.append("Certain foods")
    if "wheezing" in symptoms:
        allergens.append("Mold")

    return allergens

def main():
    st.title("Allergy Symptom Checker")
    st.write("Check the symptoms you are experiencing to identify potential allergens.")

    # User input
    symptoms = st.multiselect("Select your symptoms:", ["sneezing", "itchy eyes", "runny nose", "skin rash", "wheezing"])

    # Identify potential allergens
    if st.button("Check"):
        allergens = identify_allergens(symptoms)

        # Display results
        st.write("Based on your symptoms, the potential allergens could be:")
        for allergen in allergens:
            st.write("- " + allergen)

if __name__ == "__main__":
    main()
