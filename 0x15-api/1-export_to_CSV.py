#!/usr/bin/python3
"""Python script to gather data from an API and export it to a CSV file"""

import requests
import sys
import csv

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    user_data = user_response.json()
    user_id = user_data.get("id")
    username = user_data.get("username")

    # Fetch user's TODO list
    todo_response = requests.get("{}/todos?userId={}".format(base_url, employee_id))
    todo_data = todo_response.json()

    # Prepare the CSV file
    filename = "{}.csv".format(user_id)
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for task in todo_data:
            completed_status = "True" if task.get("completed") else "False"
            task_title = task.get("title")

            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": completed_status,
                "TASK_TITLE": task_title
            })

    print("Data exported to {}".format(filename))
