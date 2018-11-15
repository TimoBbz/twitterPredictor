import pandas
import json


def set_dataframe(filename):
    '''tweets is a json object containing all tweets about a candidate'''
    tweets=[]
    with open(filename,"r",encoding="utf-8") as fichier:
        tweets=json.load(fichier)
    df2=pandas.DataFrame(tweets)
    print(df2)
