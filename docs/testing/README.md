Besides unit tests, one can test endpoints with following CURL commands:

# 🧪 FastAPI CRUD API Test Commands (PowerShell Compatible)

This markdown file documents how to test your FastAPI CRUD endpoints using `Invoke-RestMethod` in PowerShell (instead of Bash `curl`).  
Make sure your FastAPI server is running at [http://localhost:8000](http://localhost:8000).

---

## 🔐 Authentication Header

> All authenticated endpoints require this header:

```powershell
"token" = "fake-super-secret-token"
```

---

## 📦 Items Endpoints

### ✅ Create Item (POST `/api/v1/items`)

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/items" `
  -Method Post `
  -Headers @{
    "Content-Type" = "application/json"
    "token" = "fake-super-secret-token"
  } `
  -Body '{"name": "Notebook", "description": "A lined paper notebook"}'
```

---

### 📃 Get All Items (GET `/api/v1/items`)

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/items" `
  -Headers @{
    "token" = "fake-super-secret-token"
  }
```

---

### 🔍 Get Item by ID (GET `/api/v1/items/{item_id}`)

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/items/1" `
  -Headers @{
    "token" = "fake-super-secret-token"
  }
```

---

### 🔎 Filter Items by Query (GET `/api/v1/items?name=book`)

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/items?name=book" `
  -Headers @{
    "token" = "fake-super-secret-token"
  }
```

---

## 👤 Users Endpoints

### ✅ Create User (POST `/api/v1/users`)

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/users" `
  -Method Post `
  -Headers @{
    "Content-Type" = "application/json"
  } `
  -Body '{"username": "john", "email": "john@example.com"}'
```

---

### 🔐 Get All Users (GET `/api/v1/users`)

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/users" `
  -Headers @{
    "token" = "fake-super-secret-token"
  }
```

---

### 🔐 Get User by ID (GET `/api/v1/users/1`)

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/users/1" `
  -Headers @{
    "token" = "fake-super-secret-token"
  }
```
