#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles."""
    if hot_list is None:
        hot_list = []

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
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            # Subreddit exists but no posts found
            return None
    elif response.status_code == 404:
        # Subreddit not found
        return None
    else:
        # Some other error occurred
        return None
