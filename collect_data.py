# collect_data.py
# Starter code to collect Reddit posts using the Pushshift API
# DSA210 Fall 2025 Project - Sleep-Deprived Internet

import requests
import pandas as pd
from datetime import datetime

# Example: Collect 100 posts from r/AskReddit
url = "https://api.pushshift.io/reddit/search/submission/"
params = {
    "subreddit": "AskReddit",
    "size": 100,
    "sort": "desc",
    "sort_type": "created_utc"
}

response = requests.get(url, params=params)
data = response.json().get("data", [])

# Convert JSON to DataFrame
df = pd.DataFrame([{
    "title": post.get("title"),
    "created_utc": datetime.utcfromtimestamp(post.get("created_utc")),
    "score": post.get("score"),
    "num_comments": post.get("num_comments")
} for post in data])

print(df.head())
df.to_csv("sample_reddit_data.csv", index=False)
