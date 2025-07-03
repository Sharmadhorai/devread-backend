import os
from dotenv import load_dotenv

load_dotenv()  # ✅ Load before anything else!

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from summary import generate_summary
import json


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/books")
def get_books():
    try:
        with open("books.json", "r", encoding="utf-8") as f:
            books = json.load(f)
        return books
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading books.json: {e}")

@app.get("/summarize")
async def summarize(title: str = Query(...)):
    return await generate_summary(title)
