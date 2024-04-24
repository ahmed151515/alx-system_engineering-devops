#!/usr/bin/python3
"""
solve task
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + f"/users/{sys.argv[1]}").json()
    todo = requests.get(url + f"/todos", params={"userId": sys.argv[1]}).json()
    with open(f"{user.get('id')}.cvs", 'w') as f:
        for i in todo:
            f.write(f"\"{user.get('id')}\",\"{user.get('username')}\"\
,\"{i.get('completed')}\",\"{i.get('title')}\"\n")
