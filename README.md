Prompt: OCR + LLM-Based Platform for Book Transcription with Evaluation and Ground Truth Correction

We are building a web-based OCR platform in Flask integrated with modern LLMs (OpenAI and Gemini) focused on transcribing and evaluating printed books and historical materials.

Key Requirements:
1. Book Management Interface
Display a visual list/grid of available digitized books (PDF or image collections).

Each book has metadata (title, year, source, language).

Click on a book to view thumbnails of all its pages.

2. OCR Task Selection
Allow the user to:

OCR a single page (via click).

Select multiple pages (checkbox/multi-select).

OCR the entire book.

Option to choose OCR method:

OpenAI (Vision+Text LLM).

Gemini.

Traditional OCR (Tesseract as fallback/reference).

3. Transcription Viewer
For each OCR'd page:

Show the original image on the left.

Show the transcribed text on the right.

Editable text box to allow user corrections.

Save corrections as “ground truth.”

4. Model Comparison & Scoring
When multiple models have transcribed the same page:

Allow comparison of outputs side-by-side.

Highlight differences between models and against ground truth.

Show similarity scores (e.g., CER/WER or custom LLM-based diff).

Automatically score models across multiple pages to find the most accurate one for a given book.

5. Editing & Feedback Loop
Provide a “Correct OCR” mode to fix errors.

Ground truth data is saved and can be used to:

Retrain or fine-tune future OCR tasks.

Benchmark incoming models automatically.

All versions (original OCR, edits, model name, timestamp) are logged.

6. Backend and API
Python backend (Flask or FastAPI preferred).

Modular design to support adding more OCR or LLM providers later.

REST API to:

Upload books.

Fetch page thumbnails.

Request OCR from specific models.

Submit corrections (ground truth).

Compare model performance.

7. Additional Features
Generate automatic reports: OCR accuracy per book, model performance charts, etc.

Optional: Export ground truth as JSON, TEI, or plain text for further processing.

Developer Notes:
Prioritize modularity and clean separation between UI, OCR engines, and evaluation logic.

Use clear code comments and README documentation for each module.

Ensure compatibility with Docker for deployment.

Git versioning is mandatory. Include .gitignore and basic test coverage.
