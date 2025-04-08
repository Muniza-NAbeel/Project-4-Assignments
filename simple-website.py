import streamlit as st
import pandas as pd
import random

# --- Page Setup ---
st.set_page_config(page_title="Student Data Generator", layout="centered", page_icon="📊")
st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f9f9f9;
    }
    .title {
        text-align: center;
        color: #4CAF50;
    }
    .subheader {
        text-align: center;
        color: #6c757d;
        margin-bottom: 20px;
    }
    .button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 class='title'>📊 Student CSV File Generator</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subheader'>Generate a random dataset of student records and download it as a CSV file.</h3>", unsafe_allow_html=True)

# --- Data Generation ---
names = ["Muniza", "Nabeel", "Abdul Nafay", "Aisha", "Fajar", "Anzila", "Harmain", "Zainab", "Faraan", "Ahmed"]

students = []
for i in range(1, 10):
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18, 25),
        "Grade": random.choice(["A", "B", "C", "D", "E", "F"]),
        "Marks": random.randint(40, 100),
    }
    students.append(student)

df = pd.DataFrame(students)

# --- Display Data ---
st.markdown("### 🧑‍🎓 Generated Students Data")
st.dataframe(df.style.highlight_max(axis=0, subset=["Marks"], color="#dff0d8", props="font-weight: bold;"))

# --- Download Button ---
csv_file = df.to_csv(index=False).encode("utf-8")
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>🎉 Download the CSV File</h3>", unsafe_allow_html=True)
st.download_button(
    label="⬇️ Download Student Records",
    data=csv_file,
    file_name="students.csv",
    mime="text/csv",
    help="Click to download the generated CSV file.",
    key="download_button",
)

# --- Success Message ---
st.markdown("---")
st.success("✨ Students record generated successfully!")
st.balloons()
