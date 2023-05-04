# -*- coding: utf-8 -*-
"""
Created on Wed May  3 21:11:01 2023

@author: upon
"""

import MySQLdb
import MySQLdb
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
# 從第1行開始讀，往下讀370行
#data = pd.read_csv("/data/opendata109Y120.csv", header=3, nrows=418394, encoding="utf8")
#data = pd.read_csv("opendata111Y120.csv",  encoding="utf8")
try:
    # 開啟資料庫連接
    conn = MySQLdb.connect(host="localhost",    # 主機名稱
                            user="root",         # 帳號
                            password="boopann403", # 密碼
                            database = "test_db",  #資料庫
                            port=3306)           # port
    
    # 使用cursor()方法操作資料庫
    cursor = conn.cursor()
    
    # 建立表格towndata
    sql = "Select @@version"
    #sql = """CREATE TABLE IF NOT EXISTS towndata (year CHAR(4) ,
    ##                                              site VARCHAR(20),
    #                                              people_total int(10),
    #                                              area float(10),
    #                                              population int(10))"""
    
    cursor.execute(sql)
    rows = cursor.fetchone()
    print(rows)
    #print("資料表建立完畢")


    #把cvs匯入data base
    #for i in range(len(data)):
    #    sql = """INSERT INTO towndata (statistic_yyy, district_code, site_id, village, sex,birthplace,population)
    #                                VALUES (%s, %s, %s, %s, %s,%s ,%s)"""
    #    var = (data.iloc[i,0], data.iloc[i,1], data.iloc[i,2], data.iloc[i,3], data.iloc[i,4],data.iloc[i,5],data.iloc[i,6])     
    #    cursor.execute(sql, var)
    #        
    #    conn.commit()
    
    
    
    # 永和區，各里人口排行
    #key = "新北市永和區"
    #sql = """SELECT site_id,village,SUM(population) as SumOfVillage
    #        FROM test_db.towndata
    #        WHERE site_id = "新北市永和區"
    #        GROUP BY village,site_id
    #        ORDER BY SumOfVillage  DESC"""
    #cursor.execute(sql)
    #data = cursor.fetchall()

    #print(data)
    #village = []
    #population=[]
    #for i in range(len(data)):
    #    village.append(data[i][1])
    #    population.append(data[i][2])
    #    print(data[i])
    
    sql = """SELECT site_id,SUM(population) as SumOfVillage
            FROM test_db.data_population_110
            GROUP BY site_id
            ORDER BY SumOfVillage  DESC"""   
    
    cursor.execute(sql)
    data = cursor.fetchall()   
    #print(data)
    
    site_id = []
    population = []

    for i in range(20):
        site_id.append(data[i][0])
        population.append(data[i][1])
        print(data[i])
    
    print(site_id)
    print(population)
    
    
    plt.figure(figsize=(6, 6))
    plt.bar(site_id,population)
    plt.xticks(rotation=70)
    plt.show()
    

    
except Exception as e :
    print("資料庫連接失敗", e)
    
finally:
    conn.close()
    print("資料庫連線結束")