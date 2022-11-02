#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ top ten post """
    base_url = 'https://www.reddit.com'
    api_uri = '{base}/r/{subreddit}/hot.json'.format(base=base_url,
                                                     subreddit=subreddit)

    user_agent = {'User-Agent': 'Python/requests'}
    payload = {'limit': '10'}
    response = requests.get(api_uri, headers=user_agent,
                            params=payload, allow_redirects=False)

    if response.status_code in [302, 404]:
        print('None')

    else:
        res_json = response.json()

         if res_json.get('data') and res_json.get('data').get('children'):
             hot_posts = res_json.get('data').get('children')

             for post in hot_posts:
                 if post.get('data') and post.get('data').get('title'):
                     print(post.get('data').get('title'))
