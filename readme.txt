Gabriela Kuhn - Jan 2022

## Documentation ##

Project process:
- The start point of this project is a Django project using djangorestframework
- The server can be running with run_django.bat and it connects to a RESTapi to post/get location information
- The Location Model include the fields "name, latitude, and longitude"
- Check location api in http://127.0.0.1:8000/api/location
- Posting can be done via browser or api/requests/locationpost.py. Using file data_for_test.json you can input one or more location
- The publish.py file connect to location endpoint to get data
- publish.py publish a message with location data to subscribe.py file which receive the message and handled it inside of tsp service
- tsp_service.py handle the data format, compute distance with euclidean formula and connect to tsp.py(from ortools) to compute the route plan
- Then tsp_service.py handle the return array from tsp to return the route plan with locations name to subscribe.py
- subscribe.py response to the message after the process with a route plan

How to run?
#1 - In the root folder run 'example.bat or example.sh or for linux'
    -> it will raise a local server in django which can be checked in http://127.0.0.1:8000/api/location
#2 - Also a second terminal will open at the same time to run a docker container with RabbitMQ
#3 - Besides, a third terminal will open and after 5 seconds (timeframe necessary to wait RabbitMQ server initializer) this terminal will run 'run_sub.bat'
    -> it will access api/requests/locationpost.py api to post data inside of data_for_test.json file
    -> it will also Start Consuming messages from the queue
#4 - After 10 seconds a new terminal will open and run 'run_pub.bat'
    -> it will get location api information and publish a message to subscribe
    -> check subscribe response in #3 terminal
    -> if you want to run publish again run .\run_scripts\run_pub.bat in root folder


Requirements:
- Python 3.10
- RabbitMQ Server and Erlang
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