#!/usr/bin/python3
"""Script to gather employee TODO list progress from an API"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch user's TODO list
    todo_response = requests.get("{}/todos?userId={}".format(base_url, employee_id))
    todo_data = todo_response.json()

    completed_tasks = [task for task in todo_data if task.get("completed")]
    total_tasks = len(todo_data)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
