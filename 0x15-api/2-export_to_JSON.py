#!/usr/bin/python3
"""Module export to json"""

import json
import requests
import sys


def export_json(employee_id):
    """Get the todo list for a given employee id"""
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(url, employee_id)).json()
    todos = requests.get("{}/todos?userId={}".format(url, employee_id)).json()

    tasks = [{
        "task": todo.get("title"),
        "completed": todo.get("completed"),
        "username": user.get("username")
    } for todo in todos]

    # Structure the data as required
    data = {str(employee_id): tasks}

    # Write the JSON data to file
    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("EMPLOYEE_ID must be an integer.")
        sys.exit(1)

    export_json(employee_id)
