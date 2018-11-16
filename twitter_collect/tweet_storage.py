import json
import unicodedata


def store_tweets(tweets,filename):
     with open(filename,"w") as file:
        datas={}
        for tweet in tweets:
            texte=str(unicodedata.normalize('NFD',tweet.text).encode('ascii','ignore').decode("utf-8"))
            datas[tweet.id]={"text":texte,"date":str(tweet.created_at).split(" ")[0]}
        json.dump(datas,file)
