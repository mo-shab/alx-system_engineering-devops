#!/usr/bin/python3
"""Module  to fetch data from an API"""

import requests
import sys
import csv


def export_cvs(employee_id):
    """Get the todo list for a given employee id"""
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(url, employee_id)).json()
    todos = requests.get("{}/todos?userId={}".format(url, employee_id)).json()

    with open("{}.csv".format(employee_id), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([employee_id, user.get("username"),
                             todo.get("completed"), todo.get("title")])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("EMPLOYEE_ID must be an integer.")
        sys.exit(1)

    export_cvs(employee_id)
