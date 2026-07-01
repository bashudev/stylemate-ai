import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="StyleMate AI",
    page_icon="👔",
    layout="wide"
)

st.title("👔 StyleMate AI")
st.markdown("### Your AI Personal Fashion Consultant")

st.success("✅ Version 1 is running!")

st.markdown("---")

uploaded_file = st.file_uploader(
    "📷 Upload your garment image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Garment", use_container_width=True)

    st.success("✅ Garment uploaded successfully!")