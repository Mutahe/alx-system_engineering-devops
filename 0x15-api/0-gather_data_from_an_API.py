#!/usr/bin/python3
"""
This script retrieves data of an employee through an API and displays
the employee's TODO list progress.

Usage:
    python3 script_name.py employee_id

Arguments:
    employee_id: The ID of the employee whose data needs to be fetched.

Output Format:
    First line: Employee EMPLOYEE_NAME is done with tasks (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        - EMPLOYEE_NAME: name of the employee
        - NUMBER_OF_DONE_TASKS: number of completed tasks
        - TOTAL_NUMBER_OF_TASKS: total number of tasks,
          which is the sum of completed and non-completed tasks
    Second and subsequent lines display the title of completed tasks,
    each prefixed by a tabulation and a space.

Example:
    python3 script_name.py 2
    Employee Ervin Howell is done with tasks (8/20):
        - distinctio vitae autem nihil ut molestias quo
        - voluptas quo tenetur perspiciatis explicabo natus
        - aliquam aut quasi
        - veritatis pariatur delectus
        - nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
        - repellendus veritatis molestias dicta incidunt
        - excepturi deleniti adipisci voluptatem et neque optio illum ad
        - totam atque quo nesciunt
"""

import requests
import sys

if __name__ == "__main__":
    # The URL of the API
    The_API = "https://jsonplaceholder.typicode.com/"

    # Extract the employee id from the command line argument
    employee_id = sys.argv[1]

    # Retrieve user data
    user_response = requests.get(The_API + "users/{}".format(employee_id))
    user = user_response.json()
    username = user.get("name")

    # Retrieve todo list for a specific employee
    params = {"userId": employee_id}
    todos_response = requests.get(The_API + "todos", params=params)
    todos = todos_response.json()

    # Count the number of completed tasks
    num_completed_tasks = sum(1 for todo in todos if todo.get("completed"))

    # Total number of tasks
    total_tasks = len(todos)

    # Output progress
    print("Employee {} is done with tasks ({}/{})".format(username, num_completed_tasks, total_tasks))

    # Output completed tasks
    for todo in todos:
        if todo.get("completed"):
            print("\t{}".format(todo.get("title")))
