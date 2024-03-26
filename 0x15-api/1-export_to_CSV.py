#!/usr/bin/python3
"""script to export data in the CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    USER = requests.get(URL + "users/{}".format(user_id)).json()
    user_id = sys.argv[1]
    username = USER.get("username")
    TODOS = requests.get(URL + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, n.get("completed"), n.get("title")]
         ) for n in TODOS]
