#!/usr/bin/python3
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursive function that queries the Reddit API, parses
    the title of the hot articles, and prints a sorted count
    of given keywords"""

    if counts is None:
        counts = {}
    if after is None:
        after = ''

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
               'AppleWebKit/537.36 (KHTML, like Gecko)'
               'Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title.split():
                        if word.lower() in counts:
                            counts[word.lower()] += 1
                        else:
                            counts[word.lower()] = 1
            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, after, counts)
            else:
                sorted_counts = sorted(counts.items(),
                                       key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
                return
        else:
            # Subreddit exists but no posts found
            return
    elif response.status_code == 404:
        # Subreddit not found
        return
    else:
        # Some other error occurred
        return
