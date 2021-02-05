import pandas as pd
from fuzzywuzzy import process

# STRING_1 = 'Cooley Tioga Point Cremation'
# STRING_2 = 'Cooley Tioga-Point Cremation And Burial Options, Inc.'

# Ratio = fuzz.ratio(STRING_1.lower(), STRING_2.lower())

# Partial_Ratio = fuzz.partial_ratio(STRING_1.lower(), STRING_2.lower())

# Token_Sort_Ratio = fuzz.token_sort_ratio(STRING_1, STRING_2)

# Token_Set_Ratio = fuzz.token_set_ratio(STRING_1,STRING_2)

# print('Ratio: ', Ratio)
# print('Partial Ratio: ', Partial_Ratio)
# print('Token Sort Ratio: ', Token_Sort_Ratio)
# print('Token Set Ratio: ', Token_Set_Ratio)
# a = open('fuzz3.csv')
# b = open('fuzz4.csv')
df2 = pd.read_csv('caskets_vendor.csv', encoding='utf-8')
df1 = pd.read_csv('casket_gather.csv', encoding='utf-8')

def fuzzy_merge(df_1, df_2, key1, key2, threshold=100, limit=1):
    """Fuzzy match some FH names"""

    s_list = df_2[key2].tolist()

    m_1 = df_1[key1].apply(lambda x: process.extract(x, s_list, limit=limit))
    df_1['matches'] = m_1

    m_2 = df_1['matches'].apply(lambda x: ', '.join([i[0] for i in x if i[1] >= threshold]))
    df_1['matches'] = m_2

    # print(df_1)
    return df_1.to_csv('casket_fuzz_out.csv')

fuzzy_merge(df1, df2, 'name','Description', threshold=90)
