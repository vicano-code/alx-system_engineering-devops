#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress
Use the REST API https://jsonplaceholder.typicode.com/ to access employee data
Export all employee data to json file
Usage: python3 3-dictionary_of_list_of_dictionaries.py
"""
import json
import requests


def all_employee_info_to_json():
    users_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(users_url)
    users_data = response.json()
    user_id_list = []
    tasks_list = []
    for user in users_data:
        USER_ID = user.get("id")
        USERNAME = user.get("username")
        TASK_STATUS = []
        TASK_TITLE = []
        todos = requests.get("https://jsonplaceholder.typicode.com/todos")
        for todo in todos.json():
            if todo.get("userId") == USER_ID:
                TASK_STATUS.append(todo.get("completed"))
                TASK_TITLE.append(todo.get("title"))
        tasks = []
        for i in range(len(TASK_TITLE)):
            tasks.append({"username": USERNAME, "task": TASK_TITLE[i],
                         "completed": TASK_STATUS[i]})
        user_id_list.append(USER_ID)
        tasks_list.append(tasks)
    '''Export data to json'''
    data = {}
    for i in range(len(user_id_list)):
        data[str(user_id_list[i])] = tasks_list[i]

    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == '__main__':
    all_employee_info_to_json()
