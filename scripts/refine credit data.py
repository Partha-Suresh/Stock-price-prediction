import pandas as pd

data = pd.read_csv('../data/Credit Score Classification/train.csv')

headers = data.columns.tolist()


NA_count = 0
for idx,row in data.iterrows():
    
    for header in headers:
        if(pd.isna(row[header])):
            NA_count += 1
            break


print(len(data))
print(NA_count)