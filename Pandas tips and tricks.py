# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:20:24 2020

@author: Nicholas Guthrie
Pandas tips and tricks - things I use constantly
"""

import pandas as pd


# using ranges with cut to count elements in intervals
ranges = [1, 5, 10]
df.groupby(pd.cut(df[columns], ranges)).count()

# when working with many columns, finding the column names can be
# challenging. Can search for column names as such
series = df[df.id_column == id_num]
namesearch = [col for col in series.columns if 'search_term' in col]