#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests

import requests

def count_words(subreddit, word_list, results=None):
    """Prints counts of given words found in hot posts of a given subreddit.
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    if results is None:
        results = {}

    if not word_list:
        results = {k.lower(): v for k, v in results.items()}
        sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_results:
            print(f"{word}: {count}")
        return

    word = word_list.pop(0)
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my_user_agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        count = 0
        for post in posts:
            title = post['data']['title'].lower()
            words = title.split()
            count += words.count(word)
        if count > 0:
            if word in results:
                results[word] += count
            else:
                results[word] = count

    count_words(subreddit, word_list, results)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
