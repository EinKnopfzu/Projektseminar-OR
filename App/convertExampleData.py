# -*- coding: utf-8 -*-
import csv
import numpy as np
import pandas as pd


df = pd.DataFrame()

# convert example data into dataframe
with open('Beispieldaten.csv', newline='\n', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        df.at[row[0], row[1]] = row[2]

# set index name
df.index.name = 'ID' 
# change order of some columns
col_order = ['TitlePlain', 'TitleShop', 'TitleAmazon', 'TitleLimango', 'TitleEbay', 'EbayTitleDeluxe', 'DescriptionLongMarketplaces', 'DescriptionLongShops']
for id, col in enumerate(col_order):
    df.insert(id, col, df.pop(col))
print(df)

#export dataframe to csv
df.to_csv('Beispieldaten_convertiert.csv', sep=',', encoding='utf-8')