import pytest
from pdf_handler import extract_text_from_pdf

def test_extract_text_from_pdf():
    with open("tests/sample.pdf", "rb") as pdf_file:
        text = extract_text_from_pdf(pdf_file)
        assert "expected text from the PDF" in text