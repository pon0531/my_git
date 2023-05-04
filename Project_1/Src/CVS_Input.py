# -*- coding: utf-8 -*-
"""
Created on Wed May  3 23:10:17 2023

@author: upon
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May  3 21:11:01 2023

@author: upon
"""

import MySQLdb
import pandas as pd


# 從第1行開始讀，往下讀370行
data = pd.read_csv("opendata108Y120.csv", header=3, encoding="utf8")
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

    cursor.execute(sql)
    db_info = cursor.fetchone()
    print(db_info)

    
    #把cvs匯入data base
    for i in range(len(data)):
        sql = """INSERT INTO data_population_108 (statistic_yyy, district_code, site_id, site_id_sub, village, sex,birthplace,population)
                                    VALUES (%s, %s, %s, %s, %s, %s,%s ,%s)"""
        var = (data.iloc[i,0], data.iloc[i,1], data.iloc[i,2][:3], data.iloc[i,2][3:], data.iloc[i,3], data.iloc[i,4],data.iloc[i,5],data.iloc[i,6])     
        cursor.execute(sql, var)
            
        conn.commit()
    
except Exception as e :
    print("資料庫連接失敗", e)
    
finally:
    conn.close()
    print("資料庫連線結束")