#!/usr/bin/env python
# coding: utf-8

# In[9]:


# quick_explore just just needs the name of a directory with csv files
def quick_explore(folder = 'folder_name'):
    
    # Imports
    import pandas as pd
    import matplotlib.pyplot as plt
    import os
    from preprocessor import preprocess_data

    directory = '../../data/'+folder+'/'
    
    for filename in os.listdir(directory):

        filepath = os.path.join(directory, filename)
        
        # Read CSV files
        if filename.endswith('.csv'):
            raw_df = pd.read_csv(filepath, infer_datetime_format = True)
            neg_index = 4
            
        # Read Excel files
        elif filename.endswith('.xlsx'):
            raw_df = pd.read_excel(filepath, infer_datetime_format = True)
            neg_index = 5
            
        # Skip other file types
        else:
            continue

        print()
        print('--------------'*8)
        print('--------------'*8)
        print(filename[:-neg_index].upper())
        print()

        df, redund_dict = preprocess_data(raw_df)
    return 

