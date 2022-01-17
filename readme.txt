Gabriela Kuhn - Jan 2022

## Documentation ##

Project process:
- The start point of this project is a Django project using djangorestframework
- The server can be running with run_django.bat or example.bat and it connects to a RESTapi to post/get location information
- The Location Model include the fields "name, latitude, and longitude"
- The location api can be checked in http://127.0.0.1:8000/api/location
- Posting can be done via browser or api/requests/locationpost.py. Using file data_for_test.json you can input one or more location
- The publish.py file connect to location endpoint to get data
- publish.py publish a message with location data to subscribe.py file which receive the message and handled it inside of tsp service
- tsp_service.py handle the data format, compute distance with euclidean formula and connect to tsp.py(from ortools) to compute the route plan
- Then tsp_service.py handle the return array from tsp to return the route plan with locations name to subscribe.py
- subscribe.py response to the message after the process with a route plan

How to run?
#1 - Create a Python venv and activate it
#2 - Initialize docker
#3 - run 'pip install -r requirements.txt'
#4 - In the root folder run 'example.bat'
    -> it will raise a local server in django which can be checked in http://127.0.0.1:8000/api/location
    -> Also a second terminal will open at the same time to run a docker container with RabbitMQ (docker-compose)

Testing the application
#5 - When both server are running open a third terminal and run '.\run_scripts\run_sub.bat' in the root folder
    -> it will access api/requests/locationpost.py api to post data inside of data_for_test.json file
    -> it will also Start Consuming messages from the queue
#6 - Open a new terminal and run '.\run_scripts\run_pub.bat' in root folder
    -> it will get location api information and publish a message to subscribe
    -> check subscribe response in #3 terminal
    -> if you want to run publish again run .\run_scripts\run_pub.bat in root folder

OR open 4 terminals, activate venv and directly run in each one in root folder:
- 'python manage.py runserver' -> run django server
- 'docker-compose up' -> compose rabbitMQ
- 'python api/requests/locationpost.py && python tsp_service/subscribe.py' -> post locations and start listening publish
- 'python tsp_service/publish.py' -> publish message

Requirements:
- Python 3.10
- Docker and docker-compose
- a virtualenv venv
Package             Version
------------------- ---------
absl-py             1.0.0
asgiref             3.4.1
certifi             2021.10.8
charset-normalizer  2.0.10
Django              4.0.1
djangorestframework 3.13.1
idna                3.3
numpy               1.22.0
ortools             9.2.9972
pika                1.2.0
pip                 21.1.2
protobuf            3.19.3
pytz                2021.3
requests            2.27.1
setuptools          57.0.0
six                 1.16.0
sqlparse            0.4.2
tzdata              2021.5
urllib3             1.26.8
wheel               0.36.2