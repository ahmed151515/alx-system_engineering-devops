#!/usr/bin/python3
"""
solve task
"""

import requests
import sys

url = "https://jsonplaceholder.typicode.com"
user = requests.get(url + f"/users/{sys.argv[1]}").json()
todo = requests.get(url + f"/todos", params={"userId": sys.argv[1]}).json()

completed_todo = [i for i in todo if i.get('completed') is True]

print(
    f"Employee {user.get('name')} \
is done with tasks({len(completed_todo)}/{len(todo)}):")

for i in completed_todo:
    print(f"\t{i.get('title')}")
