import streamlit as st
from PIL import Image

from services.garment_detector import detect_garment
from services.fashion_engine import get_recommendations


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

    garment = detect_garment(image)
    recommendations = get_recommendations(garment)

    st.image(image, caption="Uploaded Garment", use_container_width=True)
    st.subheader("👔 Fashion Analysis")

    st.write(f"**Garment:** {garment['garment']}")
    st.write(f"**Category:** {garment['category']}")
    st.write(f"**Primary Colour:** {garment['primary_colour']}")
    st.write(f"**Style:** {garment['style']}")
    st.write(f"**Pattern:** {garment['pattern']}")
    st.write(f"**Fabric:** {garment['fabric']}")
    st.write(f"**Season:** {', '.join(garment['season']) if garment['season'] else 'Unknown'}")
    st.write(f"**Occasion:** {', '.join(garment['occasion']) if garment['occasion'] else 'Unknown'}")
    st.write(f"**Confidence:** {garment['confidence']:.0%}")
    st.markdown("---")

    st.subheader("👖 Recommended Bottoms")

    for item in recommendations["bottoms"]:
        st.write(f"✅ {item}")

    st.subheader("👞 Recommended Footwear")

    for item in recommendations["footwear"]:
        st.write(f"✅ {item}")

    st.subheader("⌚ Recommended Accessories")

    for item in recommendations["accessories"]:
        st.write(f"✅ {item}")

    st.subheader("💡 Why these recommendations?")

    st.info(recommendations["reason"])



    st.success("✅ Garment uploaded successfully!")