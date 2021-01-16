import pandas as pd
from fuzzywuzzy import process

# STRING_1 = 'Green Hills Mortuary & Memorial Chapel'
# STRING_2 = 'Green, J C, & Sons Funeral Home'

# Ratio = fuzz.ratio(STRING_1.lower(), STRING_2.lower())

# Partial_Ratio = fuzz.partial_ratio(STRING_1.lower(), STRING_2.lower())

# Token_Sort_Ratio = fuzz.token_sort_ratio(STRING_1, STRING_2)

# Token_Set_Ratio = fuzz.token_set_ratio(STRING_1,STRING_2)

# print('Ratio: ', Ratio)
# print('Partial Ratio: ', Partial_Ratio)
# print('Token Sort Ratio: ', Token_Sort_Ratio)
# print('Token Set Ratio: ', Token_Set_Ratio)
fuzz1 = open('fuzz1.csv', 'r')
fuzz2 = open('fuzz2.csv', 'r')
df1 = pd.DataFrame(fuzz1)
df2 = pd.DataFrame(fuzz2)
df1['key'] = df1.sum(1)
df2['key'] = df2.sum(1)

for x in df2['key']:
    w = process.extract(x, df2.key.tolist(), limit=1)
# def yoursource(x):
#     if [process.extract(x, df2.key.tolist(), limit=1)][0][0][1] > 80:
#         return [process.extract(x, df2.key.tolist(), limit=1)][0]
#     else:
#         return 'no match'

# df1['key'] = df1.key.apply(yoursource)

# df = df1.merge(df2, on='key', how='inner').drop('key', 1)
print(w)
