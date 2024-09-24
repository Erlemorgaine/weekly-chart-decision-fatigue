import json
import requests
import time
import os

with open('./reddit_subreddit.json', 'r') as file:
    subreddits = json.load(file)

output_dir = './subreddits/v2/'
os.makedirs(output_dir, exist_ok=True)

for subreddit in subreddits:
    url = f'https://www.reddit.com/r/{subreddit}/search.json?q=%22decision_fatigue%22&restrict_sr=1&limit=100'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        output_path = os.path.join(output_dir, f'{subreddit}.json')
        with open(output_path, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print(f"Failed to fetch data for subreddit: {subreddit}, status code: {response.status_code}")
    
    # Wait for 3 seconds before making the next request
    time.sleep(3)