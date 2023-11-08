#!/usr/bin/python3
"""
0-subs
"""
import requests

def number_of_subscribers(subreddit):
    """
    Function to query the Reddit API and return the number of subscribers for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "my-app/0.0.1"}  # Set a custom User-Agent
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data.get("data", {}).get("subscribers", 0)
        return subscribers
    else:
        return 0

if __name__ == "__main__":
    subreddit = input("Enter a subreddit: ")
    num_subscribers = number_of_subscribers(subreddit)
    print(f"The number of subscribers in '{subreddit}' is: {num_subscribers}")
