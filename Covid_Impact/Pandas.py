import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv("Covid-19 economy impact .csv")

profile = ProfileReport(df)
profile.to_file(output_file="html_file_report.html")
