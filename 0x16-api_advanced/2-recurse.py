#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    """Recursive Top 10 func"""
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    rqst = requests.get(url, headers={'user-agent': 'jb75'},
                        allow_redirects=False)
    if rqst.status_code == 200:
        rqst = rqst.json()
        data = rqst.get('data')
        children = data.get('children')
        for post in children:
            post_data = post.get('data')
            title = post_data.get('title')
            hot_list.append(title)
        after = data.get('after')

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
