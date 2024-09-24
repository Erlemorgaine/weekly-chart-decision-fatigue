import os
import json
from datetime import datetime
import csv

def format_subreddit_data(folder_path):
    all_contents = []
    posts_per_subreddit = {}
    
    print(f'Amount of subreddits: {len(os.listdir(folder_path))}')
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)

                posts = data['data']['children']

                for post in posts:
                    title = post['data']['title']
                    text = post['data']['selftext']
                    comments = post['data']['num_comments']
                    created_utc = post['data']['created_utc']
                    date = datetime.utcfromtimestamp(created_utc).strftime('%Y-%m-%d')
                    year = datetime.utcfromtimestamp(created_utc).strftime('%Y')

                    all_contents.append({'title': title, 
                                            # 'text': text,
                                            '# comments': comments,
                                            'date': date,
                                            'year': year,
                                            'created': created_utc})


                posts_per_subreddit[filename] = len(data['data']['children'])

    
    
    return all_contents, posts_per_subreddit

def save_to_json(data, output_file):
    with open(output_file, 'w') as file:
        if isinstance(data, list):
            keys = data[0].keys() if data else []
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        elif isinstance(data, dict):
            writer = csv.writer(file)
            writer.writerow(['Subreddit', '# posts'])
            
            for key, value in data.items():
                writer.writerow([key, value])

def main():
    folder_path = './subreddits'
    output_file_timeline = 'csv-data/timeline_data.csv'
    output_file_timeline_year = 'csv-data/timeline_posts_per_year.csv'
    output_file_columns = 'csv-data/bar_data.csv'
    
    all_contents, posts_per_subreddit = format_subreddit_data(folder_path)
    save_to_json(all_contents, output_file_timeline)
    save_to_json(posts_per_subreddit, output_file_columns)

    # Create a dictionary that counts the posts for each year, and save it as csv to output_file_timeline_year
    year_count = {}
    for post in all_contents:
        year = post['year']
        if year in year_count:
            year_count[year] += 1
        else:
            year_count[year] = 1

    save_to_json(year_count, output_file_timeline_year)


if __name__ == "__main__":
    main()