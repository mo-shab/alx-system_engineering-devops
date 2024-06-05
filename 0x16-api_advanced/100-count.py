#!/usr/bin/python3
"""100-count"""


from collections import Counter
import re
import requests


def count_words(subreddit, word_list, word_counter=None, after=None):
    """Count words"""
    if word_counter is None:
        word_counter = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'myApp/0.0.1'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            normalized_word_list = set(word.lower() for word in word_list)

            for post in posts:
                title = post['data']['title']
                words_in_title = re.findall(r'\b\w+\b', title.lower())
                for word in words_in_title:
                    if word in normalized_word_list:
                        word_counter[word] += 1

            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, word_counter, after)
            else:
                if word_counter:
                    sorted_word_counts = sorted(word_counter.items(),
                                                key=lambda item: (-item[1],
                                                                  item[0]))
                    for word, count in sorted_word_counts:
                        print(f'{word}: {count}')
                return
        else:
            return
    except requests.RequestException:
        return
