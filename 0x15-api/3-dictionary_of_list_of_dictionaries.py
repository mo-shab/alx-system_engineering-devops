#!/usr/bin/python3
"""Modele export to json"""

import json
import requests
import sys


def export_json():
    """Get the todo list for all employees"""
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(url)).json()
    todos = requests.get("{}/todos".format(url)).json()

    data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        } for todo in todos if todo.get("userId") == user_id]

        data[str(user_id)] = tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == '__main__':
    export_json()
