import os
import httpx
from fastapi import HTTPException

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = MODEL = "mistralai/mistral-7b-instruct"  # ✅ free and works with summaries


headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

async def generate_summary(title: str):
    body = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": f"Summarize the developer book titled '{title}' in 5 bullet points in a developer-friendly tone."
            }
        ]
    }

    print("🔐 Using OpenRouter Key:", API_KEY[:8] + "..." if API_KEY else "❌ MISSING KEY")
    print("📨 Sending Request To:", API_URL)
    print("📦 Payload:", body)

    async with httpx.AsyncClient() as client:
        response = await client.post(API_URL, headers=headers, json=body)

    print("📬 Response Code:", response.status_code)
    print("📩 Response Text:", response.text)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="AI summary generation failed.")

    data = response.json()
    return {"summary": data["choices"][0]["message"]["content"]}
