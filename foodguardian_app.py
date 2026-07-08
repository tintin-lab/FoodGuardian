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
# OCR + Nutrition Extraction
# ===============================

import streamlit as st
import easyocr
import numpy as np
from PIL import Image
import re


# Upload images

uploaded_files = st.file_uploader(
    "Upload nutrition and ingredient label images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)


if uploaded_files:

    st.success("Images uploaded successfully!")


    # Load OCR

    reader = easyocr.Reader(['en'])


    combined_text = ""


    # -------------------------------
    # OCR reading from all images
    # -------------------------------

    for file in uploaded_files:


        image = Image.open(file)


        st.image(
            image,
            caption=file.name
        )


        # Convert image for OCR

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


    # decimal correction

    text = text.replace(",", ".")


    # show OCR result

    st.subheader("OCR Extracted Text")

    st.code(text)



    # ===============================
    # Sodium extraction
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
    # Sugar extraction
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
    # Saturated fat extraction
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
    # Display extracted values
    # ===============================


    st.subheader("Extracted Nutrition Values")


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
           
st.subheader("Extracted Nutrition")

st.write("Sodium:", sodium, "mg/100g")
st.write("Sugar:", sugar, "g/100g")
st.write("Saturated fat:", satfat, "g/100g")
