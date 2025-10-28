import pytesseract
from PIL import Image

def process_document(file_path):
    """
    Extract text from uploaded document using OCR
    """
    try:
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)
        return {
            "status": "success",
            "extracted_text": text
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
