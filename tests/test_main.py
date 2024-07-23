import pytest
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_chat_with_pdf():
    with open("tests/sample.pdf", "rb") as pdf_file:
        response = client.post("/chat/", files={"file": pdf_file}, data={"user_query": "What is this PDF about?"})
        assert response.status_code == 200
        assert "response" in response.json()

def test_invalid_file_type():
    with open("tests/sample.txt", "rb") as txt_file:
        response = client.post("/chat/", files={"file": txt_file}, data={"user_query": "What is this text about?"})
        assert response.status_code == 400
        assert response.json()["detail"] == "Only PDF files are allowed"

def test_missing_user_query():
    with open("tests/sample.pdf", "rb") as pdf_file:
        response = client.post("/chat/", files={"file": pdf_file})
        assert response.status_code == 422  # Unprocessable Entity