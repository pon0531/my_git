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
import time
import os

database_name = "Population"
basic_file_path = "../Data/opendata"
data_base_pre_name = "data_population_"
basic_file_paths = []
data_base_names = []


dirPath = r'../Data'
print(os.listdir(dirPath))
Files = [f for f in os.listdir(dirPath)]

for file_name in Files:
    if '.csv' in file_name:
        file_path_create = "../Data/" + file_name
        basic_file_paths.append(file_path_create)

        file_name = file_name.replace(".csv","")
        data_base_names.append(file_name)

try:
    # 開啟資料庫連接
    conn = MySQLdb.connect(host="localhost",    # 主機名稱
                            user="root",         # 帳號
                            password="boopann403", # 密碼
                            #database = "test_db",  #資料庫
                            port=3306)           # port
    
    # 使用cursor()方法操作資料庫
    cursor = conn.cursor()
    
    # 建立資料庫test_db
    sql = "Select @@version"

    cursor.execute(sql)
    db_info = cursor.fetchone()
    print(db_info)

    sql = """CREATE DATABASE IF NOT EXISTS `{IMG}`""".format(IMG=database_name)
    cursor.execute(sql)
    conn.close()

    print("Create database :",database_name)

    # 創造test_db後，再次connection
    conn = MySQLdb.connect(host="localhost",    # 主機名稱
                            user="root",         # 帳號
                            password="boopann403", # 密碼
                            database = database_name,  #資料庫
                            port=3306)           # port
    cursor = conn.cursor()

    for i in range(len(Files)-1): #多一個readme檔
        start_time_ = time.time()
        sql = """CREATE TABLE IF NOT EXISTS {IMG} (statistic_yyy int(4),
                                                  district_code CHAR(20),
                                                  site_id TEXT(10),
                                                  site_id_sub TEXT(10),
                                                  village TEXT(10),
                                                  sex CHAR(10),
                                                  birthplace TEXT(10),
                                                  population int(10))""".format(IMG=data_base_names[i])
        print("Input database table:",data_base_names[i])
        cursor.execute(sql)

        #把cvs匯入data base, 從第1行開始讀，往下讀nrows行
        data = pd.read_csv(basic_file_paths[i], header=1,nrows=10, encoding="utf8")
        
        #data = pd.read_csv(basic_file_paths[i], header=1, encoding="utf8")
        for j in range(len(data)):
            sql = """INSERT INTO {IMG} (statistic_yyy, district_code, site_id, site_id_sub, village, sex,birthplace,population)
                                   VALUES (%s, %s, %s, %s, %s, %s,%s ,%s)""".format(IMG=data_base_names[i])

            var = (data.iloc[j,0], data.iloc[j,1], data.iloc[j,2][:3], data.iloc[j,2][3:], data.iloc[j,3], data.iloc[j,4],data.iloc[j,5],data.iloc[j,6])
            cursor.execute(sql, var)
            conn.commit()
        end_time_ = time.time()
        print("Time elapsed for input %s: %.2f seconds" %(data_base_names[i],(end_time_ - start_time_)))
except Exception as e :
    print("資料庫連接失敗", e)
    
finally:
    conn.close()
    print("資料庫連線結束")