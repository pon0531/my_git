# -*- coding: utf-8 -*-
"""
Created on Sat May 20 22:58:57 2023

@author: upon
"""
import folium
import csv
import numpy as np

# 開啟 CSV 檔案
with open('../Data/HighWay_km.csv',encoding='utf-8') as csvfile:

# 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    lng_lat = []
    km_m = []

    for i,row in enumerate(rows):
        if i != 0:
            km_m.append(row[1])
            lng_lat.append(row[2].split(","))
            #float_lst = list(np.array(row[2].split(","), dtype = 'float'))

    m = folium.Map(location=[25.052928, 121.642517], zoom_start=8)             

    for row in range(3576):
        if (row % 50)==0:
            folium.Marker(location=[float(lng_lat[row][0]), float(lng_lat[row][1])],popup=km_m[row], icon=folium.Icon(color='blue')).add_to(m)
m
