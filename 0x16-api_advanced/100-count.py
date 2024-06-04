#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """prints a sorted count of given keywords"""
    if not subreddit or not word_list or word_list == []:
        return
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom Agent"}
    params = {"limit": 100}

    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    word_list = [word.lower() for word in word_list]
    for d in data.get('data').get('children'):
        title = d.get('data').get('title').lower()
        for word in word_list:
            if word in title:
                counts[word] = counts.get(word, 0) + title.count(word)

    after = data['data']['after']
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        counts_sorted = sorted(counts.items(),
                               key=lambda x: (-x[1], x[0].lower()))
        for word, count in counts_sorted:
            print("{}:{}".format(word, count))
