#!/usr/bin/python3
"""Contains the function number_of_subscribers."""


import requests


def number_of_subscribers(subreddit):
    """Number of subscribers for a given subreddit."""
    user = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0
