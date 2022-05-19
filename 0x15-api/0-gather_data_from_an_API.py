#!/usr/bin/python3
"""
Module that contain a py script that using
REST API, for a given employee ID, returns
information about his/her /todos list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":

    cookies = {"sessioncookie": "1233456789"}
    user_r = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                          .format(argv[1])).json()

    all_r = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    total_task = 0
    done_task = 0
    tasks = []
    
    for i in all_r:
        if i["userId"] == user_r["id"]:
            total_task += 1
            if i["completed"] is True:
                tasks.append("\t" + i["title"])
                done_task += 1
    print("Employee {} id done with task({}/{}):"
          .format(user_r['name'], done_task, total_task))
    print('\n'.join(tasks))
