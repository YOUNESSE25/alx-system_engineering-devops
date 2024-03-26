#!/usr/bin/python3
"""script to export data in the JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    users = requests.get(URL + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            m.get("id"): [{
                "task": n.get("title"),
                "completed": n.get("completed"),
                "username": m.get("username")
            } for n in requests.get(URL + "todos",
                                    params={"userId": m.get("id")}).json()]
            for m in users}, jsonfile)
