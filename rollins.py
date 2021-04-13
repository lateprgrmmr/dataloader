import glob
import pandas as pd


filepaths = []
for filepath in glob.iglob('/Users/kevinbratt/Downloads/RollinsExport/*'):
    filepaths.append(filepath)

case_data_files = []
for i in filepaths:
    for j in glob.iglob(i + '/Contracts/*At-Need Contract*.xlsx'):
        case_data_files.append(j)

# print(len(case_data_files))
df = pd.DataFrame()
# data1 = pd.read_excel(case_data_files[1], ['Vitals', 'FuneralHomeData'])
# data = pd.concat(data1, axis=1, ignore_index=False)
# df = df.append(data).fillna('')
for each in case_data_files:
    # data1 = pd.read_excel(each, ['Vitals', 'FuneralHomeData'])
    # data = pd.concat(data1, axis=1, ignore_index=False)
    data = pd.read_excel(each, 'Contract Merchandise')
    df = df.append(data).fillna('')
df.to_excel('RollinsAtNeedMerchandiseData.xlsx')
# print(df)
