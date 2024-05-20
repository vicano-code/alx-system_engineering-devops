#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress
Use the REST API https://jsonplaceholder.typicode.com/ to access the data
"""

import requests
from sys import argv


def display_employee_info():
    users_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(users_url)
    users_data = response.json()
    for user in users_data:
        if user.get("id") == int(argv[1]):
            EMPLOYEE_NAME = user.get("name")
            break
    TOTAL_NUM_TASKS = 0
    NUM_DONE_TASKS = 0
    TASK_TITLE = []
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    for todo in todos.json():
        if todo.get("userId") == int(argv[1]):
            TOTAL_NUM_TASKS += 1
            if todo.get("completed") is True:
                NUM_DONE_TASKS += 1
                TASK_TITLE.append(todo.get("title"))
    print("Employee {} is done with tasks ({}/{}):".format(EMPLOYEE_NAME,
                                                           NUM_DONE_TASKS,
                                                           TOTAL_NUM_TASKS))
    for task in TASK_TITLE:
        print("\t {}".format(task))


if __name__ == '__main__':
    display_employee_info()
