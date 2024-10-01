from fastapi import FastAPI, File, UploadFile
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from PIL import Image, ImageEnhance
import torch
import io

# Initialize FastAPI app
app = FastAPI()

# Load the model and processor once
# model = Qwen2VLForConditionalGeneration.from_pretrained(
#     "Qwen/Qwen2-VL-2B-Instruct",
#     torch_dtype="auto",
#     device_map="auto"
# )

# processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")

# Compress and enhance the image for OCR
def compress_and_enhance_image(input_image, max_size=(1024, 1024), quality=85):
    img = input_image.copy()

    # Resize the image to fit within the max dimensions
    img.thumbnail(max_size)
    
    # Convert to grayscale to enhance text contrast for OCR
    img = img.convert("L")
    
    # Increase contrast for better OCR accuracy
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)  # Adjust contrast factor as needed

    return img

# Function to extract text from image
def process_image(image: Image.Image):
    enhanced_image = compress_and_enhance_image(image)

    # Prepare prompt for model
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image"
                },
                {
                    "type": "text",
                    "text": "Extract all text from image."
                }
            ]
        }
    ]
    
    text_prompt = processor.apply_chat_template(messages, add_generation_prompt=True)

    # Process the image with the model
    inputs = processor(
        text=[text_prompt],
        images=[enhanced_image],
        padding=True,
        return_tensors="pt"
    )

    inputs = inputs.to("cuda")

    # Generate text from image
    output_ids = model.generate(**inputs, max_new_tokens=1024)

    generated_ids = [
        output_ids[len(input_ids):]
        for input_ids, output_ids in zip(inputs.input_ids, output_ids)
    ]

    output_text = processor.batch_decode(
        generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True
    )

    return output_text



# Define an API endpoint for uploading an image and extracting text
@app.post("/extract_text/")
async def extract_text_from_image(file: UploadFile = File(...)):
    # Read the image file
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    extracted_text = "['Here is the extracted text from the image:\n\nAbout - के बारे में\nAbout me - मेरे बारे में\nAbout us - एक्स मेरे बारे में\nAbout them - उनके बारे में\nAbout you - आपके बारे में\nAbout him - उनके बारे में\nAbout it - इसके बारे में\nAbout whom - जिसके बारे में\nAbout now - अभी के बारे में\nAbout today - आज के बारे में\nAbout life - जीवन के बारे में\nAbout food - खाने के बारे में\nAbout here - यहाँ के बारे में\nAbout there - यहाँ के बारे में\nAbout love - आंतर के बारे में']"
    # Process the image and extract text
    # extracted_text = process_image(image)

    return {"extracted_text": extracted_text}
