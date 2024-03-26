#!/usr/bin/python3
"""script to export data in the JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    USER = requests.get(URL + "users/{}".format(user_id)).json()
    user_id = sys.argv[1]
    username = USER.get("username")
    TODOS = requests.get(URL + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": n.get("title"),
                "completed": n.get("completed"),
                "username": username
            } for n in TODOS]}, jsonfile)
