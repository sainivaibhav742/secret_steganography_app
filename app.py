import streamlit as st
from PIL import Image
from utils import hide_data, extract_data
from io import BytesIO

st.set_page_config(page_title="🔐 Steganography App", layout="centered")
st.title("🔐 Secret Message Hider App")

tab1, tab2 = st.tabs(["📤 Hide Message", "📥 Extract Message"])

with tab1:
    uploaded_image = st.file_uploader("Upload an image (PNG/JPG)", type=['png', 'jpg', 'jpeg'])
    secret_message = st.text_area("Enter your secret message to hide")

    if st.button("🔒 Hide Message") and uploaded_image and secret_message:
        image = Image.open(uploaded_image)
        new_image = hide_data(image, secret_message)

        st.image(new_image, caption="Image with Hidden Message", use_container_width=True)

        # Save to memory buffer for download
        buffer = BytesIO()
        new_image.save(buffer, format="PNG")
        byte_data = buffer.getvalue()

        st.download_button(
            label="📥 Download Image with Hidden Message",
            data=byte_data,
            file_name="secret_output.png",
            mime="image/png"
        )

with tab2:
    encoded_image = st.file_uploader("Upload image to extract message", type=['png', 'jpg', 'jpeg'])

    if st.button("🔓 Extract Message") and encoded_image:
        image = Image.open(encoded_image)
        message = extract_data(image)
        st.success("Hidden Message Found:")
        st.code(message, language='text')
