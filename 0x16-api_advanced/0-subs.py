#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of subscribers
for a given subreddit. If an invalid subreddit is given, the function should
return 0
"""
import requests


def number_of_subscribers(subreddit):
    """ number of subscribers """
    base_url = 'https://www.reddit.com'
    api_uri = '{base}/r/{subreddit}/about.json'.format(base=base_url,
                                                       subreddit=subreddit)

    user_agent = {'User-Agent': 'Python/requests'}
    response = requests.get(api_uri, headers=user_agent, allow_redirects=False)

    if response.status_code in [302, 404]:
        return 0

    return response.json().get('data').get('subscribers')
