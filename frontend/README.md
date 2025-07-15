# 📊 Finance AI Advisor – Frontend

This is the frontend for the **Finance AI Advisor** project. It is built using **React**, **Vite**, and **Tailwind CSS**, and communicates with a FastAPI backend to analyze a stock portfolio and provide AI-generated insights.

---

## 🚀 Features

- Button to trigger AI analysis of portfolio
- Displays AI-generated **Observations** and **Suggestions** in a clean card layout
- Fully responsive and styled with Tailwind CSS
- Real-time loading feedback

---

## 🧱 Tech Stack

- [React](https://reactjs.org/)
- [Vite](https://vitejs.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [FastAPI](https://fastapi.tiangolo.com/) (Backend, not part of this repo)

---

## 📦 Setup Instructions

### 1. Clone the repository

If frontend and backend are in the same repo:
```bash
cd frontend
npm install
npm run dev
```

⚙️ Backend Integration
Make sure the FastAPI backend is running on:

```bash
http://localhost:8000/ask-ai
```

The frontend expects a GET response like:
```bash
{
  "response": "```json\n{ \"observations\": [...], \"suggestions\": [...] }\n```"
}
```
