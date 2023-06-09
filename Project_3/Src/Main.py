# -*- coding: utf-8 -*-
"""
Created on Wed May  3 21:11:01 2023

@author: felix.peng
"""

import MySQLdb
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

data_base = "mpxv"
year_month=[]
year_week=[]
SumOfCnt=[]
Size = []

# 設定python顯示中文
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

def SQL_Get_Data(sql):
    # 開啟資料庫連接
    conn = MySQLdb.connect(host="localhost",    # 主機名稱
                            user="root",         # 帳號
                            password="boopann403", # 密碼
                            database = data_base,  #資料庫
                            port=3306)           # port
    
    # 使用cursor()方法操作資料庫
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    return conn, data

def Generate_Chart_1(data):

    SumOfCnt.clear()
    Size.clear()

    for row in range(len(data)):
        year_month.append(str(data[row][0])+"/"+str(data[row][1]))
        SumOfCnt.append(data[row][2])

    # 製作圓餅圖比例
    for i in SumOfCnt:
        Size.append(round(i*100/sum(SumOfCnt),2))

    plt.figure(figsize=(10,10))
    plt.subplot(1,2,1)
    plt.xlabel('Year/Month', fontsize="13") # 設定 x 軸標題內容及大小
    plt.ylabel('Disease Cnt', fontsize="13") # 設定 y 軸標題標題內容及大小
    plt.title('猴痘分析', fontsize="18") # 設定圖表標題內容及大小

    plt.bar(year_month,SumOfCnt,color="blue")
    plt.tick_params(axis='both', which='major', labelsize=13)
    plt.tick_params(axis='both', which='minor', labelsize=13)
    plt.xticks(rotation=70)

    plt.subplot(1,2,2)
    explode=(0,0,0,0,0.1,0,0)
    plt.pie(Size, explode=explode, labels=year_month,
        autopct='%.2f%%',textprops={'fontsize': 7})

    plt.axis('equal')
    #plt.show()

    plt.savefig('../Result/chart1.png')
    plt.close()

def Generate_Chart_2(data):

    SumOfCnt.clear()
    Size.clear()

    for row in range(len(data)):
        year_week.append(str(data[row][0])+"/"+str(data[row][1]))
        SumOfCnt.append(data[row][2])

    # 製作圓餅圖比例
    for i in SumOfCnt:
        Size.append(round(i*100/sum(SumOfCnt),2))

    plt.figure(figsize=(10,10))
    plt.subplot(1,2,1)
    plt.xlabel('Year/Week', fontsize="13") # 設定 x 軸標題內容及大小
    plt.ylabel('Disease Cnt', fontsize="13") # 設定 y 軸標題標題內容及大小
    plt.title('猴痘分析', fontsize="18") # 設定圖表標題內容及大小

    plt.bar(year_week,SumOfCnt,color="blue")
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.tick_params(axis='both', which='minor', labelsize=10)
    plt.xticks(rotation=70)

    plt.subplot(1,2,2)
    explode= [0]*len(year_week)

    # 取最大值的index，將這個的pie值設為分離
    explode[SumOfCnt.index(max(SumOfCnt))] = 0.1
    plt.pie(Size, explode=explode, labels=year_week,
        autopct='%.2f%%',textprops={'fontsize': 5})

    plt.axis('equal')
    #plt.show()

    plt.savefig('../Result/chart2.png')
    plt.close()
def main():

    try:
        sql = """SELECT YEAR, month,SUM(disease_cnt) as SumOfCnt
                FROM mpxv.age_county_gender_mpxv
                GROUP BY year,month
                ORDER BY year,month DESC"""

        conn, data = SQL_Get_Data(sql)
        Generate_Chart_1(data)

        sql = """SELECT YEAR, week,SUM(disease_cnt) as SumOfCnt
                FROM mpxv.weekly_age_county_gender_mpxv
                GROUP BY year,week
                ORDER BY year,week"""

        conn, data = SQL_Get_Data(sql)
        Generate_Chart_2(data)

    except Exception as e :
        print("資料庫連接失敗", e)

    finally:
        conn.close()
        print("資料庫連線結束")

if __name__== "__main__" :

    main()