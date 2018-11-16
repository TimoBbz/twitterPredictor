import urllib.parse
import tweepy.error

from twitter_collect import twitter_connection_setup as tcs


'''def get_replies_to_candidate(num_candidate):
    connexion = tcs.twitter_setup()
    tweets=[connexion.get_status(1062841607387598848)]
#    tweets= connexion.user_timeline(id = num_candidate, count = 200)
    user = num_candidate
    result=[]
    for tweet in tweets:
        tweet_id = tweet.id
        print(tweet.text)
        q = urllib.parse.urlencode({"q": "to:%s" % user})
        print(q)
        try:
            replies = connexion.direct_messages(q, since_id=tweet_id,count=10)
            print(replies)
        except tweepy.error.TweepError as e:
            print("twitter api error: %s", e)
            continue
        for reply in replies:
            if reply.in_reply_to_status_id == tweet_id:
                result.append([tweet.id,reply])
    return result'''

def get_retweets_of_candidate(num_candidate):
    connexion = tcs.twitter_setup()
    statuses = connexion.user_timeline(id = num_candidate, count = 200)
    result=[]
    for status in statuses:
        print(status.text)
        print(status.retweet_count)
        result.append([status.id,status.retweet_count])
#        Inutile de récupérer le texte car il n'y a rien de plus que le tweet initial
#        for retweet in status.retweets():
#           print(retweet.text.replace(status.text,''))
    return result
