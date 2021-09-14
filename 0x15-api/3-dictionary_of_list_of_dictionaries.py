#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress"""

import json
import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/').json()
    j_dict = {}

    for employee in user:
        user_id = employee["id"]
        j_dict[user_id] = []
        tasks = requests.get(url + "todos/?userId={}".format(user_id)).json()
        for task in tasks:
            j_dict[user_id].append({"username": employee["username"],
                                    "task": task["title"],
                                    "completed": task["completed"]})

    with open("todo_all_employees.json", "w") as jsonfile:
        jsonfile.write((json.dumps(j_dict)))
