import streamlit as st
import requests
from PIL import Image
import io

# FastAPI backend URL
backend_url = "http://localhost:8000/extract_text/"

st.title("OCR with Search Functionality")

# File uploader to upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Initialize Session State for extracted text
if 'extracted_text' not in st.session_state:
    st.session_state.extracted_text = ""

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Extract Text"):
        # Convert image to bytes for sending to FastAPI backend
        img_bytes = io.BytesIO()
        image.save(img_bytes, format="PNG")
        img_bytes = img_bytes.getvalue()

        # Send image to FastAPI backend
        response = requests.post(backend_url, files={"file": img_bytes})

        if response.status_code == 200:
            # Extracted text from the image
            st.session_state.extracted_text = response.json().get("extracted_text", "")
        else:
            st.error("Failed to extract text. Please try again.")

# Show the extracted text if it exists
if st.session_state.extracted_text:
    st.write("### Extracted Text")
    st.write(st.session_state.extracted_text)

    # Add a text input box to search in extracted text
    search_query = st.text_input("Search the extracted text (Supports Hindi & English):", "")

    if search_query:
        # Case-insensitive search in extracted text
        if search_query.lower() in st.session_state.extracted_text.lower():
            st.success(f"'{search_query}' found in the extracted text!")
        else:
            st.error(f"'{search_query}' not found in the extracted text.")
