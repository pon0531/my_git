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

database_name = "mpxv"
basic_file_paths = []
data_base_table_names = []

dirPath = r'../Data'
print(os.listdir(dirPath))
Files = [f for f in os.listdir(dirPath)]

for file_name in Files:
    if '.csv' in file_name:
        file_path_create = "../Data/" + file_name
        basic_file_paths.append(file_path_create)

        file_name = file_name.replace(".csv","")
        data_base_table_names.append(file_name)

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
                            database = "mpxv",  #資料庫
                            port=3306)           # port
    cursor = conn.cursor()

    for i in range(len(data_base_table_names)):
        if 'Weekly_Age_County_Gender_MPXV' == data_base_table_names[i]:
            start_time_ = time.time()
            #確定病名,發病年份,發病月份,縣市,鄉鎮,性別,是否為境外移入,年齡層,確定病例數
            #disease,year,week,site_id,township,imported,year_range,disease_cnt
            sql = """CREATE TABLE IF NOT EXISTS {IMG} (disease TEXT(20),
                                                      year INT(10),
                                                      week INT(10),
                                                      site_id TEXT(10),
                                                      township TEXT(10),
                                                      sex CHAR(3),
                                                      import TEXT(10),
                                                      year_range TEXT(20),
                                                      disease_cnt INT(10))""".format(IMG=data_base_table_names[i])
            print("Input database table:",data_base_table_names[i])
            #print("SQL cmd: %s" %sql)
            cursor.execute(sql)

            #把cvs匯入data base, 從第1行開始讀，往下讀nrows行
            data = pd.read_csv(basic_file_paths[i], header=0, encoding="utf8")
         
            for j in range(len(data)):
                sql = """INSERT INTO {IMG} (disease, year, week, site_id, township, sex,import,year_range,disease_cnt)
                                       VALUES (%s, %s, %s, %s, %s, %s,%s ,%s,%s)""".format(IMG=data_base_table_names[i])
                var = (data.iloc[j,0], data.iloc[j,1], data.iloc[j,2], data.iloc[j,3], 
                       data.iloc[j,4], data.iloc[j,5], data.iloc[j,6], data.iloc[j,7],
                       data.iloc[j,8])
                cursor.execute(sql, var)
                conn.commit()

            end_time_ = time.time()
            print("Time elapsed for input %s: %.2f seconds" %(data_base_table_names[i],(end_time_ - start_time_)))
        else:
            start_time_ = time.time()
            #確定病名,發病年份,發病月份,縣市,鄉鎮,性別,是否為境外移入,年齡層,確定病例數
            #disease,year,month,site_id,township,imported,year_range,disease_cnt
            sql = """CREATE TABLE IF NOT EXISTS {IMG} (disease TEXT(20),
                                                      year INT(10),
                                                      month INT(10),
                                                      site_id TEXT(10),
                                                      township TEXT(10),
                                                      sex CHAR(3),
                                                      import TEXT(10),
                                                      year_range TEXT(20),
                                                      disease_cnt INT(10))""".format(IMG=data_base_table_names[i])
            print("Input database table:",data_base_table_names[i])
            #print("SQL cmd: %s" %sql)
            cursor.execute(sql)

            #把cvs匯入data base, 從第1行開始讀，往下讀nrows行
            data = pd.read_csv(basic_file_paths[i], header=0, encoding="utf8")

            for j in range(len(data)):
                sql = """INSERT INTO {IMG} (disease, year, month, site_id, township, sex,import,year_range,disease_cnt)
                                       VALUES (%s, %s, %s, %s, %s, %s,%s ,%s,%s)""".format(IMG=data_base_table_names[i])
                var = (data.iloc[j,0], data.iloc[j,1], data.iloc[j,2], data.iloc[j,3], 
                       data.iloc[j,4], data.iloc[j,5], data.iloc[j,6], data.iloc[j,7],
                       data.iloc[j,8])
                cursor.execute(sql, var)
                conn.commit()

            end_time_ = time.time()
            print("Time elapsed for input %s: %.2f seconds" %(data_base_table_names[i],(end_time_ - start_time_)))

except Exception as e :
    print("資料庫連接失敗", e)
    
finally:
    conn.close()
    print("資料庫連線結束")