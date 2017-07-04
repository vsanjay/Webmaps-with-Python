#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 12:37:44 2017

@author: verdusanjay
"""

import folium as fol


map = fol.Map([23.5509,87.2904])

fg = fol.FeatureGroup()

fg.add_child(fol.Marker([23.5509,87.2904],popup = "NIT DURGAPUR",icon = fol.Icon(color = 'blue')))

map.add_child(fg)

map.save('pythonmap.html')