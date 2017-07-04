#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 12:37:44 2017

@author: verdusanjay
"""

import folium as fol
import pandas as pd

airports_data = pd.read_csv("global_airports.csv")

latitude_list = list(airports_data["latitude"])

longitude_list = list(airports_data["longitude"])

name_list = list(airports_data["name"])

map = fol.Map([23.5509,87.2904])

fg = fol.FeatureGroup()

for x in range(0,len(latitude_list)):

    fg.add_child(fol.Marker([latitude_list[x],longitude_list[x]],popup = name_list[x],icon = fol.Icon(color = 'blue')))

map.add_child(fg)

map.save('pythonmap.html')