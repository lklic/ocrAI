from fastapi import FastAPI, UploadFile, File, HTTPException
from pathlib import Path
import shutil
import uuid

from .services.book_service import BookService
from .services.ocr_service import OCRService
from .services.evaluation_service import EvaluationService

app = FastAPI(title="OCR LLM Platform")
book_service = BookService()
ocr_service = OCRService()

@app.get('/books')
def list_books():
    return book_service.list_books()

@app.get('/books/{book_id}')
def get_book(book_id: str):
    try:
        return book_service.load_book(book_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail='Book not found')

@app.post('/books')
def upload_book(file: UploadFile = File(...)):
    book_id = str(uuid.uuid4())
    book_dir = Path('data/books') / book_id
    book_dir.mkdir(parents=True, exist_ok=True)
    pages_dir = book_dir / 'pages'
    pages_dir.mkdir(parents=True, exist_ok=True)
    with open(book_dir / 'metadata.json', 'w') as f:
        f.write('{"id": "%s", "title": "%s", "year": 0, "source": "upload", "language": "unknown"}' % (book_id, file.filename))
    # Assume single image upload for demo
    dest = pages_dir / '1.png'
    with dest.open('wb') as out:
        shutil.copyfileobj(file.file, out)
    return {"id": book_id}

@app.post('/books/{book_id}/pages/{page}/ocr')
def ocr_page(book_id: str, page: int, method: str = 'tesseract'):
    book = book_service.load_book(book_id)
    page_obj = next((p for p in book.pages if p.number == page), None)
    if not page_obj:
        raise HTTPException(status_code=404, detail='Page not found')
    text = ocr_service.ocr_image(page_obj.image_path, method)
    return {"text": text}

@app.post('/books/{book_id}/pages/{page}/ground_truth')
def save_gt(book_id: str, page: int, text: str):
    book_service.save_ground_truth(book_id, page, text)
    return {"status": "saved"}

@app.get('/evaluation/cer')
def evaluate(reference: str, hypothesis: str):
    score = EvaluationService.cer(reference, hypothesis)
    return {"cer": score}
