# Django Notes & Task Management App (Modified)

A responsive web application for taking notes and managing tasks, built with Django and Bootstrap 5.

## Features
- **Notes**: Create, edit, delete, and pin notes with different colors.
- **Tasks**: Manage tasks with priorities, due dates, and status toggles.
- **Dashboard**: Overview of recent notes and pending tasks.
- **Responsive**: Works on desktop and mobile devices.
- **Admin Panel**: Modern admin interface powered by Jazzmin.

## Local Setup

1. **Clone the repository** (or use the current directory)
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the server**:
   ```bash
   python manage.py runserver
   ```

## Deployment to Render (Free)

1. **Create a Render account** at [render.com](https://render.com).
2. **Create a new PostgreSQL database** on Render (Free tier).
3. **Copy the Internal Database URL**.
postgresql://sagar:qn7cOQvaBwYVvNdn3mq2tnYEK7xi1DIg@dpg-d58oajqli9vc73a6rmh0-a/notes_app_db_3b5r
4. **Create a new Web Service** on Render:
   - Connect your GitHub repository.
   - **Environment**: Python
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn notesapp.wsgi`
5. **Add Environment Variables**:
   - `SECRET_KEY`: A long random string.
   - `DATABASE_URL`: Your Render PostgreSQL URL.
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `your-app-name.onrender.com`
6. **Deploy!**

- **Admin URL**: `http://localhost:8000/admin/`
