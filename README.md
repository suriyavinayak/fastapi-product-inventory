# 📦 Product Inventory Management System

A full-stack product inventory management web application built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **React**.

---

## 🚀 Features

- **Full CRUD Operations**: Create, read, update, and delete products with instant synchronization.
- **Persistent Storage**: Robust data persistence powered by **PostgreSQL** and **SQLAlchemy ORM**.
- **Data Validation & Schemas**: Automatic request parsing and type-safe validation using **Pydantic**.
- **Interactive API Documentation**: Live Swagger UI (`/docs`) and ReDoc (`/redoc`) generated automatically by FastAPI.
- **Modern Responsive Dashboard**: Clean React frontend with real-time search, sorting, inventory counters, and auto-dismiss alerts.
- **Cross-Origin Resource Sharing (CORS)**: Configured middleware enabling secure communication between React (`http://localhost:3000`) and FastAPI (`http://localhost:8000`).

---

## 🛠️ Tech Stack

### Backend
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Server:** [Uvicorn](https://www.uvicorn.org/) (ASGI)
- **Database:** [PostgreSQL](https://www.postgresql.org/)
- **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
- **Data Validation:** [Pydantic](https://docs.pydantic.dev/)
- **Database Driver:** `psycopg2`

### Frontend
- **Library:** [React 18](https://react.dev/)
- **HTTP Client:** [Axios](https://axios-http.com/)
- **Styling:** CSS3 (Custom Responsive Design)

---

## 📂 Project Structure

```text
fastapi-learning/
│
├── main.py               # FastAPI app entry point, routing & dependency injection
├── database.py           # Database connection engine & SessionLocal factory
├── database_models.py    # SQLAlchemy ORM models (PostgreSQL table schemas)
├── models.py             # Pydantic schemas (Request/Response data validation)
├── README.md             # Project documentation
│
└── frontend/             # React single-page application
    ├── public/
    │   └── index.html    # Base HTML template
    ├── src/
    │   ├── App.js        # Main React dashboard & inventory UI logic
    │   ├── App.css       # Main application styling
    │   ├── TaglineSection.js  # Inventory banner & branding component
    │   ├── TaglineSection.css # Tagline styling
    │   └── index.js      # React DOM entry point
    ├── package.json      # Frontend dependencies & scripts
    └── package-lock.json
```

---

## 🔌 API Endpoints

FastAPI exposes the following RESTful endpoints:

| Method | Endpoint | Description | Request Body | Response |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/` | Health check / Welcome message | None | String |
| `GET` | `/products/` | Fetch all products from PostgreSQL | None | List of Products |
| `GET` | `/products/{product_id}` | Fetch a specific product by ID | None | Product object or 404 |
| `POST` | `/products/` | Add a new product to inventory | JSON (`Product`) | Confirmation & created product |
| `PUT` | `/products/{product_id}` | Update an existing product | JSON (`Product`) | Confirmation & updated product |
| `DELETE` | `/products/{product_id}` | Delete a product by ID | None | Confirmation message |

### Product Data Schema (Pydantic / JSON)
```json
{
  "id": 1,
  "name": "Smartphone",
  "description": "High-performance smartphone",
  "price": 699.99,
  "quantity": 50
}
```

---

## ⚙️ Setup and Installation

### 1. Prerequisites
- **Python 3.10+** installed
- **Node.js (v18+)** and **npm** installed
- **PostgreSQL** installed and running on `localhost:5432`

---

### 2. Database Setup
1. Open **pgAdmin** or `psql` command line.
2. Create a new database named **`telusko`**:
   ```sql
   CREATE DATABASE telusko;
   ```
3. Update your credentials in `database.py`:
   ```python
   # Replace 'root' with your PostgreSQL password
   db_url = "postgresql+psycopg2://postgres:root@localhost:5432/telusko"
   ```

---

### 3. Backend Setup (FastAPI)

1. Open your terminal in the project root directory:
   ```powershell
   cd "c:\fastapi learning"
   ```

2. Activate the virtual environment:
   * **Windows PowerShell:**
     ```powershell
     .\myenv\Scripts\Activate.ps1
     ```
   * **macOS / Linux:**
     ```bash
     source myenv/bin/activate
     ```

3. Install required Python packages:
   ```powershell
   pip install fastapi uvicorn sqlalchemy psycopg2 pydantic
   ```

4. Run the FastAPI development server:
   ```powershell
   uvicorn main:app --reload
   ```
   * Backend will be live at: **http://127.0.0.1:8000**
   * Interactive Swagger UI: **http://127.0.0.1:8000/docs**
   * Alternative ReDoc UI: **http://127.0.0.1:8000/redoc**

---

### 4. Frontend Setup (React)

1. Open a **second terminal** and navigate to the frontend folder:
   ```powershell
   cd "c:\fastapi learning\frontend"
   ```

2. Install npm packages (if not already installed):
   ```powershell
   npm install
   ```

3. Start the React development server:
   ```powershell
   npm start
   ```
   * The React app will automatically open in your browser at: **http://localhost:3000**

---

## 💡 Troubleshooting & Notes

- **CORS Issue**: If products are not displaying on the frontend, verify that `main.py` has CORS middleware configured with `http://localhost:3000` (HTTP, not HTTPS).
- **PowerShell Script Policy**: If activating the virtual environment throws an execution policy error, run:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
- **pgAdmin Refresh**: If newly added tables do not show in pgAdmin, navigate to `Databases -> telusko -> Schemas -> public -> Tables`, right-click on `Tables` and click **Refresh...**.

---

## 👨‍💻 Author & Acknowledgements
- Developed following the **Telusko** FastAPI course series.
- Customizations, setup, and enhancements by **Suriya**.
