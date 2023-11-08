#!/usr/bin/python3
"""
0-subs
"""
import requests

def number_of_subscribers(subreddit, user_agent="my_user_agent"):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': user_agent}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    data = response.json()
    subscribers = data['data']['subscribers']
    return subscribers

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)


