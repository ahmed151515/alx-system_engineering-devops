#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
    """
from requests import get


def number_of_subscribers(subreddit):

    headers = {'User-agent': 'your bot 0.1'}

    res = get(
        f"https://www.reddit.com/r/{subreddit}/about.json", headers=headers)
    if res.status_code == 200:
        res = res.json()
        return res["data"]["subscribers"]
    else:
        return 0
