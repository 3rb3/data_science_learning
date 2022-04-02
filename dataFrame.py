import pandas as pd
data = {
    'ages' : [15, 18, 23, 42],
    'heights' : [166, 180, 175, 184]
}
df = pd.DataFrame(data, index = ['James', 'abc', 'Amy', 'Dave'])
print(df)
print('----------------------')
print(df.loc['abc'])
print('----------------------')
print(df)
