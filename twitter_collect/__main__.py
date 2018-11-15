from twitter_collect import twitter_get as tg
from twitter_collect import tweet_storage as ts
from ast import literal_eval
import tweepy

with open("../CandidateData/candidates.txt") as candidates:
    names_str = candidates.read() # récupération des candidats dans la variable name
print(names_str)
names_dict = literal_eval(names_str)
for id in names_dict:
    tweet_global = tweepy.models.SearchResults()
    #récupération des tweets par mot-clé
    with open ("../CandidateData/keywords_candidate_" + str(id) + ".txt") as kw:
        kw_str = kw.read()
    kw_set = literal_eval(kw_str)
    for kw in kw_set:
        tweet_global += tg.collect(kw)
    #récupération des tweets par mot_dièse
    with open ("../CandidateData/hashtag_candidate_" + str(id) + ".txt") as ht:
        ht_str = ht.read()
    ht_set = literal_eval(ht_str)
    for ht in ht_set:
        tweet_global += tg.collect(ht)
    #stockage des tweets
    ts.store_tweets(tweet_global, "../CandidateData/collected_tweet_" + str(id) + ".txt")


