import streamlit as st

# Set up the page
st.set_page_config(page_title="BMI Calculator", page_icon="🖩", layout="centered")

# Title and introduction
st.title("Project 9: BMI Calculator 🖩")
st.markdown("""
## Calculate your Body Mass Index (BMI) 📊  
Enter your **weight** and **height** below to determine your BMI.
""")

# Input fields for weight and height
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Enter your weight (in kg):", min_value=1.0, format="%.2f")

with col2:
    height = st.number_input("Enter your height (in meters):", min_value=1.0, format="%.2f")

st.markdown("---")  # Add a separator for better UI

# Calculate BMI
if height > 0 and weight > 0:
    bmi = weight / (height ** 2)
    st.subheader("Your BMI is: ")
    st.markdown(f"**{bmi:.2f}** 🎯")

    # BMI classification
    if bmi < 18.5:
        st.error("🔴 Underweight: You may need to gain some weight for a healthy balance.")
    elif 18.5 <= bmi < 24.9:
        st.success("✅ Normal Weight: Great! You are within a healthy weight range.")
    elif 25 <= bmi < 30:
        st.warning("⚠️ Overweight: Consider adopting a healthier lifestyle.")
    elif bmi >= 30:
        st.error("🔴 Obesity: It's important to consult a healthcare provider for advice.")
    else:
        st.info("⚠️ Unexpected result. Please recheck your inputs.")

else:
    st.info("ℹ️ Please enter a valid weight and height to calculate your BMI.")
