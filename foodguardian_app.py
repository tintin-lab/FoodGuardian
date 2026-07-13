# ===============================
# Nutrition Parser
# ===============================

# Clean OCR text
text = combined_text.lower()
text = text.replace(",", ".")
text = text.replace("_", " ")
text = text.replace("ofwhich", "of which")

st.subheader("OCR Extracted Text")
st.code(text)


# -------------------------------
# Function to extract nutrition values
# -------------------------------

def extract_value(text, keywords):

    for keyword in keywords:

        pattern = rf"{keyword}.*?(\d+\.?\d*)"

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            try:
                value = float(match.group(1))

                # Ignore OCR artifacts like isolated 9
                if value == 9:
                    continue

                return value

            except:
                pass

    return None


# -------------------------------
# Extract nutrition values
# -------------------------------

nutrition = {}

nutrition["Energy (kcal)"] = extract_value(
    text,
    [
        "energy",
        "energy kcal"
    ]
)

nutrition["Protein (g)"] = extract_value(
    text,
    [
        "protein"
    ]
)

nutrition["Carbohydrate (g)"] = extract_value(
    text,
    [
        "total carbohydrate",
        "carbohydrate"
    ]
)

nutrition["Total Sugar (g)"] = extract_value(
    text,
    [
        "total sugars",
        "added sugars",
        "of which sugars",
        "sugars"
    ]
)

nutrition["Total Fat (g)"] = extract_value(
    text,
    [
        "total fat"
    ]
)

nutrition["Saturated Fat (g)"] = extract_value(
    text,
    [
        "saturated fat",
        "saturates"
    ]
)

nutrition["Trans Fat (g)"] = extract_value(
    text,
    [
        "trans fat"
    ]
)

nutrition["Sodium (mg)"] = extract_value(
    text,
    [
        "sodium"
    ]
)


# -------------------------------
# Display nutrition table
# -------------------------------

st.subheader("Extracted Nutrition Values")

for key, value in nutrition.items():

    if value is None:

        st.write(f"❌ {key}: Not detected")

    else:

        st.write(f"✅ {key}: {value}")
