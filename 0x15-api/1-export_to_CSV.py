#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress
Use the REST API https://jsonplaceholder.typicode.com/ to access the data
Export employee_id data to csv file
employee_id data given as command line argument
Usage: python3 1-export_to_CSV.py 2
"""
import csv
import requests
from sys import argv


def employee_info_to_csv():
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
    '''export data to csv file'''
    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for i in range(len(TASK_TITLE)):
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": TASK_STATUS[i],
                             "TASK_TITLE": TASK_TITLE[i]})


if __name__ == '__main__':
    employee_info_to_csv()
