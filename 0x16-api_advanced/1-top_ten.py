#!/usr/bin/python3
"""
queries Reddit API for titles of top 10 hot posts for a given subreddit
"""
import json
import requests


def top_ten(subreddit):
    """prints titles of the first 10 hot posts for a subreddit"""
    headers = {'User-Agent': 'My Custom Agent'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, params={"limit": 10})
    if response.status_code == 200:
        r = json.loads(response.text)
        for d in r.get('data').get('children'):
            title = d.get('data').get('title')
            print(title)
    else:
        print(None)
