import streamlit as st
import easyocr

st.title("FoodGuardian 🥗")


age_group = st.selectbox(
    "Select age group",
    [
        "Child (5-12 years)",
        "Adolescent (13-18 years)",
        "Adult (19-60 years)",
        "Elderly (>60 years)"
    ]
)


body_weight = st.number_input(
    "Body weight (kg)",
    min_value=5,
    max_value=150,
    value=50
)


packet_size = st.number_input(
    "Packet consumed (grams)",
    min_value=1,
    max_value=500,
    value=30
)


frequency = st.selectbox(
    "Consumption frequency",
    [
        "Daily",
        "3-5 times/week",
        "1-2 times/week",
        "Occasionally"
    ]
)
