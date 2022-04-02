import pandas as pd
df = pd.read_csv("ca_covid.csv")
df['ratio'] = df['deaths'] / df['cases']
print(df.loc[df['ratio'] == df['ratio'].max()])
