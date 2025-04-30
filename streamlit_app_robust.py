
import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(layout="wide")
st.title("Canny Edge Detection and Filter Comparison")
st.markdown("Upload a JPG or PNG image to visualize filtering and edge detection results.")

uploaded_file = st.file_uploader("Upload a JPG or PNG image", type=None)

if uploaded_file is not None:
    try:
        # Manual file type validation
        if not uploaded_file.name.lower().endswith((".jpg", ".jpeg", ".png")):
            st.error("❌ Only JPG or PNG image files are supported.")
        else:
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            image = cv2.imdecode(file_bytes, 1)
            if image is None:
                st.error("❌ Could not decode the image file.")
            else:
                st.success("✅ Image uploaded and decoded successfully!")
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                gaussian = cv2.GaussianBlur(gray, (5, 5), 1.5)
                median = cv2.medianBlur(gray, 5)
                bilateral = cv2.bilateralFilter(gray, 9, 75, 75)
                nlm = cv2.fastNlMeansDenoising(gray, None, h=10, templateWindowSize=7, searchWindowSize=21)

                filters = [gaussian, median, bilateral, nlm]
                titles = ['Gaussian', 'Median', 'Bilateral', 'Non-Local Means']

                st.subheader("🌀 Filtered Image Comparison")
                cols = st.columns(4)
                for col, f_img, title in zip(cols, filters, titles):
                    col.image(f_img, caption=title, use_column_width=True, channels="GRAY")

                st.subheader("🪄 Canny Edge Detection Results")
                edge_images = [cv2.Canny(f, 50, 150) for f in filters]
                cols = st.columns(4)
                for col, edge_img, title in zip(cols, edge_images, titles):
                    col.image(edge_img, caption=f"{title} Edges", use_column_width=True, channels="GRAY")

    except Exception as e:
        st.error(f"An unexpected error occurred while processing the image: {e}")
