import pandas
import json

def get_tweets(filename):
    tweets=[]
    with open(filename,"r",encoding="utf-8") as fichier:
        tweets=json.loads(fichier)
    print(tweets)

def set_dataframe(tweets):
    '''tweets is a json object containing all tweets about a candidate'''

