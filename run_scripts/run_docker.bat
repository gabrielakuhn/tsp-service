@echo off

echo "Welcome - Gabriela Kuhn assigment - running RabbitMQ on Docker compose..."
echo "After it, run '.\run_sub.bat' to continue..."

start cmd.exe /C .\run_scripts\run_sub.bat
docker-compose up

pause