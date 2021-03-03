#!/usr/bin/env python
# coding: utf-8

# In[1]:

# preprocess_data just needs the name of one DataFrame from the datasets
def preprocess_data( df ):
    # Imports
    import pandas as pd
    import matplotlib.pyplot as plt
    import os
    
    redund_dict = {} # key = column name, value = redundant data value
    data_list = []  # List to keep track of most important data stored in dataset

    # Try to identify the date column
    for col in df.columns:
        if col.lower().find('date') != -1:
            date_col = col
            df[date_col] = pd.to_datetime(df[date_col])#, format = '%Y/%m/%d')
    
    # Drop redundant columns and store redundant data more efficiently
    for col in df:
        # Identify columns with only one value repeated on every row
        value_counts = df[col].value_counts().count()
        # Reduce DataFrame if any columns contain only one value
        if value_counts == 1:
            k = col # keys
            v = df[col].value_counts().index[0] # values
            # Store redundant data in a dictionary
            redund_dict.update({k : v})
            # Drop redundant data columns
            df.drop(columns=[col], inplace = True)
        
        # Categorical data to groupby and explore
        elif value_counts <= 10:
            print(f'Group By: {col}')
            display(round(df.groupby([col]).describe(), 2))
            
        # Identify most important data stored in dataset
        else:
            data_list.append(col)
            #print()
            
    # Display returned objects      
    display(redund_dict)
    display(df)
    
    # Identify columns with many values observed
    for col in data_list:
        plt.figure()
        # Create visuals of data distributions
        if df[col].dtypes == '<M8[ns]': # 'datetime64[ns]': 
            df[col].value_counts().sort_index().plot(kind='hist');
        elif df[col].dtypes == 'object':
            df[col].value_counts().plot(kind='box');
        else:
            df[col].plot(kind='box');
            
            
        # Display "subplots"
        print()
        print(f'{col} Distribution:')
        plt.show()
        display(df[col].describe())
        
    return df, redund_dict

