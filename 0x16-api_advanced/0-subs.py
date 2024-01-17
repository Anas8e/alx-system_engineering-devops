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
        return "KO"
    
    results = response.json().get("data")
    return "OK" if results.get("subscribers") else "KO"


# Exemple d'utilisation :
print(number_of_subscribers("existing_subreddit"))  # Output attendu: "OK"
print(number_of_subscribers("nonexisting_subreddit"))  # Output attendu: "KO"
