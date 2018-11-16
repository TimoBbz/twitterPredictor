import seaborn
import pandas

def display(datas):
    seaborn.lineplot(x="date",y="polarity",data=datas)
