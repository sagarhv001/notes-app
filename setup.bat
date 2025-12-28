@echo off
python -m venv venv
venv\Scripts\pip install -r requirements.txt
venv\Scripts\python -m django startproject notesapp .
venv\Scripts\python manage.py startapp users
venv\Scripts\python manage.py startapp notes
venv\Scripts\python manage.py startapp tasks
echo Done!
