#!/usr/bin/python3

"""
A script using RestAPI for a given employee ID
It returns information about his TODO list progress
"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    """gets employee todo progress"""
    # API endpoint
    api_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    try:
        # Fetch data from the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad requests

        # Parse the JSON response
        todos = response.json()

        # Extract employee name
        employee_name = todos[0]['username']

        # Count completed and total tasks
        done_tasks = sum(1 for todo in todos if todo['completed'])
        total_tasks = len(todos)

        # Display progress information
        print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
        print(f"{employee_name}:", done_tasks, total_tasks)

        # Display titles of completed tasks
        for todo in todos:
            if todo['completed']:
                print(f"\t{todo['title']}")

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
    print(todos)  # Add this line to print the entire todos dictionary
    employee_name = todos[0].get('username', 'DefaultName')
    employee_name = todos[0]['user']['username']
    if 'username' in todos[0]:
        employee_name = todos[0]['username']
    else:
        employee_name = 'DefaultName'
    if todos:
        employee_name = todos[0].get('username', 'DefaultName')
    else:
        employee_name = 'DefaultName'

