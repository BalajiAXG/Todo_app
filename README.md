# ✅ Django Todo App – HTML + REST API

A beginner-friendly Django application that allows users to manage their daily tasks through both a clean web interface and a REST API.

---

## 📌 Features

- Add new tasks
- Edit existing tasks
- Mark tasks as done or undone
- Delete tasks
- View all tasks
- RESTful API endpoints for CRUD operations
- Bootstrap-powered responsive UI

---

## 🧰 Tech Stack

| Layer        | Technology               |
|--------------|---------------------------|
| Backend      | Django, Django REST Framework |
| Frontend     | HTML, Bootstrap 5         |
| Database     | SQLite (default with Django) |
| API Testing  | Postman                   |

---

## 🗂 Folder Structure (Simplified)

Todo_app/
├── main/ # Django app
│ ├── migrations/
│ ├── templates/
│ │ └── index.html # HTML UI
│ ├── models.py # Task model
│ ├── serializers.py # API serializer
│ ├── views.py # HTML + API logic
│ └── urls.py # App routing
├── simplecrud/
│ └── settings.py # Django settings
├── db.sqlite3 # SQLite database
├── manage.py # Django entry point
└── requirements.txt # Python dependencies
