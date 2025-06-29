import streamlit as st
from PIL import Image

# Start the camera
camera_image = st.camera_input("Take a picture")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    gray_img = img.convert("L")  # Convert to grayscale

    st.image(gray_img)