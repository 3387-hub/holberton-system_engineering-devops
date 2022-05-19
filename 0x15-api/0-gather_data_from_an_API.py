#!/usr/bin/python3
import requests
from sys import argv


if __name__ == "__main__":

    cookies = {"sessioncookie": "1233456789"}
    user_r = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}").json()

    all_r = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    counter = 0
    num_task = 0
    tasks = []

    for i in all_r:
        if i["userId"] == user_r["id"]:
            tasks.append("\t" + i["title"])
            counter += 1
        num_task += 1
    print(f"Employee {user_r['name']} id done with task\
        ({counter}/{num_task}):")
    print('\n'.join(tasks))
