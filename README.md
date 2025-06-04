# OCR LLM Platform

This project provides a minimal FastAPI backend for experimenting with OCR and LLM transcription of scanned books. It exposes basic endpoints to upload books, run OCR on pages and evaluate results.

## Features
* Book metadata stored on disk under `data/books/`
* OCR service using Tesseract with placeholders for OpenAI and Gemini
* Endpoint to compute character error rate (CER)
* Example unit tests using `pytest`

## Setup
Install dependencies and run the API:
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Run tests with:
```bash
pytest
```
