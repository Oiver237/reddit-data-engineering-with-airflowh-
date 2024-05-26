import pandas as pd
from utils.constants import CLIENT_ID, SECRET
from etls.reddit_etl import connect_reddit, transform_data, extract_posts, load_data_to_csv
from utils.constants import OUTPUT_PATH

def reddit_pipeline(file_name, subreddit, time_filter, limit):
    #connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'my_pipeline2 v0.1')
    #Extraction
    posts =  extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    #transformation
    post_df = transform_data(post_df)
    #loading to csv*
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(post_df, file_path)
    return file_path