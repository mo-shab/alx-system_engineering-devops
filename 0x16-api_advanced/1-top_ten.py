#!/usr/bin/python3
"""Module that print the title of
the first 10 hot post"""

import requests


def top_ten(subreddit):
    """Function that print the hot 10 posts in a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'myApp/0.0.1'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)

    except requests.RequestException:
        return (None)
