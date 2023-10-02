# pub-sub-pattern-django

# prerequisites:

1. make sure that Redis is installed
2. check that the redis server is running ```systemctl status redis-server```
3. run ```redis-cli``` in the terminal
4. docker should be installed in the system
5. use ```sudo docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management``` to start rabbitmq server

# How to run the app:
1. clone the repo ```git@github.com:C0deGeek007/pub-sub-pattern-django.git```
2. install all dependencies from requirements.txt file
3. run ```python manage.py makemigrations```
4. run ```python manage.py migrate```
5. In user_app start the server ```python manage.py runserver``` also start celery worker process ```celery -A user_app worker --loglevel=info```
6. In ERP app start the server ```python manage.py runserver``` also run the script that act as consumer ```python consumer.py```

# Problem Statement: 
Optimizing User Permission Validation in a Microservices Architecture

# Context:
In a microservices architecture, there are two distinct services: the "User" service and the "Student" service. These services have their own separate databases, and the goal is to control access to student data modification based on user permissions. Users should only be able to change student details if they have the required permissions.

# Problem:
The current system relies on a request-based permission validation mechanism, where the "Student" service sends requests to the "User" service to determine if a user has the necessary permissions. While this approach is straightforward, it has the potential to introduce performance bottlenecks due to frequent requests to the "User" service.

# Desired Outcome:
The objective is to optimize the user permission validation process while minimizing network overhead. The ideal solution should reduce the number of requests between the "Student" and "User" services while ensuring that access control is maintained.

# Proposed Solutions:
There are two proposed solutions:

# Request-Based Permission Validation: 
The "Student" service sends permission validation requests to the "User" service, which responds with the permission status for each request.

# Pub/Sub and Cache-Based Permission Management(I tried to implement this for POC there are many changes that can be made to use it in real system in production):
Implement a pub/sub mechanism where the "User" service publishes permission updates, and the "Student" service maintains a local cache of user permissions, minimizing the need for frequent external requests.

# Architectural diagram
![Blank diagram](https://github.com/C0deGeek007/pub-sub-pattern-django/assets/45477155/291e436f-1054-41ea-877d-b499d0a8ddd9)

