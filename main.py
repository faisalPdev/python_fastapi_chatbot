from fastapi import FastAPI, UploadFile, File,Form, HTTPException
from pydantic import BaseModel
from pdf_handler import extract_text_from_pdf
from chatbot import get_groq_response

app = FastAPI()

class Query(BaseModel):
    user_query: str

@app.get("/")
async def index():
    return {"message": "Hello Chat is Ready"}


@app.post("/chat/")
async def chat_with_pdf(user_query: str = Form(...),file: UploadFile = File(...)):
    
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    pdf_text = extract_text_from_pdf(file.file)

    response = get_groq_response(user_query,pdf_text)


    print(response)

    return {"response": response}
