#!/usr/bin/python3
"""
solve task
"""

import requests
import sys
if __name__ == "__main__":
    #     url = "https://jsonplaceholder.typicode.com"
    #     user = requests.get(url + f"/users/{sys.argv[1]}").json()
    #     todo = requests.get(url + f"/todos", params={"userId": sys.argv[1]}).json()

    #     completed_todo = [i for i in todo if i.get('completed') is True]

    #     print(
    #         f"Employee {user.get('name')} \
    # is done with tasks({len(completed_todo)}/{len(todo)}):")

    #     for i in completed_todo:
    #         print(f"\t {i.get('title')}")
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = main_url + "/user/{}/todos".format(sys.argv[1])
    name_url = main_url + "/users/{}".format(sys.argv[1])
    todo_result = requests.get(todo_url).json()
    name_result = requests.get(name_url).json()

    todo_num = len(todo_result)
    todo_complete = len([todo for todo in todo_result
                         if todo.get("completed")])
    name = name_result.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, todo_complete, todo_num))
    for todo in todo_result:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
