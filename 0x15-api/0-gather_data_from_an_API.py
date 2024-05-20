#!/usr/bin/python3
"""Module  to fetch data from an API"""

import requests
import sys


def get_employee_todo_list(employee_id):
    """Get the todo list for a given employee id"""
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(url, employee_id)).json()
    todos = requests.get("{}/todos?userId={}".format(url, employee_id)).json()

    completed = [todo for todo in todos if todo.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    for todo in completed:
        print("\t {}".format(todo.get("title")))



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("EMPLOYEE_ID must be an integer.")
        sys.exit(1)

    get_employee_todo_list(employee_id)
