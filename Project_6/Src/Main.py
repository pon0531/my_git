# -*- coding: utf-8 -*-
"""
Created on Sat May 20 22:58:57 2023

@author: upon
"""
import folium
import csv
from folium.plugins import MarkerCluster
from folium.plugins import HeatMap # 導入套件
# 開啟 CSV 檔案
with open('../Data/taiwan_20220101_20221125.csv',encoding='BIG5') as csvfile:

# 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    lti = []
    lng = []
    pop_up = []
    heatmap = [[0]*2 for i in range(600)]

    
# 以迴圈輸出每一列
    for i,row in enumerate(rows):
        if i != 0:
            #print(row[4])
            pop_up.append("規模:"+row[3]+",深度:"+row[4]);
            lti.append(row[2])
            lng.append(row[1])
            #print(i)
            heatmap[i][0] = row[2];
            heatmap[i][1] = row[1];
            
    Eqk_Heatmap = folium.Map(location=[float(lti[0]), float(lng[0])], zoom_start=15)   

    HeatMap(heatmap).add_to(Eqk_Heatmap)
    
    #for row in range(len(lti)):
        # print(pop_up[row])
        #folium.Marker(location=[float(lti[row]), float(lng[row])] ,popup=pop_up[row],icon=folium.Icon(color='green',icon='cloud')).add_to(Eqk_Heatmap)
Eqk_Heatmap