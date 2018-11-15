import json


def store_tweets(tweets,filename):
     with open(filename,"w") as file:
        datas={}
        for tweet in tweets:
            datas["id"]=tweet.id
            datas["id"]["text"]=tweet.text
            datas["id"]["date"]=tweet.created_at
        json.dump(datas,file)
