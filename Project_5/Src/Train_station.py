# -*- coding: utf-8 -*-
"""
Created on Sat May 20 22:58:57 2023

@author: upon
"""
import folium
import csv
from folium.plugins import MarkerCluster

# 開啟 CSV 檔案
with open('../Data/Train_Station.csv',encoding='utf-8') as csvfile:

# 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    lng_lat = []
    station_name = []
    station_code = []
    
# 以迴圈輸出每一列
    for i,row in enumerate(rows):
        if i != 0:
            #print(row[2])
            station_name.append(row[2])
            station_code.append(row[0])
            lng_lat.append(row[8].split(" "))
    Eqk_map = folium.Map(location=[30, 15], zoom_start=2, tites='OpenStreetMap') #建立新地圖
    m = folium.Map(location=[25.13411,121.73997], zoom_start=15)             

    for row in range(242):
        station_code[row] = float(station_code[row])
        if station_code[row] >= 900 and station_code[row] <= 1250:
            folium.Marker(location=[float(lng_lat[row][0]), float(lng_lat[row][1])],popup=station_name[row], icon=folium.Icon(color='green',icon='cloud')).add_to(m)
        elif station_code[row] >= 2110 and station_code[row] <= 2260:
            folium.Marker(location=[float(lng_lat[row][0]), float(lng_lat[row][1])],popup=station_name[row], icon=folium.Icon(color='red',icon='cloud')).add_to(m)
        elif station_code[row] >= 3140 and station_code[row] <= 3350:
            folium.Marker(location=[float(lng_lat[row][0]), float(lng_lat[row][1])],popup=station_name[row], icon=folium.Icon(color='gray',icon='cloud')).add_to(m)
        elif station_code[row] >= 3360 and station_code[row] <= 4400:
            folium.Marker(location=[float(lng_lat[row][0]), float(lng_lat[row][1])],popup=station_name[row], icon=folium.Icon(color='purple',icon='cloud')).add_to(m)
        elif station_code[row] >= 4410 and station_code[row] <= 5120 or station_code[row]==5999:
            folium.Marker(location=[float(lng_lat[row][0]), float(lng_lat[row][1])],popup=station_name[row], icon=folium.Icon(color='orange',icon='cloud')).add_to(m)
        elif station_code[row] >= 5130 and station_code[row] <= 6000:
            folium.Marker(location=[float(lng_lat[row][0]), float(lng_lat[row][1])],popup=station_name[row], icon=folium.Icon(color='black',icon='cloud')).add_to(m)
        elif station_code[row] >= 7120 and station_code[row] <= 7390:
            folium.Marker(location=[float(lng_lat[row][0]), float(lng_lat[row][1])],popup=station_name[row], icon=folium.Icon(color='beige',icon='cloud')).add_to(m)
        elif station_code[row] >= 7000 and station_code[row] <= 7110:
            folium.Marker(location=[float(lng_lat[row][0]), float(lng_lat[row][1])],popup=station_name[row], icon=folium.Icon(color='lightgreen',icon='cloud')).add_to(m)
        elif station_code[row] >= 6000 and station_code[row] <= 6250:
            folium.Marker(location=[float(lng_lat[row][0]), float(lng_lat[row][1])],popup=station_name[row], icon=folium.Icon(color='lightgray',icon='cloud')).add_to(m)
        else:
            folium.Marker(location=[float(lng_lat[row][0]), float(lng_lat[row][1])],popup=station_name[row], icon=folium.Icon(color='pink',icon='cloud')).add_to(m)    
m
