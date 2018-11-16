import seaborn
import pandas
from twitter_analysis import dataframe_setup as ds


def display(id1):
    filename1="CandidateData/collected_tweet_"+str(id1)+".json"
    datas1= ds.set_dataframe(filename1)
    seaborn.lineplot(x="date",y="polarity",data=datas1)
