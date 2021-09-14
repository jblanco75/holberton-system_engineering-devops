#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    e_id = argv[1]
    user = requests.get(url + 'users/' + e_id).json()
    tasks = requests.get(url + 'todos/', params={'userId': e_id}).json()
    username = user.get("username")

    with open("{}.csv".format(e_id), "w") as csvfile:
        f = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            f.writerow([e_id, username, task["completed"], task["title"]])
