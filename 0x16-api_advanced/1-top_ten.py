#!/usr/bin/python3
"""
Function that queries Reddit API and prints the title of the first
10 hot posts listed for a given  subreddit
"""

import requests


def top_ten(subreddit):
    """Top 10 func"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    param = {'limit': 10}
    rqst = requests.get(url, headers={'user-agent': 'jb75'},
                        allow_redirects=False, params=param)
    if rqst.status_code == 200:
        rqst = rqst.json()
        data = rqst.get('data')
        children = data.get('children')
        if data is not None and children is not None:
            for post in children:
                post_data = post.get('data')
                title = post_data.get('title')
                print(title)
    else:
        print('None')
