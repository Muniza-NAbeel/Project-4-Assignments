import streamlit as st  


# Set the page configuration
st.set_page_config(
    page_title="BMI Calculator",  # Title of the page
    page_icon="🏋️",  # Icon to be displayed in the tab
    layout="centered",  # Layout of the app
)
# App Title
st.title("💪 BMI Calculator")  
st.write("📏 Calculate your Body Mass Index (BMI) and know your health category!")  

# User Inputs
height = st.slider("📐 Enter your height (in cm):", 100, 250, 175)
weight = st.slider("⚖️ Enter your weight (in kg):", 40, 200, 70)

# BMI Calculation
bmi = weight / ((height / 100) ** 2)

# Display BMI and Category
st.write(f"### 🧮 Your BMI: {bmi:.2f}")

# Determine BMI Category
if bmi < 18.5:
    st.write("**Category:** 🥗 Underweight")  # BMI less than 18.5 is underweight
elif 18.5 <= bmi < 24.9:
    st.write("**Category:** 🥳 Normal weight")  # BMI between 18.5 and 24.9 is normal weight
elif 25 <= bmi < 29.9:
    st.write("**Category:** 🍔 Overweight")  # BMI between 25 and 29.9 is overweight
else:
    st.write("**Category:** 🍩 Obesity")  # BMI 30 or greater is obesity

# Display BMI Categories Table
st.write("### 📊 BMI Categories")
bmi_categories = {
    "Category": ["🥗 Underweight", "🥳 Normal weight", "🍔 Overweight", "🍩 Obesity"],  
    "BMI Range": ["< 18.5", "18.5 - 24.9", "25 - 29.9", "30 or greater"],  
}
st.table(bmi_categories)  # Display the table in the app

# Footer
st.write("💡 Tip: Maintain a balanced diet and regular exercise to keep your BMI in the normal range!")
