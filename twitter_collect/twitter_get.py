from twitter_collect import twitter_connection_setup as tcs
import tweepy


def collect(keyword):
    connexion = tcs.twitter_setup()
    first_id = 1057640510356180992
    searches = tweepy.models.SearchResults()
    while True:
        new_searches = connexion.search(keyword, language="french", count=100, since_id=first_id)
        if len(new_searches) == 0 or len(searches) > 1000:
            break
        first_id = new_searches[-1].id
        searches += new_searches
    return searches
