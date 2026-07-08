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

# ===============================
# OCR Reading (improved)
# ===============================

import numpy as np
from PIL import Image


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


        # Convert image
        image_array = np.array(image)


        # OCR
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
        combined_text = combined_text.replace("\n"," ")
        combined_text = combined_text.lower()


    st.subheader("OCR Extracted Text")

    st.write(combined_text)
    # ===============================
# Nutrition extraction
# ===============================

import re


text = combined_text.lower()


# Sodium extraction

# Sodium extraction (improved)

sodium = 0

sodium_patterns = [
    r'sodium\s*[\w\s\(\)]*?(\d+)',
    r'na\s*[\w\s]*?(\d+)'
]


for pattern in sodium_patterns:

    sodium_match = re.search(
        pattern,
        text,
        re.I
    )

    if sodium_match:

        sodium = float(
            sodium_match.group(1)
        )

        break


# Sugar extraction

# ===============================
# Improved Sugar Extraction
# ===============================

sugar = 0

sugar_patterns = [

    r'added\s*sugars?\D*(\d+\.?\d*)',

    r'total\s*sugars?\D*(\d+\.?\d*)',

    r'of\s*which\s*sugars?\D*(\d+\.?\d*)',

    r'sugars?\D*(\d+\.?\d*)'

]


for pattern in sugar_patterns:

    match = re.search(
        pattern,
        text,
        re.I
    )

    if match:
        sugar = float(match.group(1))
        break



# ===============================
# Improved Saturated Fat Extraction
# ===============================

satfat = 0


satfat_patterns = [

    r'saturated\s*fat\D*(\d+\.?\d*)\s*g',

    r'saturates\D*(\d+\.?\d*)\s*g',

    r'sat\.?\s*fat\D*(\d+\.?\d*)\s*g'

]


for pattern in satfat_patterns:

    match = re.search(
        pattern,
        text,
        re.I
    )

    if match:
        satfat = float(match.group(1))
        break
           
st.subheader("Extracted Nutrition")

st.write("Sodium:", sodium, "mg/100g")
st.write("Sugar:", sugar, "g/100g")
st.write("Saturated fat:", satfat, "g/100g")
