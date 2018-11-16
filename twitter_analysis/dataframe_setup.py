import pandas
import json
from twitter_analysis import opinion_tweets as ot


def set_dataframe(filename):
    #tweets is a json object containing all tweets about a candidate
    tweets=[]
    with open(filename,"r",encoding="utf-8") as fichier:
        tweets = json.load(fichier)
    df2 = pandas.DataFrame(tweets)
    df2 = df2.transpose()
    #ajout de la ligne de polarité
    polarity = [ot.textblob_analysis(tweet) for tweet in df2["text"]]
    df2["polarity"] = pandas.Series(polarity, index=df2.index)
    print(df2)
