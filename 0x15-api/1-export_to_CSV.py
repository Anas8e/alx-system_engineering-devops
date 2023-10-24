#!/usr/bin/python3
"""
Export employee's TODO list data to CSV format.
"""

import requests
import sys
import csv

def export_todo_list_to_csv(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch user information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    
    if "id" not in user_data:
        print(f"User with ID {employee_id} not found")
        return
    
    user_id = user_data["id"]
    username = user_data["username"]
    
    # Fetch user's TODO list
    todo_response = requests.get(f"{base_url}/todos", params={"userId": user_id})
    todo_data = todo_response.json()
    
    if not todo_data:
        print(f"No TODO list data found for user {username}")
        return
    
    # Define the CSV file name
    filename = f"{user_id}.csv"
    
    # Export TODO list data to CSV
    with open(filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        
        # Write the header row
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        # Write each TODO item to the CSV
        for todo in todo_data:
            task_completed_status = "True" if todo["completed"] else "False"
            task_title = todo["title"]
            csv_writer.writerow([user_id, username, task_completed_status, task_title])
    
    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    export_todo_list_to_csv(employee_id)
