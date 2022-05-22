#!/usr/bin/python3
"""
Module that contain function that
return the number of suscribers in
reddit (Total, non active).
"""
import requests


def number_of_subscribers(subreddit):
    req = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit), allow_redirects=False)
    print(req.status_code)
    if req.status_code == 200:
        return req.json().get('data').get('suscribers')
    else:
        return 0
