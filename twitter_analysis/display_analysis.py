import seaborn
import pandas

def sort_by_date(datas):
    df=datas.groupby('date')
    print(df)

