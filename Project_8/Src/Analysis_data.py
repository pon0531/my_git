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

ANALYSIS_AGENT_ID = 501
path = "../Data/"+"2023_0605_000402.json"


def Event_C(df, num):
    
    x =  np.arange(0,40.5,0.5)

    # Rege Event
    y1 = df["Event"][ANALYSIS_AGENT_ID]
    y1_re_gen = []

    for i in range(len(df["Event"][ANALYSIS_AGENT_ID])):
        re_gen_event_value = 0;
        if df["Event"][ANALYSIS_AGENT_ID][i] == 1:
            re_gen_event_value = -1
        elif df["Event"][ANALYSIS_AGENT_ID][i] == 2:
            re_gen_event_value = 1
        elif df["Event"][ANALYSIS_AGENT_ID][i] == 3:
            re_gen_event_value = 0
        elif df["Event"][ANALYSIS_AGENT_ID][i] == 4:
            re_gen_event_value = 0
        elif df["Event"][ANALYSIS_AGENT_ID][i] == 5:
            re_gen_event_value = -1
        y1_re_gen.append(re_gen_event_value)

    y2 = df["C"][ANALYSIS_AGENT_ID]

    plt.subplot(3, 1, 1)
    plt.plot(x, y1, color='red')
    plt.subplot(3, 1, 2)
    plt.plot(x, y1_re_gen, color='red')
    plt.subplot(3, 1, 3)
    plt.plot(x, y2, color='red')
    
    plt.show()
    
def C_C_cnt(df):
   
    Agents_All_Final_C = []
    Agents_All_Final_C_log = []
    print(len(df))
    
    for i in range (len(df)):
        Agents_All_Final_C.append(df["C"][i][80])
        #Agents_All_Final_C_log.append(math.log(df["C"][i][80]))

    #print(Agents_All_Final_C)
    print(Agents_All_Final_C_log)
    #print(Agents_All_Final_C)
    #print(Agents_All_Final_C.count(5120))
    Agents_All_Final_C_Dict = {}
    for i in range (len(df)):
        #Agents_All_Final_C_Dict[Agents_All_Final_C[i]] = Agents_All_Final_C.count(Agents_All_Final_C[i])
        Agents_All_Final_C_Dict[Agents_All_Final_C[i]] = math.log(Agents_All_Final_C.count(Agents_All_Final_C[i]))

    #print(Agents_All_Final_C_Dict)
    
    #print(Agents_All_Final_C_Dict.keys())
    #print(Agents_All_Final_C_Dict.values())
    
    
    #print("sorted:",sorted(Agents_All_Final_C_Dict.keys()))
    #print("sorted type:",type(sorted(Agents_All_Final_C_Dict.keys())))
    
    Sorted_dict_keys = sorted(Agents_All_Final_C_Dict.keys())
    #print(Sorted_dict_keys)
    
    Agents_All_C_Sorted_dict = collections.OrderedDict(sorted(Agents_All_Final_C_Dict.items()))

    #print(Agents_All_C_Sorted_dict.keys())
    #print(Agents_All_C_Sorted_dict.values())

    x = Agents_All_C_Sorted_dict.keys()
    y = Agents_All_C_Sorted_dict.values()
    
    plt.figure(figsize=(10,10))
    plt.bar(x,y)
    plt.show() 
    
def T_C(df):
    Agents_All_Final_C = []
    Agents_All_Final_T = []
    
    print(len(df))
    result_dict = {}
    for i in range (len(df)):
        Agents_All_Final_C.append(df["C"][i][80])
        Agents_All_Final_T.append(df["T"][i])
        
        if df["T"][i] in result_dict.keys():
            if df["C"][i][80] > result_dict[df["T"][i]]:
                result_dict[df["T"][i]] = df["C"][i][80]
        else:
            result_dict[df["T"][i]] = df["C"][i][80]

    print(result_dict)
    Agents_All_C_Sorted_dict = collections.OrderedDict(sorted(result_dict.items()))
    print(Agents_All_C_Sorted_dict)
    
    #plt.figure(figsize=(10, 10), dpi=100)
    #print(Agents_All_Final_C)
    #print(Agents_All_Final_T)
    
    #plt.scatter(Agents_All_Final_T, Agents_All_Final_C,s=20,c="black", alpha=0.7)
    plt.bar(Agents_All_C_Sorted_dict.keys(), Agents_All_C_Sorted_dict.values(),width=0.01)
    
    #plt.bar(Agents_All_Final_T, Agents_All_Final_C,width=0.01,color="red")
    #file_name = time.strftime("%Y_%m%d_%H%M%S")
    #file_path_create = "../Data/" + file_name +"-plot_1.png"
    #lt.savefig(file_path_create)
    plt.show()
if __name__ == '__main__':
    
    with open(path, 'r') as f:
        df = pd.read_json(f)
    
    #T_C(df)
    #C_C_cnt(df) # cant draw 
    Event_C(df, ANALYSIS_AGENT_ID)