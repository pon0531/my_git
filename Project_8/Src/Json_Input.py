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

database_name = "Tvl_v3"
basic_file_paths = []
data_base_table_names = []

dirPath = r'../Data'
print(os.listdir(dirPath))
Files = [f for f in os.listdir(dirPath)]

for file_name in Files:
    if '.json' in file_name:
        file_path_create = "../Data/" + file_name
        basic_file_paths.append(file_path_create)

        file_name = file_name.replace(".json","")
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
                            database = "tvl_v3",  #資料庫
                            port=3306)           # port
    cursor = conn.cursor()

    print(len(data_base_table_names))
    for i in range(len(data_base_table_names)):
        start_time_ = time.time()
        sql = """CREATE TABLE IF NOT EXISTS {IMG} (Agent_Ind INT(10),
                                                T FLOAT(5),
                                              Point_x FLOAT(8),
                                              Point_y FLOAT(8),
                                              C0 FLOAT(15),
                                              C1 FLOAT(15),C2 FLOAT(15),C3 FLOAT(15),C4 FLOAT(15),C5 FLOAT(15),C6 FLOAT(15),C7 FLOAT(15),C8 FLOAT(15),C9 FLOAT(15),C10 FLOAT(15),
                                              C11 FLOAT(15),C12 FLOAT(15),C13 FLOAT(15),C14 FLOAT(15),C15 FLOAT(15),C16 FLOAT(15),C17 FLOAT(15),C18 FLOAT(15),C19 FLOAT(15),C20 FLOAT(15),
                                              C21 FLOAT(15),C22 FLOAT(15),C23 FLOAT(15),C24 FLOAT(15),C25 FLOAT(15),C26 FLOAT(15),C27 FLOAT(15),C28 FLOAT(15),C29 FLOAT(15),C30 FLOAT(15),
                                              C31 FLOAT(15),C32 FLOAT(15),C33 FLOAT(15),C34 FLOAT(15),C35 FLOAT(15),C36 FLOAT(15),C37 FLOAT(15),C38 FLOAT(15),C39 FLOAT(15),C40 FLOAT(15),
                                              C41 FLOAT(15),C42 FLOAT(15),C43 FLOAT(15),C44 FLOAT(15),C45 FLOAT(15),C46 FLOAT(15),C47 FLOAT(15),C48 FLOAT(15),C49 FLOAT(15),C50 FLOAT(15),
                                              C51 FLOAT(15),C52 FLOAT(15),C53 FLOAT(15),C54 FLOAT(15),C55 FLOAT(15),C56 FLOAT(15),C57 FLOAT(15),C58 FLOAT(15),C59 FLOAT(15),C60 FLOAT(15),
                                              C61 FLOAT(15),C62 FLOAT(15),C63 FLOAT(15),C64 FLOAT(15),C65 FLOAT(15),C66 FLOAT(15),C67 FLOAT(15),C68 FLOAT(15),C69 FLOAT(15),C70 FLOAT(15),
                                              C71 FLOAT(15),C72 FLOAT(15),C73 FLOAT(15),C74 FLOAT(15),C75 FLOAT(15),C76 FLOAT(15),C77 FLOAT(15),C78 FLOAT(15),C79 FLOAT(15),
                                              C80 FLOAT(15),
                                              E0 FLOAT(15),
                                              E1 FLOAT(15),E2 FLOAT(15),E3 FLOAT(15),E4 FLOAT(15),E5 FLOAT(15),E6 FLOAT(15),E7 FLOAT(15),E8 FLOAT(15),E9 FLOAT(15),E10 FLOAT(15),
                                              E11 FLOAT(15),E12 FLOAT(15),E13 FLOAT(15),E14 FLOAT(15),E15 FLOAT(15),E16 FLOAT(15),E17 FLOAT(15),E18 FLOAT(15),E19 FLOAT(15),E20 FLOAT(15),
                                              E21 FLOAT(15),E22 FLOAT(15),E23 FLOAT(15),E24 FLOAT(15),E25 FLOAT(15),E26 FLOAT(15),E27 FLOAT(15),E28 FLOAT(15),E29 FLOAT(15),E30 FLOAT(15),
                                              E31 FLOAT(15),E32 FLOAT(15),E33 FLOAT(15),E34 FLOAT(15),E35 FLOAT(15),E36 FLOAT(15),E37 FLOAT(15),E38 FLOAT(15),E39 FLOAT(15),E40 FLOAT(15),
                                              E41 FLOAT(15),E42 FLOAT(15),E43 FLOAT(15),E44 FLOAT(15),E45 FLOAT(15),E46 FLOAT(15),E47 FLOAT(15),E48 FLOAT(15),E49 FLOAT(15),E50 FLOAT(15),
                                              E51 FLOAT(15),E52 FLOAT(15),E53 FLOAT(15),E54 FLOAT(15),E55 FLOAT(15),E56 FLOAT(15),E57 FLOAT(15),E58 FLOAT(15),E59 FLOAT(15),E60 FLOAT(15),
                                              E61 FLOAT(15),E62 FLOAT(15),E63 FLOAT(15),E64 FLOAT(15),E65 FLOAT(15),E66 FLOAT(15),E67 FLOAT(15),E68 FLOAT(15),E69 FLOAT(15),E70 FLOAT(15),
                                              E71 FLOAT(15),E72 FLOAT(15),E73 FLOAT(15),E74 FLOAT(15),E75 FLOAT(15),E76 FLOAT(15),E77 FLOAT(15),E78 FLOAT(15),E79 FLOAT(15),
                                              E80 FLOAT(15),
                                              TP0 TEXT(30),
                                              TP1 TEXT(30),TP2 TEXT(30),TP3 TEXT(30),TP4 TEXT(30),TP5 TEXT(30),TP6 TEXT(30),TP7 TEXT(30),TP8 TEXT(30),TP9 TEXT(30),TP10 TEXT(30),
                                              TP11 TEXT(30),TP12 TEXT(30),TP13 TEXT(30),TP14 TEXT(30),TP15 TEXT(30),TP16 TEXT(30),TP17 TEXT(30),TP18 TEXT(30),TP19 TEXT(30),TP20 TEXT(30),
                                              TP21 TEXT(30),TP22 TEXT(30),TP23 TEXT(30),TP24 TEXT(30),TP25 TEXT(30),TP26 TEXT(30),TP27 TEXT(30),TP28 TEXT(30),TP29 TEXT(30),TP30 TEXT(30),
                                              TP31 TEXT(30),TP32 TEXT(30),TP33 TEXT(30),TP34 TEXT(30),TP35 TEXT(30),TP36 TEXT(30),TP37 TEXT(30),TP38 TEXT(30),TP39 TEXT(30))""".format(IMG=data_base_table_names[i])
        print("Input database table:",data_base_table_names[i])
        #print("SQL cmd: %s" %sql)
        cursor.execute(sql)
        print(basic_file_paths)
        path = "../Data/"+data_base_table_names[i]+".json"
        print(path)
        with open(path, 'r') as f:
            df = pd.read_json(f)

        for j in range(len(df)):
            sql = """INSERT INTO {IMG} (Agent_Ind, T, Point_x, Point_y,
                                        C0,
                                        C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,
                                        C11,C12,C13,C14,C15,C16,C17,C18,C19,C20,
                                        C21,C22,C23,C24,C25,C26,C27,C28,C29,C30,
                                        C31,C32,C33,C34,C35,C36,C37,C38,C39,C40,
                                        C41,C42,C43,C44,C45,C46,C47,C48,C49,C50,
                                        C51,C52,C53,C54,C55,C56,C57,C58,C59,C60,
                                        C61,C62,C63,C64,C65,C66,C67,C68,C69,C70,
                                        C71,C72,C73,C74,C75,C76,C77,C78,C79,C80,
                                        E0,
                                        E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,
                                        E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,
                                        E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,
                                        E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,
                                        E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,
                                        E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,
                                        E61,E62,E63,E64,E65,E66,E67,E68,E69,E70,
                                        E71,E72,E73,E74,E75,E76,E77,E78,E79,E80,
                                        TP0,
                                        TP1,TP2,TP3,TP4,TP5,TP6,TP7,TP8,TP9,TP10,
                                        TP11,TP12,TP13,TP14,TP15,TP16,TP17,TP18,TP19,TP20,
                                        TP21,TP22,TP23,TP24,TP25,TP26,TP27,TP28,TP29,TP30,
                                        TP31,TP32,TP33,TP34,TP35,TP36,TP37,TP38,TP39)
                                       VALUES (%s, %s, %s, %s, %s, %s,%s ,%s, %s, %s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s, %s, %s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s, %s,%s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s, %s, %s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s, %s,%s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s, %s,%s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s, %s,%s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s,%s,%s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s,%s,%s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s,%s,%s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s,%s,%s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s,%s,%s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s,%s,%s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s,%s,%s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s,%s,%s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s,%s,%s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s,%s,%s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s,%s,%s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s,%s,%s,
                                               %s, %s, %s, %s, %s, %s,%s ,%s,%s,%s,
                                               %s, %s, %s, %s, %s, %s)""".format(IMG=data_base_table_names[i])
            
            var = (df["Agent_Ind"][j],
                   df["T"][j],
                   df["Point"][j][0],
                   df["Point"][j][1],
                   df["C"][j][0],
                   df["C"][j][1],df["C"][j][2],df["C"][j][3],df["C"][j][4],df["C"][j][5],df["C"][j][6],df["C"][j][7],df["C"][j][8],df["C"][j][9],df["C"][j][10],
                   df["C"][j][11],df["C"][j][12],df["C"][j][13],df["C"][j][14],df["C"][j][15],df["C"][j][16],df["C"][j][17],df["C"][j][18],df["C"][j][19],df["C"][j][20],
                   df["C"][j][21],df["C"][j][22],df["C"][j][23],df["C"][j][24],df["C"][j][25],df["C"][j][26],df["C"][j][27],df["C"][j][28],df["C"][j][29],df["C"][j][30],
                   df["C"][j][31],df["C"][j][32],df["C"][j][33],df["C"][j][34],df["C"][j][35],df["C"][j][36],df["C"][j][37],df["C"][j][38],df["C"][j][39],df["C"][j][40],
                   df["C"][j][41],df["C"][j][42],df["C"][j][43],df["C"][j][44],df["C"][j][45],df["C"][j][46],df["C"][j][47],df["C"][j][48],df["C"][j][49],df["C"][j][50],
                   df["C"][j][51],df["C"][j][52],df["C"][j][53],df["C"][j][54],df["C"][j][55],df["C"][j][56],df["C"][j][57],df["C"][j][58],df["C"][j][59],df["C"][j][60],
                   df["C"][j][61],df["C"][j][62],df["C"][j][63],df["C"][j][64],df["C"][j][65],df["C"][j][66],df["C"][j][67],df["C"][j][68],df["C"][j][69],df["C"][j][70],
                   df["C"][j][71],df["C"][j][72],df["C"][j][73],df["C"][j][74],df["C"][j][75],df["C"][j][76],df["C"][j][77],df["C"][j][78],df["C"][j][79],df["C"][j][80],
                   df["Event"][j][0],
                   df["Event"][j][1],df["Event"][j][2],df["Event"][j][3],df["Event"][j][4],df["Event"][j][5],df["Event"][j][6],df["Event"][j][7],df["Event"][j][8],df["Event"][j][9],df["Event"][j][10],
                   df["Event"][j][11],df["Event"][j][12],df["Event"][j][13],df["Event"][j][14],df["Event"][j][15],df["Event"][j][16],df["Event"][j][17],df["Event"][j][18],df["Event"][j][19],df["Event"][j][20],
                   df["Event"][j][21],df["Event"][j][22],df["Event"][j][23],df["Event"][j][24],df["Event"][j][25],df["Event"][j][26],df["Event"][j][27],df["Event"][j][28],df["Event"][j][29],df["Event"][j][30],
                   df["Event"][j][31],df["Event"][j][32],df["Event"][j][33],df["Event"][j][34],df["Event"][j][35],df["Event"][j][36],df["Event"][j][37],df["Event"][j][38],df["Event"][j][39],df["Event"][j][40],
                   df["Event"][j][41],df["Event"][j][42],df["Event"][j][43],df["Event"][j][44],df["Event"][j][45],df["Event"][j][46],df["Event"][j][47],df["Event"][j][48],df["Event"][j][49],df["Event"][j][50],
                   df["Event"][j][51],df["Event"][j][52],df["Event"][j][53],df["Event"][j][54],df["Event"][j][55],df["Event"][j][56],df["Event"][j][57],df["Event"][j][58],df["Event"][j][59],df["Event"][j][60],
                   df["Event"][j][61],df["Event"][j][62],df["Event"][j][63],df["Event"][j][64],df["Event"][j][65],df["Event"][j][66],df["Event"][j][67],df["Event"][j][68],df["Event"][j][69],df["Event"][j][70],
                   df["Event"][j][71],df["Event"][j][72],df["Event"][j][73],df["Event"][j][74],df["Event"][j][75],df["Event"][j][76],df["Event"][j][77],df["Event"][j][78],df["Event"][j][79],df["Event"][j][80],
                   str(df["TouchPoint"][j][0]),
                   str(df["TouchPoint"][j][1]),str(df["TouchPoint"][j][2]),str(df["TouchPoint"][j][3]),str(df["TouchPoint"][j][4]),str(df["TouchPoint"][j][5]),str(df["TouchPoint"][j][6]),str(df["TouchPoint"][j][7]),str(df["TouchPoint"][j][8]),str(df["TouchPoint"][j][9]),str(df["TouchPoint"][j][10]),
                   str(df["TouchPoint"][j][11]),str(df["TouchPoint"][j][12]),str(df["TouchPoint"][j][13]),str(df["TouchPoint"][j][14]),str(df["TouchPoint"][j][15]),str(df["TouchPoint"][j][16]),str(df["TouchPoint"][j][17]),str(df["TouchPoint"][j][18]),str(df["TouchPoint"][j][19]),str(df["TouchPoint"][j][20]),
                   str(df["TouchPoint"][j][21]),str(df["TouchPoint"][j][22]),str(df["TouchPoint"][j][23]),str(df["TouchPoint"][j][24]),str(df["TouchPoint"][j][25]),str(df["TouchPoint"][j][26]),str(df["TouchPoint"][j][27]),str(df["TouchPoint"][j][28]),str(df["TouchPoint"][j][29]),str(df["TouchPoint"][j][30]),
                   str(df["TouchPoint"][j][31]),str(df["TouchPoint"][j][32]),str(df["TouchPoint"][j][33]),str(df["TouchPoint"][j][34]),str(df["TouchPoint"][j][35]),str(df["TouchPoint"][j][36]),str(df["TouchPoint"][j][37]),str(df["TouchPoint"][j][38]),str(df["TouchPoint"][j][39]))
            cursor.execute(sql, var)
            conn.commit()


        end_time_ = time.time()
        print("Time elapsed for input %s: %.2f seconds" %(data_base_table_names[i],(end_time_ - start_time_)))
    
except Exception as e :
    print("資料庫連接失敗", e)

finally:
    conn.close()
    print("資料庫連線結束")