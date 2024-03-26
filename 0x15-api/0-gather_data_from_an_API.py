#!/usr/bin/python3
"""script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress."""
import sys
import requests

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    USER = requests.get(URL + "users/{}".format(sys.argv[1])).json()
    TODOS = requests.get(URL + "todos", params={"userId": sys.argv[1]}).json()

    completed = [i.get("title") for i in TODOS if i.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        USER.get("name"), len(completed), len(TODOS)))
    [print("\t {}".format(n)) for n in completed]
