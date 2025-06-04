from pydantic import BaseModel
from typing import List, Optional

class Page(BaseModel):
    number: int
    image_path: str
    ocr_text: Optional[str] = None
    ground_truth: Optional[str] = None

class Book(BaseModel):
    id: str
    title: str
    year: int
    source: str
    language: str
    pages: List[Page] = []
