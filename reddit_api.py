import praw
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('REDDIT_USER_AGENT') 
username = os.getenv('REDDIT_USERNAME')
password = os.getenv('REDDIT_PASSWORD')

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username,
                     password=password)



subreddit = reddit.subreddit('all') 
query = '"decision fatigue"'

posts = subreddit.search(query, limit=1000)

for submission in posts: 
    print(f"Title: {submission.title}")
    print(f"subreddit: {submission.subreddit}")

print(len(list(posts)))
 