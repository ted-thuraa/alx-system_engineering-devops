#!/usr/bin/python3
"""
 a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests

def top_ten(subreddit)
	""" does above. ensure no redirects """
	url =  'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
	request = requests.get(url, headers={'User-Agent': 'MyAPI/0.1'})
	if request.status_code != 200:
		print(None)
		return None
	request = request.json()
	if 'data' in request:
		for thread in request.get('data') .get('children'):
			print(thread.get('data').get('title'))
	else:
		print(None)
		return None
