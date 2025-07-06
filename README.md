# 🚀 DevRead – AI-Powered Developer Book Summarizer

![DevRead Banner](https://your-screenshot-url-if-any.com/banner.png)

DevRead is a cross-platform app built for developers to **search and summarize popular programming books** using AI. Powered by OpenRouter and designed with a neon-themed UI, it’s your personal dev-book cheat sheet!

---

## 🔧 Tech Stack

| Tech         | Description                       |
|--------------|-----------------------------------|
| 🧠 OpenRouter | Free AI API (Cypher model)        |
| ⚙️ FastAPI     | Python backend for book summary  |
| 💻 Flutter    | Android/iOS app with dark neon UI |
| 🌐 React      | (Optional) Web version            |
| 🔐 Firebase   | Secure login (optional)           |

---

## ✨ Features

- 📚 5000+ popular developer books
- 🔍 Smart search with instant filtering
- 🧠 AI-generated dev-style summaries
- 🕘 Summary history tracking
- 🎨 Neon dark mode UI
- 📦 Works offline via APK
- 💬 (Coming Soon) Chat-based book assistant

---

## 🛠️ Local Setup Guide

### 🔹 Backend (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
