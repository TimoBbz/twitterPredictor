import tweepy
from tweepy import StreamListener
from tweepy.streaming import StreamListener
from twitter_collect import twitter_connection_setup as tcs


def get_tweets_from_candidates_search_queries(queries, twitter_api):
    tweet_list = []
    for query in queries:
        tweets = twitter_api.search(query)
        for tweet in tweets:
            tweet_list.append(tweet.text)
    return tweet_list


class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True


def collect_by_streaming(num_candidate):
    connexion = tcs.twitter_setup()
    #création de l'instance de connexion
    listener = StdOutListener()

    stream = tweepy.Stream(auth=connexion.auth, listener=listener)
    stream.filter(follow=[num_candidate], track=["Emmanuel Macron"])
    stream.filter()


