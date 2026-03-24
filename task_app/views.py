from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from task_app.models import Task
import json

USER_FILE = '/Users/shaileshmohite/Documents/AirTribe/django-track-engine-api/user.json'
TASK_FILE = '/Users/shaileshmohite/Documents/AirTribe/django-track-engine-api/task.json'

@api_view(['POST'])
def add_task(request: Request):
    
    #read from request body
    data = request.data

    #read from task.json
    with open(TASK_FILE, 'r') as file:
        tasks: list = json.load(file)
    
    # create a new task
    new_task = {
        "id": data['id'],
        "name": data['name'],
        "user_id": data['user_id'],
        "description": data['description'],
        "completed": data['completed']
    }
    # add task to tasks list
    tasks.append(new_task)
    # write to task.json
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)
    return Response({'message': 'Task added successfully', 'task': new_task})