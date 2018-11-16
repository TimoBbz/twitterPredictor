from twitter_collect import twitter_connection_setup as tcs


def collect(keyword):
    connexion = tcs.twitter_setup()
    return connexion.search(keyword,language="french")
