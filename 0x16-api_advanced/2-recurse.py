#!/usr/bin/python3
"""
a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should
return none.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """ list of titles of hot articles """
    base_url = 'https://www.reddit.com'
    api_uri = '{base}/r/{subreddit}/hot.json'.format(base=base_url,
                                                     subreddit=subreddit)

    user_agent = {'User-Agent': 'Python/requests'}
    payload = {'after': after, 'limit': '100'}
    response = requests.get(api_uri, headers=user_agent,
                            params=payload, allow_redirects=False)

    if response.status_code == 200:
        res = response.json()
        hot_posts = res.get('data').get('children')
        after = res.get('data').get('after')

        for post in hot_posts:
            hot_list.append(post.get('data').get('title'))

        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list

    return None
