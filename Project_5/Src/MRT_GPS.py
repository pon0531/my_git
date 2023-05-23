# -*- coding: utf-8 -*-
"""
Created on Sat May 20 22:58:57 2023

@author: upon
"""
import folium
import csv
from folium.plugins import MarkerCluster

# 開啟 CSV 檔案
with open('../Data/MRT_GPS.csv',encoding='big5') as csvfile:

    rows = csv.reader(csvfile)

    exit_name = []
    mrt_lti = []
    mrt_lng = []

    for i,row in enumerate(rows):
        if i != 0:
            exit_name.append(row[1])
            mrt_lti.append(row[4])
            mrt_lng.append(row[3])

 
    s = folium.Map(location=[float(mrt_lti[0]), float(mrt_lng[0])], zoom_start=15)         
    m = MarkerCluster().add_to(s)
    for row in range(len(mrt_lti)):
        #print(row)
        folium.Marker(location=[float(mrt_lti[row]), float(mrt_lng[row])],popup=exit_name[row], icon=folium.Icon(color='green',icon='cloud')).add_to(m)
s