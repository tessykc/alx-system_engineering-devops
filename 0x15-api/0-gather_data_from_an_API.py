#!/usr/bin/python3

"""
A script using RestAPI for a given employee ID
It returns information about his TODO list progress
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """gets employee todo progress"""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()
        if user_response.status_code != 200:
            print(
                "Failed to fetch data. Please try again later.")
            return
        if todos_response.status_code != 200:
            print(
                "Failed to fetch data. Please try again later.")
            return

        employee_name = user_data['name']
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task['completed']]
        num_done_tasks = len(done_tasks)

        print(f"Employee {employee_name} is done with tasks"
              f"({num_done_tasks}/{total_tasks}):")
        print(f"{employee_name}: {num_done_tasks}/{total_tasks}")

        for task in done_tasks:
            print(f"\t{task['title']}")

    except requests.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
