from pathlib import Path
import json
from typing import List
from ..models.book import Book, Page

class BookService:
    def __init__(self, base_path: Path = Path('data/books')):
        self.base_path = base_path
        self.base_path.mkdir(parents=True, exist_ok=True)

    def list_books(self) -> List[Book]:
        books = []
        for book_dir in self.base_path.iterdir():
            meta_file = book_dir / 'metadata.json'
            if meta_file.exists():
                with open(meta_file) as f:
                    meta = json.load(f)
                books.append(Book(**meta, pages=[]))
        return books

    def load_book(self, book_id: str) -> Book:
        book_dir = self.base_path / book_id
        meta_file = book_dir / 'metadata.json'
        if not meta_file.exists():
            raise FileNotFoundError(f'Book {book_id} not found')
        with open(meta_file) as f:
            meta = json.load(f)
        pages = []
        for img in sorted(book_dir.glob('pages/*.png')):
            number = int(img.stem)
            gt_file = book_dir / 'ground_truth' / f'{img.stem}.txt'
            gt_text = None
            if gt_file.exists():
                gt_text = gt_file.read_text()
            pages.append(Page(number=number, image_path=str(img), ground_truth=gt_text))
        return Book(**meta, pages=pages)

    def save_ground_truth(self, book_id: str, page_number: int, text: str) -> None:
        book_dir = self.base_path / book_id / 'ground_truth'
        book_dir.mkdir(parents=True, exist_ok=True)
        gt_file = book_dir / f'{page_number}.txt'
        gt_file.write_text(text)
