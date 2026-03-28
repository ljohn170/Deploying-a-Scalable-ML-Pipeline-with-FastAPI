import pandas as pd

df = pd.read_csv("data/census.csv")

print(df.head())
print(df.columns)
print(df.shape)
print(df.dtypes)