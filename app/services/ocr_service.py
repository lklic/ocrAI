from PIL import Image
import pytesseract

class OCRService:
    def ocr_image(self, image_path: str, method: str = 'tesseract') -> str:
        if method == 'tesseract':
            return pytesseract.image_to_string(Image.open(image_path))
        elif method == 'openai':
            return 'openai placeholder'
        elif method == 'gemini':
            return 'gemini placeholder'
        else:
            raise ValueError('Unknown OCR method')
