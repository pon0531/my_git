# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:44:14 2023

@author: USER
"""
import MySQLdb
import tkinter as tk
import os
import numpy as np
import cv2
import pandas as pd
import math
import collections
import matplotlib.pyplot as plt
import threading
import time
from PIL import ImageTk, Image
from TvL_Model import TvL_model
from TvL_SQL_Input import Json_input
from enum import Enum
import threading

class List_item:
    LIST_ITEM_RICH_TOP = 0
    LIST_ITEM_LUCKY_TOP = 1
    LIST_ITEM_UNLUCKY_TOP = 2
    LIST_ITEM_TALENT_TOP = 3
    LIST_ITEM_TALENT_BOTTOM=4
    LIST_ITEM_TALENT_HIST = 5
    LIST_ITEM_CAPTIAL_20_80 = 6
    LIST_ITEM_CAPTIAL_LUCKY = 7
    LIST_ITEM_CAPTIAL_UNLUCKY = 8
    LIST_ITEM_LUCKY_CNT = 9
    LIST_ITEM_UNLUCKY_CNT = 10
    LIST_ITEM_ALL_RUN_TOP = 11
    
global_database = "tvl_v9"
class Button_TvL:
    
    def __init__(self, root, no, h, w, texts, layer, file_name):
        self.no = no
        self.file_name = file_name
        self.text = texts
        self.root = root     
        self.pic_file_path = ""

        if layer == 0:
            self.btn = tk.Button(root,
                               text=texts,
                               font=('Arial',10,'bold'),
                               activebackground='red',
                               activeforeground='white',
                               height= h, width=w,
                               bd=1,
                               image = file_name,
                               command=lambda: self.btn_cb_start_model(no, texts,file_name));
            self.btn.pack()
        elif layer == 1:
            self.btn = tk.Button(root,
                               #text=self.Global_Test_Cnt,
                               activebackground='red',
                               activeforeground='white',
                               padx=0,pady=0,
                               font=('Arial',10,'bold'),
                               height= h, width=w,
                               bd=0,bg='black',
                               image = no,
                               command=lambda: self.btn_cb_analysis_list(no, texts,file_name));
            self.btn.pack(side='left')
        elif layer == 2:
            self.btn = tk.Button(root,
                               text=texts,
                               activebackground='red',
                               activeforeground='white',
                               font=('Arial',10,'bold'),
                               height= h, width=w,
                               command=lambda: self.btn_cb_table_list(no, texts,file_name));
            self.btn.pack()
        elif layer == 3:
            self.btn = tk.Button(root,
                               text=texts,
                               activebackground='red',
                               activeforeground='white',
                               font=('Arial',10,'bold'),
                               height= h, width=w,
                               bd=4,bg='red',
                               command=lambda: self.btn_cb_bar_chart_list(no, texts,file_name));
            self.btn.grid(row=0,column=no,sticky=tk.S+tk.W)

    def model_running(self,texts):

        print("start model background")

        # get cnt from label input
        exe_cnt = int(texts.get())
        
        img = Image.open("life.jpg")
        resized_img = img.resize((30,30), Image.ANTIALIAS)
        img_obj_life = ImageTk.PhotoImage(resized_img)  

        #create_new_database_table = []

        for i in range(exe_cnt):
            
            # Model create new data
            create_new_database_table = TvL_model()
            
        #for i in range(exe_cnt):
            
            # SQL input data to SQL database
            Json_input(global_database,create_new_database_table)
            
            # Create new botton
            Button_TvL(root, img_obj_life,30,30, create_new_database_table,1,create_new_database_table)

    def btn_cb_start_model(self, no, texts,file_name):

        print("start model")

        #t = threading.Thread(target=model_running,args=(create_new_database_table,exe_cnt,))
        #t = threading.Thread(target=model_running)
        #t = threading.Thread(target=model_running,args=(texts,file_name,))
        t = threading.Thread(target=self.model_running,args=(texts,))
        t.start()
    def btn_cb_analysis_list(self, no, texts,file_name):
        print("btn_cb_analysis_list")

        root = tk.Tk()
        root.title("分析圖列表")
        root.geometry('300x600')

        buttons.append(Button_TvL(root, 0, 1,25,"Rich Top排名",2,file_name))
        buttons.append(Button_TvL(root, 1, 1,25,"Lucky 排名",2,file_name))
        buttons.append(Button_TvL(root, 2, 1,25,"Unlucky 排名",2,file_name))
        buttons.append(Button_TvL(root, 3, 1,25,"Talent Top排名",2,file_name))
        buttons.append(Button_TvL(root, 4, 1,25,"Talent Bottom排名",2,file_name))
        buttons.append(Button_TvL(root, 5, 1,25,"Talent 分布圖",2,file_name))
        buttons.append(Button_TvL(root, 6, 1,25,"20/80 財產分布圖",2,file_name))
        buttons.append(Button_TvL(root, 7, 1,25,"Lucky & C分佈",2,file_name))
        buttons.append(Button_TvL(root, 8, 1,25,"Unlucky & C分佈",2,file_name))
        buttons.append(Button_TvL(root, 9, 1,25,"Lucky Event 分佈",2,file_name))
        buttons.append(Button_TvL(root, 10, 1,25,"Unlucky Event 分佈",2,file_name))
        buttons.append(Button_TvL(root, 11, 1,25,"All Run Tops",2,file_name))
    
    
    def open_pic_thread(self):
        
        print(self.pic_file_path)
        img = cv2.imread(self.pic_file_path)
        cv2.imshow(self.pic_file_path, img)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def btn_cb_bar_chart_list(self, no, texts,file_name):
        
        print("btn_cb_bar_chart_list")

        conn = MySQLdb.connect(host="localhost",    # 主機名稱
                            user="root",         # 帳號
                            password="boopann403", # 密碼
                            database = global_database,  #資料庫
                            port=3306)           # port
    
        # 使用cursor()方法操作資料庫
        cursor = conn.cursor()
    
        # 建立資料庫test_db
        sql = "Select @@version"

        cursor.execute(sql)
        db_info = cursor.fetchone()
        #print(db_info)

        sql = """SELECT T
                FROM {IMG}
                WHERE Agent_Ind = {IMG2}""".format(IMG=file_name,IMG2=texts)
        cursor.execute(sql)
        T =cursor.fetchone()

        sql = """SELECT E0,E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22,E23,E24,E25,E26,E27,E28,E29,E30,E31,E32,E33,E34,E35,E36,E37,E38,E39,E40,E41,E42,E43,E44,E45,E46,E47,E48,E49,E50,E51,E52,E53,E54,E55,E56,E57,E58,E59,E60,E61,E62,E63,E64,E65,E66,E67,E68,E69,E70,E71,E72,E73,E74,E75,E76,E77,E78,E79,E80
                FROM {IMG}
                WHERE Agent_Ind = {IMG2}""".format(IMG=file_name,IMG2=texts)
        result = cursor.execute(sql)
        db_info =cursor.fetchall()
        
        
        sql = """SELECT C0,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16,C17,C18,C19,C20,C21,C22,C23,C24,C25,C26,C27,C28,C29,C30,C31,C32,C33,C34,C35,C36,C37,C38,C39,C40,C41,C42,C43,C44,C45,C46,C47,C48,C49,C50,C51,C52,C53,C54,C55,C56,C57,C58,C59,C60,C61,C62,C63,C64,C65,C66,C67,C68,C69,C70,C71,C72,C73,C74,C75,C76,C77,C78,C79,C80
                FROM {IMG}
                WHERE Agent_Ind = {IMG2}""".format(IMG=file_name,IMG2=texts)
        result = cursor.execute(sql)
        y2 =cursor.fetchall()
        y1 =[]
  
    
        sql = """SELECT LUCKY,UNLUCKY
                FROM {IMG}
                WHERE Agent_Ind = {IMG2}""".format(IMG=file_name,IMG2=texts)
        cursor.execute(sql)
        result=cursor.fetchone()          

        Lucky_Unlucky = np.array(result)       

        for i in range(81):
            y1.append(db_info[0][i])

        y1_re_gen = []
        lucky_cnt = 0
        unlucky_cnt = 0

        for i in range (81):
            re_gen_event_value = 0;
            if y1[i] == 1:   #unlucky
                re_gen_event_value = -1
                unlucky_cnt = unlucky_cnt + 1
            elif y1[i] == 2: #lucky and success
                re_gen_event_value = 1
                lucky_cnt = lucky_cnt + 1
            elif y1[i] == 3: # lucky and unlucky same period
                re_gen_event_value = 0
                #lucky_cnt = lucky_cnt + 1
                #unlucky_cnt = unlucky_cnt + 1
            elif y1[i] == 4: # lucky but not success
                re_gen_event_value = 0
                #lucky_cnt = lucky_cnt + 1
            elif y1[i] == 5: # unlucky and lucky but no success
                re_gen_event_value = -1
                #lucky_cnt = lucky_cnt + 1
                unlucky_cnt = unlucky_cnt + 1
            y1_re_gen.append(re_gen_event_value)

        plt.figure(figsize=(10, 10), dpi=70)
        x =  np.arange(0,40.5,0.5)

        plt.suptitle("Agent_"+str(texts)+",Talent:"+str(T[0]),fontsize=30)
        
        plt.subplot(3, 1, 1).set_title("Luck("+str(int(Lucky_Unlucky[0]))+") & Unlucky("+str(int(Lucky_Unlucky[1]))+") Event Chart 1", fontsize=12)
        plt.ylim(0,5)
        
        color = "red"
        plt.tick_params(
                axis='y',
                color='red',
                width=5,
                length=10,
                direction='inout',
                colors='red')
        plt.plot(x, y1, color=color)
        
        # cancel x ticks
        plt.xticks(ticks=[])
        
        plt.subplot(3, 1, 2).set_title("Luck("+str(lucky_cnt)+") & Unlucky("+str(unlucky_cnt)+") Event Chart 2", fontsize=12)
        plt.ylim(-1,1)
        plt.tick_params(
                axis='y',
                color='red',
                width=5,
                length=10,
                direction='inout',
                colors='red')

        plt.plot(x, y1_re_gen, color=color)

        plt.xticks(ticks=[])
    
        plt.subplot(3, 1, 3).set_title("Captial of Agent", fontsize=12)
        plt.plot(x, y2[0], color=color)

        file_path_create = "../Data/" + file_name +"_plot_1_"+str(texts)+".png"
        plt.savefig(file_path_create)

        plt.savefig(file_path_create)
        self.pic_file_path = file_path_create

        img = cv2.imread(file_path_create)
        cv2.imshow(file_path_create, img)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def btn_cb_table_list(self, no, texts,file_name):

        print("btn_cb_table_list")

        # 開啟資料庫連接
        conn = MySQLdb.connect(host="localhost",    # 主機名稱
                            user="root",         # 帳號
                            password="boopann403", # 密碼
                            database = global_database,  #資料庫
                            port=3306)           # port
    
        # 使用cursor()方法操作資料庫
        cursor = conn.cursor()

        if no == List_item.LIST_ITEM_RICH_TOP:
            print("Rich list")
            buttons_lucky_list = []
            buttons_unlucky_list = []
            
            root = tk.Tk()
            root.title(file_name)
            root.geometry('900x200')
    
            sql = """SELECT Agent_Ind, C80
                        FROM {IMG}
                        ORDER BY C80 DESC
                        LIMIT 30""".format(IMG=file_name)
            result = cursor.execute(sql)
            db_info = cursor.fetchall()
            
            for i,row in enumerate(db_info):
                if row[1] == 0:
                    buttons_unlucky_list.append(Button_TvL(root, i, int(row[1]), 2,row[0], 3,self.file_name))
                else:
                    buttons_unlucky_list.append(Button_TvL(root, i, int(math.log(row[1])), 2,row[0], 3,self.file_name))
                
            conn.close()

        if no == List_item.LIST_ITEM_LUCKY_TOP:
            print("Lucky list")
            buttons_unlucky_list = []
            
            root = tk.Tk()
            root.title(file_name)
            root.geometry('900x200')

            sql = """SELECT Agent_Ind, C80
                        FROM {IMG}
                        ORDER BY LUCKY DESC
                        LIMIT 30""".format(IMG=file_name)
            result = cursor.execute(sql)
            db_info = cursor.fetchall()
            
            for i,row in enumerate(db_info):
                if row[1] == 0:
                    buttons_unlucky_list.append(Button_TvL(root, i, int(row[1]), 2,row[0], 3,self.file_name))
                else:
                    buttons_unlucky_list.append(Button_TvL(root, i, int(math.log(row[1])), 2,row[0], 3,self.file_name))

            conn.close()

        if no == List_item.LIST_ITEM_UNLUCKY_TOP:
            print("Unlucky list")
            buttons_unlucky_list = []
            
            root = tk.Tk()
            root.title(file_name)
            root.geometry('900x200')

            sql = """SELECT Agent_Ind, C80
                        FROM {IMG}
                        ORDER BY UNLUCKY DESC
                        LIMIT 30""".format(IMG=file_name)
            result = cursor.execute(sql)
            db_info = cursor.fetchall()
            
            for i,row in enumerate(db_info):
                if row[1] == 0:
                    buttons_unlucky_list.append(Button_TvL(root, i, 5+int(row[1]), 2,row[0], 3,self.file_name))
                else:
                    buttons_lucky_list.append(Button_TvL(root, i, int((row[1])**(0.5)), 2,row[0], 3,self.file_name))

            conn.close()
        
        if no == List_item.LIST_ITEM_TALENT_TOP:
            print("Talent top list")
            buttons_unlucky_list = []
            
            root = tk.Tk()
            root.title(file_name)
            root.geometry('900x200')
        
            sql = """SELECT Agent_Ind, C80,T
                        FROM {IMG}
                        ORDER BY T DESC
                        LIMIT 30""".format(IMG=file_name)
            result = cursor.execute(sql)
            db_info = cursor.fetchall()

            for i,row in enumerate(db_info):
                if row[1] == 0:
                    buttons_unlucky_list.append(Button_TvL(root, i, int(row[1]), 2,row[0], 3,self.file_name))
                else:
                    buttons_unlucky_list.append(Button_TvL(root, i, int(math.log(row[1])), 2,row[0], 3,self.file_name))

            conn.close()
        if no == List_item.LIST_ITEM_TALENT_BOTTOM:
            print("Talent bottom list")
            buttons_unlucky_list = []
            
            root = tk.Tk()
            root.title(file_name)
            root.geometry('900x200')
        
            sql = """SELECT Agent_Ind, C80,T
                        FROM {IMG}
                        ORDER BY T
                        LIMIT 30""".format(IMG=file_name)
            result = cursor.execute(sql)
            db_info = cursor.fetchall()

            for i,row in enumerate(db_info):
                if row[1] == 0:
                    buttons_unlucky_list.append(Button_TvL(root, i, int(row[1]), 2,row[0], 3,self.file_name))
                else:
                    buttons_unlucky_list.append(Button_TvL(root, i, int(math.log(row[1])), 2,row[0], 3,self.file_name))
            conn.close()
        if no == List_item.LIST_ITEM_TALENT_HIST:
            print("Talent hist")

            sql = """SELECT T
                        FROM {IMG}""".format(IMG=file_name)

            result = cursor.execute(sql)
            db_info = cursor.fetchall()
            Agents_T = []

            for i,row in enumerate(db_info):
                Agents_T.append(row[0])

            file_path_create = "../Data/" + file_name +"_plot_2_Talent_list.png"
            
            plt.figure(figsize=(12, 8), dpi=70)
            plt.hist(Agents_T, bins = 100)

            plt.savefig(file_path_create)
            self.pic_file_path = file_path_create

            img = cv2.imread(file_path_create)
            cv2.imshow(file_path_create, img)
            
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            conn.close()
            
        if no == List_item.LIST_ITEM_CAPTIAL_20_80:
            print("Property 20/80")
            buttons_unlucky_list = []

            sql = """SELECT C80
                    FROM {IMG}
                    ORDER BY C80 desc""".format(IMG=file_name)
            result = cursor.execute(sql)
            db_info = cursor.fetchall()
            C80_all = []

            for i,row in enumerate(db_info):
                C80_all.append(row[0])

            sum_20 = 0
            sum_all = 0

            for i in range(len(C80_all)):
                if i > 20:
                    sum_20  = C80_all[i] + sum_20
                sum_all = C80_all[i] + sum_all
                
            file_path_create = "../Data/" + file_name +"_plot_pie.png"

            # Draw picture
            
            x = [sum_20,(sum_all-sum_20)]
            percent = [sum_20/sum_all,(sum_all-sum_20)/(sum_all-sum_20)]

            plt.pie(x,
            radius=1.5,
            textprops={'color':'w', 'weight':'bold', 'size':12},  # 設定文字樣式
            pctdistance=0.8,
            wedgeprops={'linewidth':3,'edgecolor':'w'})   # 繪製每個扇形的外框

            plt.savefig(file_path_create)
            self.pic_file_path = file_path_create

            img = cv2.imread(file_path_create)
            cv2.imshow(file_path_create, img)
            
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            conn.close()

        if no == List_item.LIST_ITEM_CAPTIAL_LUCKY:
            print("Lucky & C")
            buttons_unlucky_list = []

            sql = """SELECT C80, LUCKY
                    FROM {IMG}
                    ORDER BY Agent_Ind""".format(IMG=file_name)
            result = cursor.execute(sql)

            db_info = cursor.fetchall()
            C80_all = []
            Lucky_cnt_list = []

            for i,row in enumerate(db_info):
                if row[0] == 0:
                    C80_all.append(0)
                else:
                    C80_all.append(math.log(row[0]))

                Lucky_cnt_list.append(row[1])

            fig = plt.figure(figsize=(10,10),dpi=70)

            plt.xlabel("Value of log(Capital)")
            plt.ylabel("Counts of Lucky")
            plt.scatter(C80_all, Lucky_cnt_list ,s=15,c="black", alpha=0.7)

            file_path_create = "../Data/" + file_name +"-plot_2.png"
            plt.savefig(file_path_create)

            img = cv2.imread(file_path_create)
            cv2.imshow(file_path_create, img)

            cv2.waitKey(0)
            cv2.destroyAllWindows()

            conn.close()
        if no == List_item.LIST_ITEM_CAPTIAL_UNLUCKY:
            print("Unlucky & C")
            buttons_unlucky_list = []

            sql = """SELECT C80, UNLUCKY
                    FROM {IMG}
                    ORDER BY Agent_Ind""".format(IMG=file_name)
            result = cursor.execute(sql)

            db_info = cursor.fetchall()
            C80_all = []
            Lucky_cnt_list = []

            for i,row in enumerate(db_info):
                if row[0] == 0:
                    C80_all.append(0)
                else:
                    C80_all.append(math.log(row[0]))

                Lucky_cnt_list.append(row[1])

            fig = plt.figure(figsize=(10,10),dpi=70)

            plt.xlabel("Value of log(Capital)")
            plt.ylabel("Counts of Lucky")
            plt.scatter(C80_all, Lucky_cnt_list ,s=15,c="black", alpha=0.7)

            file_path_create = "../Data/" + file_name +"-plot_2.png"
            plt.savefig(file_path_create)

            img = cv2.imread(file_path_create)
            cv2.imshow(file_path_create, img)

            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            conn.close()            

        if no == List_item.LIST_ITEM_LUCKY_CNT:
            print("Lucky Event Analysis")
            buttons_unlucky_list = []

            sql = """SELECT LUCKY
                        FROM {IMG}
                        ORDER BY LUCKY DESC""".format(IMG=file_name)
            result = cursor.execute(sql)
            db_info = cursor.fetchall()
            
            Lucky_cnt = {}
            Lucky_cnt_t = []
            for i,row in enumerate(db_info):
                print(i)
                Lucky_cnt_t.append(row[0])

            print("Lucky_cnt=",Lucky_cnt)
            print("len of Lucky cnt = ",len(Lucky_cnt_t))
            for i in range(len(Lucky_cnt_t)):
                Lucky_cnt[Lucky_cnt_t[i]] = Lucky_cnt_t.count(Lucky_cnt_t[i])
            
            print(Lucky_cnt)
            print("sum = ",sum(Lucky_cnt.values()))
            
            re_gen_y = []
            print("len lucky cnt key",(len(Lucky_cnt.keys())))
            print("len lucky cnt value",(len(Lucky_cnt.values())))
            for row in (Lucky_cnt.keys()):
                print("row = ",row)
                print(Lucky_cnt[row])
                if Lucky_cnt[row] == 0:
                    re_gen_y.append(0)
                else:
                    re_gen_y.append(math.log((Lucky_cnt[row])))
            
            print("reverse",re_gen_y)
            
            print("keys",Lucky_cnt.keys())
            plt.bar(Lucky_cnt.keys(),re_gen_y)

            file_path_create = "../Data/" + file_name +"-plot_3.png"
            plt.savefig(file_path_create)

            img = cv2.imread(file_path_create)
            cv2.imshow(file_path_create, img)

            cv2.waitKey(0)
            cv2.destroyAllWindows()
                        
            conn.close()   

        if no == List_item.LIST_ITEM_UNLUCKY_CNT:
            print("Lucky Event Analysis")
            buttons_unlucky_list = []

            sql = """SELECT UNLUCKY
                        FROM {IMG}
                        ORDER BY LUCKY DESC""".format(IMG=file_name)
            result = cursor.execute(sql)
            db_info = cursor.fetchall()
            
            Lucky_cnt = {}
            Lucky_cnt_t = []
            for i,row in enumerate(db_info):
                print(i)
                Lucky_cnt_t.append(row[0])

            print("Lucky_cnt=",Lucky_cnt)
            print("len of Lucky cnt = ",len(Lucky_cnt_t))
            for i in range(len(Lucky_cnt_t)):
                Lucky_cnt[Lucky_cnt_t[i]] = Lucky_cnt_t.count(Lucky_cnt_t[i])
            
            print(Lucky_cnt)
            print("sum = ",sum(Lucky_cnt.values()))
            
            re_gen_y = []
            print("len lucky cnt key",(len(Lucky_cnt.keys())))
            print("len lucky cnt value",(len(Lucky_cnt.values())))
            for row in (Lucky_cnt.keys()):
                print("row = ",row)
                print(Lucky_cnt[row])
                if Lucky_cnt[row] == 0:
                    re_gen_y.append(0)
                else:
                    re_gen_y.append(math.log((Lucky_cnt[row])))
            
            print("reverse",re_gen_y)
            
            print("keys",Lucky_cnt.keys())
            plt.bar(Lucky_cnt.keys(),re_gen_y)

            file_path_create = "../Data/" + file_name +"-plot_3.png"
            plt.savefig(file_path_create)

            img = cv2.imread(file_path_create)
            cv2.imshow(file_path_create, img)

            cv2.waitKey(0)
            cv2.destroyAllWindows()
                        
            conn.close()               

        if no == List_item.LIST_ITEM_ALL_RUN_TOP:
            print("Lucky Event Analysis")
            buttons_unlucky_list = []

            
            root = tk.Tk()
            root.title(file_name)
            root.geometry('900x300')
    

            # 使用cursor()方法操作資料庫
            cursor = conn.cursor()
        
            sql = """SHOW TABLES
                    FROM {IMG}""".format(IMG=global_database)
            result = cursor.execute(sql)
            db_info = cursor.fetchall()

            data_base_table_names = []
            

            for i,row in enumerate(db_info):
                data_base_table_names.append(row[0])

            print(data_base_table_names)
            
            Top_Agents = []
            for i,row in enumerate(data_base_table_names):
                print(row)
                sql = """SELECT Agent_Ind,C80
                        FROM {IMG} 
                        WHERE C80 =  (SELECT MAX(C80) 
    			                      	FROM {IMG})""".format(IMG=row)
        
                result = cursor.execute(sql)
                Top_Agent = cursor.fetchall()
                #Top_Agents.append(Top_Agent+data_base_table_names)
                #Top_Agent[0].append(data_base_table_names)
                
                #Top_Agents[row] = (Top_Agent[0][1],Top_Agent[0][0])
                
               #Top_Agents[Top_Agent[0][1]] = (row,Top_Agent[0][0])
                Top_Agents.append([row,Top_Agent[0][1],Top_Agent[0][0]])

            print("Top Agents",Top_Agents)
            Sorted_Agents = sorted(Top_Agents, key = lambda x : x[1], reverse=True)

            #Sorted_Agents = Top_Agents.sort(key=2)
            print("Sorted_Agents",Sorted_Agents)
            
            print("Sorted_Agents0",Sorted_Agents[0])
            print("Sorted_Agents000",Sorted_Agents[0][0])
            print("Sorted_Agents001",Sorted_Agents[0][1])
            print("Sorted_Agents002",Sorted_Agents[0][2])
            
            for i in range (len(Sorted_Agents)):
                if int(Sorted_Agents[i][1]) == 0:
                    buttons_unlucky_list.append(Button_TvL(root, i, Sorted_Agents[i][1], 2,Sorted_Agents[i][2], 3, Sorted_Agents[i][0]))
                else:
                    buttons_unlucky_list.append(Button_TvL(root, i, int(math.log(Sorted_Agents[i][1])), 2,Sorted_Agents[i][2], 3, Sorted_Agents[i][0]))

            
                #print(Sorted_Agents[0][1][2])
            #print(Top_Agents.keys())
            #print(Top_Agents.values())
            
            conn.close()
                    
        plt.clf()
            
                     
    def __repr__(self):
        #return "{"+f"\"no\":{self.no},\"btn\":{self.btn},\"fun\":{self.fun}"+"}]"
        return self.text

if __name__ == '__main__':

    # 開啟資料庫連接
    conn = MySQLdb.connect(host="localhost",    # 主機名稱
                            user="root",         # 帳號
                            password="boopann403", # 密碼
                            #database = "test_db",  #資料庫
                            port=3306)           # port
    
    # 使用cursor()方法操作資料庫
    cursor = conn.cursor()
    
    sql = """CREATE DATABASE IF NOT EXISTS `{IMG}`""".format(IMG=global_database)
    cursor.execute(sql)
    conn.close()

    # 開啟資料庫連接
    conn = MySQLdb.connect(host="localhost",    # 主機名稱
                        user="root",         # 帳號
                        password="boopann403", # 密碼
                        database = global_database,  #資料庫
                        port=3306)           # port

    # 使用cursor()方法操作資料庫
    cursor = conn.cursor()

    sql = """SHOW TABLES
            FROM {IMG}""".format(IMG=global_database)
    result = cursor.execute(sql)
    db_info = cursor.fetchall()

    basic_file_paths = []
    data_base_table_names = []
    
    conn.close()
    for i,row in enumerate(db_info):
        data_base_table_names.append(row[0])

    root = tk.Tk()
    root.title('Talent vs Lucks Analysis')
    root.geometry('400x600')
    
    buttons = []
    k = len(data_base_table_names)

    database_msg = tk.StringVar(value="tvl_v4") # 身高
    exe_cnt_msg = tk.IntVar(value=1) # 體重

    img = Image.open("Trailer-TvL.png")
    resized_img = img.resize((400,169), Image.ANTIALIAS)
    img_obj = ImageTk.PhotoImage(resized_img)

    img = Image.open("ig-nobel-prize-2022.png")
    resized_img = img.resize((400,169), Image.ANTIALIAS)
    img_obj2 = ImageTk.PhotoImage(resized_img)

    img = Image.open("start.jpg")
    resized_img = img.resize((400,169), Image.ANTIALIAS)
    img_obj3 = ImageTk.PhotoImage(resized_img)   
    
    # 設定 Label
    exe_cnt_msg = tk.Label(root, text="TvL Model Execution Count", foreground="red", padx=0, pady=0)
    exe_cnt_msg.pack()

    # 設定 Entry
    exe_cnt_msg = tk.Entry(root, foreground="green", textvariable=exe_cnt_msg)
    exe_cnt_msg.pack() 

    Button_TvL(root, 0,160,400, exe_cnt_msg,0, img_obj3)
    Button_TvL(root, 0,160,400, exe_cnt_msg,0, img_obj)
    Button_TvL(root, 0,166,400, exe_cnt_msg,0, img_obj2)    

    img = Image.open("life.jpg")
    resized_img = img.resize((30,30), Image.ANTIALIAS)
    img_obj_life = ImageTk.PhotoImage(resized_img)   

    for i in range(len(data_base_table_names)-1,-1,-1):
        buttons.append(Button_TvL(root, img_obj_life,30,30, data_base_table_names[i],1,data_base_table_names[i]))

    root.mainloop()