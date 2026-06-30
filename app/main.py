from services.color_extractor import get_average_color
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="StyleMate AI",
    page_icon="👔",
    layout="wide"
)

st.title("👔 StyleMate AI")
st.markdown("### Your AI Personal Fashion Consultant")

st.markdown("---")

st.markdown(
"""
### Welcome!

Upload a photo of any garment and StyleMate AI will help you:

- 👔 Create coordinated outfits
- 👟 Recommend matching footwear
- 👜 Suggest bags and accessories
- 📈 Check current fashion trends
- 🛍️ Find similar products online

---
"""
)

uploaded_file = st.file_uploader(
    "📷 Upload your garment image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    average_color = get_average_color(image)

    st.write("### Average RGB Colour")

    st.json(average_color)

    st.image(image, caption="Uploaded Garment", use_container_width="stretch")

    st.success("✅ Garment uploaded successfully!")