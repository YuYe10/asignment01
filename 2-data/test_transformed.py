import pandas as pd  

df = pd.read_csv('transformed.csv.gz', compression='gzip')  
print(df.head())  