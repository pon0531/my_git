# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:48:42 2023

@author: USER
"""
import random
import matplotlib.pyplot as plt
import time
import numpy as np
from matplotlib.ticker import MaxNLocator
import os

PERIOD = 80 # Max value is 80 for 40 years
LUCKY_BALL_NUM = 500
AGENT_NUM = 1000 # 2 times of LUCKY BALL
BOUNDARY_X_Y = 201


class Agent:
    def __init__(self, ind, C, T, Axis_x, Axis_y):
        self.Num = ind
        self.C = [-1]*(PERIOD+1);     # Capital
        self.T = T;          # Talent
        self.Event = [0]*(PERIOD+1); # 1:lucky, -1:unlucky
        self.Point = [Axis_x,Axis_y]
        self.TouchPoint =[[-1,-1,-1,-1]] #period, ball no, touch ball x, touch ball y
        self.C[0] = C # init capital
        #self.Point[(Axis_x,Axis_y)]*40

    def __repr__(self):
        #return f"Agent_Ind:{self.Num} C:{self.C} T:{self.T} Event:{self.Event} Point:{self.Point} TouchPoint:{self.TouchPoint}"
        #return f"{self.Num},{self.C},{self.T},{self.Event},{self.Point},{self.TouchPoint}"
        if self.Num == (AGENT_NUM-1):
            return "{"+f"\"Agent_Ind\":{self.Num},\"T\":{self.T},\"Point\":{self.Point},\"C\":{self.C},\"Event\":{self.Event},\"TouchPoint\":{self.TouchPoint}"+"}]"
        else:
            return "{"+f"\"Agent_Ind\":{self.Num},\"T\":{self.T},\"Point\":{self.Point},\"C\":{self.C},\"Event\":{self.Event},\"TouchPoint\":{self.TouchPoint}"+"},"
    
    def Outoput(self):
        test = self.Point[0],self.Point[1]
        print(self.Point[0],self.Point[1])
        return test
class Circle:
    def __init__(self, ind, Event, Axis_x, Axis_y):
        self.Event = Event
        self.Point = [[Axis_x,Axis_y]]
        self.Num = ind
    def __repr__(self):
        return f"<Circle Index:{self.Num} type:{self.Event} Point:{self.Point} >"


def Generate_T_by_para(nums, mu, sigma):
    nums = [] 
    mu = 0.6
    sigma = 0.1
        
    for i in range(1000): 
        nums.append(random.normalvariate(mu, sigma))
    return nums

def ran_num(max):
    return round(random.uniform(0, max), 2)


def Circle_move(period, circle):

    lucky_circle_r = 2
    #print(circle.Point[0][0]) #x
    #print(circle.Point[0][1]) #y
   #print(circle.Point[period-1])
    #print(circle.Point[period-1][0])
    # cal the point of distance = 2 , need compare with previous point

    next_x = round(random.uniform(circle.Point[period-1][0]-1, circle.Point[period-1][0]+1), 2)
    
    
    if next_x <= 0 :
        next_x = 0

    if next_x >= BOUNDARY_X_Y :
        next_x = BOUNDARY_X_Y

    # next_y = round(((lucky_circle_r**2-(next_x-circle.Point[period-1][0])**2)**(0.5)+circle.Point[period-1][1]),2)
    
    if(0.5 >= ran_num(1)):
        next_y = round((circle.Point[period-1][1]+(lucky_circle_r**2-(next_x-circle.Point[period-1][0])**2)**(0.5)),2)
    else:
        next_y = round((circle.Point[period-1][1]-(lucky_circle_r**2-(next_x-circle.Point[period-1][0])**2)**(0.5)),2)

    if next_y <= 0 :
        next_y = 0
    if next_y >= BOUNDARY_X_Y :
        next_y = BOUNDARY_X_Y
        
    if (next_x == 0) or (next_x == BOUNDARY_X_Y) or (next_y == 0) or (next_y == BOUNDARY_X_Y):
         # print(next_x,next_y)   
         dis = ((next_x - circle.Point[period-1][0])**2 + (next_y- circle.Point[period-1][1])**2)**(0.5)
         # print(dis)

    dis = ((next_x - circle.Point[period-1][0])**2 + (next_y- circle.Point[period-1][1])**2)**(0.5)
    #print("ddis:",dis)
    


    circle.Point.append([next_x,next_y])

def Circle_touch_Agents(period, circle, agent):
    
    Touch_dis = 1
    
    # fast check for touch
    
    #if((circle.Point[period][0]-agent.Point[0])>Touch_dis 
    #   or (agent.Point[0]-circle.Point[period][0])>Touch_dis
    #   or (circle.Point[period][1]-agent.Point[1])>Touch_dis
    #   or (agent.Point[1]-circle.Point[period][1])>Touch_dis):
    #    agent.C[period] = agent.C[period-1]
        
    #    return agent.C
 
   # if((circle.Point[0][1]-agent.Point[1])>2):
    #    agent.C[period] = agent.C[period-1]
    #    return agent.C

    dis = ((circle.Point[period][0]-agent.Point[0])**2+(circle.Point[period][1]-agent.Point[1])**2)**(0.5)
    #print("dis=",round(dis,2))
    
    #if circle.Num == 0: # fist time assign to period    
    #   agent.C[period] = agent.C[period-1]
    if agent.C[period] == -1: # first assign
        agent.C[period] = agent.C[period-1]
    #print("period",period)
    #print(agent.C[period-1] ,agent.C[period] )
    
    if(dis <= Touch_dis):
        #agent.Event[period] = circle.Event;
        #print("C_EVENT: ",circle.Event)
        
        agent.TouchPoint.append([period, circle.Num, circle.Point[period][0],circle.Point[period][1]])
        if(circle.Event == 0x2): # touch the lucky ball
            #print("Touch Red")
            if(agent.T >= ran_num(1)): # check talent and randon value
                agent.C[period] = 2*(agent.C[period])
                #agent.C[period] = 2*(agent.C[period])
   
                agent.Event[period] = agent.Event[period]|0x2;
                #print("Period:",period)
                #print(agent.C[period] ,agent.C[period-1] )
                #for i in range(0,period+1):
                #    print(agent.C[i],end=" ")
                    #print()
                    #print(agent.Event[i],end=" ")
                #print()
                #for i in range(0,period):
                #    print(agent.C[i],end=" ")
                #    print()
                    #print(agent.Event[i],end=" ")
                #print()                
                #print("Touch, smart enough to perfit luck")
            else:
                #agent.Event[period] = -7
                agent.Event[period] = agent.Event[period]|0x4;
                #for i in range(0,period):
                #    print(agent.C[i],end=" ")
                #    #print(agent.Event[i],end=" ")
                #print()
                #for i in range(0,period):
                #    #print(agent.C[i],end=" ")
                #    print(agent.Event[i],end=" ")
                #print()
                #print("Touch, but smart enough to perfit luck")
           #     print()
        else: # touch the unlucky ball
                #print("touch unlucky ball")
                #agent.C[period] = (agent.C[period-1])/2
                agent.C[period] = (agent.C[period])/2
                agent.Event[period] = agent.Event[period]|0x1;
                if(agent.C[period] < 1):
                    agent.C[period] = 0;

                #for i in range(0,period):
                #    print(agent.C[i],end=" ")
                   # print(agent.Event[i],end=" ")
                #print()
                #for i in range(0,period):
                    #print(agent.C[i],end=" ")
                #    print(agent.Event[i],end=" ")
                #print()
                #print(agent.C[period-1] ,agent.C[period] )
                #print(agent.C)
                #print(agent.Event)

    #else:
    #    agent.TouchPoint.append([period, circle.Num, -1,-1])
        #print(period)
    #    print("no touch")
    #    agent.C[period] = agent.C[period-1]

    return agent.C

if __name__ == '__main__':
    
    C_init = 10
    Agents = []
    Circles = []
    print("hello Talent vs Luck")
    
    start = time.time()
    for i in range (int(LUCKY_BALL_NUM/2)):
        #Lucky points
        Circles.append(Circle(i, 0x2, ran_num(BOUNDARY_X_Y), ran_num(BOUNDARY_X_Y)))
        #Unlucky points
        Circles.append(Circle(i, 0x1, ran_num(BOUNDARY_X_Y), ran_num(BOUNDARY_X_Y)))

    # init Agents
    Agents_T = Generate_T_by_para(AGENT_NUM,0.6,0.1)
    for i in range (AGENT_NUM):
        Agents.append(Agent(i, C_init, round(Agents_T[i],2),ran_num(BOUNDARY_X_Y),ran_num(BOUNDARY_X_Y)))

    for i in range (1,PERIOD+1):
        for j in range(LUCKY_BALL_NUM):
            Circle_move(i,Circles[j])

   # for row in enumerate(Circles):
   #    print(row)

    #for row in Agents:
    #    print(row)
    
    #print(Agents[3])
    #print(Circles[3])
    #Circle_touch_Agents(1, Circles[0], Agents[0])
    #Circle_touch_Agents(2, Circles[0], Agents[0])


    for k in range(1,PERIOD+1):
         #print("Period: ",k)   
         for i in range(LUCKY_BALL_NUM):
             #print("Ball= ",i)
             for j in range(AGENT_NUM):
                #print("Agent: ",j)   
                Agents[j].C = Circle_touch_Agents(k, Circles[i], Agents[j])
            
    ##for row in Agents:
     #    print(row)
    #for i in range (AGENT_NUM):
    #    print(Agents[i].Point)
    
    scatter_lucky_x = []
    scatter_lucky_y = []
    scatter_unlucky_x = []
    scatter_unlucky_y = []    
    for lucky_bal_no in range (LUCKY_BALL_NUM):
        for period_t in range (PERIOD+1):
            #print(i)
            #print(Circles[lucky_bal_no].Point[period_t])
            if Circles[lucky_bal_no].Event == 0x2:
                scatter_lucky_x.append(Circles[lucky_bal_no].Point[period_t][0])
                scatter_lucky_y.append(Circles[lucky_bal_no].Point[period_t][1])
            else:
                scatter_unlucky_x.append(Circles[lucky_bal_no].Point[period_t][0])
                scatter_unlucky_y.append(Circles[lucky_bal_no].Point[period_t][1])
               
    #for row in Circle[0]:
    #    print(row)
    
    plt.figure(figsize=(10, 10), dpi=100)
    scatter_agent_x = []
    scatter_agent_y = []
    
    for i in range (AGENT_NUM):
        scatter_agent_x.append(Agents[i].Point[0])
        scatter_agent_y.append(Agents[i].Point[1])


    plt.scatter(scatter_agent_x, scatter_agent_y,s=20,c="black", alpha=0.7)
    plt.scatter(scatter_lucky_x, scatter_lucky_y,s=40,c="red", alpha=0.7)
    plt.scatter(scatter_unlucky_x, scatter_unlucky_y,s=40,c="green", alpha=0.7)
    
    file_name = time.strftime("%Y_%m%d_%H%M%S")
    file_path_create = "../Data/" + file_name +"-plot_1.png"
    plt.savefig(file_path_create)
    plt.show()
    
    #for i in range (5):
        #print(Agents[i])
        #print(Agents[i].C)
        #print(Agents[i].Event)
    end = time.time()
    print("Model exection time：%f sec "% (end - start))
    start = time.time()
    # 輸出結果
   
    
    
    rich_man_cnt = 0
    rich_man_id = []
    talent_man_id = []
    print("Rich Man id:",end = "")
    
    for i in range(AGENT_NUM):
        if(Agents[i].C[80] > 500):
            print("rich man:",end=" ")
            print(i,end=" ")
            print(Agents[i].T,end=" ")
            print(Agents[i].C[80])
            rich_man_cnt = rich_man_cnt +1
            rich_man_id.append(i)
        
        if(Agents[i].T > 0.8):
            print("talent man:",end=" ")
            print(i,end=" ")
            print(Agents[i].T,end=" ")
            print(Agents[i].C[80])
            talent_man_id.append(i)
            
    print()
    # print(Agents[263])
    #print("count:",len(Agents_T))
    # plotting a graph 
    plt.hist(Agents_T, bins = 100) 
    #plt.show()
    file_path_create = "../Data/" + file_name +"-plot_2.png"
    plt.savefig(file_path_create)
    print("Rich Man cnt:",rich_man_cnt)
    
    #file_name = time.strftime("%Y-%m%d-%H%M%S")
    
    for i in range(len(Agents)):
        for j in range(len(Agents[i].TouchPoint), 40):
            Agents[i].TouchPoint.append([-1,-1,-1,-1])

    file_path_create = "../Data/" + file_name +".json"
    with open(file_path_create, 'w') as f:
        #for i in range(len(rich_man_id)):
        #    print(Agents[rich_man_id[i]], file=f)
        #    print()
        print("[",end="",file=f)
        for i in range(len(Agents)):
            print(Agents[i], file=f)
       #     print(Agents[i].Outoput(), file=f)
            #print()
            #print(Circles)
    end = time.time()
    print("Output exection time：%f sec "% (end - start))
            