#!/usr/bin/python3
"""Get top 10 posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Top 10 posts of a subreddit."""
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Alx python3 1.0'})

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    r = requests.get(url, headers=headers).json()
    top_ten = r.get('data', {}).get('children', [])
    if not top_ten:
        print(None)
    for t in top_ten:
        print(t.get('data').get('title'))
