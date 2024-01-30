import requests
import json

def get_all_employees_todo():
    # API endpoint for all todos
    api_url = 'https://jsonplaceholder.typicode.com/todos'

    try:
        # Fetch data from the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad requests

        # Parse the JSON response
        todos = response.json()

        # Organize data by user ID
        data_by_user = {}
        for todo in todos:
            user_id = todo['userId']
            if user_id not in data_by_user:
                data_by_user[user_id] = []

            data_by_user[user_id].append({
                "username": todo['username'],
                "task": todo['title'],
                "completed": todo['completed']
            })

        # Export data to JSON
        json_data = {}
        for user_id, user_data in data_by_user.items():
            json_data[user_id] = user_data

        json_filename = 'todo_all_employees.json'
        with open(json_filename, 'w') as json_file:
            json.dump(json_data, json_file, indent=2)

        print(f"Data exported to {json_filename}")

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")

if __name__ == "__main__":
    get_all_employees_todo()
