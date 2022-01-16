@echo off

echo "Welcome - Gabriela Kuhn assigment - running Django localserver and RabbitMQ on Docker..."
echo "Subscribe is listening, run '.\run_pub.bat' to publish message with locations data and check the response here..."

timeout 5
start cmd.exe /C .\run_scripts\run_pub.bat
cmd /k ".\venv\Scripts\activate.bat && python api/requests/locationpost.py && python tsp_service/subscribe.py"
pause

