# Job Tracker API

A production-style backend application for tracking job applications, built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

---

## Features

- RESTful API
- Versioned API routes
- Centralized configuration
- Structured logging
- PostgreSQL database
- SQLAlchemy ORM
- Alembic database migrations
- JWT Authentication *(coming soon)*
- Automated testing *(coming soon)*

---

## Tech Stack

- Python 3.14+
- FastAPI
- SQLAlchemy 2.0
- Alembic
- PostgreSQL
- Uvicorn
- Ruff
- Black
- Pytest
- uv

---

## Project Structure

```text
app/
├── api/
├── auth/
├── core/
├── db/
├── models/
├── repositories/
├── schemas/
├── services/
├── utils/
└── main.py
```

---

## Running the Project

```bash
uv sync
python -m uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Status

🚧 Under active development.