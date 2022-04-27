#!/usr/bin/python3
"""Get number of subcribers from a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Number of subscribers if subreddit exists or 0."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Alx python3 1.0'})

    response = requests.get(url, headers=headers).json()

    subscribers = response.get('data', {}).get('subscribers')
    if subscribers:
        return subscribers
    return 0
