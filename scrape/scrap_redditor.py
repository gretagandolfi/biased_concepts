import praw
import pandas as pd
import time
import pickle
import re

reddit = praw.Reddit(client_id='lzOo_k4qtUITUA', client_secret='4YYaofL7Jm5CXeaqWuYlGPvwUkQ', user_agent='greta')

# submissions
topics_dict = {"title":[],
                "text":[]}

for x in reddit.redditor('name_of_moderator').new(limit=None):
    if 'Submission' in str(type(x)):
        topics_dict["title"].append(x.title)
        topics_dict["text"].append(x.selftext)

topics_data = pd.DataFrame(topics_dict)
topics_data.to_csv('name_of_moderator.csv')

# comments
topics_dict = {"body":[],
                "sub":[]}

for x in reddit.redditor('name_of_moderator').comments.new(limit=None):
        topics_dict["body"].append(x.body)
        topics_dict["sub"].append(x.submission)

topics_data = pd.DataFrame(topics_dict)

topics_data.to_csv('name_of_moderator_comm.csv')
