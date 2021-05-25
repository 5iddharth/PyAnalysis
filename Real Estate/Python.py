import pandas as pd
import numpy as np 
from pandas_profiling import ProfileReport, profile_report
import matplotlib.pyplot


csv = pd.read_csv("USA.csv")
df = pd.DataFrame(csv)
df.columns = ['Country Name', 'Country Code', 'Series Name', 'Series Code',
       '1990', '2000', '2011', '2012',
       '2013', '2014', '2015', '2016',
       '2017', '2018', '2019', '2020']
df.head().columns

df.iloc[[55,56,57]]
df.drop([55,56,57], inplace=True)

df.index
df.reset_index(drop=True,inplace=True)

df.iloc[[55,56]]
df.drop([55,56], inplace=True)

df.isnull().sum()
df.duplicated().sum()

df.replace('..',0)
df.drop(['2020'], axis=1, inplace=True)

profile = profile_report(df)
profile.to_file(output = "file.html")