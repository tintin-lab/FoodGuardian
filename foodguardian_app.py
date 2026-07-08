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
# ===============================
# Image Upload
# ===============================

uploaded_files = st.file_uploader(
    "Upload nutrition and ingredient label images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)


import numpy as np
from PIL import Image


# ===============================
# OCR Reading (fixed)
# ===============================

if uploaded_files:

    st.success("Images uploaded successfully!")

    reader = easyocr.Reader(['en'])

    combined_text = ""

    for file in uploaded_files:

        image = Image.open(file)

        st.image(
            image,
            caption=file.name
        )

        image_array = np.array(image)

        text = reader.readtext(
            image_array,
            detail=0
        )

        extracted_text = " ".join(text)

        combined_text += "\n" + extracted_text


    st.subheader("Number of images analyzed")
    st.write(len(uploaded_files))


    st.subheader("Extracted Label Text")
    st.write(combined_text)
