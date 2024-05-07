#!/usr/bin/python3
'''
    function that queries the Reddit API and returns the number
of subscribers for a given subreddit
'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
        number of subscribers
    '''
    Usr = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=Usr).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
