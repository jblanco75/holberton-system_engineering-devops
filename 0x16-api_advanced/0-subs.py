#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    rqst = requests.get(url, headers={'user-agent': 'jb75'},
                        allow_redirects=False)
    if rqst.status_code == 200:
        subscribers = rqst.json().get("data").get("subscribers")
        return subscribers
    return (0)
