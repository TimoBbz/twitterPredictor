from twitter_collect import twitter_connection_setup as tcs



def get_retweets_of_candidate(num_candidate):
    connexion = tcs.twitter_setup()
    statuses = connexion.user_timeline(id = num_candidate, count = 200)
    result=[]
    for status in statuses:
        print(status.text)
        print(status.retweet_count)
        result.append([status,status.retweet_count])
#        Inutile de récupérer le texte car il n'y a rien de plus que le tweet initial
#        for retweet in status.retweets():
#           print(retweet.text.replace(status.text,''))
    return result
