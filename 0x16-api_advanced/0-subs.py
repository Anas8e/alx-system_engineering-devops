#!/usr/bin/python3
"""Module for task 0"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'linux:0x16.api.adbanced:v1.0.0 (by /u/Anas8e)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0

    results = response.json().get("data")
    return results.get("subscribers")
