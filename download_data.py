import pandas as pd

url="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

cases=pd.read_csv(url)
cases=cases.drop(["Province/State","Lat","Long"],axis=1)
cases=cases.groupby("Country/Region").sum()

df=cases.T
df.columns.name=None
date=pd.date_range(start=df.index[0], end=df.index[-1])
df.index=date
df=df.reset_index()
a=list(df.columns)
a[0]="date"
df.columns=a
df.to_csv("new_datav2.csv")