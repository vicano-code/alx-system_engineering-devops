#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress
Use the REST API https://jsonplaceholder.typicode.com/ to access employee data
Export employee_Id data to json file
employee_id_data given as command-line argument
Usage: python3 2-export_to_JSON.py 2
"""
import json
import requests
from sys import argv


def employee_info_to_json():
    users_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(users_url)
    users_data = response.json()
    for user in users_data:
        if user.get("id") == int(argv[1]):
            USERNAME = user.get("username")
            break
    TASK_STATUS = []
    TASK_TITLE = []
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    for todo in todos.json():
        if todo.get("userId") == int(argv[1]):
            TASK_STATUS.append(todo.get("completed"))
            TASK_TITLE.append(todo.get("title"))
    '''export data to json file'''
    tasks = []
    for i in range(len(TASK_TITLE)):
        tasks.append({"task": TASK_TITLE[i], "completed": TASK_STATUS[i],
                     "username": USERNAME})
    data = {str(argv[1]): tasks}
    filename = "{}.json".format(argv[1])
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == '__main__':
    employee_info_to_json()
