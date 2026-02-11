import streamlit as st
from PIL import Image
from rembg import remove
import io

st.title("AI Background Remover")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)

    st.subheader("Original Image")
    st.image(img, use_container_width=True)

    if st.button("Remove Background"):
        with st.spinner("Removing background... Please wait"):
            # Remove background
            output = remove(img)

            # Convert output to PIL Image if needed
            if isinstance(output, bytes):
                output = Image.open(io.BytesIO(output))

        st.subheader("Background Removed")
        st.image(output, use_container_width=True)

        # Download button
        buf = io.BytesIO()
        output.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Image",
            data=byte_im,
            file_name="background_removed.png",
            mime="image/png"
        )
