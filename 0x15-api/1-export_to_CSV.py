#!/usr/bin/python3
import requests
import csv
import sys

def get_user_info(user_id):
    """Gets user info"""
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(user_url)
    user_data = response.json()
    return user_data['username']


def get_employee_todo_progress(employee_id):
    """gets employee todo progress"""
    # API endpoint
    api_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    try:
        """Fetch data from the API"""
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad requests

        """Parse the JSON response"""
        todos = response.json()

        """Extract employee name"""
        employee_name = get_user_info(employee_id)

        """Count completed and total tasks"""
        done_tasks = sum(1 for todo in todos if todo['completed'])
        total_tasks = len(todos)

        """Display progress information"""
        print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
        print(f"{employee_name}:", done_tasks, total_tasks)

        """Display titles of completed tasks"""
        for todo in todos:
            if todo['completed']:
                print(f"\t{todo['title']}")

        """Export data to CSV"""
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for todo in todos:
                csv_writer.writerow([employee_id, employee_name, todo['completed'], todo['title']])

        print(f"\nData exported to {csv_filename}")

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
