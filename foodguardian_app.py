import streamlit as st
import easyocr
import numpy as np
from PIL import Image
import re


# ===============================
# Title
# ===============================

st.title("FoodGuardian 🥗")

st.write(
    "Food label analysis using OCR and nutrition extraction"
)


# ===============================
# User Information
# ===============================

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



# ===============================
# OCR + Extraction
# ===============================

if uploaded_files:

    st.success(
        f"{len(uploaded_files)} images uploaded successfully!"
    )


    reader = easyocr.Reader(['en'])


    combined_text = ""


    # -------------------------------
    # OCR Reading
    # -------------------------------

    for file in uploaded_files:


        image = Image.open(file)


        st.image(
            image,
            caption=file.name
        )


        image_array = np.array(image)


        result = reader.readtext(
            image_array,
            detail=1
        )


        extracted_lines = []


        for item in result:

            extracted_lines.append(
                item[1]
            )


        extracted_text = " ".join(
            extracted_lines
        )


        combined_text += "\n" + extracted_text



    # -------------------------------
    # Clean OCR text
    # -------------------------------

    text = combined_text.lower()

    text = text.replace(",", ".")


    st.subheader("OCR Extracted Text")

    st.code(text)



    # ===============================
    # Sodium Extraction
    # ===============================

    sodium = 0


    sodium_patterns = [

        r'sodium\D*(\d+\.?\d*)\s*(?:mg|g)',

        r'na\D*(\d+\.?\d*)\s*(?:mg|g)'

    ]


    for pattern in sodium_patterns:

        match = re.search(
            pattern,
            text,
            re.I
        )

        if match:

            sodium = float(
                match.group(1)
            )

            break



    # ===============================
    # Sugar Extraction
    # ===============================

    sugar = 0


    sugar_patterns = [

        r'added\s*sugars?\D*(\d+\.?\d*)\s*(?:g|gm)',

        r'total\s*sugars?\D*(\d+\.?\d*)\s*(?:g|gm)',

        r'of\s*which\s*sugars?\D*(\d+\.?\d*)\s*(?:g|gm)',

        r'sugars?\D*(\d+\.?\d*)\s*(?:g|gm)'

    ]


    for pattern in sugar_patterns:

        match = re.search(
            pattern,
            text,
            re.I
        )


        if match:

            sugar = float(
                match.group(1)
            )

            break



    # ===============================
    # Saturated Fat Extraction
    # ===============================

    satfat = 0


    satfat_patterns = [

        r'saturated\s*fat\D*(\d+\.?\d*)\s*(?:g|gm)',

        r'saturates\D*(\d+\.?\d*)\s*(?:g|gm)',

        r'sat\.?\s*fat\D*(\d+\.?\d*)\s*(?:g|gm)'

    ]


    for pattern in satfat_patterns:

        match = re.search(
            pattern,
            text,
            re.I
        )


        if match:

            satfat = float(
                match.group(1)
            )

            break



    # ===============================
    # Display Nutrition
    # ===============================

    st.subheader(
        "Extracted Nutrition Values"
    )


    st.write(
        "Sodium:",
        sodium,
        "mg"
    )


    st.write(
        "Sugar:",
        sugar,
        "g"
    )


    st.write(
        "Saturated Fat:",
        satfat,
        "g"
    )
    
