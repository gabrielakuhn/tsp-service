@echo off
echo "Welcome - Gabriela Kuhn assigment - running Django localserver, RabbitMQ in docker, Subscribe and Publish ..."
echo "Check/Edit the location list in http://127.0.0.1:8000/api/location"

start cmd.exe /C .\run_scripts\run_docker.bat
cmd /k ".\venv\Scripts\activate.bat && pip install -r requirements.txt && python manage.py runserver"

pause