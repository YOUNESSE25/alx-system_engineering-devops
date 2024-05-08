#!/usr/bin/python3
''' function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit'''
import requests
from sys import argv


def top_ten(subreddit):
    '''function that queries the Reddit API and prints the titles
    of the first 10 '''
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "alx25"}
    response = requests.get(url, headers=headers,
                            params={"limit": 10}, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(i.get("data").get("title")) for i in results.get("children")]


if __name__ == "__main__":
    top_ten(argv[1])
