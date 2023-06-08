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
#from Json_Input import Json_input

PERIOD = 80 # Max value is 80 for 40 years
LUCKY_BALL_NUM = 500
AGENT_NUM = 1000 # 2 times of LUCKY BALL
BOUNDARY_X_Y = 201

# define class Agent
class Agent:
    def __init__(self, ind, C, T, Axis_x, Axis_y):
        self.Num = ind
        self.C = [-1]*(PERIOD+1);     # Capital
        self.T = T;          # Talent
        self.Event = [0]*(PERIOD+1); # 1:lucky, -1:unlucky
        self.Point = [Axis_x,Axis_y]
        self.TouchPoint =[[-1,-1,-1,-1]] #period, ball no, touch ball x, touch ball y
        self.C[0] = C # init capital


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
    
# define Luck class
class Circle:
    def __init__(self, ind, Event, Axis_x, Axis_y):
        self.Event = Event
        self.Point = [[Axis_x,Axis_y]]
        self.Num = ind
    def __repr__(self):
        if self.Num == (LUCKY_BALL_NUM/2-1) and self.Event == 1:
            return "{"+f"\"No\":{self.Num},\"Event\":{self.Event},\"Point\":{self.Point}"+"}]"
        else:
            return "{"+f"\"No\":{self.Num},\"Event\":{self.Event},\"Point\":{self.Point}"+"},"


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
    circle.Point.append([next_x,next_y])

def Circle_touch_Agents(period, circle, agent):
    
    Touch_dis = 1

    if agent.C[period] == -1: # first assign
        agent.C[period] = agent.C[period-1]

    if (circle.Point[period][0] > agent.Point[0]) and ((circle.Point[period][0]-agent.Point[0]) > 1.3):
        return agent.C
    if (circle.Point[period][0] < agent.Point[0]) and ((agent.Point[0] - circle.Point[period][0]) > 1.3):
        return agent.C

    if ((circle.Point[period][1] > agent.Point[1])) and ((circle.Point[period][1]-agent.Point[1]) > 1.3):
        return agent.C
    if ((circle.Point[period][1] < agent.Point[1])) and ((agent.Point[1] - circle.Point[period][1]) > 1.3):
        return agent.C
    dis = ((circle.Point[period][0]-agent.Point[0])**2+(circle.Point[period][1]-agent.Point[1])**2)**(0.5)

    if(dis <= Touch_dis):

        agent.TouchPoint.append([period, circle.Num, circle.Point[period][0],circle.Point[period][1]])
        if(circle.Event == 0x2): # touch the lucky ball
            #print("Touch Red")
            if(agent.T >= ran_num(1)): # check talent and randon value
                agent.C[period] = 2*(agent.C[period])
                # Lucky and get
                agent.Event[period] = agent.Event[period]|0x2;
            else:
                # lucky but not get
                agent.Event[period] = agent.Event[period]|0x4;

        else: # touch the unlucky ball
                agent.C[period] = (agent.C[period])/2
                # nulucky
                agent.Event[period] = agent.Event[period]|0x1;
                if(agent.C[period] < 1):
                    agent.C[period] = 0;
    #else:
    #    print("no touch")


    return agent.C

#if __name__ == '__main__':
def TvL_model(): 
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

    for k in range(1,PERIOD+1):
         #print("Period: ",k)   
         for i in range(LUCKY_BALL_NUM):
             #print("Ball= ",i)
             for j in range(AGENT_NUM):
                #print("Agent: ",j)   
                Agents[j].C = Circle_touch_Agents(k, Circles[i], Agents[j])

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

    plt.figure(figsize=(10, 10), dpi=70)
    scatter_agent_x = []
    scatter_agent_y = []
    
    for i in range (AGENT_NUM):
        scatter_agent_x.append(Agents[i].Point[0])
        scatter_agent_y.append(Agents[i].Point[1])

    plt.scatter(scatter_agent_x, scatter_agent_y,s=3,c="black", alpha=0.7)
    plt.scatter(scatter_lucky_x, scatter_lucky_y,s=3,c="red", alpha=0.7)
    plt.scatter(scatter_unlucky_x, scatter_unlucky_y,s=2,c="green", alpha=0.7)
    
    file_name = time.strftime("%Y_%m%d_%H%M%S")
    file_path_create = "../Data/" + file_name +"-plot_1.png"
    plt.savefig(file_path_create)
    plt.show()

    end = time.time()
    print("Model exection time：%f sec "% (end - start))
    start = time.time()

    for i in range(len(Agents)):
        for j in range(len(Agents[i].TouchPoint), 40):
            Agents[i].TouchPoint.append([-1,-1,-1,-1])

    file_path_create = "../Data/" + file_name +"_Agents.json"

    with open(file_path_create, 'w') as f:
        print("[",end="",file=f)
        for i in range(len(Agents)):
            print(Agents[i], file=f)

    end = time.time()
    print("Output exection time：%f sec "% (end - start))
    
    return file_name +"_Agents"

if __name__ == '__main__':
    TvL_model()
    
    