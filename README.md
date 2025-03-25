# 🚀 FastAPI Template Project

A production-ready, modular FastAPI backend template with:

- Clean project architecture (versioned API, services, models, schemas, etc.)
- Pydantic v2 compatibility
- SQLAlchemy 2.x support with SQLite
- Dependency injection & basic auth simulation
- Pytest test suite with 100% passing tests
- Future-ready: Docker, OAuth2, Alembic, deployment support

---

## 🗂️ Project Structure

```
fastapi-template-dev/
├── src/
│   ├── app/
│   │   ├── api/              ← Route handlers (v1)
│   │   ├── core/             ← App config, settings
│   │   ├── db/               ← Database connection/session
│   │   ├── dependencies/     ← Dependency injections (e.g., auth)
│   │   ├── models/           ← SQLAlchemy models
│   │   ├── schemas/          ← Pydantic models
│   │   ├── services/         ← Business logic layer
│   │   └── main.py           ← FastAPI app instance
│   └── scripts/
│       └── initialize_db.py  ← Creates tables
├── tests/                    ← Unit test files
│   ├── test_items.py
│   └── test_main.py
├── .env.example              ← Environment config sample
├── requirements.txt          ← Dependencies
├── pytest.ini                ← Pytest config (for path resolution)
└── README.md
```

---
## 📊 Diagram


```mermaid
Copy
Edit
graph TD
  %% Entry Point
  Run[run.py] -->|launches| Uvicorn[Uvicorn Server]
  Uvicorn --> AppMain[app.main.py (FastAPI App)]

  %% App Layer
  AppMain --> Router[api.v1.items.py]
  AppMain --> Settings[core.config.py]

  %% Router Layer
  Router --> Schemas[schemas.item.py]
  Router --> Service[services.item_service.py]
  Router --> Auth[dependencies.auth.py]

  %% Service Layer
  Service --> Session[db.session.py]
  Service --> ORM[models.item.py]

  %% Database
  ORM --> DB[(SQLite Database)]
```

---
## 🧪 Tests

Run all tests:

```bash
pytest
```

All tests currently pass ✅. Test files cover:
- Auth behavior
- CRUD endpoints
- Error cases (missing tokens, invalid routes)

---

## ⚙️ Setup & Run Locally

### 1. Clone & Setup

```bash
git clone https://github.com/yourusername/fastapi-template-dev.git
cd fastapi-template-dev
python -m venv env
env\Scripts\activate  # or source env/bin/activate on Unix
pip install -r requirements.txt
```

### 2. Set Environment Variables

Copy `.env.example` and name it `.env`

```bash
cp .env.example .env
```

### 3. Initialize the Database

```bash
python src/scripts/initialize_db.py
```

### 4. Run the Server

```bash
uvicorn app.main:app --reload --app-dir src
```

Open browser:
- API: http://localhost:8000
- Docs: http://localhost:8000/docs

---

## 🔐 Simulated Authentication

Add this header to your requests to access protected routes:

```
token: fake-super-secret-token
```

---

## 🧱 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic v2](https://docs.pydantic.dev/)
- [SQLAlchemy 2](https://docs.sqlalchemy.org/en/20/)
- [Pytest](https://docs.pytest.org/)
- [Uvicorn](https://www.uvicorn.org/)
- SQLite (for local/dev)

---

## 📦 Roadmap / To-Do

| Task                                | Purpose                         |
|-------------------------------------|---------------------------------|
| 🔐 Add OAuth2 + JWT auth            | Secure real users               |
| 👥 Add CRUD for Users or Posts      | Demonstrate relationships       |
| 🛢 Add Alembic migrations           | Safer schema evolution          |
| 🐳 Add Dockerfile + docker-compose  | Simplified deployment           |
| ☁️ Deploy to Render / Azure / Railway | Live demo hosting              |

---
