import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_books_empty():
    response = client.get('/books')
    assert response.status_code == 200
    assert response.json() == []

def test_cer():
    response = client.get('/evaluation/cer', params={'reference': 'abc', 'hypothesis': 'abc'})
    assert response.status_code == 200
    assert response.json()['cer'] == 0.0
