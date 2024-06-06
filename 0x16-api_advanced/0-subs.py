#!/usr/bin/python3
"""
Query Reddit API for the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """returns number of subscribers for a given subreddit"""
    headers = {'User-Agent': 'CustomAgent1.0 by u/vic-ano'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        r = response.json()
        return r['data']['subscribers']
    else:
        return 0
