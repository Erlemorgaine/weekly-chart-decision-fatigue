import json
import os
import csv

with open('/Users/erlemorgainemonfils/Documents/datawrapper/weekly_charts/reddit_subreddit_groups.json', 'r') as f:
    subreddit_groups = json.load(f)

group_counts = {}

for group, subreddits in subreddit_groups.items():
    total_count = 0
    for subreddit in subreddits:

        subreddit_path = f'./subreddits/{subreddit}.json'
        if os.path.exists(subreddit_path):
            
            with open(subreddit_path, 'r') as subreddit_file:
                subreddit_data = json.load(subreddit_file)
                # data.children contain the posts
                total_count += len(subreddit_data.get('data', {}).get('children', []))
    
    group_counts[group] = total_count

# Save the result to a CSV file
csv_path = './csv-data/grouped-post-data.csv'
os.makedirs(os.path.dirname(csv_path), exist_ok=True)
with open(csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Category', '# posts', '# subreddits'])
    for group, count in group_counts.items():
        writer.writerow([group, count, len(subreddit_groups[group])])