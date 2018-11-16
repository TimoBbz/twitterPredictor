import pytest
from twitter_collect import *
from twitter_analysis import dataframe_setup as ds


def test_collect():
    filename=""
    tweets = ds.get_tweets(filename)
    data =  ds.set_dataframe(tweets)
    assert 'tweet_textual_content' in data.columns

