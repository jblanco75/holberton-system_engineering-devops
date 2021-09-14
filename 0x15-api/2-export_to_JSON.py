#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    e_id = argv[1]
    user = requests.get(url + 'users/' + e_id).json()
    tasks = requests.get(url + 'todos/', params={'userId': e_id}).json()
    username = user.get("username")

    to_dict = []
    for task in tasks:
        to_dict.append({"task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": username})
    j_dict = {e_id: to_dict}

    with open('{}.json'.format(e_id), "w") as jsonfile:
        json.dump(j_dict, jsonfile)
