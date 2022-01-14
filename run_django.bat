@echo off
echo "Welcome - Gabriela Kuhn assigment - running Django localserver..."
echo "Check/Edit the location list in http://127.0.0.1:8000/api/location"
echo "After it, run '.\run_docker.bat' to continue..."

cmd /k ".\venv\Scripts\activate.bat && pip install -r requirements.txt && python manage.py runserver"

pause