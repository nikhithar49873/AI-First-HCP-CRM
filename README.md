# AI-First HCP CRM

## Project Overview

AI-First HCP CRM is an AI-powered Healthcare CRM application that helps medical representatives record doctor interactions efficiently. Users can enter meeting notes, and the AI assistant extracts structured information to automatically populate the interaction form before saving it to the database.

---

## Features

- AI-assisted interaction logging
- Automatic extraction of doctor details
- Auto-fill interaction form
- Store interactions in SQLite
- FastAPI REST APIs
- React frontend
- LangGraph agent workflow
- Groq LLM integration

---

## Tech Stack

Frontend
- React
- Vite
- Axios

Backend
- FastAPI
- SQLAlchemy
- LangGraph
- Groq API

Database
- SQLite

---

## How to Run

### Backend

```bash
cd backend
venv\Scripts\activate
python -m uvicorn app.main:app --reload
