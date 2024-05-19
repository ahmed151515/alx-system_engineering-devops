#!/usr/bin/python3
"""_summary_
    """
from requests import get


def top_ten(subreddit):
    header = {'User-agent': 'My-User-Agent'}

    res = get(f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
              headers=header, allow_redirects=False)
    # return json.dumps(res, indent=4)
    if res.status_code >= 300:
        print('None')
    else:
        res = res.json()
        posts = res["data"]["children"]
        for i, p in enumerate(posts):
            if i == 0:
                continue
            print(p["data"]["title"])
