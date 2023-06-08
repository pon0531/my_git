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


global_database = "tvl_v4"
class Button_TvL:
    lobal_Test_Cnt = 0
    
    def __init__(self, root, no, h, w, texts, layer, file_name):
        self.no = no
        self.file_name = file_name
        self.text = texts
        self.root = root     
        self.pic_file_path = ""

        if layer == 0: # start model button
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
        elif layer == 1: # table button
            self.btn = tk.Button(root,
                               #text=self.Global_Test_Cnt,
                               activebackground='red',
                               activeforeground='white',
                               padx=0,pady=0,
                               font=('Arial',10,'bold'),
                               height= h, width=w,
                               bd=0,bg='black',
                               image = no,
                               command=lambda: self.btn_cb_fun(no, texts,file_name));
            self.btn.pack(side='left')
        elif layer == 5: # table button
            self.btn = tk.Button(root,
                               #text=self.Global_Test_Cnt,
                               activebackground='red',
                               activeforeground='white',
                               padx=2,pady=2,
                               font=('Arial',10,'bold'),
                               height= h, width=w,
                               bd=5,bg='red',
                               command=lambda: self.btn_cb_fun(no, texts,file_name));
            self.btn.pack()
        elif layer == 2:
            self.btn = tk.Button(root,
                               text=texts,
                               activebackground='red',
                               font=('Arial',10,'bold'),
                               height= h, width=w,
                               command=lambda: self.btn_cb_fun2(no, texts,file_name));
            self.btn.pack()
        elif layer == 3:
            self.btn = tk.Button(root,
                               text=texts,
                               activebackground='red',
                               activeforeground='white',
                               font=('Arial',10,'bold'),
                               height= h, width=w,
                               bd=4,bg='red',
                               command=lambda: self.Analysis_1(no, texts,file_name));
            self.btn.grid(row=0,column=no,sticky=tk.S+tk.W)
        elif layer == 4:
            self.btn = tk.Button(root,
                               text=texts,
                               activebackground='red',
                               activeforeground='white',
                               font=('Arial',10,'bold'),
                               height= h, width=w,
                               bd=40,bg='red',
                               command=lambda: self.Analysis_2(no, texts,file_name));
            #self.btn.grid(row=0,column=no,sticky=tk.S+tk.W)

    def btn_cb_start_model(self, no, texts,file_name):

        print("start model")

        # get cnt from label input
        exe_cnt = int(texts.get())
        
        img = Image.open("life.jpg")
        resized_img = img.resize((30,30), Image.ANTIALIAS)
        img_obj_life = ImageTk.PhotoImage(resized_img)  

        for i in range(exe_cnt):
            
            # Model create new data
            create_new_database_table = TvL_model()
            
            # SQL input data to SQL database
            Json_input(global_database,create_new_database_table)
            
            # Create new botton
            Button_TvL(root, img_obj_life,30,30, create_new_database_table,1,create_new_database_table)
        
    def btn_cb_fun(self, no, texts,file_name):
        print(no)
        print("func",texts)
        print("func",self.file_name)
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
        
    def open_pic_thread(self):
        
        print(self.pic_file_path)
        img = cv2.imread(self.pic_file_path)
        cv2.imshow(self.pic_file_path, img)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def Analysis_1(self, no, texts,file_name):
        
        print("Analysis_1",texts)
        print("Analysis_1 no",no)
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

    def btn_cb_fun2(self, no, texts,file_name):
        print(no)
        print("func2",texts)
        print("func2",self.file_name)

        # 開啟資料庫連接
        conn = MySQLdb.connect(host="localhost",    # 主機名稱
                            user="root",         # 帳號
                            password="boopann403", # 密碼
                            database = global_database,  #資料庫
                            port=3306)           # port
    
        # 使用cursor()方法操作資料庫
        cursor = conn.cursor()


        if no == 0:
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
                print(row)
                ##print(row[0])
                print("path = ",file_name)

                if row[1] == 0:
                    buttons_unlucky_list.append(Button_TvL(root, i, int(row[1]), 2,row[0], 3,self.file_name))
                else:
                    buttons_unlucky_list.append(Button_TvL(root, i, int(math.log(row[1])), 2,row[0], 3,self.file_name))
                
            conn.close()
    
        if no == 1:
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
                print(row)
                print(row[0])
                print(row[1])
                #print("path = ",file_name)
                
                if row[1] == 0:
                    buttons_unlucky_list.append(Button_TvL(root, i, int(row[1]), 2,row[0], 3,self.file_name))
                else:
                    buttons_unlucky_list.append(Button_TvL(root, i, int(math.log(row[1])), 2,row[0], 3,self.file_name))

            conn.close()

        if no == 2:
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
                print(row)
                print(row[0])
                print(row[1])
                #print("path = ",file_name)
                
                if row[1] == 0:
                    buttons_unlucky_list.append(Button_TvL(root, i, 5+int(row[1]), 2,row[0], 3,self.file_name))
                else:
                    buttons_lucky_list.append(Button_TvL(root, i, int((row[1])**(0.5)), 2,row[0], 3,self.file_name))

            conn.close()
        
        if no == 3:
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
            print(db_info)
            for i,row in enumerate(db_info):
                if row[1] == 0:
                    buttons_unlucky_list.append(Button_TvL(root, i, int(row[1]), 2,row[0], 3,self.file_name))
                else:
                    buttons_unlucky_list.append(Button_TvL(root, i, int(math.log(row[1])), 2,row[0], 3,self.file_name))

            conn.close()
        if no == 4:
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
            print(db_info)
            for i,row in enumerate(db_info):
                if row[1] == 0:
                    buttons_unlucky_list.append(Button_TvL(root, i, int(row[1]), 2,row[0], 3,self.file_name))
                else:
                    buttons_unlucky_list.append(Button_TvL(root, i, int(math.log(row[1])), 2,row[0], 3,self.file_name))
            conn.close()
        if no == 5:
            print("Talent hist")

            sql = """SELECT T
                        FROM {IMG}""".format(IMG=file_name)

            result = cursor.execute(sql)
            db_info = cursor.fetchall()
            Agents_T = []

            for i,row in enumerate(db_info):
                Agents_T.append(row[0])

            file_path_create = "../Data/" + file_name +"_plot_2_Talent_list.png"
            print(file_path_create)
            
            plt.figure(figsize=(12, 8), dpi=70)
            plt.hist(Agents_T, bins = 100)

            plt.savefig(file_path_create)
            self.pic_file_path = file_path_create

            img = cv2.imread(file_path_create)
            cv2.imshow(file_path_create, img)
            
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            conn.close()
            
        if no == 6:
            print("Property 20/80")
            buttons_unlucky_list = []

            sql = """SELECT C80
                    FROM {IMG}
                    ORDER BY C80 desc""".format(IMG=file_name)
            result = cursor.execute(sql)
            db_info = cursor.fetchall()
            C80_all = []

            for i,row in enumerate(db_info):
                print(row[0])
                C80_all.append(row[0])

            sum_20 = 0
            sum_all = 0
            print(C80_all)
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

        if no == 7:
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
                print(row[0])
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
        if no == 8:
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
                print(row[0])
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