import streamlit as st
import os

st.title('AI Fitness Trainer: Exercise Analysis')

exercise_option = st.selectbox(
    "Choose an Exercise",
    ["Squats", "Bicep Curls"]
)

# ✅ Handle Missing Video File
recorded_file = 'output_sample.mp4'
if not os.path.exists(recorded_file):
    st.warning("Video file not found. Please upload or place 'output_sample.mp4' in the project folder.")
else:
    sample_vid = st.empty()
    sample_vid.video(recorded_file)

st.write(f"Currently Analyzing: {exercise_option}")
