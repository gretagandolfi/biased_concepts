import praw
import pandas as pd
import time
import pickle
import re

reddit = praw.Reddit(client_id='lzOo_k4qtUITUA', client_secret='4YYaofL7Jm5CXeaqWuYlGPvwUkQ', user_agent='greta')

topics_dict = { "title":[],
                "score":[], 
                "id":[], "url":[], 
                "comms_num": [], 
                "created": [], 
                "body":[]}

subreddit = reddit.subreddit('name of the subreddit')

top_subreddit = subreddit.top(limit = None)

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)

topics_data.to_csv('name of the subreddit.csv')
