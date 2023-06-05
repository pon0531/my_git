# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 20:14:56 2023

@author: upon
"""

import MySQLdb
import pandas as pd
import time
import os
import matplotlib.pyplot as plt
import numpy as np
import collections
import math

ANALYSIS_AGENT_ID = 44
path = "../Data/"+"2023_0605_173648_Agents.json"

def Single_Agent_Id_Event_C(df, num):
    
    x =  np.arange(0,40.5,0.5)

    # Rege Event
    y1 = df["Event"][ANALYSIS_AGENT_ID]

    y1_re_gen = []
    lucky_cnt = 0
    unlucky_cnt = 0

    for i in range(len(df["Event"][ANALYSIS_AGENT_ID])):
        re_gen_event_value = 0;
        if df["Event"][ANALYSIS_AGENT_ID][i] == 1:   #unlucky
            re_gen_event_value = -1
            unlucky_cnt = unlucky_cnt + 1
        elif df["Event"][ANALYSIS_AGENT_ID][i] == 2: #lucky and success
            re_gen_event_value = 1
            lucky_cnt = lucky_cnt + 1
        elif df["Event"][ANALYSIS_AGENT_ID][i] == 3: # lucky and unlucky same period
            re_gen_event_value = 0
            lucky_cnt = lucky_cnt + 1
            unlucky_cnt = unlucky_cnt + 1
        elif df["Event"][ANALYSIS_AGENT_ID][i] == 4: # lucky but not success
            re_gen_event_value = 0
            lucky_cnt = lucky_cnt + 1
        elif df["Event"][ANALYSIS_AGENT_ID][i] == 5: # unlucky and lucky but no success
            re_gen_event_value = -1
            lucky_cnt = lucky_cnt + 1
            unlucky_cnt = unlucky_cnt + 1
        y1_re_gen.append(re_gen_event_value)


    print("lucky cnt:",lucky_cnt)
    print("unlucky cnt:",unlucky_cnt)
    y2 = df["C"][ANALYSIS_AGENT_ID]
    #print(y2)
    #print(df["Event"][ANALYSIS_AGENT_ID])

    plt.subplot(3, 1, 1).set_title("Luck & Unlucky Chart 1", fontsize=8)
    plt.suptitle('test')
    plt.plot(x, y1, color='red')
    plt.xticks(ticks=[])
    #plot.xticks([])
    plt.subplot(3, 1, 2).set_title("Luck & Unlucky Chart 2", fontsize=8)
    plt.plot(x, y1_re_gen, color='red')
    plt.xticks(ticks=[])

    plt.subplot(3, 1, 3).set_title("Captial of Agent", fontsize=8)
    plt.plot(x, y2, color='red')
    
    plt.show()

def Total_Agent_Id_Event_C(df):

    x =  np.arange(0,40.5,0.5)

    # Rege Event
    y1 = df["Event"][ANALYSIS_AGENT_ID]
    y1_re_gen = []

    lucky = {}
    unlucky = {}

    for i in range(len(df)):

        lucky_cnt = 0
        unlucky_cnt = 0
        re_gen_event_value = 0;

        for j in range(len(df["Event"][i])):
            #print("EVET:",df["Event"][ANALYSIS_AGENT_ID][i])
            if df["Event"][i][j] == 1:   #unlucky
                re_gen_event_value = -1
                unlucky_cnt = unlucky_cnt + 1
            elif df["Event"][i][j] == 2: #lucky and success
                re_gen_event_value = 1
                lucky_cnt = lucky_cnt + 1
            elif df["Event"][i][j] == 3: # lucky and unlucky same period
                re_gen_event_value = 0
                lucky_cnt = lucky_cnt + 1
                unlucky_cnt = unlucky_cnt + 1
            elif df["Event"][i][j] == 4: # lucky but not success
                re_gen_event_value = 0
                lucky_cnt = lucky_cnt + 1
            elif df["Event"][i][j] == 5: # unlucky and lucky but no success
                re_gen_event_value = -1
                lucky_cnt = lucky_cnt + 1
                unlucky_cnt = unlucky_cnt + 1

        lucky[df["C"][i][80]] = lucky_cnt
        unlucky[df["C"][i][80]] = unlucky_cnt

    plt.subplot(2, 1, 1)
    plt.bar(lucky.keys(), lucky.values(), color='red',width=200)
    plt.subplot(2, 1, 2)
    plt.bar(unlucky.keys(), unlucky.values(), color='green',width=200)

    plt.show()
    
def C_C_cnt(df):
   
    Agents_All_Final_C = []
    Agents_All_Final_C_log = []
    print(len(df))
    
    for i in range (len(df)):
        if(df["C"][i][80] != 0):
            Agents_All_Final_C.append(df["C"][i][80])
        else:
            Agents_All_Final_C.append(0)

    print(Agents_All_Final_C_log)

    Agents_All_Final_C_Dict = {}
    for i in range (len(df)):
        #Agents_All_Final_C_Dict[Agents_All_Final_C[i]] = Agents_All_Final_C.count(Agents_All_Final_C[i])
        Agents_All_Final_C_Dict[Agents_All_Final_C[i]] = math.log(Agents_All_Final_C.count(Agents_All_Final_C[i]),5)

    Sorted_dict_keys = sorted(Agents_All_Final_C_Dict.keys())
    
    Agents_All_C_Sorted_dict = collections.OrderedDict(sorted(Agents_All_Final_C_Dict.items()))

    x = Agents_All_C_Sorted_dict.keys()
    y = Agents_All_C_Sorted_dict.values()

    plt.subplot(2, 1, 1)
    plt.bar(x,y,width=100)
    
    plt.subplot(2, 1, 2)
    plt.hist(Agents_All_Final_C, bins = 100) 
    plt.show() 
    
def T_C(df):
    Agents_All_Final_C = []
    Agents_All_Final_T = []

    print(len(df))
    result_dict = {}
    result_dict_log = {}
    for i in range (len(df)):
        Agents_All_Final_C.append(df["C"][i][80])
        Agents_All_Final_T.append(df["T"][i])
        
        if df["T"][i] in result_dict.keys():
            if df["C"][i][80] > result_dict[df["T"][i]]:
                result_dict_log[df["T"][i]] = math.log(df["C"][i][80])
                result_dict[df["T"][i]] = (df["C"][i][80])
        else:
            if df["C"][i][80] != 0:
                result_dict_log[df["T"][i]] = math.log(df["C"][i][80])
                result_dict[df["T"][i]] = (df["C"][i][80])

    Agents_All_C_Sorted_dict = collections.OrderedDict(sorted(result_dict.items()))

    plt.subplot(2, 1, 1)
    #plt.scatter(Agents_All_Final_T, Agents_All_Final_C,s=20,c="black", alpha=0.7)
    plt.bar(Agents_All_C_Sorted_dict.keys(), Agents_All_C_Sorted_dict.values(),width=0.01)

    plt.subplot(2, 1, 2)
    plt.bar(result_dict_log.keys(), result_dict_log.values(),width=0.01)

    plt.show()
if __name__ == '__main__':

    with open(path, 'r') as f:
        df = pd.read_json(f)

        C_C_cnt(df)
        T_C(df)
        Total_Agent_Id_Event_C(df)
        Single_Agent_Id_Event_C(df, ANALYSIS_AGENT_ID)