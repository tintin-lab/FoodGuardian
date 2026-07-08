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

# Sugar extraction (improved)

sugar = 0

sugar_patterns = [
    r'total\s*sugars?\s*[\w\s]*?([\d\.]+)',
    r'added\s*sugars?\s*[\w\s]*?([\d\.]+)',
    r'sugars?\s*[\w\s]*?([\d\.]+)',
    r'sugar\s*[\w\s]*?([\d\.]+)'
]


for pattern in sugar_patterns:

    sugar_match = re.search(
        pattern,
        text,
        re.I
    )

    if sugar_match:

        sugar = float(
            sugar_match.group(1)
        )

        break

# Saturated fat extraction

# Saturated fat extraction (improved)

satfat = 0

satfat_patterns = [
    r'saturated\s*fat\s*[\w\s]*?([\d\.]+)',
    r'sat\.?\s*fat\s*[\w\s]*?([\d\.]+)',
    r'saturates\s*[\w\s]*?([\d\.]+)'
]


for pattern in satfat_patterns:

    satfat_match = re.search(
        pattern,
        text,
        re.I
    )

    if satfat_match:
        satfat = float(
            satfat_match.group(1)
        )
        break
st.subheader("Extracted Nutrition")

st.write("Sodium:", sodium, "mg/100g")
st.write("Sugar:", sugar, "g/100g")
st.write("Saturated fat:", satfat, "g/100g")
