#!/usr/bin/python3
"""Contains recurse function"""
from requests import get


def recurse(subreddit, hot_list=[]):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'jomojay-app2'}
    params = {'limit': 100}
    if isinstance(after, str):
        if after != "DONE":
            params['after'] = after
        else:
            return hot_list
    res = get(url, headers=headers, params=params, allow_redirects=False)
    if res.status_code != 200:
        return None
    data = res.json().get('data', {})
    after = data.get('after', 'DONE')
    if not after:
        after = "DONE"
    hot_list = hot_list + [item.get('data', {}).get('title')
                           for item in data.get('children', [])]
    return recurse(subreddit, hot_list, after)
