Besides unit tests, one can test endpoints with following CURL commands:


# 🧪 API Endpoint Tests (via `curl` - PowerShell Compatible)

Make sure your server is running locally at `http://localhost:8000`.

> 🔐 All protected routes require this header:
```
-H "token: fake-super-secret-token"
```

---

## ✅ Create Item (POST `/api/v1/items`)

```powershell
curl -X POST "http://localhost:8000/api/v1/items" `
     -H "Content-Type: application/json" `
     -H "token: fake-super-secret-token" `
     -d '{"name": "Notebook", "description": "A lined paper notebook"}'
```

---

## 📋 List All Items (GET `/api/v1/items`)

```powershell
curl -X GET "http://localhost:8000/api/v1/items" `
     -H "token: fake-super-secret-token"
```

## 📋 List Items with Filters (Query Parameters)

```powershell
curl -X GET "http://localhost:8000/api/v1/items?name=note&description=lined" `
     -H "token: fake-super-secret-token"
```

---

## 🔍 Get Single Item by ID (GET `/api/v1/items/{item_id}`)

```powershell
curl -X GET "http://localhost:8000/api/v1/items/1" `
     -H "token: fake-super-secret-token"
```

---

## 👤 Create User (Public, POST `/api/v1/users`)

```powershell
curl -X POST "http://localhost:8000/api/v1/users" `
     -H "Content-Type: application/json" `
     -d '{"username": "alice", "email": "alice@example.com"}'
```

---

## 👤 Get All Users (Auth Required)

```powershell
curl -X GET "http://localhost:8000/api/v1/users" `
     -H "token: fake-super-secret-token"
```

---

## 👤 Get User by ID (Auth Required)

```powershell
curl -X GET "http://localhost:8000/api/v1/users/1" `
     -H "token: fake-super-secret-token"
```
