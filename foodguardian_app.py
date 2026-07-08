import streamlit as st

st.title("FoodGuardian 🥗")

st.write(
    "Upload your snack nutrition and ingredient label images"
)

uploaded_files = st.file_uploader(
    "Upload images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)


if uploaded_files:

    st.success("Images uploaded successfully!")

    for file in uploaded_files:

        st.image(
            file,
            caption=file.name
        )
