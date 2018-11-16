import seaborn
import matplotlib.pyplot as plt
import pandas
from twitter_analysis import dataframe_setup as ds


def display(ids):
    n=len(ids)
    filename="../CandidateData/collected_tweet_"+str(ids[0])+".json"
    datas= ds.set_dataframe(filename)
    dateindex=pandas.DatetimeIndex(start="2018-11-05",periods=1,end="2018-11-16")
    total=pandas.DataFrame(index=dateindex)
    for id in ids:
        filename="../CandidateData/collected_tweet_"+str(id)+".json"
        datas= ds.set_dataframe(filename)
        datas_sorted=datas.groupby('date').mean()
        #datas_sorted.name(str(id))
        print(datas_sorted["polarity"])
        total.append({id:datas_sorted["polarity"]},ignore_index=True)


    print(total)

    #seaborn.lineplot(x="date",y="polarity",data=total)

    plt.show()
