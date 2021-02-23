#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 14:10:13 2021

@author: siyuanzhang
"""
import pycountry
import pandas as pd
import geopandas as gpd
import geocoder
import re 
import mapclassify
country = []
import csv
regex = '^[A-Za-z_][A-Za-z0-9_]*'
data = pd.read_csv('filte_data.csv')

data = data.groupby('country').sum()



#data_transposed.plot(y = ['Arizona'], use_index=True)


world = gpd.read_file(r'country.shp')

world.replace('Brazil','Brasil',inplace = True)
world.replace('Italy','Italia',inplace = True)




merge = world.join(data,on ='name', how = 'right' )

ax = merge.plot(column='agreg',
                cmap = 'OrRd',
                figsize=(10,5),
                legend=True,
                edgecolor = 'black',
                linewidth =0.4
                )






'''
for user_location,row in data.iterrows():
           
        g = geocoder.osm(user_location)
        
        if g==None:
           
            continue
        elif g.json ==None:
           
            continue
        else:
            x = g.json['lat'], g.json['lng']
            g = geocoder.osm(x, method='reverse')
            if g.json['country'] != None:
                print (g.json['country'])
               
                country.append([g.json['country']])
                

file = open('filted.csv','w+',newline='')
with file:
    write = csv.writer(file)
    write.writerows(country)

'''




