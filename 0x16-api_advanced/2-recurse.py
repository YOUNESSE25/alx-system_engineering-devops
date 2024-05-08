#!/usr/bin/python3
'''function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit'''
from requests import get
from sys import argv


def recurse(subreddit, hot_list=[]):
    '''function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit'''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 100}
    headers = {'User-Agent': 'jomojay-app1'}
    if isinstance(after, str):
        if after != "DONE":
            params['after'] = after
        else:
            return hot_list
    rest = get(url, headers=headers, params=params, allow_redirects=False)
    if rest.status_code != 200:
        return None
    data = rest.json().get('data', {})
    after = data.get('after', 'DONE')
    if not after:
        after = "DONE"
    hot_list = hot_list + [itm.get('data', {}).get('title')
                           for itm in data.get('children', [])]
    return recurse(subreddit, hot_list)


if __name__ == "__main__":
    recurse(argv[1])

