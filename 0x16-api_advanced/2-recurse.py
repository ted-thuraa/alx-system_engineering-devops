#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.

Hint: The Reddit API uses pagination for separating pages of responses
"""
import requests

def recurse(subreddit, hot_list=[], afters=""):
	"""You may change the prototype, but it must be able to be called with just a subreddit supplied.
	"""
	url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit, afters)
	headers = {'User-Agent': 'MyAPI/0.1'}
	main = requests.get(url, headers=headers, allow_redirects=False)
	if (main.json().get('error') == 404):
		return None
	if (afters is not None):
		afters = main.json()['data']['after']
		for post in main.json()['data']['children']:
			hot_list.append(post['data']['title'])
		recurse(subreddit, hot_list, afters)
	return hot_list
