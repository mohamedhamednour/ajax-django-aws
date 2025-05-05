# 🐍 Django Backend Project

This is the backend for the Django-based web application.

---

## 🚀 How to Run the Project Locally (Without Docker)

1. **Create and activate virtual environment:**

```bash
cd backend
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000



🐳 How to Run the Project with Docker
 docker-compose up --build

