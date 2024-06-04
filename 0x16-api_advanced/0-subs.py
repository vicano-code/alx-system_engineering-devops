#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
not active users, total subscribers for a given subreddit
If not a valid subreddit, return 0.
Usage >> python3 0-main.py programming
"""
import requests


def number_of_subscribers(subreddit):
    """returns number of subscribers for a given subreddit"""
    headers = {'User-Agent': 'My Custom Agent'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        r = response.json()
        return r['data']['subscribers']
    else:
        return 0
