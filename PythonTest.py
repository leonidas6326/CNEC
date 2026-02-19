
import streamlit as st 
import pandas as pd
import numpy as np
# Function to calculate total points
def calculate_points(age, seer_stage, hysterectomy, chemotherapy):
    points = 0
    
    # Age points
    if age < 35:
        points += 0
    elif 35 <= age <= 49:
        points += 4
    elif 50 <= age <= 64:
        points += 21
    else:  # age >= 65
        points += 44

    # SEER stage points
    if seer_stage == "Localized":
        points += 0
    elif seer_stage == "Regional":
        points += 44
    elif seer_stage == "Distant":
        points += 100

    # Hysterectomy points
    if hysterectomy == "Done":
        points += 0
    else:  # Not done
        points += 39

    # Chemotherapy points
    if chemotherapy == "Done":
        points += 0
    else:  # Not done
        points += 49
    
    return points

# Function to calculate survival probability (adjust according to your nomogram's conversion)
def calculate_survival_probability(points):
    # Assuming a linear conversion, adjust according to your real mapping (or curve)
    if points < 51:
        survival_probability = 0.60  # Example value for low risk
    elif points < 101:
        survival_probability = 0.37  # Intermediate
    else:
        survival_probability = 0.09  # High risk
    return survival_probability

# Streamlit user interface
st.title("5-Year Overall Survival Risk Calculator For Patients with Cervical Neuroendocrine Carcinoma")

# User inputs
age = st.selectbox("Age", [i for i in range(18, 101)])
seer_stage = st.selectbox("SEER Stage", ["Localized", "Regional", "Distant"])
hystectomy = st.selectbox("Hysterectomy", ["Done", "Not done"])
chemotherapy = st.selectbox("Chemotherapy", ["Done", "Not done"])

# Calculate points and survival probability
points = calculate_points(age, sex, seer_stage, hysterectomy, chemotherapy)
survival_probability = calculate_survival_probability(points)

# Display results
st.write(f"Total Risk Points: {points}")
st.write(f"Estimated 5-Year Survival Probability: {survival_probability * 100:.2f}%")


