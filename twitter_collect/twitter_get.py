from twitter_collect import twitter_connection_setup as tcs


def collect():
    connexion = tcs.twitter_setup()
    tweets = connexion.search("Emmanuel Macron",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)


def collect_by_user(user_id):
    connexion = tcs.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    for status in statuses:
        print(status.text)
    return
