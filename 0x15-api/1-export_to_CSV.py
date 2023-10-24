#!/usr/bin/python3
"""
Check student .CSV output of user information
"""

import csv
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info(id):
    """ Check user information """

    # Retrieve user information
    response = requests.get(users_url + str(id))
    if response.status_code != 200:
        print("User ID and Username: API request failed")
        return

    user_data = response.json()
    if not user_data:
        print("User ID and Username: User not found")
        return

    username = user_data[0]['username']

    # Check if the CSV file exists
    try:
        with open(str(id) + ".csv", 'r') as f:
            csv_data = f.read()

        # Verify User ID and Username in the CSV data
        if str(id) in csv_data and username in csv_data:
            print("User ID and Username: OK")
        else:
            print("User ID or Username: Incorrect")
    except FileNotFoundError:
        print("User ID and Username: CSV file not found")


if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_info(int(sys.argv[1]))
