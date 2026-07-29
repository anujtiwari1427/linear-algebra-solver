import io
import re
import numpy as np
from PIL import Image
from typing import Tuple, Optional

# Global OCR reader instance
_easyocr_reader = None

def get_easyocr_reader():
    global _easyocr_reader
    if _easyocr_reader is None:
        try:
            import easyocr
            # Load English reader without GPU requirement
            _easyocr_reader = easyocr.Reader(['en'], gpu=False)
        except Exception:
            _easyocr_reader = False
    return _easyocr_reader

def extract_text_from_image(image: Image.Image) -> str:
    """Extracts text from an image using EasyOCR, pytesseract, or basic image fallback."""
    # Try EasyOCR first
    reader = get_easyocr_reader()
    if reader:
        try:
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format=image.format or 'PNG')
            results = reader.readtext(img_byte_arr.getvalue(), detail=0)
            return " ".join(results)
        except Exception:
            pass

    # Try Pytesseract
    try:
        import pytesseract
        text = pytesseract.image_to_string(image)
        if text.strip():
            return text
    except Exception:
        pass

    return ""

def extract_numbers_from_text(text: str) -> list[float]:
    """Extracts all floating point and integer numbers from text string."""
    # Find all signed integers and float numbers
    tokens = re.findall(r'[-+]?\d*\.?\d+', text)
    numbers = []
    for tok in tokens:
        try:
            val = float(tok)
            numbers.append(val)
        except ValueError:
            pass
    return numbers

def process_image_matrix_upload(
    image_bytes: bytes,
    target_rows: int = 3,
    target_cols: int = 3
) -> Tuple[Optional[np.ndarray], str]:
    """
    Processes an uploaded image file, performs OCR text extraction,
    and attempts to construct a target_rows x target_cols matrix.
    Returns (matrix_or_None, extracted_text).
    """
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        raw_text = extract_text_from_image(image)
        numbers = extract_numbers_from_text(raw_text)

        required_size = target_rows * target_cols
        if len(numbers) >= required_size:
            # Take the first required_size numbers and reshape
            mat_data = np.array(numbers[:required_size]).reshape(target_rows, target_cols)
            return mat_data, raw_text
        elif len(numbers) > 0:
            # Pad with zeros if fewer numbers found
            padded = np.zeros(required_size)
            padded[:len(numbers)] = numbers
            mat_data = padded.reshape(target_rows, target_cols)
            return mat_data, raw_text
        else:
            return None, raw_text if raw_text else "No text/numbers detected in image."
    except Exception as e:
        return None, f"Image processing error: {e}"
