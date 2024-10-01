---

# OCR Implementation Using Qwen2-VL Model

This project demonstrates the implementation of an OCR (Optical Character Recognition) system using the **Qwen2-VL** model, which supports multi-lingual text extraction. The solution processes images to extract text in various languages, including Hindi and English, and presents a user-friendly interface built with **FastAPI** (backend) and **Streamlit** (frontend).

## How It Works

1. **Backend (FastAPI)**:
    - The **backend** handles the heavy lifting of OCR using the Qwen2-VL model.
    - Users upload images via the frontend, and the backend processes these images, extracting text.
    - GPU acceleration is used on local machines for faster processing, especially when dealing with larger models like Qwen2-VL.

2. **Frontend (Streamlit)**:
    - The **frontend** provides a simple interface for uploading images and receiving the extracted text.
    - Users can search within the extracted text for keywords.
    - Unfortunately, due to Streamlit’s lack of GPU access, the full deployment of the solution (with real-time inference for all image types) could not be hosted online.(**deployed to show working of website using dummy text**)

3. **OCR Model**:
    - The **Qwen2-VL** model was selected after testing various other models like **Tesseract** and **EasyOCR** for their accuracy and multi-lingual capabilities.
    - The **ocr-implementation-qwen.ipynb** notebook demonstrates how the model was tested with various sample images.

## Key Features

- Multi-lingual OCR with high accuracy, handling both Hindi and English text.
- Simple and intuitive user interface for uploading images and extracting text.
- Real-time search functionality within the extracted text.
- GPU acceleration for fast image processing (on local machines as inaccessible on streamlit).

## Setup Instructions

### Backend Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/atharva6507/OCR_IMPLEMENTATION.git
    ```

2. Navigate to the **backend** folder:
    ```bash
    cd backend
    ```

3. Set up the virtual environment (optional but recommended):
    ```bash
    python -m venv ocr_env
    source ocr_env/bin/activate  # Linux/macOS
    ocr_env\Scripts\activate     # Windows
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the FastAPI server:
    ```bash
    uvicorn app:app --reload
    ```

### Frontend Setup

1. Navigate to the **frontend** folder:
    ```bash
    cd frontend
    ```

2. Set up the virtual environment (optional but recommended):
    ```bash
    python -m venv ocr_env
    source ocr_env/bin/activate  # Linux/macOS
    ocr_env\Scripts\activate     # Windows
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run streamlit_app.py
    ```

### Testing the Model

To test the Qwen2-VL model used in this project, refer to the Jupyter notebook **ocr-implementation-qwen.ipynb**, which provides step-by-step usage of the model with sample images.

## GPU Access and Deployment Constraints

Due to Streamlit's lack of GPU support, deploying the full model for real-time OCR processing is not feasible on the Streamlit platform. The project works efficiently on local machines with CUDA-enabled GPUs, but server deployment would be slow without proper GPU access.

## Future Improvements

- Host the solution on a platform with GPU access to enable real-time processing for larger, more complex images.
- Optimize model performance for CPU usage in environments where GPU access is unavailable.

---