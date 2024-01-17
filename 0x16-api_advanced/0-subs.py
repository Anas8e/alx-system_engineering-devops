#!/usr/bin/python3
"""
Function to query subscribers on a given Reddit subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.

    Args:
        subreddit (str): The subreddit name.

    Returns:
        int: Number of subscribers, or 0 if invalid subreddit.
    """
    # URL for the Reddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Custom User-Agent header to avoid Too Many Requests errors
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    
    # Make the API request with no following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code == 200:
        # Parse JSON response and return the number of subscribers
        return response.json().get("data", {}).get("subscribers", 0)
    else:
        # Invalid subreddit or other error, return 0
        return 0
