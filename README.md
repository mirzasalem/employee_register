# 📘 Employee Register — Documentation

A comprehensive documentation for the **Employee Register** project.  

**Employee Register** is a simple full-stack application that allows users to:

- **Add new employees**
 <img width="800" height="600" alt="Screenshot from 2026-01-11 01-10-26" src="https://github.com/user-attachments/assets/d976e252-4279-467b-a0b9-d48a3fecd993" />

- **View employee details**
- **Edit existing employee records**
- **Delete employee records**
  <img width="800" height="600" alt="Screenshot from 2026-01-11 01-19-02" src="https://github.com/user-attachments/assets/e26d7f0e-10f5-4c29-adb1-7e1068487b1b" />

It is designed to keep an organized record of employee information (like name, designation, department, etc.) in a database and display it in a user-friendly dashboard.

---

## 📌 Project Overview

This project allows CRUD operations on employee data, keeping it organized and accessible. The system typically includes features such as:

- Employee registration
- Employee listing
- Employee updates
- Employee deletion

---


---

## 🛠️ Technology Stack

| Layer    | Technology           |
|----------|-------------------|
| Backend  | Python / Django    |
| Frontend | HTML, CSS, Bootstrap |
| Database |  MySQL     |
| Others   | Django Template Engine |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mirzasalem/employee_register.git
cd employee_register
```
2️⃣ Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Database Migration
```bash
python manage.py makemigrations
python manage.py migrate
```
<img width="800" height="600" alt="Screenshot from 2026-01-11 01-15-33" src="https://github.com/user-attachments/assets/85df5479-6a2e-43d9-92d3-1714019f7422" />

5️⃣ Run Development Server
```bash
python manage.py runserver
```
## 🔐 Authentication & Authorization

This project uses **Django’s built-in authentication system** to ensure secure access to employee data.

### Authentication
<img width="800" height="600" alt="Screenshot from 2026-01-11 00-59-14" src="https://github.com/user-attachments/assets/333e1417-a8fd-4839-ba6b-92f73f448a54" />

- User **registration**, **login**, and **logout** are implemented
- Passwords are securely stored using Django password hashing
- Invalid login attempts display error messages

### Authorization
<img width="800" height="600" alt="Screenshot from 2026-01-11 01-01-34" src="https://github.com/user-attachments/assets/bddad093-beb3-4efa-81fd-20116813a65b" />

- Employee list view is protected using `@login_required`
- Only **staff users** (`is_staff=True`) can delete employee records
- Unauthorized actions are restricted with proper feedback

### Security Features
- Session-based authentication
- Login-protected views
- Role-based access control
- Django messages for user notifications
- Group-based authorization
- Permission-based access control

## 🖼 Static & Media Files Configuration

This project uses **static files** for CSS, JavaScript, and images, and **media files** for uploaded employee images.

### Static Files

- **Settings:**
```python
STATIC_URL = '/static/img/'
STATICFILES_DIRS = [BASE_DIR / "static"]
Purpose: Serve CSS, JS, and static images
```
Location: static/ directory at the project root

Media Files (Image Uploads)
Settings:

```
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
Purpose: Store uploaded employee images

Location: media/ directory

### URL Configuration (for Development)
To serve media files in development mode, add this to your urls.py:

```
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



