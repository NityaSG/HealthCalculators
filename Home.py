import streamlit as st
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
#st.set_page_config(page_title="home")
z,x,c=st.columns([1,10,1])
x.image('THealthzoo.png')
st.image('banner.jpg')
st.write("Welcome to the ThinkRoman Ventures Healthcare Calculator App! We are dedicated to providing you with a comprehensive set of healthcare calculators designed to assess and evaluate various aspects of your health. Whether you need to determine your risk for specific medical conditions, assess the severity of a health issue, or make informed decisions about your well-being, our app offers a wide range of calculators to cater to your needs. From cardiovascular risk assessment to bone health evaluation, our calculators are designed to empower you with valuable insights and information. Take control of your health journey with the ThinkRoman Ventures Healthcare Calculator App and make informed decisions for a healthier future.")
st.caption("Disclaimer: The calculators provided in the ThinkRoman Ventures Healthcare Calculator App are intended for informational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment. These calculators are designed to offer general assessments and insights based on the provided inputs and algorithms. However, they are not intended to provide a clinical diagnosis or replace the expertise of healthcare professionals. Always consult with a qualified healthcare provider for personalized medical advice and guidance tailored to your specific health needs. ThinkRoman Ventures disclaims any liability for the accuracy, completeness, or reliability of the information provided by the calculators. By using the app, you acknowledge and understand that the results obtained from the calculators are not intended for clinical decision-making and should not be used as a substitute for professional medical judgment.")