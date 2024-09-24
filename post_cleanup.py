import os
import json

def load_json_files(folder_path):
    data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            with open(os.path.join(folder_path, filename), 'r') as file:
                content = json.load(file)
                if 'data' in content and 'children' in content['data']:
                    data.extend(content['data']['children'])
    return data

def filter_items(items, term):
    filtered_items = []
    for item in items:
        if 'title' in item['data'] and term in item['data']['title'].lower():
            filtered_items.append(item)
        elif 'selftext' in item['data'] and term in item['data']['selftext'].lower():
            filtered_items.append(item)
    return filtered_items

def filter_items_no_DF(items, term):
    filtered_items = []
    for item in items:
        if ('title' not in item['data'] or term not in item['data']['title'].lower()) and ('selftext' not in item['data'] or term not in item['data']['selftext'].lower()):
            filtered_items.append(item)
    return filtered_items

def map_items(items):
    mapped_items = []
    for item in items:
        mapped_item = {
            'title': item['data'].get('title', ''),
            'selftext': item['data'].get('selftext', ''),
            'subreddit': item['data'].get('subreddit', '')
        }
        mapped_items.append(mapped_item)
    return mapped_items

def save_to_json(data, output_path):
    with open(output_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    folder_path = 'subreddits'
    term = 'decision fatigue'
    output_path = 'no_DF_found.json'

    items = load_json_files(folder_path)
    print(f"Total items: {len(items)}")

    filtered_items = filter_items(items, term)
    print(f"Filtered items: {len(filtered_items)}")

    # no_df = filter_items_no_DF(items, term)
    # mapped_items = map_items(no_df)
    # save_to_json(mapped_items, output_path)
    # print(f"Filtered and mapped items saved to {output_path}")

if __name__ == "__main__":
    main()