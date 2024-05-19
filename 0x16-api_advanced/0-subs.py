#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
    """
from requests import get


def number_of_subscribers(subreddit):

    headers = {'User-agent': 'My-User-Agent'}

    res = get(
        f"https://www.reddit.com/r/{subreddit}/about.json", headers=headers, allow_redirects=False)
    if res.status_code < 300:
        res = res.json()
        return res["data"]["subscribers"]
    else:
        return 0
