#!/usr/bin/python3
'''
    function that queries the Reddit API and returns the number
    of subscribers for a given subreddit
'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''number of subscribers'''
    if subreddit is None:
        return 0
    if type(subreddit) is not str:
        return 0
    user = {'User-Agent': 'younesse'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user,
                       allow_redirects=False).json()
    sub = url.get("data", {}).get("subscribers", 0)
    return sub


if __name__ == "__main__":
    number_of_subscribers(argv[1])
