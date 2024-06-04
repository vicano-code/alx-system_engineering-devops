#!/usr/bin/python3
"""
A Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, return None
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Return titles of all hot articles for a given subreddit or None"""
    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        for d in response.json().get('data').get('children'):
            title = d.get('data').get('title')
            hot_list.append(title)

            after = response.json().get('data').get('after')

            if after is None:
                return hot_list
            else:
                recurse(subreddit, hotlist, after)
    else:
        return None
