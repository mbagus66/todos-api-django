ToDo API with Django and Django Rest Framework

Requirements
 - Python 3
 - Django
 - Django Rest Framework

To run
 - python3 manage.py runserver


Access to get token
 - POST http://localhost:8000/get-token/
with Body
 - username : mbagus66
 - password : indonesia200

you will get token auth
   "token" : "fc10b7b3b347dd71dd2aef4641334ac3eb08c452"


Access to endpoint
 - GET http://localhost:8000/todos
With Headers
 - Authorization : Token fc10b7b3b347dd71dd2aef4641334ac3eb08c452


Endpoint
 - GET /todos – to get all todo list
 - GET /todos/<str:id> – to get the detail of specific todo list
 - POST /todos – to post a new todo
 - PUT /todos/<str:id> – to update a todo or mark as done
 - DELETE /todos/<str:id> – to delete a todo

Thank to :
https://github.com/gitgik/django-rest-api