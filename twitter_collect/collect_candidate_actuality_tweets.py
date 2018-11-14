def get_tweets_from_candidates_search_queries(queries, twitter_api):
    tweet_list = []
    for query in queries:
        tweets = twitter_api.search(query)
        for tweet in tweets:
            tweet_list.append(tweet.text)
    return tweet_list
