import pandas as pd
df = pd.read_csv("content/oye.csv")
date=input("enter date - dd/mm/yyyy")
df[date]='A'
df.to_csv("content/oye.csv" , index=False)


