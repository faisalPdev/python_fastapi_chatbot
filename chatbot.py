
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


GROQ_API_KEY=os.getenv("GROQ_API_KEY")



def get_groq_response(user_query,pdf_text):
    prompt = f"Based on the following PDF content: {pdf_text}\n\n{user_query}"
    client = Groq(
    api_key=GROQ_API_KEY,
    )
    response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama3-8b-8192",
    )

    return response.choices[0].message.content
