@echo off

echo "Welcome - Gabriela Kuhn assigment - running Django localserver and RabbitMQ on Docker..."
echo "Subscribe is listening, run '.\run_pub.bat' to publish message with locations data and check the response here..."

cmd /k ".\venv\Scripts\activate.bat && python api/requests/locationpost.py && python tsp_service/subscribe.py"
pause

