#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
    """
from requests import get


def number_of_subscribers(subreddit):

    header = {'User-agent': 'My-User-Agent'}

    res = get(
        f"https://www.reddit.com/r/{subreddit}/about.json"
        , headers=header, allow_redirects=False)
    if res.status_code < 300:
        res = res.json()
        return res["data"]["subscribers"]
    else:
        return 0
