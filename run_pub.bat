@echo off

echo "Welcome - Gabriela Kuhn assigment - publishing the message..."
echo "Message was publish, go to subscribe terminal to check the response..."

cmd /k ".\venv\Scripts\activate.bat && python tsp_service/publish.py"
pause

