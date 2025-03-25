![API Development](https://img.shields.io/badge/API%20Development-%20FastAPI%20|%20REST%20|%20Unit%20Tests%20-blue)

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

### Overview

```mermaid
graph TD
    Run["▶️ run.py<br/>Entry Point"] -->|launches| Uvicorn["🌀 Uvicorn<br/>ASGI Server"]
    Uvicorn --> AppMain["🚀 app.main.py<br/>FastAPI App"]

    %% App Layer
    AppMain --> Router["📦 api.v1.items.py<br/>Routes"]
    AppMain --> Settings["⚙️ core.config.py<br/>Settings"]

    %% Router Layer
    Router --> Schemas["🧾 schemas.item.py"]
    Router --> Service["🧠 services.item_service.py"]
    Router --> Auth["🔐 dependencies.auth.py"]

    %% Service Layer
    Service --> Session["🔗 db.session.py"]
    Service --> ORM["🧱 models.item.py"]

    %% Database
    ORM --> DB["🗄️ SQLite Database (test.db)"]
```
### Request Flow

```mermaid
sequenceDiagram
    autonumber
    participant Browser as 🧑‍💻 Browser (User)
    participant OS as 🖥️ Operating System
    participant Uvicorn as 🌀 Uvicorn (ASGI Server)
    participant FastAPI as 🚀 FastAPI App
    participant App as 🧠 Route Function (e.g. /items)

    Note over Browser: User visits http://127.0.0.1:8000/api/v1/items

    Browser->>OS: Send HTTP GET request
    OS->>Uvicorn: Deliver TCP packet with HTTP request

    Note over Uvicorn: Uvicorn listens on 127.0.0.1:8000
    Uvicorn->>Uvicorn: Parse HTTP method and route
    Uvicorn->>FastAPI: Call FastAPI ASGI app

    FastAPI->>FastAPI: Match route: GET /api/v1/items
    FastAPI->>FastAPI: Inject dependencies (e.g. get_current_user)
    FastAPI->>App: Call endpoint function

    App->>DB: Read from SQLite via SQLAlchemy
    DB-->>App: Return queried items

    App-->>FastAPI: Return Python list of dicts

    FastAPI->>FastAPI: Serialize to JSON
    FastAPI->>Uvicorn: Send response body + headers

    Uvicorn->>OS: Compose HTTP response
    OS->>Browser: Return HTTP 200 + JSON payload

    Browser->>Browser: Render JSON in UI

    Note over Browser,App: End-to-end request/response cycle
```
---
## 🧪 Tests

Run all tests:

```bash
pytest
```

All tests currently pass. Test files cover:
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
