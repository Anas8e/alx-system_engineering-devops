#!/usr/bin/python3
"""Module for task 0"""


# Import necessary modules
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The subreddit name.

    Returns:
        int: Number of subscribers, or 0 if invalid subreddit.
    """
    # Set custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Make API request
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers)

    # Check if the subreddit is valid
    if response.status_code == 200:
        # Parse JSON response and return subscriber count
        return response.json()['data']['subscribers']
    else:
        return 0
