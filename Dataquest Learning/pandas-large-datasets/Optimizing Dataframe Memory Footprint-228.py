## 2. Introduction ##

import pandas as pd
moma = pd.read_csv("moma.csv")
print(moma.info())

## 3. How Pandas Represents Values in a Dataframe ##

import pandas as pd
moma = pd.read_csv("moma.csv")
print(moma._data)

## 5. Different Types Have Different Memory Footprints ##

total_bytes = moma.size*8
total_megabytes = total_bytes/1048576
print(total_bytes)
print(total_megabytes)

## 7. Calculating the True Memory Footprint ##

obj_cols = moma.select_dtypes(include=['object'])
obj_cols_mem = obj_cols.memory_usage(deep=True)
print(obj_cols_mem)
obj_cols_sum = obj_cols_mem.sum()/1048576
print(obj_cols_sum)

## 9. Optimizing Integer Columns With Subtypes ##

import numpy as np
col_max = moma['ExhibitionSortOrder'].max()
col_min = moma['ExhibitionSortOrder'].min()

if col_max <  np.iinfo("int8").max and col_min > np.iinfo("int8").min:
    moma['ExhibitionSortOrder'] = moma['ExhibitionSortOrder'].astype("int8")
elif col_max <  np.iinfo("int16").max and col_min > np.iinfo("int16").min:
    moma['ExhibitionSortOrder'] = moma['ExhibitionSortOrder'].astype("int16")
elif col_max <  np.iinfo("int32").max and col_min > np.iinfo("int32").min:
    moma['ExhibitionSortOrder'] = moma['ExhibitionSortOrder'].astype("int32")
elif col_max <  np.iinfo("int64").max and col_min > np.iinfo("int64").min:
    moma['ExhibitionSortOrder'] = moma['ExhibitionSortOrder'].astype("int64")
print(moma['ExhibitionSortOrder'].dtype)
print(moma['ExhibitionSortOrder'].memory_usage(deep=True))

## 10. Optimizing Float Columns With Subtypes ##

moma = pd.read_csv("moma.csv")
moma['ExhibitionSortOrder'] = moma['ExhibitionSortOrder'].astype("int16")
float_cols = moma.select_dtypes(include=['float'])
print(float_cols.dtypes)
for col in float_cols.columns:
    moma[col] = pd.to_numeric(moma[col], downcast='float')
print(moma.select_dtypes(include=['float']).dtypes)

## 12. Converting To DateTime ##

moma["ExhibitionBeginDate"] = pd.to_datetime(moma["ExhibitionBeginDate"])
moma["ExhibitionEndDate"] = pd.to_datetime(moma["ExhibitionEndDate"])
print(moma[["ExhibitionBeginDate", "ExhibitionEndDate"]].memory_usage(deep=True))

## 14. Converting to Categorical to Save Memory ##

obj_cols = moma.select_dtypes(include=['object'])
for col in obj_cols.columns:
    num_unique_values = len(moma[col].unique())
    num_total_values = len(moma[col])
    if num_unique_values / num_total_values < 0.5:
        moma[col] = moma[col].astype('category')
        
print(moma.info(memory_usage='deep'))

## 15. Selecting Types While Reading the Data In ##

keep_cols = ['ExhibitionID', 'ExhibitionNumber', 'ExhibitionBeginDate', 'ExhibitionEndDate', 'ExhibitionSortOrder', 'ExhibitionRole', 'ConstituentType', 'DisplayName', 'Institution', 'Nationality', 'Gender']
moma = pd.read_csv("moma.csv", parse_dates=["ExhibitionBeginDate", "ExhibitionEndDate"], usecols=keep_cols)
print(moma.memory_usage(deep=True).sum()/(1024*1024))