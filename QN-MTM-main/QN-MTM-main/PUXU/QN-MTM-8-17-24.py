#Section1 setup
import random
from random import expovariate, randint
import sys
from turtle import pos, position
from matplotlib.figure import Figure
import simpy
import math
import numpy as np
from numpy import arange as npar
import pyautogui as ag
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog
from tkinter import simpledialog, messagebox
import os
import time

import pickle
import shutil
from tkinter import Button

from tkinter import messagebox


#Section2
global track1D_curse_loc, track1D_freq, track1D_amp, track1D_response
global track2D_target_loc_x, track2D_target_loc_y, track2D_cursor_loc_x, track2D_cursor_loc_y, track2D_freq, track2D_amp, track2D_response
global judgei_target_dic
global N
global length_count

def tmu_to_milliseconds(tmu):
    """
    Converts TMU (Time Measurement Unit) to milliseconds.
    
    Parameters:
    tmu (float): The time in TMU.
    
    Returns:
    float: The time in milliseconds.
    """
    return tmu * 36  # 1 TMU = 36 milliseconds

ppt=1000
cpt=35
mpt=24
dummy= 1000
#2.1 GUI Data record


#GUI Data Record 
global saved
saved=0

if saved==0:
    global path
    path='backup/'
    def mkdir(path):
        path=path.rstrip('/')
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs (path)
        else:
            return False
    mkdir(path)
  

#save variable
def save_var(v,filename):
    f=open(filename,'wb')
    pickle.dump(v,f)
    f.close()
    return filename

def load_var(filename):
    f=open(filename,'rb')
    r=pickle.load(f)
    f.close()
    return r

def copy_search_file(srcDir,desDir):
    ls=os.listdir(srcDir)
    for line in ls:
        filePath=os.path.join(srcDir,line)
        if os.path.isfile(filePath):
            shutil.copy(filePath,desDir)
    shutil.rmtree(srcDir)


#2.2 General GUI classes
#4.5 Servers
env = simpy.Environment()
class QN_MHP (object):
    
        
    server1 = simpy.Resource(env,10e5)
    server2= simpy.Resource(env, 4)
    server3 = simpy.Resource(env, 4)
    server4 = simpy.Resource(env,5)
    server5 = simpy.Resource(env,10e5)
    server6= simpy.Resource(env, 4)
    server7 = simpy.Resource(env, 4)
    server8 = simpy.Resource(env,5)
    serverA = simpy.PreemptiveResource(env,4)
    serverB = simpy.PreemptiveResource(env,4)
    serverC = simpy.Resource(env,5)
    serverD = simpy.Resource(env,10e5)
    serverE = simpy.Resource(env,1)
    serverF = simpy.Resource(env,1)
    serverG = simpy.Resource(env,10e5)
    serverW = simpy.Resource(env,1)
    serverY = simpy.Resource(env,2)
    serverZ = simpy.Resource(env,5)
    righthand = simpy.Resource(env,1)
    lefthand = simpy.Resource(env,1)
    eyes = simpy.Resource(env,1)
    
    server1_b = simpy.Resource(env,10e5)
    server2_b= simpy.Resource(env, 4)
    server3_b = simpy.Resource(env, 4)
    server4_b = simpy.Resource(env,5)
    server5_b = simpy.Resource(env,10e5)
    server6_b= simpy.Resource(env, 4)
    server7_b = simpy.Resource(env, 4)
    server8_b = simpy.Resource(env,5)
    serverA_b = simpy.PreemptiveResource(env,4)
    serverB_b = simpy.PreemptiveResource(env,4)
    serverC_b = simpy.Resource(env,5)
    serverD_b = simpy.Resource(env,10e5)
    serverE_b = simpy.Resource(env,1)
    serverF_b = simpy.Resource(env,1)
    serverG_b = simpy.Resource(env,10e5)
    serverW_b = simpy.Resource(env,1)
    serverY_b = simpy.Resource(env,2)
    serverZ_b = simpy.Resource(env,5)
    righthand_b = simpy.Resource(env,1)
    lefthand_b = simpy.Resource(env,1)
    eyes_b = simpy.Resource(env,1)

    left_arm_hand = simpy.Resource(env, capacity=1)
    right_arm_hand = simpy.Resource(env, capacity=1)
    body_leg_foot = simpy.Resource(env, capacity=1)
    eyes = simpy.Resource(env, capacity=1)
   
    def __init__(self, env):
        self.env = env
        

#perception
def server1(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):
    with qn_mhp.server1.request() as request:
        yield request
        yield env.timeout(ppt)


def server2(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):
    if anim==1:       
        Structure_and_Animation().enter(qn_mhp.server2, '2', '1_2', i, j, k,generation)
        with qn_mhp.server2.request() as request:
            yield request
            Structure_and_Animation().add('2', i, j, k,generation)
            yield env.timeout(ppt)
        outserver_dic[2]=1
        Structure_and_Animation().delete(i, j, k, '2',generation)
        Structure_and_Animation().enter(qn_mhp.server4, '4', '2_4', i, j, k,generation)

    else:       
        with qn_mhp.server2.request() as request:
            yield request
            yield env.timeout(ppt)
        outserver_dic[2]=1
            
def server3(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):  
    if anim==1:
        Structure_and_Animation().enter(qn_mhp.server3, '3', '1_3', i, j, k,generation)
        with qn_mhp.server3.request() as request:        
            yield request
            Structure_and_Animation().add('3', i, j, k,generation)
            yield env.timeout(ppt) 
        outserver_dic[3]=1
        Structure_and_Animation().delete(i, j, k, '3',generation)
        Structure_and_Animation().enter(qn_mhp.server4, '4', '3_4', i, j, k,generation)
    else:
        with qn_mhp.server3.request() as request:        
            yield request
            yield env.timeout(ppt) 
        outserver_dic[3]=1

def server4(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):
    with qn_mhp.server4.request() as request:
        yield request
        yield env.timeout(ppt)

def server5(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):
    with qn_mhp.server5.request() as request:
        yield request
        yield env.timeout(ppt)

def server6(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):
    if anim==1:       
        Structure_and_Animation().enter(qn_mhp.server6, '6', '5_6', i, j, k,generation)
        with qn_mhp.server6.request() as request:
            yield request
            Structure_and_Animation().add('6', i, j, k,generation)
            yield env.timeout(ppt)
        outserver_dic[6]=1
        Structure_and_Animation().delete(i, j, k, '6',generation)
        Structure_and_Animation().enter(qn_mhp.server8, '8', '6_8', i, j, k,generation)
    else:       
        with qn_mhp.server6.request() as request:
            yield request
            yield env.timeout(ppt)
        outserver_dic[6]=1

def server7(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):  
    if anim==1:
        Structure_and_Animation().enter(qn_mhp.server7, '7', '5_7', i, j, k,generation)
        with qn_mhp.server7.request() as request:        
            yield request
            Structure_and_Animation().add('7', i, j, k,generation)
            yield env.timeout(ppt) 
        outserver_dic[7]=1
        Structure_and_Animation().delete(i, j, k, '7',generation)
        Structure_and_Animation().enter(qn_mhp.server8, '8', '7_8', i, j, k,generation)
    else:
        with qn_mhp.server7.request() as request:        
            yield request
            yield env.timeout(ppt) 
        outserver_dic[7]=1

def server8(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):
    with qn_mhp.server8.request() as request:
        yield request
        yield env.timeout(ppt)

def left_arm_hand_server(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    with qn_mhp.left_arm_hand.request() as request:
        yield request
        yield env.timeout(dummy)  # Simulate processing time

def right_arm_hand_server(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    with qn_mhp.right_arm_hand.request() as request:
        yield request
        yield env.timeout(dummy)  # Simulate processing time

def body_leg_foot_server(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    with qn_mhp.body_leg_foot.request() as request:
        yield request
        yield env.timeout(dummy)  # Simulate processing time

def eyes_server(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    with qn_mhp.eyes.request() as request:
        yield request
        yield env.timeout(dummy)  # Simulate processing time


#cognition
def serverA(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,prio,generation):
    if anim==1:
        if outserver_dic[4]==1:
            Structure_and_Animation().enter(qn_mhp.serverA,'A','4_A', i, j, k,generation)
        else:
            Structure_and_Animation().enter(qn_mhp.serverA,'A','8_A', i, j, k,generation)
        with qn_mhp.serverA.request(priority=prio) as request:                       
            yield request   
            Structure_and_Animation().add('A', i, j, k,generation)         
            try:
                yield env.timeout(cpt)  #use cpt time
                             
            except simpy.Interrupt:
                forced_exit_dic[(i[0],k)]=['%.2fmsec'%(arrival_time), attribute]  
                print('%.2fmsec, entity %s is forced to exit serverA'%(env.now, (i[0],k)))
              
            Structure_and_Animation().delete(i, j, k, 'A',generation)   
    else:
        with qn_mhp.serverA.request(priority=prio) as request:                       
            yield request                   
            try:
                yield env.timeout(cpt)  #use cpt time               
            except simpy.Interrupt:
                forced_exit_dic[(i[0],k)]=['%.2fmsec'%(arrival_time), attribute]  
                print('%.2fmsec, entity %s is forced to exit serverA'%(env.now, (i[0],k)))
        
def serverB(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,prio,generation):
    if anim==1:
        if outserver_dic[4]==2:
            Structure_and_Animation().enter(qn_mhp.serverB,'B','4_B', i, j, k,generation)
        else:
            Structure_and_Animation().enter(qn_mhp.serverB,'B','8_B', i, j, k,generation)
        with qn_mhp.serverB.request(priority=prio) as request:                       
            yield request 
            Structure_and_Animation().add('B', i, j, k,generation)         
            try:
                yield env.timeout(cpt)  #use cpt time
                              
            except simpy.Interrupt:
                forced_exit_dic[(i[0],k)]=['%.2fmsec'%(arrival_time), attribute]  
                print('%.2fmsec, entity %s is forced to exit serverB'%(env.now, (i[0],k)))
            Structure_and_Animation().delete(i, j, k, 'B',generation)  
    else:
        with qn_mhp.serverB.request(priority=prio) as request:                       
            yield request                   
            try:
                yield env.timeout(cpt)  #use cpt time               
            except simpy.Interrupt:
                forced_exit_dic[(i[0],k)]=['%.2fmsec'%(arrival_time), attribute]  
                print('%.2fmsec, entity %s is forced to exit serverB'%(env.now, (i[0],k)))

def serverC(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):
    with qn_mhp.serverC.request() as request:
        yield request
        yield env.timeout(cpt)    
        
def serverF(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):
    with qn_mhp.serverC.request() as request:
        yield request
        yield env.timeout(cpt)  

#To be decided:
    #serverD, serverG, serverH, 

#Motor
def serverW(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):
    with qn_mhp.serverW.request() as request:
        yield request
        yield env.timeout(mpt)  
        
def serverY(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):
    with qn_mhp.serverW.request() as request:
        yield request
        yield env.timeout(mpt)  
        
def serverZ(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):
    with qn_mhp.serverW.request() as request:
        yield request
        yield env.timeout(mpt)  
        
def server22(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):
    with qn_mhp.serverW.request() as request:
        yield request
        yield env.timeout(20)  

#To be decided: 
    #serverV, server21, ser server23, server24

def calculate_tmu_for_reach(distance_cm, reach_case, hand_motion_before, hand_motion_after):
    # Define the TMU lookup table based on the image provided
    tmu_table = {
        'A': {  # Case A
            2.0: 2.0, 2.5: 2.5, 5.1: 4.0, 7.6: 5.3, 10.1: 6.1, 12.5: 6.5, 15.2: 7.0, 17.8: 7.4, 20.3: 7.9,
            22.9: 8.3, 25.4: 8.7, 30.5: 9.6, 35.6: 10.5, 40.6: 11.4, 45.7: 12.3, 50.8: 13.1, 55.9: 14.0,
            61.0: 14.9, 66.0: 15.8, 71.1: 16.7, 76.2: 17.5
        },
        'B': {  # Case B
            2.0: 2.0, 2.5: 2.5, 5.1: 4.0, 7.6: 5.3, 10.1: 6.4, 12.5: 7.8, 15.2: 8.6, 17.8: 9.3, 20.3: 10.1,
            22.9: 10.8, 25.4: 11.5, 30.5: 12.9, 35.6: 14.4, 40.6: 15.8, 45.7: 17.2, 50.8: 18.6, 55.9: 20.1,
            61.0: 21.5, 66.0: 22.9, 71.1: 24.4, 76.2: 25.8
        },
        'C_or_D': {  # Case C or D
            2.0: 2.0, 2.5: 3.6, 5.1: 5.9, 7.6: 7.3, 10.1: 8.4, 12.5: 9.4, 15.2: 10.1, 17.8: 10.8, 20.3: 11.5,
            22.9: 12.2, 25.4: 12.9, 30.5: 14.2, 35.6: 15.6, 40.6: 17.0, 45.7: 18.4, 50.8: 19.8, 55.9: 21.2,
            61.0: 22.5, 66.0: 23.9, 71.1: 25.3, 76.2: 26.7
        },
        'E': {  # Case E
            2.0: 2.0, 2.5: 2.4, 5.1: 3.8, 7.6: 5.3, 10.1: 6.8, 12.5: 7.4, 15.2: 8.0, 17.8: 8.7, 20.3: 9.3,
            22.9: 9.9, 25.4: 10.5, 30.5: 11.8, 35.6: 13.0, 40.6: 14.2, 45.7: 15.5, 50.8: 16.7, 55.9: 18.0,
            61.0: 19.2, 66.0: 20.4, 71.1: 21.7, 76.2: 22.9
        }
    }
    
    hand_motion_tmu = {
        'A': {  # Hand in Motion A
            2.0: 1.6, 2.5: 2.3, 5.1: 3.5, 7.6: 4.5, 10.1: 4.9, 12.5: 5.3, 15.2: 5.7, 17.8: 6.1, 20.3: 6.5,
            22.9: 6.9, 25.4: 7.3, 30.5: 8.1, 35.6: 8.9, 40.6: 9.7, 45.7: 10.5, 50.8: 11.3, 55.9: 12.1,
            61.0: 12.9, 66.0: 13.7, 71.1: 14.5, 76.2: 15.3
        },
        'B': {  # Hand in Motion B
            2.0: 1.6, 2.5: 2.3, 5.1: 2.7, 7.6: 3.6, 10.1: 4.3, 12.5: 5.0, 15.2: 5.7, 17.8: 6.5, 20.3: 7.2,
            22.9: 7.9, 25.4: 8.6, 30.5: 10.1, 35.6: 11.5, 40.6: 12.9, 45.7: 14.4, 50.8: 15.8, 55.9: 17.3,
            61.0: 18.8, 66.0: 20.2, 71.1: 21.7, 76.2: 23.2
        }
    }
    
    # Round the distance to the nearest predefined distance in the table
    distances = sorted(tmu_table['A'].keys())
    rounded_distance = min(distances, key=lambda x: abs(x - distance_cm))
    
    # Calculate the base TMU based on the reach case
    if reach_case in ['A', 'B', 'E']:
        tmu = tmu_table[reach_case][rounded_distance]
    elif reach_case in ['C', 'D']:
        tmu = tmu_table['C_or_D'][rounded_distance]
    else:
        raise ValueError(f"Unknown reach case: {reach_case}")
    
    # Add TMU for hand motion before or after if applicable
    if hand_motion_before == 'Yes' or hand_motion_after == 'Yes':
        if hand_motion_before == 'Yes':
            tmu += hand_motion_tmu['A'][rounded_distance]
        if hand_motion_after == 'Yes':
            tmu += hand_motion_tmu['B'][rounded_distance]
    
    return tmu

def Reach(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Reach starts for entity #{i[0], k}')
    
    # Retrieve the relevant information from the attribute
    arm = attribute.get('arm')  # 'left' or 'right'
    reach_case = attribute.get('reach_case')  # 'A', 'B', 'C', 'D', or 'E'
    distance_cm = attribute.get('distance_cm')  # The distance of the reach
    hand_motion_before = attribute.get('hand_motion_before')  # 'Yes' or 'No'
    hand_motion_after = attribute.get('hand_motion_after')  # 'Yes' or 'No'

    if not all([arm, reach_case, distance_cm, hand_motion_before, hand_motion_after]):
        print(f"Missing attribute for entity: {i}. Attributes received: {attribute}")
        return
    
    # Calculate the TMU for the reach
    tmu = calculate_tmu_for_reach(distance_cm, reach_case, hand_motion_before, hand_motion_after)
    
    # Convert TMU to milliseconds
    ppt = tmu_to_milliseconds(tmu)
    
    # Process with the left or right arm/hand based on the attribute
    if arm == 'left':
        with qn_mhp.left_arm_hand.request() as request:
            yield request  # Request the left arm/hand resource
            yield env.timeout(ppt)  # Simulate processing time
            update_total_time('Left Arm/Hand', ppt)
    elif arm == 'right':
        with qn_mhp.right_arm_hand.request() as request:
            yield request  # Request the right arm/hand resource
            yield env.timeout(ppt)  # Simulate processing time
            update_total_time('Right Arm/Hand', ppt)
    else:
        print(f'Unknown arm attribute for entity: {i}, expected "left" or "right", got: {arm}')

    print(f'{env.now:.2f} msec, Reach ends for entity #{i[0], k}')

            
        
def calculate_tmu_for_move(distance, weight, move_case, hand_in_motion):
    # Define the distance intervals and corresponding TMU values based on the table
    distance_intervals = [
        0.75, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30
    ]
    
    # Define the constant and factor based on the weight and move_case
    if weight <= 2.5:
        constant, factor = 0, 1.00
    elif weight <= 7.5:
        constant, factor = 2.2, 1.06
    elif weight <= 12.5:
        constant, factor = 3.9, 1.11
    elif weight <= 17.5:
        constant, factor = 5.6, 1.17
    elif weight <= 22.5:
        constant, factor = 7.4, 1.22
    elif weight <= 27.5:
        constant, factor = 9.1, 1.28
    elif weight <= 32.5:
        constant, factor = 10.8, 1.33
    elif weight <= 37.5:
        constant, factor = 12.5, 1.39
    elif weight <= 42.5:
        constant, factor = 14.3, 1.44
    elif weight <= 47.5:
        constant, factor = 16.0, 1.50
    else:
        raise ValueError("Weight exceeds the limit in the table.")

    # Determine the distance index
    for i, d in enumerate(distance_intervals):
        if distance <= d:
            distance_index = i
            break
    else:
        raise ValueError("Distance exceeds the limit in the table.")
    
    # Base TMU values for each case
    base_tmu_values = {
        "A": [2.0, 2.5, 3.6, 4.9, 6.1, 7.3, 8.1, 8.9, 9.7, 10.5, 11.3, 12.9, 14.4, 16.0, 17.6, 19.2, 20.8, 22.4, 24.0, 25.5, 27.1],
        "B": [2.0, 2.5, 4.6, 5.7, 6.9, 8.0, 8.9, 9.7, 10.5, 11.5, 12.2, 13.9, 15.8, 17.6, 19.4, 20.6, 22.4, 24.0, 25.5, 27.1],
        "C": [2.0, 3.6, 4.9, 6.7, 8.4, 9.2, 10.3, 11.1, 11.5, 12.7, 13.5, 15.2, 16.8, 18.7, 20.4, 23.8, 25.5, 27.3, 29.0, 30.7]
    }
    
    base_tmu = base_tmu_values[move_case][distance_index]

    # Apply formula to calculate final TMU
    tmu = base_tmu + (constant + (factor * base_tmu))
    
    # Add extra TMU if hand was in motion before/after
    if hand_in_motion == "Yes":
        tmu += 1.7 if move_case == "A" else 2.9
    
    return tmu

def Move(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Move starts for entity #{i[0], k}')
    
    # Extract relevant attributes
    distance = attribute.get('distance')
    weight = attribute.get('weight')
    move_case = attribute.get('move_case')
    hand_in_motion = attribute.get('hand_in_motion')

    # Calculate TMU based on the given parameters
    tmu = calculate_tmu_for_move(distance, weight, move_case, hand_in_motion)
    
    # Convert TMU to milliseconds
    ppt = tmu_to_milliseconds(tmu)
    
    # Process with left or right arm/hand based on the 'arm' attribute
    arm = attribute.get('arm')
    
    if arm == 'left':
        with qn_mhp.left_arm_hand.request() as request:
            yield request  # Request the left arm/hand resource
            yield env.timeout(ppt)  # Simulate processing time
            update_total_time('Left Arm/Hand', ppt)
    elif arm == 'right':
        with qn_mhp.right_arm_hand.request() as request:
            yield request  # Request the right arm/hand resource
            yield env.timeout(ppt)  # Simulate processing time
            update_total_time('Right Arm/Hand', ppt)
    else:
        print(f'Unknown arm attribute for entity: {i}, expected "left" or "right", got: {arm}')

    print(f'{env.now:.2f} msec, Move ends for entity #{i[0], k}')


            

def Turn(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Turn starts for entity #{i[0], k}')
    
    degree_of_turn = int(attribute.get('degree_of_turn', 0))  # Get the degree of turn
    weight_class = attribute.get('weight_of_turned_object', '').lower()  # Get the weight class

    # Use the table to determine the correct TMU based on degree and weight
    tmu = 0
    if weight_class == "small":
        if degree_of_turn <= 45:
            tmu = 3.5
        elif degree_of_turn <= 90:
            tmu = 5.4
        elif degree_of_turn <= 135:
            tmu = 7.4
        elif degree_of_turn <= 180:
            tmu = 9.4
    elif weight_class == "medium":
        if degree_of_turn <= 45:
            tmu = 5.5
        elif degree_of_turn <= 90:
            tmu = 8.5
        elif degree_of_turn <= 135:
            tmu = 11.6
        elif degree_of_turn <= 180:
            tmu = 14.8
    elif weight_class == "large":
        if degree_of_turn <= 45:
            tmu = 10.5
        elif degree_of_turn <= 90:
            tmu = 16.2
        elif degree_of_turn <= 135:
            tmu = 22.2
        elif degree_of_turn <= 180:
            tmu = 28.2

    # Convert TMU to milliseconds
    processing_time = tmu_to_milliseconds(tmu)
    
    with qn_mhp.body_leg_foot.request() as request:
        yield request  # Request the body/leg/foot resource
        yield env.timeout(processing_time)  # Simulate processing time
        update_total_time('Body/Leg/Foot', processing_time)
    
    print(f'{env.now:.2f} msec, Turn ends for entity #{i[0], k}')


    

def Apply_pressure(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Apply Pressure starts for entity #{i[0], k}')

    # Load the selection data
    apply_pressure_data = load_var(path+'/apply_pressure_entity_dic.txt')
    selected_case = apply_pressure_data.get("case_of_apply_pressure", "A")  # Default to "A" if not found

    # Identify the TMU value based on the case
    if selected_case == "A":
        tmu_value = 10.6  # TMU for Case A
    elif selected_case == "B":
        tmu_value = 16.2  # TMU for Case B
    else:
        raise ValueError(f"Unknown case: {selected_case}")

    # Convert TMU to milliseconds
    simulation_time = tmu_to_milliseconds(tmu_value)

    # Process with left or right arm/hand based on attribute
    arm = attribute.get('arm')  # Get the arm attribute from the dictionary
    
    if arm == 'left':
        with qn_mhp.left_arm_hand.request() as request:
            yield request  # Request the left arm/hand resource
            yield env.timeout(simulation_time)  # Simulate processing time
            update_total_time('Left Arm/Hand', simulation_time)
    elif arm == 'right':
        with qn_mhp.right_arm_hand.request() as request:
            yield request  # Request the right arm/hand resource
            yield env.timeout(simulation_time)  # Simulate processing time
            update_total_time('Right Arm/Hand', simulation_time)
    else:
        print(f'Unknown arm attribute for entity: {i}, expected "left" or "right", got: {arm}')

    print(f'{env.now:.2f} msec, Apply Pressure ends for entity #{i[0], k}')



def Grasp(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Grasp starts for entity #{i[0], k}')
    
    # Load the grasp data
    grasp_data = load_var(path + '/grasp_entity_dic.txt')
    case_of_grasp = grasp_data.get("case_of_grasp")

    # Assign TMU based on the case
    tmu_values = {
        "1A": 2.0,
        "1B": 3.5,
        "1C1": 7.3,
        "1C2": 8.7,
        "1C3": 10.8,
        "2": 5.6,
        "3": 5.6,
        "4A": 7.3,
        "4B": 9.1,
        "4C": 12.9,
        "5": 0.0
    }

    tmu = tmu_values.get(case_of_grasp, 0)
    duration_ms = tmu * 36  # Convert TMU to milliseconds
    
    # Process with left or right arm/hand based on attribute
    arm = attribute.get('arm')  # Get the arm attribute from the dictionary

    if arm == 'left':
        with qn_mhp.left_arm_hand.request() as request:
            yield request  # Request the left arm/hand resource
            yield env.timeout(duration_ms)  # Simulate processing time
            update_total_time('Left Arm/Hand', duration_ms)
    elif arm == 'right':
        with qn_mhp.right_arm_hand.request() as request:
            yield request  # Request the right arm/hand resource
            yield env.timeout(duration_ms)  # Simulate processing time
            update_total_time('Right Arm/Hand', duration_ms)
    else:
        print(f'Unknown arm attribute for entity: {i}, expected "left" or "right", got: {arm}')

    print(f'{env.now:.2f} msec, Grasp ends for entity #{i[0], k}')

                
                
def Position(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Position starts for entity #{i[0], k}')
    
    # Retrieve relevant attributes
    arm = attribute.get('arm')  # Get the arm attribute from the dictionary
    class_of_fit = attribute.get('class_of_fit')  # Get the class of fit
    symmetry = attribute.get('symmetry')  # Get the symmetry type
    easy_to_handle = attribute.get('easy_to_handle')  # Get the ease of handling attribute

    # Determine TMU based on class of fit, symmetry, and ease of handling
    tmu_value = 0
    if class_of_fit == "1: Loose":
        if symmetry == "S":
            tmu_value = 5.6 if easy_to_handle == "Yes" else 11.2
        elif symmetry == "SS":
            tmu_value = 9.1 if easy_to_handle == "Yes" else 14.7
        elif symmetry == "NS":
            tmu_value = 10.4 if easy_to_handle == "Yes" else 16.0
    elif class_of_fit == "2: Close":
        if symmetry == "S":
            tmu_value = 16.2 if easy_to_handle == "Yes" else 21.8
        elif symmetry == "SS":
            tmu_value = 19.7 if easy_to_handle == "Yes" else 25.3
        elif symmetry == "NS":
            tmu_value = 21.0 if easy_to_handle == "Yes" else 26.6
    elif class_of_fit == "3: Exact":
        if symmetry == "S":
            tmu_value = 43.0 if easy_to_handle == "Yes" else 48.6
        elif symmetry == "SS":
            tmu_value = 46.5 if easy_to_handle == "Yes" else 52.1
        elif symmetry == "NS":
            tmu_value = 47.8 if easy_to_handle == "Yes" else 53.4
    
    # Convert TMU to milliseconds
    ppt = tmu_to_milliseconds(tmu_value)
    
    # Process with left or right arm/hand based on attribute
    if arm == 'left':
        with qn_mhp.left_arm_hand.request() as request:
            yield request  # Request the left arm/hand resource
            yield env.timeout(ppt)  # Simulate processing time
            update_total_time('Left Arm/Hand', ppt)
    elif arm == 'right':
        with qn_mhp.right_arm_hand.request() as request:
            yield request  # Request the right arm/hand resource
            yield env.timeout(ppt)  # Simulate processing time
            update_total_time('Right Arm/Hand', ppt)
    else:
        print(f'Unknown arm attribute for entity: {i}, expected "left" or "right", got: {arm}')

    print(f'{env.now:.2f} msec, Position ends for entity #{i[0], k}')


def Release(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Release starts for entity #{i[0], k}')

    # Load the selection data
    release_data = load_var(path+'/release_entity_dic.txt')
    selected_case = release_data.get("case_of_release", "1")  # Default to "1" if not found

    # Identify the TMU value based on the case
    if selected_case == "1":
        tmu_value = 2.0  # TMU for Case 1
    elif selected_case == "2":
        tmu_value = 0.0  # TMU for Case 2
    else:
        raise ValueError(f"Unknown case: {selected_case}")

    # Convert TMU to milliseconds
    simulation_time = tmu_to_milliseconds(tmu_value)

    # Process with left or right arm/hand based on attribute
    arm = attribute.get('arm')  # Get the arm attribute from the dictionary
    
    if arm == 'left':
        with qn_mhp.left_arm_hand.request() as request:
            yield request  # Request the left arm/hand resource
            yield env.timeout(simulation_time)  # Simulate processing time
            update_total_time('Left Arm/Hand', simulation_time)
    elif arm == 'right':
        with qn_mhp.right_arm_hand.request() as request:
            yield request  # Request the right arm/hand resource
            yield env.timeout(simulation_time)  # Simulate processing time
            update_total_time('Right Arm/Hand', simulation_time)
    else:
        print(f'Unknown arm attribute for entity: {i}, expected "left" or "right", got: {arm}')

    print(f'{env.now:.2f} msec, Release ends for entity #{i[0], k}')

    


def Disengage(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Disengage starts for entity #{i[0], k}')
    
    # Load the disengage data
    disengage_data = load_var(path + '/disengage_entity_dic.txt')
    class_of_fit = disengage_data.get("class_of_fit")
    ease_of_handling = disengage_data.get("ease_of_handling")

    # Determine the TMU based on class of fit and ease of handling
    tmu_values = {
        ("1", "easy"): 4.0,
        ("1", "difficult"): 5.7,
        ("2", "easy"): 7.5,
        ("2", "difficult"): 11.8,
        ("3", "easy"): 22.9,
        ("3", "difficult"): 34.7,
    }

    tmu = tmu_values.get((class_of_fit, ease_of_handling), 0)
    duration_ms = tmu * 1.028  # Convert TMU to milliseconds

    # Process with left or right arm/hand based on attribute
    arm = attribute.get('arm')  # Get the arm attribute from the dictionary

    if arm == 'left':
        with qn_mhp.left_arm_hand.request() as request:
            yield request  # Request the left arm/hand resource
            yield env.timeout(duration_ms)  # Simulate processing time
            update_total_time('Left Arm/Hand', duration_ms)
    elif arm == 'right':
        with qn_mhp.right_arm_hand.request() as request:
            yield request  # Request the right arm/hand resource
            yield env.timeout(duration_ms)  # Simulate processing time
            update_total_time('Right Arm/Hand', duration_ms)
    else:
        print(f'Unknown arm attribute for entity: {i}, expected "left" or "right", got: {arm}')

    print(f'{env.now:.2f} msec, Disengage ends for entity #{i[0], k}')

        
    
def Sidestep(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Sidestep starts for entity #{i[0], k}')

    # Load the selection data
    sidestep_data = load_var(path+'/sidestep_entity_dic.txt')
    selected_case = sidestep_data.get("case_of_sidestep", "1")  # Default to "1" if not found

    # Identify the TMU value based on the case
    if selected_case == "1":
        tmu_value = 17.0  # TMU for Case 1
    elif selected_case == "2":
        tmu_value = 34.1  # TMU for Case 2
    else:
        raise ValueError(f"Unknown case: {selected_case}")

    # Convert TMU to milliseconds
    simulation_time = tmu_to_milliseconds(tmu_value)

    # Process with body/leg/foot based on attribute
    body_part = attribute.get('body_part')  # Get the body part attribute from the dictionary
    
    if body_part == 'body':
        with qn_mhp.body_leg_foot.request() as request:
            yield request  # Request the body/leg/foot resource
            yield env.timeout(simulation_time)  # Simulate processing time
            update_total_time('Body/Leg/Foot', simulation_time)
    else:
        print(f'Unknown body part attribute for entity: {i}, expected "body", got: {body_part}')
    
    print(f'{env.now:.2f} msec, Sidestep ends for entity #{i[0], k}')


def Foot_motion_hinge_at_ankle(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Foot motion hinge at ankle starts for entity #{i[0], k}')
    duration_ms = tmu_to_milliseconds(8.5)  # Convert TMU to milliseconds
    yield env.timeout(duration_ms)  # Simulate processing time
    update_total_time('Body/Leg/Foot', duration_ms)
    print(f'{env.now:.2f} msec, Foot motion hinge at ankle ends for entity #{i[0], k}')

def Foot_motion_with_heavy_pressure(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Foot motion with heavy pressure starts for entity #{i[0], k}')
    duration_ms = tmu_to_milliseconds(19.1)  # Convert TMU to milliseconds
    yield env.timeout(duration_ms)  # Simulate processing time
    update_total_time('Body/Leg/Foot', duration_ms)
    print(f'{env.now:.2f} msec, Foot motion with heavy pressure ends for entity #{i[0], k}')

def Leg_or_Foreleg_motion(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Leg or Foreleg motion starts for entity #{i[0], k}')
    duration_ms = tmu_to_milliseconds(7.1)  # Convert TMU to milliseconds
    yield env.timeout(duration_ms)  # Simulate processing time
    update_total_time('Body/Leg/Foot', duration_ms)
    print(f'{env.now:.2f} msec, Leg or Foreleg motion ends for entity #{i[0], k}')

def Bend_Stoop_Kneel_on_One_Knee(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Bend/Stoop/Kneel on One Knee starts for entity #{i[0], k}')
    duration_ms = tmu_to_milliseconds(29.0)  # Convert TMU to milliseconds
    yield env.timeout(duration_ms)  # Simulate processing time
    update_total_time('Body/Leg/Foot', duration_ms)
    print(f'{env.now:.2f} msec, Bend/Stoop/Kneel on One Knee ends for entity #{i[0], k}')

def Kneel_on_Floor_Both_Knees(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Kneel on Floor Both Knees starts for entity #{i[0], k}')
    duration_ms = tmu_to_milliseconds(69.4)  # Convert TMU to milliseconds
    yield env.timeout(duration_ms)  # Simulate processing time
    update_total_time('Body/Leg/Foot', duration_ms)
    print(f'{env.now:.2f} msec, Kneel on Floor Both Knees ends for entity #{i[0], k}')

def Arise_on_One_Knee(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Arise on One Knee starts for entity #{i[0], k}')
    duration_ms = tmu_to_milliseconds(31.9)  # Convert TMU to milliseconds
    yield env.timeout(duration_ms)  # Simulate processing time
    update_total_time('Body/Leg/Foot', duration_ms)
    print(f'{env.now:.2f} msec, Arise on One Knee ends for entity #{i[0], k}')

def Arise_from_Kneel_on_Floor_Both_Knees(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Arise from Kneel on Floor Both Knees starts for entity #{i[0], k}')
    duration_ms = tmu_to_milliseconds(76.7)  # Convert TMU to milliseconds
    yield env.timeout(duration_ms)  # Simulate processing time
    update_total_time('Body/Leg/Foot', duration_ms)
    print(f'{env.now:.2f} msec, Arise from Kneel on Floor Both Knees ends for entity #{i[0], k}')

def Sit(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Sit starts for entity #{i[0], k}')
    duration_ms = tmu_to_milliseconds(34.7)  # Convert TMU to milliseconds
    yield env.timeout(duration_ms)  # Simulate processing time
    update_total_time('Body/Leg/Foot', duration_ms)
    print(f'{env.now:.2f} msec, Sit ends for entity #{i[0], k}')

def Stand_from_Sitting_Position(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Stand from Sitting Position starts for entity #{i[0], k}')
    duration_ms = tmu_to_milliseconds(43.4)  # Convert TMU to milliseconds
    yield env.timeout(duration_ms)  # Simulate processing time
    update_total_time('Body/Leg/Foot', duration_ms)
    print(f'{env.now:.2f} msec, Stand from Sitting Position ends for entity #{i[0], k}')


def Turn_Body_degrees(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Turn Body degrees starts for entity #{i[0], k}')

    # Load the selection data
    turn_body_data = load_var(path+'/turn_body_degrees_entity_dic.txt')
    selected_case = turn_body_data.get("case_of_turn_body", "1")  # Default to "1" if not found

    # Identify the TMU value based on the case
    if selected_case == "1":
        tmu_value = 18.6  # TMU for Case 1
    elif selected_case == "2":
        tmu_value = 37.2  # TMU for Case 2
    else:
        raise ValueError(f"Unknown case: {selected_case}")

    # Convert TMU to milliseconds
    simulation_time = tmu_to_milliseconds(tmu_value)

    # Simulate processing time
    yield env.timeout(simulation_time)
    update_total_time('Body/Leg/Foot', simulation_time)

    print(f'{env.now:.2f} msec, Turn Body degrees ends for entity #{i[0], k}')



def Walk_per_foot(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Walk per foot starts for entity #{i[0], k}')
    
    # Convert TMU to milliseconds
    tmu_value = 5.3  # TMU value for Walk per foot
    duration_ms = tmu_value * 36  # Convert TMU to milliseconds
    
    yield env.timeout(duration_ms)  # Simulate processing time
    update_total_time('Body/Leg/Foot', duration_ms)
    
    print(f'{env.now:.2f} msec, Walk per foot ends for entity #{i[0], k}')
   
    
def Walk_per_pace(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Walk per pace starts for entity #{i[0], k}')
    
    # Convert TMU to milliseconds
    tmu_value = 15.0  # TMU value for Walk per pace
    duration_ms = tmu_value * 36  # Convert TMU to milliseconds
    
    yield env.timeout(duration_ms)  # Simulate processing time
    update_total_time('Body/Leg/Foot', duration_ms)
    
    print(f'{env.now:.2f} msec, Walk per pace ends for entity #{i[0], k}')



def Eye_travel(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Eye Travel starts for entity #{i[0], k}')
    
    # Retrieve the L and D values along with the calculated TMU value
    eye_travel_data = load_var(path + '/eye_travel_entity_dic.txt')
    tmu_value = eye_travel_data.get("tmu_value", 0)  # Default to 0 if not found

    # Convert TMU to milliseconds
    simulation_time = tmu_value * 36  # 1 TMU = 0.036 seconds (or 36 milliseconds)

    # Simulate processing time based on TMU
    yield env.timeout(simulation_time)
    update_total_time('Eye', simulation_time)
    
    print(f'{env.now:.2f} msec, Eye Travel ends for entity #{i[0], k}')


def Eye_focus(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, Eye Focus starts for entity #{i[0], k}')
    
    # Convert TMU to milliseconds
    tmu_value = 7.3  # TMU value for Eye Focus
    duration_ms = tmu_value * 36  # Convert TMU to milliseconds
    
    yield env.timeout(duration_ms)  # Simulate processing time
    update_total_time('Eye', duration_ms)
    
    print(f'{env.now:.2f} msec, Eye Focus ends for entity #{i[0], k}')



def END_OF_TASK(env, qn_mhp, i, j, k, attribute, outserver_dic, arrival_time, generation):
    print(f'{env.now:.2f} msec, END OF TASK starts for entity #{i[0], k}')
    yield env.timeout(ppt)  # Simulate processing time
    print(f'{env.now:.2f} msec, END OF TASK ends for entity #{i[0], k}')

#Main menu UI
total_times = {
    'Left Arm/Hand': 0,
    'Right Arm/Hand': 0,
    'Body/Leg/Foot': 0,
    'Eye': 0
}
def update_total_time(part, time):
    global total_times
    total_times[part] += time

def run_simulation(me_tasks):
    global total_times
    total_times = {
        'Left Arm/Hand': 0,
        'Right Arm/Hand': 0,
        'Body/Leg/Foot': 0,
        'Eye': 0
    }
    
    env = simpy.Environment()
    qn_mhp = QN_MHP(env)
    outserver_dic = {}
    arrival_time = 0
    generation = 1
    
    # Run the MEs chosen by the user
    for task in me_tasks:
        if task['name'] == 'Reach':
            env.process(Reach(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Move':
            env.process(Move(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Turn':
            env.process(Turn(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Apply Pressure':
            env.process(Apply_pressure(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Grasp':
            env.process(Grasp(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Position':
            env.process(Position(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Release':
            env.process(Release(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Disengage':
            env.process(Disengage(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Sidestep':
            env.process(Sidestep(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Foot Motion Hinge at Ankle':
            env.process(Foot_motion_hinge_at_ankle(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Foot Motion with Heavy Pressure':
            env.process(Foot_motion_with_heavy_pressure(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Leg or Foreleg Motion':
            env.process(Leg_or_Foreleg_motion(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Bend/Stoop/Kneel on One Knee':
            env.process(Bend_Stoop_Kneel_on_One_Knee(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Kneel on Floor Both Knees':
            env.process(Kneel_on_Floor_Both_Knees(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Arise on One Knee':
            env.process(Arise_on_One_Knee(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Arise from Kneel on Floor Both Knees':
            env.process(Arise_from_Kneel_on_Floor_Both_Knees(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Sit':
            env.process(Sit(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Stand from Sitting Position':
            env.process(Stand_from_Sitting_Position(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Turn Body Degrees':
            env.process(Turn_Body_degrees(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Walk per Foot':
            env.process(Walk_per_foot(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Walk per Pace':
            env.process(Walk_per_pace(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Eye Travel':
            env.process(Eye_travel(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'Eye Focus':
            env.process(Eye_focus(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
        elif task['name'] == 'END OF TASK':
            env.process(END_OF_TASK(env, qn_mhp, [1], 1, 1, task['attribute'], outserver_dic, arrival_time, generation))
    
    env.run()
    
    # Calculate the task duration
    task_duration = max(total_times.values())
    
    # Display the results
    result_message = (
        f"Total time for Left Arm/Hand: {total_times['Left Arm/Hand']} ms\n"
        f"Total time for Right Arm/Hand: {total_times['Right Arm/Hand']} ms\n"
        f"Total time for Body/Leg/Foot: {total_times['Body/Leg/Foot']} ms\n"
        f"Total time for Eye: {total_times['Eye']} ms\n"
        f"Task duration: {task_duration} ms"
    )
    
    messagebox.showinfo("Simulation Results", result_message)

selected_mes = []

class GUI_task_def_step1:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Define Task step1: define permissible MEs for each step')
        sw=self.root.winfo_screenwidth() 
        ww=1200
        sh=self.root.winfo_screenheight()   
        wh=800
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        self.interface()
        
    def interface(self):
        for r in range(100):
            self.root.rowconfigure(r,weight=1)
        for c in range(100):
            self.root.columnconfigure(c,weight=1)
        #title
        tk.Label(self.root,text='Step1:  define permissible MEs for each step',font=('bold',14),anchor='w')\
            .grid(row = 0,column=0,pady=10,columnspan=10,sticky='w')
        #tk.Label(self.root,text='Step2: click the Apply button, and click the b_e button in the automatically generated task list to open the setting interface of the selected b_e',font=('bold',14))\
            #.grid(row = 19,column=0,pady=3,columnspan=18,sticky='w')
        self.l_tn= tk.Label(self.root,text='Task Name',font=('bold',14),relief='ridge',width=15)
        self.l_tn.grid(row = 1,column=0,pady=1,padx=1)
        self.l_order=tk.Label(self.root,text='Motion\n Elements\n and \n Steps',font=('bold',14),relief='ridge',height=32)
        self.l_order.grid(row = 2,column=0,rowspan=21,pady=1)
        
        #Combobox
        self.combobox={}
        global tbd_list
        tbd_list=['TBD1','TBD2','TBD3']
        save_var(tbd_list, path+'/tbd_list.txt')
        for r in range(2,23):
            for c in range(1,7):
                if c==1: #choose order
                    self.value = tk.StringVar()
                    '''
                    if saved==1:
                        self.value.set(load_var(path+'task_info_dic.txt')[(r,c)])
                    else:
                        self.value.set('')
                    '''
                    value_order_list = ['','Step-1','Step-2','Step-3','Step-4','Step-5','Step-6','Step-7','Step-8','Step-9','Step-10','Step-11','Step-12','Step-13','Step-14','Step-15','Step-16','Step-17','Step-18','Step-19','Step-20','AddStep']
                    value_order_element = value_order_list[r-1]
                    value_order = [value_order_element,'']
                    self.combobox[(r,c)] = ttk.Combobox(
                        master = self.root,
                        width=15,
                        state='readonly',
                        cursor='arrow',
                        values=value_order,
                        #textvariable=self.value,
                        font=('bold',10)
                        )
                    self.combobox[(r,c)].bind('<<ComboboxSelected>>',self.pick)
                    self.combobox[(r,c)].grid(row=r,column=c, padx=5)###############################################################  
                    
                    if saved==1 and load_var(path+'/task_info_dic.txt')[(r,c)]!='':
                        self.combobox[(r,c)].current(eval(load_var(path+'/task_info_dic.txt')[(r,c)]))
                    else:
                        self.combobox[(r,c)].current(0)
                      
                        
                else: #choose behavior elements
                    self.value = tk.StringVar()
                    if c==2:
                        value_be = ['No','Yes','']
                    elif c==3:
                        value_be = ['','Reach','Move', 'Turn', 'Apply Pressure','Grasp','Position','Release','Disengage','END OF TASK']
                    elif c==4:
                        value_be = ['','Sidestep','Foot Motion Hinge at Ankle', 'Foot motion with Heavy Pressure','Leg or Foreleg Motion', 'Bend/Stoop/Kneel on One Knee','Arise(Bend/Stoop/Kneel) on One Knee',\
                                    'Kneel on Floor Both Knees', 'Arise from Kneel on Floor Both Knees','Sit','Stand from Sitting Position', 'Turn Body 45-90 Degrees','Walk Per Foot', 'Walk Per Pace ','END OF TASK']
                    elif c==5:
                        value_be = ['','Reach','Move', 'Turn', 'Apply Pressure','Grasp','Position','Release','Disengage','END OF TASK']
                    elif c==6:
                        value_be = ['','Eye Travel','Eye Focus','END OF TASK']

                    self.combobox[(r,c)] = ttk.Combobox(
                        master = self.root,
                        width=50,
                        state='readonly',
                        cursor='arrow',
                        values=value_be,  
                        font=('bold',10)
                        )
                    self.combobox[(r,c)].bind('<<ComboboxSelected>>',self.pick)
                    self.combobox[(r,c)].grid(row=r,column=c, padx=5)################################################################
                    if saved==1 and load_var(path+'/task_info_dic.txt')[(r,c)]!='':
                        for item in range(len(value_be)):
                            if load_var(path+'/task_info_dic.txt')[(r,c)]==value_be[item]:
                                self.combobox[(r,c)].current(item)
                    else:
                        self.combobox[(r,c)].current(0)
        global sub_info_dic
        sub_info_dic={}
        save_var(sub_info_dic, path+'/sub_info_dic.txt')           
        global operator_name_list
        operator_name_list = ['Reach','Move', 'Turn', 'Apply Pressure','Grasp','Position','Release','Disengage','Sidestep','Foot Motion Hinge at Ankle', 'Foot motion with Heavy Pressure','Leg or Foreleg Motion', 'Bend/Stoop/Kneel on One Knee','Arise(Bend/Stoop/Kneel) on One Knee',\
                                    'Kneel on Floor Both Knees', 'Arise from Kneel on Floor Both Knees','Sit','Stand from Sitting Position', 'Turn Body 45-90 Degrees','Walk Per Foot', 'Walk Per Pace ','Eye Travel','Eye Focus']

        self.Button_next=tk.Button(self.root,text='Next: ME Specification',font=16,command=self.next_event)
        self.Button_next.grid(row=23,column=1,columnspan=3,pady=30,ipady=3)#
        self.Button_save = tk.Button(self.root, text='Save and Back to Main Menu', font=16, command=self.save_and_back)
        self.Button_save.grid(row=23,column=5,columnspan=3,pady=30,ipady=3)#

        for c in range(2,7):
            self.value = tk.StringVar()
            self.value.set('')
            if c == 2:
             value_tn = ['Concurrent with Previous Step(Yes/No)?','Left Arm/Hand','Body/Leg/Foot','Right Arm/Hand','Eye','']
            elif c == 3:
             value_tn = ['Left Arm/Hand','Concurrent with Previous Step(Yes/No)?','Body/Leg/Foot','Right Arm/Hand','Eye','']
            elif c == 4:
             value_tn = ['Body/Leg/Foot','Concurrent with Previous Step(Yes/No)?','Left Arm/Hand','Right Arm/Hand','Eye','']
            elif c == 5:
             value_tn = ['Right Arm/Hand','Concurrent with Previous Step(Yes/No)?','Left Arm/Hand','Body/Leg/Foot','Eye','']
            elif c == 6:
             value_tn = ['Eye','Concurrent with Previous Step(Yes/No)?','Left Arm/Hand','Body/Leg/Foot','Right Arm/Hand','']
           # self.combobox[(1,c)] = ttk.Combobox(
                #master = self.root,
                #state='readonly',
                #cursor='arrow',
                #values=value_tn, 
                #width=25
                #)
            #self.combobox[(r,c)].bind('<<ComboboxSelected>>',self.pick)
            #self.combobox[(r,c)].grid(row=1,column=2*c-1,padx=5,columnspan=2)###########################################################################
            
            #if saved==1 and load_var(path+'/task_info_dic.txt')[(1,c)]!='':
                #self.combobox[(1,c)].current(eval(load_var(path+'/task_info_dic.txt')[(1,c)]))
                #print(self.combobox[(1,c)].get())
            #else:
                #self.combobox[(1,c)].current(0)
            self.combobox[(1,c)] = ttk.Combobox(
                        master = self.root,
                        width=50,
                        state='readonly',
                        cursor='arrow',
                        values=value_tn,  
                        font=('bold',10)
                        )
            self.combobox[(1,c)].bind('<<ComboboxSelected>>',self.pick)
            self.combobox[(1,c)].grid(row=1,column=c, padx=5)################################################################
            if saved==1 and load_var(path+'/task_info_dic.txt')[(1,c)]!='':
                        for item in range(len(value_be)):
                            if load_var(path+'/task_info_dic.txt')[(1,c)]==value_be[item]:
                                self.combobox[(1,c)].current(item)
            else:
                        self.combobox[(1,c)].current(0)
            
 
    # Get combobox user input    
    def pick(self, *arg):
        global task_info_dic, task_info_dic_f
        task_info_dic = {}
        for r in range(1, 23):
            if r == 1:
                for c in range(2, 7):
                   task_info_dic[(r, c)] = self.combobox[(r, c)].get()
            else:
                for c in range(1, 7):
                   task_info_dic[(r, c)] = self.combobox[(r, c)].get()
        task_info_dic_f = save_var(task_info_dic, path + '/task_info_dic.txt')

    def next_event(self):
        global task_info_dic, task_info_dic_f
        task_info_dic = {}
        for r in range(1, 23):
            if r == 1:
               for c in range(2, 7):
                 task_info_dic[(r, c)] = self.combobox[(r, c)].get()
            else:
               for c in range(1, 7):
                task_info_dic[(r, c)] = self.combobox[(r, c)].get()
        task_info_dic_f = save_var(task_info_dic, path + '/task_info_dic.txt')
    
        GUI_task_def_step2().root.mainloop()

    def save_and_back(self):
        self.save_selected_mes()
        self.root.destroy()

    def get_selected_mes(self):
        me_tasks = []
        for r in range(2, 23):
            for c in range(3, 7):
                me_name = self.combobox[(r, c)].get()
                if me_name:
                   task_info = {
                    'name': me_name,
                    'attribute': self.extract_me_attributes(r, c, me_name)
                   }
                   me_tasks.append(task_info)
        return me_tasks

    def extract_me_attributes(self, row, col, me_name):
        """Extract and return the attributes needed for the specified motion element (ME)."""
        attributes = {}

        if me_name == 'Reach':
         attributes['arm'] = 'Left' if col == 3 else 'Right'
         attributes['distance_cm'] = float(self.combobox[(row, col + 1)].get())  # Get distance
         attributes['reach_case'] = self.combobox[(row, col + 2)].get()  # Get case type
         attributes['hand_motion_before'] = self.combobox[(row, col + 3)].get()
         attributes['hand_motion_after'] = self.combobox[(row, col + 4)].get()

        elif me_name == 'Move':
         attributes['arm'] = 'Left' if col == 3 else 'Right'
         attributes['distance'] = float(self.combobox[(row, col + 1)].get())
         attributes['weight'] = float(self.combobox[(row, col + 2)].get())
         attributes['move_case'] = self.combobox[(row, col + 3)].get()
         attributes['hand_in_motion'] = self.combobox[(row, col + 4)].get()

        elif me_name == 'Turn':
         attributes['degree_of_turn'] = int(self.combobox[(row, col + 1)].get())
         attributes['weight_of_turned_object'] = self.combobox[(row, col + 2)].get().lower()

        elif me_name == 'Apply Pressure':
        # Attributes for 'Apply Pressure' ME
         attributes['arm'] = 'Left' if col == 3 else 'Right'

        elif me_name == 'Grasp':
        # Attributes for 'Grasp' ME
         attributes['arm'] = 'Left' if col == 3 else 'Right'

        elif me_name == 'Position':
         attributes['arm'] = 'Left' if col == 3 else 'Right'
         attributes['class_of_fit'] = self.combobox[(row, col + 1)].get()
         attributes['symmetry'] = self.combobox[(row, col + 2)].get()
         attributes['easy_to_handle'] = self.combobox[(row, col + 3)].get()

        elif me_name == 'Release':
         attributes['arm'] = 'Left' if col == 3 else 'Right'

        elif me_name == 'Disengage':
         attributes['arm'] = 'Left' if col == 3 else 'Right'

        elif me_name == 'Sidestep':
         attributes['body_part'] = 'body'

        elif me_name == 'Foot Motion Hinge at Ankle':
         attributes['body_part'] = 'foot'

        elif me_name == 'Foot Motion with Heavy Pressure':
         attributes['body_part'] = 'foot'

        elif me_name == 'Leg or Foreleg Motion':
         attributes['body_part'] = 'leg'

        elif me_name == 'Bend/Stoop/Kneel on One Knee':
         attributes['body_part'] = 'leg'

        elif me_name == 'Kneel on Floor Both Knees':
         attributes['body_part'] = 'leg'

        elif me_name == 'Arise on One Knee':
         attributes['body_part'] = 'leg'

        elif me_name == 'Arise from Kneel on Floor Both Knees':
         attributes['body_part'] = 'leg'

        elif me_name == 'Sit':
         attributes['body_part'] = 'body'

        elif me_name == 'Stand from Sitting Position':
         attributes['body_part'] = 'body'

        elif me_name == 'Turn Body Degrees':
         attributes['body_part'] = 'body'

        elif me_name == 'Walk per Foot':
         attributes['body_part'] = 'foot'

        elif me_name == 'Walk per Pace':
         attributes['body_part'] = 'foot'

        elif me_name == 'Eye Travel':
         attributes['tmu_value'] = self.combobox[(row, col + 1)].get()

        elif me_name == 'Eye Focus':
         attributes['tmu_value'] = 7.3  # For example

        return attributes

    def save_selected_mes(self):
     global selected_mes
     selected_mes = self.get_selected_mes()


class GUI_User_Main:
   
    def __init__(self):
    
        self.root = tk.Tk()    
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=1000      #window width
        wh=500      #window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.root.title('Main Menu')
        self.root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        self.interface()
        
    def interface(self):
        #title Lable
        self.title=tk.Label(
            self.root,
            text='QN-MTM Software',
            font=('bold',30)
            )
        self.title.pack(pady=50)
        
        #open
        self.task=tk.Button(
            self.root,
            text='open...',
            font=('',15),
            relief='sunken',
            command=self.readFile
            )
        self.task.place(x=0,y=0,width=100,height=30)
        
        #save as
        #open
        self.task=tk.Button(
            self.root,
            text='save as',
            font=('',15),
            relief='sunken',
            command=self.saveFile
            )
        self.task.place(x=100,y=0,width=100,height=30)

        
        #define task button
        self.task=tk.Button(
            self.root,
            text='1. Define Task',
            font=('',20),
            command=self.task_event
            )
        self.task.place(x=270,y=150,width=450,height=50)
        
        #Define parameter button
        self.parameter=tk.Button(
            self.root,
            text='2. Define Simulation Parameters',
            font=('',20),
            command=self.parameter_event
            )
        self.parameter.place(x=270,y=230,width=450,height=50)

        #Start button
        self.Button_start = tk.Button(self.root, text='Start', font=('', 20), command=self.start_simulation)
        self.Button_start.place(x=450,y=400,width=100,height=40)
        
    def task_event(self):
        task_def_gui = GUI_task_def_step1()
        task_def_gui.root.mainloop()
        task_def_gui.save_selected_mes()

        
    def parameter_event(self):
        GUI_simulation_parameter().root.mainloop()
        
    def saveFile(self):
        global path
        path=filedialog.askdirectory(title='select or create a folder to save')
        copy_search_file('backup/', path)
    
    def readFile(self):
        global path
        path=filedialog.askdirectory(title='select or create a folder to save')
        global saved
        saved=1

    def start_simulation(self):
     self.root.withdraw()  # Hide the root window
     num_simulations = simpledialog.askinteger("Input", "How many times do you want to run the simulation?", initialvalue=1, minvalue=1)

     global selected_mes
     global total_times  # Ensure global total_times is used if needed

     total_times = self.get_max_simulation_times(selected_mes)
    
     if not isinstance(total_times, dict) or not total_times:
        messagebox.showerror("Error", "Simulation times could not be calculated. Please check the input.")
        self.root.deiconify()  # Show the root window again
        return

     max_time_per_simulation = max(total_times.values())
     final_simulation_time = max_time_per_simulation * num_simulations

     result_message = (
        f"Total time for Left Arm/Hand: {total_times['Left Arm/Hand']} ms\n"
        f"Total time for Right Arm/Hand: {total_times['Right Arm/Hand']} ms\n"
        f"Total time for Body/Leg/Foot: {total_times['Body/Leg/Foot']} ms\n"
        f"Total time for Eye: {total_times['Eye']} ms\n"
        f"Final simulation time for {num_simulations} simulations: {final_simulation_time} ms"
     )

     messagebox.showinfo("Simulation Results", result_message)
     self.root.deiconify()  # Show the root window again

    def get_max_simulation_times(self, selected_mes):
        return selected_mes







#define task UI
        
                                       
class GUI_task_def_step2:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Define Task step2: ME Specification')
        sw=self.root.winfo_screenwidth() 
        ww=1000
        sh=self.root.winfo_screenheight()   
        wh=800
        self.root.geometry('%dx%d'%(ww,wh))
        self.interface()
        
    def interface(self):
        for r in range(100):
            self.root.rowconfigure(r,weight=1)
        for c in range(100):
            self.root.columnconfigure(c,weight=1)
        #title
        tk.Label(self.root,text='Step2: click the ME button in the automatically generated task list to open the setting interface of the selected ME',font=('bold',14))\
            .grid(row = 0,column=0,pady=3,columnspan=18,sticky='w')
        
        self.button={}
        self.l_tn= tk.Label(self.root,text='Task No.',font=('bold',15),height=2)
        self.l_tn.grid(row = 1,column=0,pady=3,padx=3)
        column_=1
        for c in range(2,7):
            if task_info_dic[(1,c)]!='':
                if task_info_dic[(1,c)]=='Left Arm/Hand':
                    self.task_no='1'###########################################################################################################
                    tk.Label(self.root,text=task_info_dic[(1,c)],font=14).grid(row=1,column=column_)
                    row_=2
                    for r in range(2,23):
                        if task_info_dic[(r,c)]!='':
                            if task_info_dic[(r,c)]=='Reach':
                                self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.reach_event1,width=18)
                            elif task_info_dic[(r,c)]=='Move':
                                self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.move_event1,width=18)
                            elif task_info_dic[(r,c)]=='Turn':
                                self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.turn_event1,width=18)  
                            elif task_info_dic[(r,c)]=='Apply Pressure':
                                self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.apply_pressure_event1,width=18)  
                            elif task_info_dic[(r,c)]=='Grasp':
                                self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.grasp_event1,width=18)  
                            elif task_info_dic[(r,c)]=='Position':
                                self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.position_event1,width=18)                           
                            elif task_info_dic[(r,c)]=='Release':
                                self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.release_event1,width=18)
                            elif task_info_dic[(r,c)]=='Disengage':
                                self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.disengage_event1,width=18)  
                            #elif task_info_dic[(r,c)]=='END OF TASK':#
                                #self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.track1D_ev,width=18)  
                            #elif task_info_dic[(r,2*c-1)]=='Tracking_2D':
                                #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.track2D_event1,width=18)                             
                            #elif task_info_dic[(r,2*c-1)]=='Static_2DTracing':
                                #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.static_tracing_event1,width=18)          
                            #elif task_info_dic[(r,2*c-1)]=='Dynamic_1D':
                                #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.dynamic1D_event1,width=18)
                            #elif task_info_dic[(r,2*c-1)]=='Dynamic_2D':
                                #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.dynamic2D_event1,width=18) 
                            #elif task_info_dic[(r,2*c-1)]=='TBD1':
                                #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.tbd1_event1,width=18)    
                            #elif task_info_dic[(r,2*c-1)]=='TBD2':
                                #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.tbd2_event1,width=18)  
                            #elif task_info_dic[(r,2*c-1)]=='TBD3':
                                #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.tbd3_event1,width=18)                      
                            #else:
                                #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,width=18)
                            self.button[(r,c)].grid(row=row_,column=column_)        
                            row_+=1
                if task_info_dic[(1,c)]=='Body/Leg/Foot':
                     self.task_no='2'
                     tk.Label(self.root,text=task_info_dic[(1,c)],font=14).grid(row=1,column=column_)
                     row_=2
                     for r in range(2,23):
                         if task_info_dic[(r,c)]!='':
                             if task_info_dic[(r,c)]=='Sidestep':
                                 self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.sidestep_event2,width=18)
                             elif task_info_dic[(r,c)]=='Foot Motion Hinge at Ankle':
                                 self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.hear_event2,width=18)
                             elif task_info_dic[(r,c)]=='Foot motion with Heavy Pressure':
                                 self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.judgei_event2,width=18)  
                             elif task_info_dic[(r,c)]=='Leg or Foreleg Motion':
                                 self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.lookat_event2,width=18)  
                             elif task_info_dic[(r,c)]=='Bend/Stoop/Kneel on One Knee':
                                 self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.choice_event2,width=18)  
                             elif task_info_dic[(r,c)]=='Arise (Bend/Stoop/Kneel) on One Knee':
                                 self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.count_event2,width=18)
                             elif task_info_dic[(r,c)]=='Kneel on Floor Both Knees':
                                self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.cal_single_digit_num_event2,width=18)  
                             elif task_info_dic[(r,c)]=='Arise from Kneel on Floor Both Knees':
                                 self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.lookfor_event2,width=18) 
                             elif task_info_dic[(r,c)]=='Sit':
                                 self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.track1D_event2,width=18)  
                             elif task_info_dic[(r,c)]=='Stand from Sitting Position':
                                 self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.track2D_event2,width=18)                             
                             elif task_info_dic[(r,c)]=='Turn Body 45-90 Degrees':
                                 self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.turn_body_event2,width=18)  
                             elif task_info_dic[(r,c)]=='Walk Per Foot':
                                 self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.dynamic1D_event2,width=18)     
                             elif task_info_dic[(r,c)]=='Walk Per Pace':
                                 self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.dynamic2D_event2,width=18)     
                             #elif task_info_dic[(r,2*c-1)]=='TBD1':
                                 #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.tbd1_event2,width=18)    
                             #elif task_info_dic[(r,2*c-1)]=='TBD2':
                                 #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.tbd2_event2,width=18)  
                             #elif task_info_dic[(r,2*c-1)]=='TBD3':
                                 #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.tbd3_event2,width=18)                      
                             #else:
                                 #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,width=18)
                             self.button[(r,c)].grid(row=row_,column=column_)        
                             row_+=1
                if task_info_dic[(1,c)]=='Right Arm/Hand':
                    self.task_no='3'###########################################################################################################
                    tk.Label(self.root,text=task_info_dic[(1,c)],font=14).grid(row=1,column=column_)
                    row_=2
                    for r in range(2,23):
                        if task_info_dic[(r,c)]!='':
                            if task_info_dic[(r,c)]=='Reach':
                                self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.reach_event3,width=18)
                            elif task_info_dic[(r,c)]=='Move':
                                self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.move_event3,width=18)
                            elif task_info_dic[(r,c)]=='Turn':
                                self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.turn_event3,width=18)  
                            elif task_info_dic[(r,c)]=='Apply Pressure':
                                self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.apply_pressure_event3,width=18)  
                            elif task_info_dic[(r,c)]=='Grasp':
                                self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.grasp_event3,width=18)  
                            elif task_info_dic[(r,c)]=='Position':
                                self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.position_event3,width=18)                           
                            elif task_info_dic[(r,c)]=='Release':
                                self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.release_event3,width=18)
                            elif task_info_dic[(r,c)]=='Disengage':
                                self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.disengage_event3,width=18)  
                            #elif task_info_dic[(r,c)]=='END OF TASK':#
                                #self.button[(r,c)]=tk.Button(self.root,text=task_info_dic[(r,c)],font=16,height=1,command=self.end_event1,width=18)  
                            #elif task_info_dic[(r,2*c-1)]=='Tracking_2D':
                                #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.track2D_event1,width=18)                             
                            #elif task_info_dic[(r,2*c-1)]=='Static_2DTracing':
                                #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.static_tracing_event1,width=18)          
                            #elif task_info_dic[(r,2*c-1)]=='Dynamic_1D':
                                #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.dynamic1D_event1,width=18)
                            #elif task_info_dic[(r,2*c-1)]=='Dynamic_2D':
                                #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.dynamic2D_event1,width=18) 
                            #elif task_info_dic[(r,2*c-1)]=='TBD1':
                                #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.tbd1_event1,width=18)    
                            #elif task_info_dic[(r,2*c-1)]=='TBD2':
                                #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.tbd2_event1,width=18)  
                            #elif task_info_dic[(r,2*c-1)]=='TBD3':
                                #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.tbd3_event1,width=18)                      
                            #else:
                                #self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,width=18)
                            self.button[(r,c)].grid(row=row_,column=column_)        
                            row_+=1
                
                column_+=1
            self.Button_save=tk.Button(self.root,text='Save and Back to Step1',font=16,command=self.root.destroy)
            self.Button_save.place(x=700,y=700,width=230,height=50)
            
    
    #BE data record as part of task def step2, have important broad effect.
    #Currently for 2 tasks, can be expanded to 5 (currect) or more (in future)
    def reach_event1(self):
        GUI_ME_Reach('1').root.mainloop()
    def move_event1(self):
        GUI_ME_Move('1').root.mainloop()
    def turn_event1(self):
        GUI_ME_Turn('1').root.mainloop()
    def apply_pressure_event1(self):
        GUI_ME_Apply_Pressure('1').root.mainloop()
    def grasp_event1(self):
        GUI_ME_Grasp('1').root.mainloop()
    def position_event1(self):
        GUI_ME_Position('1').root.mainloop()
    def release_event1(self):
        GUI_ME_Release('1').root.mainloop()
    def disengage_event1(self):
        GUI_ME_Disengage('1').root.mainloop()
    #def track2D_event1(self):
        #GUI_BE_track2D('1').root.mainloop()
    #def static_tracing_event1(self):
        #GUI_BE_static_tracing('1').root.mainloop()
    #def dynamic1D_event1(self):
        #GUI_BE_dynamic1D('1').root.mainloop()
    #def dynamic2D_event1(self):
        #GUI_BE_dynamic2D('1').root.mainloop()

    def reach_event3(self):
        GUI_ME_Reach('3').root.mainloop()
    def move_event3(self):
        GUI_ME_Move('3').root.mainloop()
    def turn_event3(self):
        GUI_ME_Turn('3').root.mainloop()
    def apply_pressure_event3(self):
        GUI_ME_Apply_Pressure('3').root.mainloop()
    def grasp_event3(self):
        GUI_ME_Grasp('3').root.mainloop()
    def position_event3(self):
        GUI_ME_Position('3').root.mainloop()
    def release_event3(self):
        GUI_ME_Release('3').root.mainloop()
    def disengage_event3(self):
        GUI_ME_Disengage('3').root.mainloop()


    def sidestep_event2(self):
        GUI_ME_Sidestep('2').root.mainloop()
    def turn_body_event2(self):
        GUI_ME_Turn_body('2').root.mainloop()
    #def choice_event2(self):
       # GUI_BE_Choice('2').root.mainloop()
    #def count_event2(self):
        #GUI_BE_Count('2').root.mainloop()
    #def judgei_event2(self):
        #GUI_BE_Judgei('2').root.mainloop()
    #def cal_single_digit_num_event2(self):
        #GUI_BE_Cal_single_digit_num('2').root.mainloop()
    #def lookat_event2(self):
       # GUI_BE_Lookat('2').root.mainloop()
    #def lookfor_event2(self):
       # GUI_BE_Lookfor('2').root.mainloop()
   # def count_event2(self):
       # GUI_BE_Count('2').root.mainloop()
    #def track1D_event2(self):
       # GUI_BE_track1D('2').root.mainloop()
   # def track2D_event2(self):
       # GUI_BE_track2D('2').root.mainloop()
    #def static_tracing_event2(self):
       # GUI_BE_static_tracing('2').root.mainloop()
    #def dynamic1D_event2(self):
       # GUI_BE_dynamic1D('2').root.mainloop()
    #def dynamic2D_event2(self):
        #GUI_BE_dynamic2D('2').root.mainloop()

#GUI for simulation
# class GUI_simulation_parameter:
#     def __init__(self):  
#         self.root = tk.Tk()    
#         sw=self.root.winfo_screenwidth()        #screen width
#         sh=self.root.winfo_screenheight()       #screen height
#         ww=800      #window width
#         wh=400      #window height
#         x=(sw-ww)/2  #window coordinate (left_up point)
#         y=(sh-wh)/2  #window coordinate
#         self.root.title('Define Simulation Parameters')
#         self.root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
#         self.v=tk.IntVar()
#         self.interface()
        
#     def interface(self):
        
#         #label
#         self.simtime=tk.Label(
#             self.root,
#             text='Simulation Time (msec):',
#             font=('bold',17)
#             )
#         self.simtime.place(x=20,y=50)

#         self.animation=tk.Label(
#             self.root,
#             text='Animation:',
#             font=('bold',17)
#             )
        
        
#         self.animation.place(x=20,y=200)
        
#         #entry 
#         self.entry_simtime=tk.Entry(self.root,font=('',15))
#         self.entry_simtime.place(x=400,y=50,width=120,height=40)
        
#         if saved==1:
#             self.entry_simtime.insert(0,load_var(path+'/simtime.txt'))

#         #Radiobutton  

        

#         if saved == 1:
#             if load_var(path+'/anim.txt') == 1:
                
#                 self.choose = tk.StringVar(self.root,"yes" )
#             else:
#                 self.choose = tk.StringVar(self.root,"no" )
                
#         else:
#             self.choose = tk.StringVar(self.root, " ")

#         #self.v=tk.IntVar()
#         self.rb_yes=tk.Radiobutton(
#             self.root,
#             text='YES',
#             font=('',15),
#             variable=self.choose,
#             value='yes',
#             borderwidth=10,
 
#             )
#         self.rb_yes.place(x=2*100,y=190)
        
#         self.rb_no=tk.Radiobutton(
#             self.root,
#             text='NO',
#             font=('',15),
#             variable=self.choose,
#             value='no',
#             borderwidth=10,

#             )
#         self.rb_no.place(x=3*100,y=190)       
        
            
   
#         #ok button
#         self.Button_ok=tk.Button(self.root,text='Save and Back to Main Menu',font=('',18),command=self.event)
#         self.Button_ok.place(x=400,y=350,height=40)

        
        
#     def event(self):
#         global SIMTIME, IAT, Choice_num,anim,Presented_num
#         SIMTIME=eval(self.entry_simtime.get())
#         #Presented_num=eval(self.entry_Presented.get())
#         #anim=1 : animation on; anim=0: animaiton off
      
#         if self.choose.get() == 'yes':
#             anim = 1
#         else:
#             anim=0
#         save_var(anim, path+'/anim.txt')
#         save_var(SIMTIME, path+'/simtime.txt')
#         self.root.destroy()

#Below is Ziqi's version of GUI_simulation_parameter with type checking for input and radio button with default value    
class GUI_simulation_parameter:
    def __init__(self):  
        self.root = tk.Tk()    
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=800      #window width
        wh=400      #window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.root.title('Define Simulation Parameters')
        self.root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        self.v=tk.IntVar()
        self.interface()
        
    def interface(self):
        
        #label
        self.simtime=tk.Label(
            self.root,
            text='Simulation Time (msec):',
            font=('bold',17)
            )
        self.simtime.place(x=20,y=50)

        self.animation=tk.Label(
            self.root,
            text='Animation:',
            font=('bold',17)
            )
        
        
        self.animation.place(x=20,y=200)
        
        #entry 
        self.entry_simtime=tk.Entry(self.root,font=('',15))
        self.entry_simtime.place(x=400,y=50,width=120,height=40)
        
        if saved==1:
            self.entry_simtime.insert(0,load_var(path+'/simtime.txt'))

        #Radiobutton  

        if saved == 1:
            if load_var(path+'/anim.txt') == 1:
                self.choose = tk.StringVar(self.root,"yes")
            else:
                self.choose = tk.StringVar(self.root,"no")
        else:
            self.choose = tk.StringVar(self.root, "yes")

        self.rb_yes=tk.Radiobutton(
            self.root,
            text='YES',
            font=('',15),
            variable=self.choose,
            value='yes',
            borderwidth=10,
            )
        self.rb_yes.place(x=2*100,y=190)
        
        self.rb_no=tk.Radiobutton(
            self.root,
            text='NO',
            font=('',15),
            variable=self.choose,
            value='no',
            borderwidth=10,
            )
        self.rb_no.place(x=3*100,y=190)       
        
        #ok button
        self.Button_ok=tk.Button(self.root,text='Save and Back to Main Menu',font=('',18),command=self.event)
        self.Button_ok.place(x=400,y=350,height=40)
        
    def event(self):
        global SIMTIME, IAT, Choice_num, anim, Presented_num
        try:
            SIMTIME = int(self.entry_simtime.get())
            if SIMTIME <= 0:
                raise ValueError
            
            if self.choose.get() == 'yes':
                anim = 1
            else:
                anim = 0
            save_var(anim, path+'/anim.txt')
            save_var(SIMTIME, path+'/simtime.txt')
            self.root.destroy()
        except ValueError:
            self.show_error_message()
            return #Ziqi edited, add this line to exit the function after showing the error message
    
    def show_error_message(self):
        error_window = tk.Toplevel(self.root)
        error_window.title("Error")
        error_window.geometry("500x100")
        error_label = tk.Label(error_window, text="Please enter a positive integer for simulation time.", font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()

#2.3 ME Specific GUI

see_entity_dic={}
hear_entity_dic={}
class GUI_ME_Reach:
    def __init__(self, task_no):
        self.root = tk.Tk()
        sw = self.root.winfo_screenwidth()  # screen width
        sh = self.root.winfo_screenheight()  # screen height
        ww = 1200  # window width
        wh = 400  # window height
        x = (sw - ww) / 2  # window coordinate (left_up point)
        y = (sh - wh) / 2  # window coordinate
        self.root.title('ME Specification: Reach')
        self.root.geometry('%dx%d+%d+%d' % (ww, wh, x, y))
        self.task_no = task_no

        self.See()

    def See(self):
        # title Label
        tk.Label(self.root, text='Please Specify REACH:', font=('bold', 14)) \
            .grid(row=0, column=0, pady=3, columnspan=10, sticky='w')
        
        title_ls = ['Distance of Reach (inches)', 'Case of Reach (A, B, C, D, E)', 'Hand in Motion BEFORE Reach?', 'Hand in Motion AFTER Reach?']
        for c in range(1, 5):
            tk.Label(self.root, text=title_ls[c - 1], font=('bold', 12), width=33, relief='sunken') \
                .grid(row=1, column=c)
        
        tk.Label(self.root, text="Users enter number", font=('bold', 12), width=33, relief='sunken') \
            .grid(row=2, column=1)
        tk.Label(self.root, text="Users select one of the five below", font=('bold', 12), width=33, relief='sunken') \
            .grid(row=2, column=2)
        tk.Label(self.root, text="Yes/No", font=('bold', 12), width=33, relief='sunken') \
            .grid(row=2, column=3)
        tk.Label(self.root, text="Yes/No", font=('bold', 12), width=33, relief='sunken') \
            .grid(row=2, column=4)

        # REACH case descriptions
        reach_cases = [
            "",
            "",
            "",
            "",
            "A: Reach to object in fixed location, or to object in other hand or on which other hand rests.",
            "B: Reach to single object in location which may vary slightly from cycle to cycle.",
            "C: Reach to object jumbled with other objects in a group so that search and select occur.",
            "D: Reach to a very small object or where accurate grasp is required.",
            "E: Reach to indefinite location to get hand in position for body balance or next motion or out of way."
        ]
        
        for idx, case in enumerate(reach_cases, start=1):
            tk.Label(self.root, text=case, font=('bold', 12), width=150, relief='flat', anchor='w') \
                .grid(row=idx + 3, column=0, columnspan=5, sticky='w')

        self.see = {}

        for r in range(3, 7):
            self.see[(r, 1)] = tk.Entry(self.root, width=30)
            self.see[(r, 1)].grid(row=r, column=1)

            self.see[(r, 2)] = ttk.Combobox(
                master=self.root,
                width=33,
                state='readonly',
                cursor='arrow',
                values=["A", "B","C", "D", "E"],
                font=('bold', 10)
            )
            self.see[(r, 2)].grid(row=r, column=2)

            self.see[(r, 3)] = ttk.Combobox(
                master=self.root,
                width=33,
                state='readonly',
                cursor='arrow',
                values=["Yes", "No"],
                font=('bold', 10)
            )
            self.see[(r, 3)].grid(row=r, column=3)

            self.see[(r, 4)] = ttk.Combobox(
                master=self.root,
                width=33,
                state='readonly',
                cursor='arrow',
                values=["Yes", "No"],
                font=('bold', 10)
            )
            self.see[(r, 4)].grid(row=r, column=4)

        self.Button_ok = tk.Button(self.root, text='Save and Back to Step2', font=16, command=self.entry_event)
        self.Button_ok.grid(row=14, rowspan=3, column=2, columnspan=2, pady=30, ipady=3)

    def entry_event(self):
        try:
        # Validate entry fields only if any field in a row is filled
            for r in range(3, 7):
               row_filled = any(self.see[(r, c)].get().strip() for c in range(1, 5))
               if row_filled:
                  for c in range(1, 5):
                    val_str = self.see[(r, c)].get().strip()
                    if val_str == "":
                        raise ValueError(f"Please fill all required fields in row {r}.")
                    if c == 1 and (not val_str.isdigit() or int(val_str) <= 0):
                        raise ValueError(f"Please enter a positive integer at row {r}, column {c}.")
        
        # If validation passes, update dictionary and save variables
            for r in range(3, 7):
               see_entity_dic[(r, 1)] = self.see[(r, 1)].get()
               for c in range(2, 5):
                see_entity_dic[(r, c)] = self.see[(r, c)].get() if self.see[(r, c)].get().strip() else None

        # Assuming the arm information is determined by the task and known beforehand
            if self.task_no == '1':
                arm_information = 'left'  # or 'right' based on your context
            if self.task_no == '3':
                arm_information = 'right'

            attribute = {
            'arm': arm_information,
            # Add other relevant attributes here
            }

        # Save the dictionary to a file or any required storage
            save_var(attribute, path+'/attribute_dic.txt')
            save_var(see_entity_dic, path+'/see_entity_dic.txt')

            self.root.destroy()

        except ValueError as e:
            self.show_error_message(str(e))

    def start_simulation(self):
        self.root.destroy()
        run_simulation()

    def show_error_message(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Input Error")
        error_window.geometry("400x100")
        error_label = tk.Label(error_window, text=message, font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()
 



class GUI_ME_Move:
    def __init__(self, task_no):
        self.root = tk.Tk()
        sw = self.root.winfo_screenwidth()  # screen width
        sh = self.root.winfo_screenheight()  # screen height
        ww = 1100  # window width
        wh = 320  # window height
        x = (sw - ww) / 2  # window coordinate (left_up point)
        y = (sh - wh) / 2  # window coordinate
        self.root.title('Please Specify MOVE')
        self.root.geometry('%dx%d+%d+%d' % (ww, wh, x, y))
        self.task_no = task_no
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        tk.Label(self.root, text='Please Specify MOVE:', font=('bold', 14)) \
            .grid(row=0, column=0, pady=3, columnspan=10, sticky='w')
        
        # Header Labels
        headers = ['Distance Moved (inches)', 'Case of MOVE (A, B, C)', 'Weight of Moved Object (lbs.)', 'Hand in Motion before/after MOVE?']
        for c in range(1, 5):
            tk.Label(self.root, text=headers[c - 1], font=('bold', 14), width=33, relief='sunken') \
                .grid(row=1, column=c)
        
        # Input Fields
        self.inputs = {}
        for r in range(2, 3):
            self.inputs[(r, 1)] = tk.Entry(self.root, width=25)
            self.inputs[(r, 1)].grid(row=r, column=1)

            self.inputs[(r, 2)] = ttk.Combobox(
                master=self.root,
                width=23,
                state='readonly',
                cursor='arrow',
                values=["A", "B", "C"],
                font=('bold', 10)
            )
            self.inputs[(r, 2)].grid(row=r, column=2)

            self.inputs[(r, 3)] = tk.Entry(self.root, width=25)
            self.inputs[(r, 3)].grid(row=r, column=3)

            self.inputs[(r, 4)] = ttk.Combobox(
                master=self.root,
                width=23,
                state='readonly',
                cursor='arrow',
                values=["Yes", "No"],
                font=('bold', 10)
            )
            self.inputs[(r, 4)].grid(row=r, column=4)

        # Description Labels
        move_cases = [
            "A: Move object to other hand or against stop.",
            "B: Move object to approximate or indefinite location.",
            "C: Move object to exact location."
        ]

        for idx, case in enumerate(move_cases, start=1):
            tk.Label(self.root, text=case, font=('bold', 12), width=110, relief='flat', anchor='w') \
                .grid(row=idx + 4, column=0, columnspan=5, sticky='w')

        # Save Button
        self.Button_ok = tk.Button(self.root, text='Save and Back to Step2', font=16, command=self.save_data)
        self.Button_ok.grid(row=8, rowspan=3, column=2, columnspan=2, pady=30, ipady=3)

    def save_data(self):
        try:
            # Validate entry fields only if any field in a row is filled
            for r in range(2, 3):
                row_filled = any(self.inputs[(r, c)].get().strip() for c in range(1, 5))
                if row_filled:
                    for c in range(1, 5):
                        val_str = self.inputs[(r, c)].get().strip()
                        if val_str == "":
                            raise ValueError(f"Please fill all required fields in row {r}.")
                        if c == 1 and (not val_str.isdigit() or int(val_str) <= 0):
                            raise ValueError(f"Please enter a positive integer for distance moved at row {r}, column {c}.")
                        if c == 3 and (not val_str.isdigit() or int(val_str) <= 0):
                            raise ValueError(f"Please enter a positive integer for weight of moved object at row {r}, column {c}.")
            
            # If validation passes, save variables
            move_data = {}
            for r in range(2, 3):
                move_data[(r, 1)] = self.inputs[(r, 1)].get()
                for c in range(2, 5):
                    move_data[(r, c)] = self.inputs[(r, c)].get().strip()
            # Save the move_data dictionary to a file or any required storage
            if self.task_no == '1':
                arm_information = 'left'  # or 'right' based on your context
            if self.task_no == '3':
                arm_information = 'right'

            attribute = {
            'arm': arm_information,
            # Add other relevant attributes here
            }

        # Save the dictionary to a file or any required storage
            save_var(attribute, path+'/attribute_dic.txt')
            save_var(move_data, path+'/move_entity_dic.txt')
            self.root.destroy()

        except ValueError as e:
            self.show_error_message(str(e))

    def show_error_message(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Input Error")
        error_window.geometry("400x100")
        error_label = tk.Label(error_window, text=message, font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()


class GUI_ME_Turn:
    def __init__(self, task_no):
        self.root = tk.Tk()
        sw = self.root.winfo_screenwidth()  # screen width
        sh = self.root.winfo_screenheight()  # screen height
        ww = 700  # window width
        wh = 250  # window height
        x = (sw - ww) / 2  # window coordinate (left_up point)
        y = (sh - wh) / 2  # window coordinate
        self.root.title('Please Specify TURN:')
        self.root.geometry('%dx%d+%d+%d' % (ww, wh, x, y))
        self.task_no = task_no
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        tk.Label(self.root, text='Please Specify TURN:', font=('bold', 14)) \
            .grid(row=0, column=0, pady=3, columnspan=10, sticky='w')
        
        # Header Labels
        headers = ['Degree of TURN (10-180)', 'Weight of TURNED object (Small, Medium, Large)']
        for c in range(1, 3):
            tk.Label(self.root, text=headers[c - 1], font=('bold', 14), width=45, relief='sunken') \
                .grid(row=1, column=c)
        
        # Input Fields
        self.inputs = {}
        for r in range(2, 3):
            self.inputs[(r, 1)] = tk.Entry(self.root, width=45)
            self.inputs[(r, 1)].grid(row=r, column=1)

            self.inputs[(r, 2)] = ttk.Combobox(
                master=self.root,
                width=45,
                state='readonly',
                cursor='arrow',
                values=["Small", "Medium", "Large"],
                font=('bold', 10)
            )
            self.inputs[(r, 2)].grid(row=r, column=2)

        # Description Labels
        descriptions = [
            "Description of Small/Medium/Large Objects:",
            "Small: 0-2 lbs, Medium: 2.1-10 lbs, Large: 10.1-35 lbs"
        ]

        for idx, desc in enumerate(descriptions, start=1):
            tk.Label(self.root, text=desc, font=('bold', 12), width=70, relief='flat', anchor='w') \
                .grid(row=idx + 4, column=0, columnspan=5, sticky='w')

        # Save Button
        self.Button_ok = tk.Button(self.root, text='Save and Back to Step2', font=16, command=self.save_data)
        self.Button_ok.grid(row=8, rowspan=3, column=1, columnspan=2, pady=30, ipady=3)

    def save_data(self):
        try:
        # Validate entry fields
           val_str_degree = self.inputs[(2, 1)].get().strip()
           val_str_weight = self.inputs[(2, 2)].get().strip()

           if val_str_degree == "" or val_str_weight == "":
            raise ValueError("Please fill all required fields.")
           if not val_str_degree.isdigit() or not (10 <= int(val_str_degree) <= 180):
            raise ValueError("Please enter a valid degree of TURN between 10 and 180.")

        # Save variables
           turn_data = {
            "degree_of_turn": val_str_degree,
            "weight_of_turned_object": val_str_weight
           }

           if self.task_no == '1':
            arm_information = 'left'
           elif self.task_no == '3':
            arm_information = 'right'
           else:
            arm_information = 'unknown'

           attribute = {
            'arm': arm_information,
            'degree_of_turn': val_str_degree,
            'weight_of_turned_object': val_str_weight
           }

           save_var(attribute, path+'/attribute_dic.txt')
           save_var(turn_data, path+'/turn_entity_dic.txt')
           self.root.destroy()

        except ValueError as e:
             self.show_error_message(str(e))

    def show_error_message(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Input Error")
        error_window.geometry("400x100")
        error_label = tk.Label(error_window, text=message, font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()

class GUI_ME_Apply_Pressure:
    def __init__(self, task_no):
        self.root = tk.Tk()
        sw = self.root.winfo_screenwidth()  # screen width
        sh = self.root.winfo_screenheight()  # screen height
        ww = 700  # window width
        wh = 200  # window height
        x = (sw - ww) / 2  # window coordinate (left_up point)
        y = (sh - wh) / 2  # window coordinate
        self.root.title('Please Specify Case of Apply Pressure')
        self.root.geometry('%dx%d+%d+%d' % (ww, wh, x, y))
        self.task_no = task_no
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        tk.Label(self.root, text='Please Specify Case of Apply Pressure:', font=('bold', 14)) \
            .grid(row=0, column=0, pady=3, columnspan=10, sticky='w')
        
        # Header Label
        header = 'Case of APPLY PRESSURE (A—Light Pressure or B—Heavy Pressure)'
        tk.Label(self.root, text=header, font=('bold', 12), width=60, relief='sunken') \
            .grid(row=1, column=1, columnspan=2)

        # User Selection Instruction
        tk.Label(self.root, text="Users select A or B", font=('bold', 14), width=60, relief='sunken') \
            .grid(row=2, column=1, columnspan=2)

        # Input Field
        self.selection = {}
        self.selection[self.task_no] = ttk.Combobox(
            master=self.root,
            width=20,
            state='readonly',
            cursor='arrow',
            values=["A", "B"],
            font=('bold', 10)
        )
        self.selection[self.task_no].grid(row=3, column=1, columnspan=2, pady=10)

        # Save Button
        self.Button_ok = tk.Button(self.root, text='Save and Back to Step2', font=16, command=self.save_data)
        self.Button_ok.grid(row=4, rowspan=3, column=1, columnspan=2, pady=20, ipady=3)

    def save_data(self):
        try:
            selected_value = self.selection[self.task_no].get().strip()
            if selected_value not in ["A", "B"]:
                raise ValueError("Please select either A or B.")
            
            # Save variables
            apply_pressure_data = {
                "case_of_apply_pressure": selected_value
            }
            # Save the apply_pressure_data dictionary to a file or any required 
            if self.task_no == '1':
                arm_information = 'left'  # or 'right' based on your context
            if self.task_no == '3':
                arm_information = 'right'

            attribute = {
            'arm': arm_information,
            # Add other relevant attributes here
            }

        # Save the dictionary to a file or any required storage
            save_var(attribute, path+'/attribute_dic.txt')
            save_var(apply_pressure_data, path+'/apply_pressure_entity_dic.txt')
            self.root.destroy()

        except ValueError as e:
            self.show_error_message(str(e))

    def show_error_message(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Input Error")
        error_window.geometry("400x100")
        error_label = tk.Label(error_window, text=message, font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()
    
class GUI_ME_Grasp:
    def __init__(self, task_no):
        self.root = tk.Tk()
        sw = self.root.winfo_screenwidth()  # screen width
        sh = self.root.winfo_screenheight()  # screen height
        ww = 900  # window width
        wh = 600  # window height
        x = (sw - ww) / 2  # window coordinate (left_up point)
        y = (sh - wh) / 2  # window coordinate
        self.root.title('Please Specify Case of GRASP')
        self.root.geometry('%dx%d+%d+%d' % (ww, wh, x, y))
        self.task_no = task_no
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        tk.Label(self.root, text='Please Specify Case of GRASP', font=('bold', 14)) \
            .grid(row=0, column=0, pady=3, columnspan=10, sticky='w')
        tk.Label(self.root, text='(Note: Choose 1 of the following 11)', font=('bold', 12)) \
            .grid(row=1, column=0, pady=3, columnspan=10, sticky='w')
        
        # Header Labels
        headers = ['Case of GRASP', 'Description']
        tk.Label(self.root, text=headers[0], font=('bold', 14), width=15, relief='sunken') \
            .grid(row=2, column=0)
        tk.Label(self.root, text=headers[1], font=('bold', 14), width=80, relief='sunken') \
            .grid(row=2, column=1, columnspan=9)

        # Grasp Cases and Descriptions
        grasp_cases = [
            ("1A", "Pickup object of any size object, easily grasped"),
            ("1B", "Pickup very small object or object lying close against flat surface"),
            ("1C1", "Interference with grasp on bottom and one side of nearly cylindrical object. Diameter larger than ½ inch."),
            ("1C2", "Interference with grasp on bottom and one side of nearly cylindrical object. Diameter ¼ to ½ inch."),
            ("1C3", "Interference with grasp on bottom and one side of nearly cylindrical object. Diameter less than ¼ inch."),
            ("2", "Regrasp"),
            ("3", "Transfer Grasp"),
            ("4A", "Object jumbled with other objects so search and select occur. Larger than 1” x 1” x 1”"),
            ("4B", "Object jumbled with other objects so search and select occur. Between ¼” x ¼” x ½” and 1” x 1” x 1”"),
            ("4C", "Object jumbled with other objects so search and select occur. Smaller than ¼” x ¼” x ½”"),
            ("5", "Contact, sliding or hook grasp")
        ]

        for idx, (case, desc) in enumerate(grasp_cases, start=3):
            tk.Label(self.root, text=case, font=('bold', 12), width=15, relief='sunken') \
                .grid(row=idx, column=0)
            tk.Label(self.root, text=desc, font=('bold', 12), width=120, relief='sunken', anchor='w') \
                .grid(row=idx, column=1, columnspan=9)

        # Combobox for user selection
        self.selection = {}
        self.selection[self.task_no] = ttk.Combobox(
            master=self.root,
            width=10,
            state='readonly',
            cursor='arrow',
            values=[case for case, desc in grasp_cases],
            font=('bold', 10)
        )
        self.selection[self.task_no].grid(row=16, column=0, pady=10, columnspan=2)

        # Save Button
        self.Button_ok = tk.Button(self.root, text='Save and Back to Step2', font=16, command=self.save_data)
        self.Button_ok.grid(row=17, rowspan=3, column=1, columnspan=2, pady=20, ipady=3)

    def save_data(self):
       grasp_cases = [
         ("1A", "Pickup object of any size object, easily grasped"),
         ("1B", "Pickup very small object or object lying close against flat surface"),
         ("1C1", "Interference with grasp on bottom and one side of nearly cylindrical object. Diameter larger than ½ inch."),
         ("1C2", "Interference with grasp on bottom and one side of nearly cylindrical object. Diameter ¼ to ½ inch."),
         ("1C3", "Interference with grasp on bottom and one side of nearly cylindrical object. Diameter less than ¼ inch."),
         ("2", "Regrasp"),
         ("3", "Transfer Grasp"),
         ("4A", "Object jumbled with other objects so search and select occur. Larger than 1” x 1” x 1”"),
         ("4B", "Object jumbled with other objects so search and select occur. Between ¼” x ¼” x ½” and 1” x 1” x 1”"),
         ("4C", "Object jumbled with other objects so search and select occur. Smaller than ¼” x ¼” x ½”"),
         ("5", "Contact, sliding or hook grasp")
        ]
       try:
        selected_value = self.selection[self.task_no].get().strip()
        if selected_value not in [case for case, desc in grasp_cases]:
            raise ValueError("Please select a valid Case of GRASP.")
        
        # Save variables
        grasp_data = {
            "case_of_grasp": selected_value
        }
        
        # Save the grasp_data dictionary to a file or any required storage
        save_var(grasp_data, path+'/grasp_entity_dic.txt')
        self.root.destroy()

       except ValueError as e:
        self.show_error_message(str(e))


    def show_error_message(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Input Error")
        error_window.geometry("400x100")
        error_label = tk.Label(error_window, text=message, font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()

class GUI_ME_Position:
    def __init__(self, task_no):
        self.root = tk.Tk()
        sw = self.root.winfo_screenwidth()  # screen width
        sh = self.root.winfo_screenheight()  # screen height
        ww = 700  # window width
        wh = 350  # window height
        x = (sw - ww) / 2  # window coordinate (left_up point)
        y = (sh - wh) / 2  # window coordinate
        self.root.title('Please Specify Class of Fit and Symmetry')
        self.root.geometry('%dx%d+%d+%d' % (ww, wh, x, y))
        self.task_no = task_no
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        tk.Label(self.root, text='Please Specify Class of Fit:', font=('bold', 14)) \
            .grid(row=0, column=0, pady=3, columnspan=10, sticky='w')
        tk.Label(self.root, text='(Note: Choose 1 of the following 3):', font=('bold', 12)) \
            .grid(row=1, column=0, pady=3, columnspan=10, sticky='w')
        
        # Header Labels
        headers = ['Class of Fit', 'Description']
        tk.Label(self.root, text=headers[0], font=('bold', 14), width=15, relief='sunken') \
            .grid(row=2, column=0)
        tk.Label(self.root, text=headers[1], font=('bold', 14), width=50, relief='sunken') \
            .grid(row=2, column=1, columnspan=9)

        # Class of Fit and Descriptions
        class_of_fit = [
            ("1: Loose", "No pressure required"),
            ("2: Close", "Light pressure required"),
            ("3: Exact", "Heavy pressure required")
        ]

        for idx, (fit, desc) in enumerate(class_of_fit, start=3):
            tk.Label(self.root, text=fit, font=('bold', 12), width=15, relief='sunken') \
                .grid(row=idx, column=0)
            tk.Label(self.root, text=desc, font=('bold', 12), width=50, relief='sunken', anchor='w') \
                .grid(row=idx, column=1, columnspan=9)

        # Combobox for user selection of Class of Fit
        self.selection_fit = ttk.Combobox(
            master=self.root,
            width=10,
            state='readonly',
            cursor='arrow',
            values=["1: Loose", "2: Close", "3: Exact"],
            font=('bold', 10)
        )
        self.selection_fit.grid(row=6, column=0, pady=10, columnspan=2)

        # Title Label for Symmetry Selection
        tk.Label(self.root, text='Please Specify Symmetry:', font=('bold', 14)) \
            .grid(row=7, column=0, pady=3, columnspan=10, sticky='w')
        tk.Label(self.root, text='(Choose 1: S = Symmetrical, SS = Semi-Symmetrical, NS = Non-Symmetrical)', font=('bold', 12)) \
            .grid(row=8, column=0, pady=3, columnspan=10, sticky='w')

        # Combobox for Symmetry Selection
        self.selection_symmetry = ttk.Combobox(
            master=self.root,
            width=10,
            state='readonly',
            cursor='arrow',
            values=["S", "SS", "NS"],
            font=('bold', 10)
        )
        self.selection_symmetry.grid(row=9, column=0, pady=10, columnspan=2)

        # Save Button
        self.Button_ok = tk.Button(self.root, text='Save and Back to Step2', font=16, command=self.save_data)
        self.Button_ok.grid(row=10, rowspan=3, column=1, columnspan=2, pady=20, ipady=3)

    def save_data(self):
        class_of_fit = [
            ("1: Loose", "No pressure required"),
            ("2: Close", "Light pressure required"),
            ("3: Exact", "Heavy pressure required")
        ]
        try:
            selected_fit = self.selection_fit.get().strip()
            selected_symmetry = self.selection_symmetry.get().strip()
            if selected_fit not in [fit for fit, desc in class_of_fit] or selected_symmetry not in ["S", "SS", "NS"]:
                raise ValueError("Please select valid inputs.")
            
            # Save variables
            fit_data = {
                "class_of_fit": selected_fit,
                "symmetry": selected_symmetry
            }
            # Save the fit_data dictionary to a file or any required storage
            if self.task_no == '1':
                arm_information = 'left'  # or 'right' based on your context
            if self.task_no == '3':
                arm_information = 'right'

            attribute = {
            'arm': arm_information,
            # Add other relevant attributes here
            }

        # Save the dictionary to a file or any required storage
            save_var(attribute, path+'/attribute_dic.txt')
            save_var(fit_data, path+'/fit_entity_dic.txt')
            self.root.destroy()

        except ValueError as e:
            self.show_error_message(str(e))

    def show_error_message(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Input Error")
        error_window.geometry("400x100")
        error_label = tk.Label(error_window, text=message, font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()


class GUI_ME_Release:
    def __init__(self, task_no):
        self.root = tk.Tk()
        sw = self.root.winfo_screenwidth()  # screen width
        sh = self.root.winfo_screenheight()  # screen height
        ww = 700  # window width
        wh = 300  # window height
        x = (sw - ww) / 2  # window coordinate (left_up point)
        y = (sh - wh) / 2  # window coordinate
        self.root.title('Please Specify Case of RELEASE')
        self.root.geometry('%dx%d+%d+%d' % (ww, wh, x, y))
        self.task_no = task_no
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        tk.Label(self.root, text='Please Specify Case of RELEASE:', font=('bold', 14)) \
            .grid(row=0, column=0, pady=3, columnspan=10, sticky='w')
        
        # Header Labels
        headers = ['Case of RELEASE', 'Description']
        tk.Label(self.root, text=headers[0], font=('bold', 14), width=15, relief='sunken') \
            .grid(row=1, column=0)
        tk.Label(self.root, text=headers[1], font=('bold', 14), width=50, relief='sunken') \
            .grid(row=1, column=1, columnspan=9)

        # Case of Release and Descriptions
        release_cases = [
            ("1", "Normal release performed by opening fingers as independent motion"),
            ("2", "Contact release")
        ]

        for idx, (case, desc) in enumerate(release_cases, start=2):
            tk.Label(self.root, text=case, font=('bold', 12), width=15, relief='sunken') \
                .grid(row=idx, column=0)
            tk.Label(self.root, text=desc, font=('bold', 12), width=50, relief='sunken', anchor='w') \
                .grid(row=idx, column=1, columnspan=9)

        # Combobox for user selection
        self.selection = {}
        self.selection[self.task_no] = ttk.Combobox(
            master=self.root,
            width=10,
            state='readonly',
            cursor='arrow',
            values=[case for case, desc in release_cases],
            font=('bold', 10)
        )
        self.selection[self.task_no].grid(row=5, column=0, pady=10, columnspan=2)

        # Save Button
        self.Button_ok = tk.Button(self.root, text='Save and Back to Step2', font=16, command=self.save_data)
        self.Button_ok.grid(row=6, rowspan=3, column=1, columnspan=2, pady=20, ipady=3)

    def save_data(self):
        release_cases = [
            ("1", "Normal release performed by opening fingers as independent motion"),
            ("2", "Contact release")
        ]
        try:
            selected_value = self.selection[self.task_no].get().strip()
            if selected_value not in [case for case, desc in release_cases]:
                raise ValueError("Please select a valid Case of RELEASE.")
            
            # Save variables
            release_data = {
                "case_of_release": selected_value
            }
            # Save the release_data dictionary to a file or any required storage
            if self.task_no == '1':
                arm_information = 'left'  # or 'right' based on your context
            if self.task_no == '3':
                arm_information = 'right'

            attribute = {
            'arm': arm_information,
            # Add other relevant attributes here
            }

        # Save the dictionary to a file or any required storage
            save_var(attribute, path+'/attribute_dic.txt')
            save_var(release_data, path+'/release_entity_dic.txt')
            self.root.destroy()

        except ValueError as e:
            self.show_error_message(str(e))

    def show_error_message(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Input Error")
        error_window.geometry("400x100")
        error_label = tk.Label(error_window, text=message, font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()

class GUI_ME_Disengage:
    def __init__(self, task_no):
        self.root = tk.Tk()
        sw = self.root.winfo_screenwidth()  # screen width
        sh = self.root.winfo_screenheight()  # screen height
        ww = 1000  # window width
        wh = 550  # window height
        x = (sw - ww) / 2  # window coordinate (left_up point)
        y = (sh - wh) / 2  # window coordinate
        self.root.title('Open "Please Specify Class of Fit"')
        self.root.geometry('%dx%d+%d+%d' % (ww, wh, x, y))
        self.task_no = task_no
        self.setup_ui()
        
    def setup_ui(self):
        # Title Label for Class of Fit
        tk.Label(self.root, text='Please Specify Class of Fit:', font=('bold', 14)) \
            .grid(row=0, column=0, pady=3, columnspan=10, sticky='w')
        tk.Label(self.root, text='(Choose 1 of the following 3):', font=('bold', 12)) \
            .grid(row=1, column=0, pady=3, columnspan=10, sticky='w')
        
        # Header Labels
        headers = ['Class of Fit', 'Description']
        tk.Label(self.root, text=headers[0], font=('bold', 14), width=15, relief='sunken') \
            .grid(row=2, column=0)
        tk.Label(self.root, text=headers[1], font=('bold', 14), width=50, relief='sunken') \
            .grid(row=2, column=1, columnspan=9)

        # Class of Fit and Descriptions
        class_of_fit = [
            ("1", "Very slight effort, blends with subsequent move"),
            ("2", "Normal effort, slight recoil"),
            ("3", "Considerable effort, hand recoils markedly")
        ]

        for idx, (fit, desc) in enumerate(class_of_fit, start=3):
            tk.Label(self.root, text=f"Class {fit}", font=('bold', 12), width=15, relief='sunken') \
                .grid(row=idx, column=0)
            tk.Label(self.root, text=desc, font=('bold', 12), width=50, relief='sunken', anchor='w') \
                .grid(row=idx, column=1, columnspan=9)

        # Combobox for user selection of Class of Fit
        self.selection_fit = ttk.Combobox(
            master=self.root,
            width=10,
            state='readonly',
            cursor='arrow',
            values=["1", "2", "3"],  # Using numeric classes as per the table
            font=('bold', 10)
        )
        self.selection_fit.grid(row=6, column=0, pady=10, columnspan=2)

        # Title Label for Yes/No Question
        tk.Label(self.root, text='Is the object easy to handle:', font=('bold', 14)) \
            .grid(row=7, column=0, pady=3, columnspan=10, sticky='w')
        tk.Label(self.root, text='Yes/No answer only', font=('bold', 14), fg="blue") \
            .grid(row=8, column=0, pady=3, columnspan=10, sticky='w')

        # Combobox for Yes/No question
        self.selection_yesno = ttk.Combobox(
            master=self.root,
            width=10,
            state='readonly',
            cursor='arrow',
            values=["Yes", "No"],
            font=('bold', 10)
        )
        self.selection_yesno.grid(row=9, column=0, pady=10, columnspan=2)

        # Save Button
        self.Button_ok = tk.Button(self.root, text='Save and Back to Step2', font=16, command=self.save_data)
        self.Button_ok.grid(row=10, rowspan=3, column=1, columnspan=2, pady=20, ipady=3)

    def save_data(self):
        try:
            selected_fit = self.selection_fit.get().strip()
            selected_yesno = self.selection_yesno.get().strip()
            if selected_fit not in ["1", "2", "3"] or selected_yesno not in ["Yes", "No"]:
                raise ValueError("Please select valid inputs.")
            
            # Save variables
            disengage_data = {
                "class_of_fit": selected_fit,
                "ease_of_handling": "easy" if selected_yesno == "Yes" else "difficult"
            }

            # Determine arm information based on the task number
            if self.task_no == '1':
                arm_information = 'left'
            elif self.task_no == '3':
                arm_information = 'right'
            else:
                arm_information = 'unknown'

            attribute = {
                'arm': arm_information,
            }

            # Save the dictionaries to the specified files
            save_var(attribute, path+'/attribute_dic.txt')
            save_var(disengage_data, path+'/disengage_entity_dic.txt')
            self.root.destroy()

        except ValueError as e:
            self.show_error_message(str(e))

    def show_error_message(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Input Error")
        error_window.geometry("400x100")
        error_label = tk.Label(error_window, text=message, font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()

        

class GUI_ME_Sidestep:
    def __init__(self, task_no):
        self.root = tk.Tk()
        sw = self.root.winfo_screenwidth()  # screen width
        sh = self.root.winfo_screenheight()  # screen height
        ww = 700  # window width
        wh = 300  # window height
        x = (sw - ww) / 2  # window coordinate (left_up point)
        y = (sh - wh) / 2  # window coordinate
        self.root.title('Open "Please Specify CASE of SIDESTEP"')
        self.root.geometry('%dx%d+%d+%d' % (ww, wh, x, y))
        self.task_no = task_no
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        tk.Label(self.root, text='Please Specify CASE of SIDESTEP:', font=('bold', 14)) \
            .grid(row=0, column=0, pady=3, columnspan=10, sticky='w')
        
        # Header Labels
        headers = ['Case of SIDESTEP', 'Description']
        tk.Label(self.root, text=headers[0], font=('bold', 14), width=15, relief='sunken') \
            .grid(row=1, column=0)
        tk.Label(self.root, text=headers[1], font=('bold', 14), width=50, relief='sunken') \
            .grid(row=1, column=1, columnspan=9)

        # Case of SIDESTEP and Descriptions
        sidestep_cases = [
            ("1", "Complete when leading leg contacts floor"),
            ("2", "Lagging leg must contact floor before next motion can be made")
        ]

        for idx, (case, desc) in enumerate(sidestep_cases, start=2):
            tk.Label(self.root, text=case, font=('bold', 12), width=15, relief='sunken') \
                .grid(row=idx, column=0)
            tk.Label(self.root, text=desc, font=('bold', 12), width=50, relief='sunken', anchor='w') \
                .grid(row=idx, column=1, columnspan=9)

        # Combobox for user selection
        self.selection = {}
        self.selection[self.task_no] = ttk.Combobox(
            master=self.root,
            width=10,
            state='readonly',
            cursor='arrow',
            values=[case for case, desc in sidestep_cases],
            font=('bold', 10)
        )
        self.selection[self.task_no].grid(row=5, column=0, pady=10, columnspan=2)

        # Save Button
        self.Button_ok = tk.Button(self.root, text='Save and Back to Step2', font=16, command=self.save_data)
        self.Button_ok.grid(row=6, rowspan=3, column=1, columnspan=2, pady=20, ipady=3)

    def save_data(self):
        sidestep_cases = [
            ("1", "Complete when leading leg contacts floor"),
            ("2", "Lagging leg must contact floor before next motion can be made")
        ]
        try:
            selected_value = self.selection[self.task_no].get().strip()
            if selected_value not in [case for case, desc in sidestep_cases]:
                raise ValueError("Please select a valid Case of SIDESTEP.")
            
            # Save variables
            sidestep_data = {
                "case_of_sidestep": selected_value
            }
            attribute = {'body_part': 'body'} 
            save_var(attribute, path+'/attribute_dic.txt')
            # Save the sidestep_data dictionary to a file or any required storage
            save_var(sidestep_data, path+'/sidestep_entity_dic.txt')
            self.root.destroy()

        except ValueError as e:
            self.show_error_message(str(e))

    def show_error_message(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Input Error")
        error_window.geometry("400x100")
        error_label = tk.Label(error_window, text=message, font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()

        
class GUI_ME_Turn_body:
    def __init__(self, task_no):
        self.root = tk.Tk()
        sw = self.root.winfo_screenwidth()  # screen width
        sh = self.root.winfo_screenheight()  # screen height
        ww = 700  # window width
        wh = 300  # window height
        x = (sw - ww) / 2  # window coordinate (left_up point)
        y = (sh - wh) / 2  # window coordinate
        self.root.title('Open "Please Specify CASE of TURN BODY"')
        self.root.geometry('%dx%d+%d+%d' % (ww, wh, x, y))
        self.task_no = task_no
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        tk.Label(self.root, text='Please Specify CASE of TURN BODY:', font=('bold', 14)) \
            .grid(row=0, column=0, pady=3, columnspan=10, sticky='w')
        
        # Header Labels
        headers = ['Case of TURN BODY', 'Description']
        tk.Label(self.root, text=headers[0], font=('bold', 14), width=20, relief='sunken') \
            .grid(row=1, column=0)
        tk.Label(self.root, text=headers[1], font=('bold', 14), width=50, relief='sunken') \
            .grid(row=1, column=1, columnspan=9)

        # Case of TURN BODY and Descriptions
        turn_body_cases = [
            ("1", "Complete when leading leg contacts floor"),
            ("2", "Lagging leg must contact floor before next motion can be made")
        ]

        for idx, (case, desc) in enumerate(turn_body_cases, start=2):
            tk.Label(self.root, text=case, font=('bold', 12), width=20, relief='sunken') \
                .grid(row=idx, column=0)
            tk.Label(self.root, text=desc, font=('bold', 12), width=50, relief='sunken', anchor='w') \
                .grid(row=idx, column=1, columnspan=9)

        # Combobox for user selection
        self.selection = {}
        self.selection[self.task_no] = ttk.Combobox(
            master=self.root,
            width=10,
            state='readonly',
            cursor='arrow',
            values=[case for case, desc in turn_body_cases],
            font=('bold', 10)
        )
        self.selection[self.task_no].grid(row=4, column=0, pady=10, columnspan=2)

        # Save Button
        self.Button_ok = tk.Button(self.root, text='Save and Back to Step2', font=16, command=self.save_data)
        self.Button_ok.grid(row=5, rowspan=3, column=1, columnspan=2, pady=20, ipady=3)

    def save_data(self):
        turn_body_cases = [
            ("1", "Complete when leading leg contacts floor"),
            ("2", "Lagging leg must contact floor before next motion can be made")
        ]
        try:
            selected_value = self.selection[self.task_no].get().strip()
            if selected_value not in [case for case, desc in turn_body_cases]:
                raise ValueError("Please select a valid Case of TURN BODY.")
            
            # Save variables
            turn_body_data = {
                "case_of_turn_body": selected_value
            }
            # Save the turn_body_data dictionary to a file or any required storage
            save_var(turn_body_data, path+'/turn_body_entity_dic.txt')
            self.root.destroy()

        except ValueError as e:
            self.show_error_message(str(e))

    def show_error_message(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Input Error")
        error_window.geometry("400x100")
        error_label = tk.Label(error_window, text=message, font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()

class GUI_ME_Eye_Travel:
    def __init__(self, task_no):
        self.root = tk.Tk()
        sw = self.root.winfo_screenwidth()  # screen width
        sh = self.root.winfo_screenheight()  # screen height
        ww = 600  # window width
        wh = 300  # window height
        x = (sw - ww) / 2  # window coordinate (left_up point)
        y = (sh - wh) / 2  # window coordinate
        self.root.title('Please Specify Eye Travel Parameters')
        self.root.geometry('%dx%d+%d+%d' % (ww, wh, x, y))
        self.task_no = task_no
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        tk.Label(self.root, text='Please Specify Eye Travel Parameters:', font=('bold', 14)) \
            .grid(row=0, column=0, pady=3, columnspan=10, sticky='w')

        # Label for Eye Travel Distance (L)
        tk.Label(self.root, text='Eye Travel Distance (L) in cm:', font=('bold', 12)) \
            .grid(row=1, column=0, pady=3, sticky='w')
        self.entry_L = tk.Entry(self.root, width=15)
        self.entry_L.grid(row=1, column=1, pady=3, sticky='w')

        # Label for Distance from Eye to Line of Eye Travel (D)
        tk.Label(self.root, text='Distance from Eye to Line of Eye Travel (D) in cm:', font=('bold', 12)) \
            .grid(row=2, column=0, pady=3, sticky='w')
        self.entry_D = tk.Entry(self.root, width=15)
        self.entry_D.grid(row=2, column=1, pady=3, sticky='w')

        # Save Button
        self.Button_ok = tk.Button(self.root, text='Save and Back to Step2', font=16, command=self.save_data)
        self.Button_ok.grid(row=3, column=0, columnspan=2, pady=20, ipady=3)

    def save_data(self):
        try:
            # Get the input values
            L = float(self.entry_L.get().strip())
            D = float(self.entry_D.get().strip())

            if L <= 0 or D <= 0:
                raise ValueError("Distances must be positive numbers.")

            # Calculate the TMU based on the formula: 15.2 * L / D
            tmu_value = 15.2 * L / D

            # Save the TMU value
            eye_travel_data = {
                "L": L,
                "D": D,
                "tmu_value": tmu_value
            }

            save_var(eye_travel_data, path+'/eye_travel_entity_dic.txt')
            self.root.destroy()

        except ValueError as e:
            self.show_error_message(str(e))

    def show_error_message(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Input Error")
        error_window.geometry("400x100")
        error_label = tk.Label(error_window, text=message, font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()

class GUI_BE_static_tracing:
    def __init__(self,task_no):
    
        self.root = tk.Tk()    
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=500    #window width
        wh=700 #window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.root.title('Static_2DTracing')
        self.root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        self.task_no=task_no
        tk.Label(self.root,text='Select trajectory shape:',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        value_static2D_shape = ['Sin','Exp','Ln']
        self.static2D_shape={}
        self.static2D_shape[self.task_no] = ttk.Combobox(
            master = self.root,
            state='readonly',
            cursor='arrow',
            width=22,
            values=value_static2D_shape, 
            )
        #self.stimulitype.bind('<<ComboboxSelected>>',self.pick)
        self.static2D_shape[self.task_no].pack(anchor='w',padx=10)
        
        if saved==1:
            for item in range(len(value_static2D_shape)):
                if load_var(path+'/static2D_shape.txt')==value_static2D_shape[item]:
                    self.static2D_shape[self.task_no].current(item)
        
        tk.Label(self.root,text='Enter target starting location (x): (An integer in 0-100) ',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        self.static2D_target_loc_x={}
        
        self.static2D_target_loc_x[self.task_no]=tk.Entry(self.root,width=20)
        self.static2D_target_loc_x[self.task_no].pack(anchor='w',padx=10)
        if saved==1:
            self.static2D_target_loc_x[self.task_no].insert(0,str(load_var(path+'/static2D_target_loc_x.txt')))
        
        tk.Label(self.root,text='Enter cursor starting location (x): (An integer in 0-100) ',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        self.static2D_cursor_loc_x={}
        
        self.static2D_cursor_loc_x[self.task_no]=tk.Entry(self.root,width=20)
        self.static2D_cursor_loc_x[self.task_no].pack(anchor='w',padx=10)
        if saved==1:
            self.static2D_cursor_loc_x[self.task_no].insert(0,str(load_var(path+'/static2D_cursor_loc_x.txt')))
        
        tk.Label(self.root,text='Select target movement frequency:',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        
        value_static2D_freq = ['Slow','Medium','Quick']
        
        self.static2D_freq={}
        self.static2D_freq[self.task_no] = ttk.Combobox(
            master = self.root,
            state='readonly',
            cursor='arrow',
            width=22,
            values=value_static2D_freq, 
            )
        #self.stimulitype.bind('<<ComboboxSelected>>',self.pick)
        self.static2D_freq[self.task_no].pack(anchor='w',padx=10)
        
        if saved==1:
            for item in range(len(value_static2D_freq)):
                if load_var(path+'/static2D_freq.txt')==value_static2D_freq[item]:
                    self.static2D_freq[self.task_no].current(item)
        
        
        tk.Label(self.root,text='Select target movement amplitude:',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        
        value_static2D_amp = ['Small','Medium','Large']
        self.static2D_amp={}
        self.static2D_amp[self.task_no] = ttk.Combobox(
            master = self.root,
            state='readonly',
            cursor='arrow',
            width=22,
            values=value_static2D_amp, 
            )
        #self.stimulitype.bind('<<ComboboxSelected>>',self.pick)
        self.static2D_amp[self.task_no].pack(anchor='w',padx=10)
        
        if saved==1:
            for item in range(len(value_static2D_amp)):
                if load_var(path+'/static2D_amp.txt')==value_static2D_amp[item]:
                    self.static2D_amp[self.task_no].current(item)
        
        tk.Label(self.root,text='Select response method:',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        
        value_static2D_response = ['Click mouse','Press keyboard']
        
        self.static2D_response={}
        self.static2D_response[self.task_no] = ttk.Combobox(
            master = self.root,
            state='readonly',
            cursor='arrow',
            width=22,
            values=value_static2D_response, 
            )
        #self.stimulitype.bind('<<ComboboxSelected>>',self.pick)
        self.static2D_response[self.task_no].pack(anchor='w',padx=10)
        
        if saved==1:
            for item in range(len(value_static2D_response)):
                if load_var(path+'/static2D_response.txt')==value_static2D_response[item]:
                    self.static2D_response[self.task_no].current(item)
        
        self.Button_ok=tk.Button(self.root,text='OK',font=16,command=self.entry_event)
        self.Button_ok.pack()
    #Ziqi's modification of type checking    
    def entry_event(self):
        global static2D_shape, static2D_target_loc_x, static2D_cursor_loc_x, static2D_freq, static2D_amp, static2D_response
        try:
            static2D_cursor_loc_x = int(self.static2D_cursor_loc_x[self.task_no].get())
            if static2D_cursor_loc_x < 0 or static2D_cursor_loc_x > 100:
                raise ValueError
            save_var(static2D_cursor_loc_x, path+'/static2D_cursor_loc_x.txt')
            
            static2D_target_loc_x = int(self.static2D_target_loc_x[self.task_no].get())
            if static2D_target_loc_x < 0 or static2D_target_loc_x > 100:
                raise ValueError
            save_var(static2D_target_loc_x, path+'/static2D_target_loc_x.txt')
            
            static2D_freq = self.static2D_freq[self.task_no].get()
            save_var(static2D_freq, path+'/static2D_freq.txt')
            
            static2D_amp = self.static2D_amp[self.task_no].get()
            save_var(static2D_amp, path+'/static2D_amp.txt')
            
            static2D_shape = self.static2D_shape[self.task_no].get()
            save_var(static2D_shape, path+'/static2D_shape.txt')
            
            static2D_response = self.static2D_response[self.task_no].get()
            save_var(static2D_response, path+'/static2D_response.txt')
            
            self.root.destroy()
        except ValueError:
            self.show_error_message()
            return
            
    def show_error_message(self):
        error_window = tk.Toplevel(self.root)
        error_window.title("Error")
        error_window.geometry("300x100")
        error_label = tk.Label(error_window, text="Please enter an integer between 0 and 100 for the target and cursor starting locations.", font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()


class GUI_BE_dynamic1D:
    def __init__(self,task_no):
    
        self.root = tk.Tk()    
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=500    #window width
        wh=500 #window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.root.title('Dynamic_1D')
        self.root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        self.task_no=task_no
        tk.Label(self.root,text='Enter curse starting location: (An integer in 1-100) ',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        self.dynamic1D_cursor_loc={}
        
        self.dynamic1D_cursor_loc[self.task_no]=tk.Entry(self.root,width=20)
        self.dynamic1D_cursor_loc[self.task_no].pack(anchor='w',padx=10)
        if saved==1:
            self.dynamic1D_cursor_loc[self.task_no].insert(0,str(load_var(path+'/dynamic1D_cursor_loc.txt')))
        tk.Label(self.root,text='Select target movement dynamic1D_freq:',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        
        value_dynamic1D_freq = ['Slow','Medium','Quick']
        
        self.dynamic1D_freq={}
        self.dynamic1D_freq[self.task_no] = ttk.Combobox(
            master = self.root,
            state='readonly',
            cursor='arrow',
            width=22,
            values=value_dynamic1D_freq, 
            )
        #self.stimulitype.bind('<<ComboboxSelected>>',self.pick)
        self.dynamic1D_freq[self.task_no].pack(anchor='w',padx=10)
        
        if saved==1:
            for item in range(len(value_dynamic1D_freq)):
                if load_var(path+'/dynamic1D_freq.txt')==value_dynamic1D_freq[item]:
                    self.dynamic1D_freq[self.task_no].current(item)
        
        
        tk.Label(self.root,text='Select target movement dynamic1D_amp:',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        
        value_dynamic1D_amp = ['Small','Medium','Large']
        self.dynamic1D_amp={}
        self.dynamic1D_amp[self.task_no] = ttk.Combobox(
            master = self.root,
            state='readonly',
            cursor='arrow',
            width=22,
            values=value_dynamic1D_amp, 
            )
        #self.stimulitype.bind('<<ComboboxSelected>>',self.pick)
        self.dynamic1D_amp[self.task_no].pack(anchor='w',padx=10)
        
        if saved==1:
            for item in range(len(value_dynamic1D_amp)):
                if load_var(path+'/dynamic1D_amp.txt')==value_dynamic1D_amp[item]:
                    self.dynamic1D_amp[self.task_no].current(item)
        
        tk.Label(self.root,text='Select response method:',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        
        value_dynamic1D_response = ['Click mouse','Press keyboard']
        
        self.dynamic1D_response={}
        self.dynamic1D_response[self.task_no] = ttk.Combobox(
            master = self.root,
            state='readonly',
            cursor='arrow',
            width=22,
            values=value_dynamic1D_response, 
            )
        #self.stimulitype.bind('<<ComboboxSelected>>',self.pick)
        self.dynamic1D_response[self.task_no].pack(anchor='w',padx=10)
        
        if saved==1:
            for item in range(len(value_dynamic1D_response)):
                if load_var(path+'/dynamic1D_response.txt')==value_dynamic1D_response[item]:
                    self.dynamic1D_response[self.task_no].current(item)
        
        self.Button_ok=tk.Button(self.root,text='OK',font=16,command=self.entry_event)
        self.Button_ok.pack()
    #Ziqi's modification of type checking    
    def entry_event(self):
        global dynamic1D_cursor_loc, dynamic1D_freq, dynamic1D_amp, dynamic1D_response
        try:
            dynamic1D_cursor_loc = int(self.dynamic1D_cursor_loc[self.task_no].get())
            if dynamic1D_cursor_loc < 1 or dynamic1D_cursor_loc > 100:
                raise ValueError
            save_var(dynamic1D_cursor_loc, path+'/dynamic1D_cursor_loc.txt')
            
            dynamic1D_freq = self.dynamic1D_freq[self.task_no].get()
            save_var(dynamic1D_freq, path+'/dynamic1D_freq.txt')
            
            dynamic1D_amp = self.dynamic1D_amp[self.task_no].get()
            save_var(dynamic1D_amp, path+'/dynamic1D_amp.txt')
            
            dynamic1D_response = self.dynamic1D_response[self.task_no].get()
            save_var(dynamic1D_response, path+'/dynamic1D_response.txt')
            
            self.root.destroy()
        except ValueError:
            self.show_error_message()
            return
            
    def show_error_message(self):
        error_window = tk.Toplevel(self.root)
        error_window.title("Error")
        error_window.geometry("300x100")
        error_label = tk.Label(error_window, text="Please enter an integer between 1 and 100 for the cursor starting location.", font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()

class GUI_BE_dynamic2D:
    def __init__(self,task_no):
    
        self.root = tk.Tk()    
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=500    #window width
        wh=700 #window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.root.title('Dynamic_2DTracing')
        self.root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        self.task_no=task_no
        tk.Label(self.root,text='Select trajectory shape:',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        value_dynamic2D_shape = ['Sin','Exp','Ln']
        self.dynamic2D_shape={}
        self.dynamic2D_shape[self.task_no] = ttk.Combobox(
            master = self.root,
            state='readonly',
            cursor='arrow',
            width=22,
            values=value_dynamic2D_shape, 
            )
        #self.stimulitype.bind('<<ComboboxSelected>>',self.pick)
        self.dynamic2D_shape[self.task_no].pack(anchor='w',padx=10)
        
        if saved==1:
            for item in range(len(value_dynamic2D_shape)):
                if load_var(path+'/dynamic2D_shape.txt')==value_dynamic2D_shape[item]:
                    self.dynamic2D_shape[self.task_no].current(item)
        
        tk.Label(self.root,text='Enter target starting location (x): (An integer in 0-100) ',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        self.dynamic2D_target_loc_x={}
        
        self.dynamic2D_target_loc_x[self.task_no]=tk.Entry(self.root,width=20)
        self.dynamic2D_target_loc_x[self.task_no].pack(anchor='w',padx=10)
        if saved==1:
            self.dynamic2D_target_loc_x[self.task_no].insert(0,str(load_var(path+'/dynamic2D_target_loc_x.txt')))
        
        tk.Label(self.root,text='Enter cursor starting location (x): (An integer in 0-100) ',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        self.dynamic2D_cursor_loc_x={}
        
        self.dynamic2D_cursor_loc_x[self.task_no]=tk.Entry(self.root,width=20)
        self.dynamic2D_cursor_loc_x[self.task_no].pack(anchor='w',padx=10)
        if saved==1:
            self.dynamic2D_cursor_loc_x[self.task_no].insert(0,str(load_var(path+'/dynamic2D_cursor_loc_x.txt')))
        
        tk.Label(self.root,text='Select target movement frequency:',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        
        value_dynamic2D_freq = ['Slow','Medium','Quick']
        
        self.dynamic2D_freq={}
        self.dynamic2D_freq[self.task_no] = ttk.Combobox(
            master = self.root,
            state='readonly',
            cursor='arrow',
            width=22,
            values=value_dynamic2D_freq, 
            )
        #self.stimulitype.bind('<<ComboboxSelected>>',self.pick)
        self.dynamic2D_freq[self.task_no].pack(anchor='w',padx=10)
        
        if saved==1:
            for item in range(len(value_dynamic2D_freq)):
                if load_var(path+'/dynamic2D_freq.txt')==value_dynamic2D_freq[item]:
                    self.dynamic2D_freq[self.task_no].current(item)
        
        
        tk.Label(self.root,text='Select target movement amplitude:',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        
        value_dynamic2D_amp = ['Small','Medium','Large']
        self.dynamic2D_amp={}
        self.dynamic2D_amp[self.task_no] = ttk.Combobox(
            master = self.root,
            state='readonly',
            cursor='arrow',
            width=22,
            values=value_dynamic2D_amp, 
            )
        #self.stimulitype.bind('<<ComboboxSelected>>',self.pick)
        self.dynamic2D_amp[self.task_no].pack(anchor='w',padx=10)
        
        if saved==1:
            for item in range(len(value_dynamic2D_amp)):
                if load_var(path+'/dynamic2D_amp.txt')==value_dynamic2D_amp[item]:
                    self.dynamic2D_amp[self.task_no].current(item)
        
        tk.Label(self.root,text='Select response method:',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        
        value_dynamic2D_response = ['Click mouse','Press keyboard']
        
        self.dynamic2D_response={}
        self.dynamic2D_response[self.task_no] = ttk.Combobox(
            master = self.root,
            state='readonly',
            cursor='arrow',
            width=22,
            values=value_dynamic2D_response, 
            )
        #self.stimulitype.bind('<<ComboboxSelected>>',self.pick)
        self.dynamic2D_response[self.task_no].pack(anchor='w',padx=10)
        
        if saved==1:
            for item in range(len(value_dynamic2D_response)):
                if load_var(path+'/dynamic2D_response.txt')==value_dynamic2D_response[item]:
                    self.dynamic2D_response[self.task_no].current(item)
        
        self.Button_ok=tk.Button(self.root,text='OK',font=16,command=self.entry_event)
        self.Button_ok.pack()
        
    def entry_event(self):
        global dynamic2D_shape, dynamic2D_target_loc_x, dynamic2D_cursor_loc_x, dynamic2D_freq, dynamic2D_amp, dynamic2D_response
        try:
            dynamic2D_cursor_loc_x = int(self.dynamic2D_cursor_loc_x[self.task_no].get())
            if dynamic2D_cursor_loc_x < 0 or dynamic2D_cursor_loc_x > 100:
                raise ValueError
            save_var(dynamic2D_cursor_loc_x, path+'/dynamic2D_cursor_loc_x.txt')
            
            dynamic2D_target_loc_x = int(self.dynamic2D_target_loc_x[self.task_no].get())
            if dynamic2D_target_loc_x < 0 or dynamic2D_target_loc_x > 100:
                raise ValueError
            save_var(dynamic2D_target_loc_x, path+'/dynamic2D_target_loc_x.txt')
            
            dynamic2D_freq = self.dynamic2D_freq[self.task_no].get()
            save_var(dynamic2D_freq, path+'/dynamic2D_freq.txt')
            
            dynamic2D_amp = self.dynamic2D_amp[self.task_no].get()
            save_var(dynamic2D_amp, path+'/dynamic2D_amp.txt')
            
            dynamic2D_shape = self.dynamic2D_shape[self.task_no].get()
            save_var(dynamic2D_shape, path+'/dynamic2D_shape.txt')
            
            dynamic2D_response = self.dynamic2D_response[self.task_no].get()
            save_var(dynamic2D_response, path+'/dynamic2D_response.txt')
            
            self.root.destroy()
        except ValueError:
            self.show_error_message()
            return
            
    def show_error_message(self):
        error_window = tk.Toplevel(self.root)
        error_window.title("Error")
        error_window.geometry("300x100")
        error_label = tk.Label(error_window, text="Please enter an integer between 0 and 100 for the target and cursor starting locations.", font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()

# a = GUI_User_Main()
# a.root.mainloop()   

user_interface = GUI_User_Main()
user_interface.root.mainloop()


#-----------------------
#Section3 Structure and Animation

#3.1 structure and animation window definition


class myCanvas(tk.Frame):
    def __init__(self, root,w,h):
        self.root = root
        self.w = w
        self.h = h
        self.canvas = tk.Canvas(root, width=self.w, height=self.h)
        self.canvas.pack( fill=tk.BOTH, expand=tk.YES)
        root.bind('<Configure>', self.resize)
    def resize(self, event):
        wscale=event.width/self.w
        hscale=event.height/self.h
        h_font=self.h/36
        arrow_1=self.w/91
        arrow_2=arrow_1
        arrow_3=self.h/256
        if wscale>1.05 or wscale<0.95 or hscale>1.05 or hscale<0.95:
            for m in range(1,25):
                self.canvas.itemconfig('text'+str(m),font=("Times New Roman",int(h_font*hscale)))
            for m in range(1,29):
                self.canvas.itemconfig('link_1x_'+str(m),arrowshape=[arrow_1*wscale,arrow_2*wscale,arrow_3*hscale])
            for m in range(1,17):
                self.canvas.itemconfig('link_1y_'+str(m),arrowshape=[arrow_1*hscale,arrow_2*hscale,arrow_3*wscale])
            for m in range(1,3):
                self.canvas.itemconfig('link_2y_'+str(m),arrowshape=[arrow_1*hscale,arrow_2*hscale,arrow_3*wscale])
            self.canvas.itemconfig('link_2x', arrowshape=[arrow_1*wscale,arrow_2*wscale,arrow_3*hscale])
            self.canvas.itemconfig('link_slope',arrowshape=[arrow_1*wscale,arrow_2*wscale,arrow_3*hscale])

            self.canvas.scale('all',0,0,wscale,hscale)
            self.w=event.width
            self.h=event.height
            self.canvas.pack(fill=tk.BOTH, expand=tk.YES)


#3.2 structure and animation

class Structure_and_Animation:   
    root = tk.Tk()
    w=root.winfo_screenwidth()/8*5
    h=root.winfo_screenheight()/3*2
    dx = w//30 
    frame=myCanvas(root,w,h)
    frame.canvas.pack(fill="both",expand=True)
    dx = w/30
    Capacity = {}
    Capacity['1']=10e5
    Capacity['2']=4
    Capacity['3']=4
    Capacity['4']=5
    Capacity['5']=10e5
    Capacity['6']=4
    Capacity['7']=4
    Capacity['8']=5
    Capacity['A']=4
    Capacity['B']=4
    Capacity['C']=5
    Capacity['D']=10e5
    Capacity['E']=1
    Capacity['F']=1
    Capacity['G']=10e5
    Capacity['H'] = 10e5  #unknown
    Capacity['W']=1
    Capacity['X'] = 10e5  #unknown
    Capacity['Y']=2
    Capacity['Z']=5
    Capacity['V']=10e5    #unknown
    Capacity['21']=1     #mouth
    Capacity['22'] = 1   #eye
    Capacity['23']=1     #lefthand
    Capacity['24']=1     #righthand
    space={}
   
    entity_loc={}
    entity_num={}
    ls=[]
    for k,v in Capacity.items():
        if v !=10e5:
            ls.append(v)
            circle_r = dx/max(ls)/2   #radius of circle entity
            
    save_dic={}
    save_dic_copy={}
    Cache=list() 
    occupy_dic={}
    loc_dic={}
    s={}
    
    
    def  background (self):
        
        dx=self.dx
        frame=self.frame
        capacity=self.Capacity
        space=self.space
        #generate the rectangles and text
        Boxes=list()
        Boxes.append({'name':'1','location':[3,3,4,4]})
        Boxes.append({'name':'2','location':[5, 1, 6, 2]})
        Boxes.append({'name':'3','location':[5, 5, 6, 6]})
        Boxes.append({'name':'4','location':[7, 3, 8, 4]})
        Cache=self.Cache
        Cache.append({'name':'0_1','location':[2.5,3,3,4]})
        Cache.append({'name':'1_2','location':[4.5,1,5,2]})
        Cache.append({'name':'1_3','location':[4.5,5,5,6]})
        Cache.append({'name':'2_4','location':[7,2.5,8,3]})
        Cache.append({'name':'3_4','location':[7,4,8,4.5]})
       
        Boxes.append({'name':'5','location':[3, 10,4, 11]})
        Boxes.append({'name':'6','location':[5, 8, 6, 9]})
        Boxes.append({'name':'7','location':[5, 12,6, 13]})
        Boxes.append({'name':'8','location':[7, 10,8, 11]})
        Cache.append({'name':'0_5','location':[2.5,10,3,11]})
        Cache.append({'name':'5_6','location':[4.5,8,5,9]})
        Cache.append({'name':'5_7','location':[4.5,12,5,13]})
        Cache.append({'name':'6_8','location':[7,9.5,8,10]})
        Cache.append({'name':'7_8','location':[7,11,8,11.5]})
         
        Boxes.append({'name':'A','location':[11, 6, 12, 7]})
        Cache.append({'name':'4_A','location':[10.5,6,11,6.5]})
        Cache.append({'name':'8_A','location':[10.5,6.5,11,7]})
        Cache.append({'name':'C_A','location':[11,7,12,7.5]})
        
        Boxes.append({'name':'B','location':[11, 9, 12, 10]})
        Cache.append({'name':'4_B','location':[10.5,9,11,9.5]})
        Cache.append({'name':'8_B','location':[10.5,9.5,11,10]})
        Cache.append({'name':'C_B','location':[11,8.5,12,9]})

        Boxes.append({'name':'C','location':[12.7, 7.5, 13.7, 8.5]})
        #Cache.append({'name':'A_C','location':[12.2,7.5,12.7,7.75]})
        Cache.append({'name':'A_C','location':[12.2,7.5,12.7,7.9]})
        #Cache.append({'name':'B_C','location':[12.2,7.75,12.7,8.25]})
        Cache.append({'name':'B_C','location':[12.2,7.9,12.7,8.15]})
        Cache.append({'name':'D_C','location':[13.3,7.1,13.7,7.5]})
        Cache.append({'name':'F_C','location':[13.2,8.5,13.7,9]})
        Cache.append({'name':'G_C','location':[13.7,7.5,14.2,8.5]})
        Cache.append({'name':'H_C','location':[13.7,8.5,14.2,9]})
        #Cache.append({'name':'X_C','location':[12.2,8.25,12.7,8.5]})
        Cache.append({'name':'X_C','location':[12.2,8.15,12.7,8.5]})

        Boxes.append({'name':'D','location':[13, 5, 14, 6]})
        Cache.append({'name':'G_D','location':[14,5,14.5,6]})
        Cache.append({'name':'C_D','location':[13.3,6,13.7,6.4]})

        Boxes.append({'name':'F','location':[13, 10, 14, 11]})
        Cache.append({'name':'C_F','location':[13,9.5,14,10]})
        Cache.append({'name':'H_F','location':[14,10,14.4,11]})

        Boxes.append({'name':'H','location':[15, 10, 16, 11]})
        Cache.append({'name':'C_H','location':[14.6,9.5,15,10]})
        Cache.append({'name':'G_H','location':[15,9.5,16,10]})
        Cache.append({'name':'F_H','location':[14.6,10,15,11]})

        Boxes.append({'name':'G','location':[15, 7.5, 16, 8.5]})
        Cache.append({'name':'C_G','location':[14.5,7.5,15,8.5]})
        Cache.append({'name':'H_G','location':[15,8.5,16,9]})

        Boxes.append({'name':'V','location':[20, 3, 21, 4]})
        Cache.append({'name':'A_V','location':[20,2.5,21,3]})
        Cache.append({'name':'B_V','location':[19.5,3.5,20,4]})
        Cache.append({'name':'C_V','location':[19.5,3,20,3.5]})
      
        Boxes.append({'name':'W','location':[20, 5.5, 21, 6.5]})
        Cache.append({'name':'V_W','location':[20,5,21,5.5]})
        Cache.append({'name':'A_W','location':[19.5,5.5,20,5.7]})
        Cache.append({'name':'C_W','location':[19.5,5.7,20,5.9]})
        Cache.append({'name':'D_W','location':[19.5,5.9,20,6.1]})
        Cache.append({'name':'B_W','location':[19.5,6.1,20,6.3]})
        Cache.append({'name':'X_W','location':[19.5,6.3,20,6.5]})

        Boxes.append({'name':'Y','location':[20, 9, 21, 10]})
        Cache.append({'name':'W_Y','location':[20,8.5,21,9]})
        Cache.append({'name':'X_Y','location':[20,10,21,10.5]})
        Cache.append({'name':'C_Y','location':[19.5,9,20,10]})
            
        Boxes.append({'name':'X','location':[20, 11, 21, 12]})
        Cache.append({'name':'B_X','location':[20,12,20.5,12.5]})
        Cache.append({'name':'21_X','location':[20.5,12,21,12.5]})
        Cache.append({'name':'Z_X','location':[21,11,21.5,12]})
        Cache.append({'name':'A_X','location':[19.5,11.3,20,12]})

        Boxes.append({'name':'Z','location':[22, 9, 23, 10]})
        Cache.append({'name':'V_Z','location':[22,8.5,23,9]})
        Cache.append({'name':'Y_Z','location':[21.5,9,22,10]})

        Boxes.append({'name':'21','location':[24, 3, 25, 4]})
        Boxes.append({'name':'22','location':[24, 5.5, 25, 6.5]})
        Boxes.append({'name':'23','location':[24, 9, 25, 10]})
        Boxes.append({'name':'24','location':[24, 11, 25, 12]})
        Cache.append({'name':'Z_21','location':[23.5,3,24,4]})
        Cache.append({'name':'Z_22','location':[23.5,5.5,24,6.5]})
        Cache.append({'name':'Z_23','location':[23.5,9,24,10]})
        Cache.append({'name':'Z_24','location':[23.5,11,24,12]})

        links=list()
        links.append({'name':'0_1','location':[1.9, 3.5, 3,  3.5],'arrows':'1x'}) 
        links.append({'name':'1_2','location':[3.5, 3, 3.5, 1.5, 5, 1.5],'arrows':'1x'})
        links.append({'name':'1_3','location':[3.5, 4, 3.5, 5.5, 5, 5.5],'arrows':'1x'})  
        links.append({'name':'0_5','location':[1.9, 10.5, 3, 10.5],'arrows':'1x'}) 
        links.append({'name':'5_6','location':[3.5, 10, 3.5, 8.5, 5, 8.5],'arrows':'1x'})
        links.append({'name':'5_7','location':[3.5, 11, 3.5, 12.5, 5, 12.5],'arrows':'1x'}) 
        links.append({'name':'4_A','location':[8, 3.4, 9.1, 3.4, 9.1, 6.25, 11, 6.25],'arrows':'1x'}) 
        links.append({'name':'4_B','location':[8, 3.6, 8.9, 3.6, 8.9, 9.25, 11, 9.25],'arrows':'1x'}) 
        links.append({'name':'8_B','location':[8, 10.4, 8.7, 10.4, 8.7, 6.75,11, 6.75],'arrows':'1x'})### 
        links.append({'name':'8_A','location':[8, 10.6, 9.1, 10.6, 9.1, 9.75, 11, 9.75, ],'arrows':'1x'})### 
        links.append({'name':'A_W','location':[11.5, 6, 11.5, 1.3, 19.2, 1.3,19.2, 5.6, 20, 5.6],'arrows':'1x'}) 
        links.append({'name':'A_X','location':[11.7, 6, 11.7, 2.2, 18, 2.2, 18, 11.6, 20, 11.6],'arrows':'1x'}) 
        links.append({'name':'C_A','location':[11.5, 7.75, 11.5, 7],'arrows':'1y'}) 
        #links.append({'name':'A_C','location':[11.5, 7.75, 12.7, 7.75],'arrows':'1x'}) 
        links.append({'name':'A_C','location':[11.5, 7.75, 12.7, 7.75],'arrows':'1x'})
        links.append({'name':'C_B','location':[11.5, 8.25, 11.5, 9],'arrows':'1y'}) 
        #links.append({'name':'B_C','location':[11.5, 8.25, 12.7, 8.25],'arrows':'1x'}) 
        links.append({'name':'B_C','location':[11.5, 8, 12.7, 8],'arrows':'1x'})
        links.append({'name':'B_W','location':[11.5, 10, 11.5, 13, 19.2, 13, 19.2, 6.2, 20, 6.2],'arrows':'1x'}) 
        links.append({'name':'B_V','location':[11.7, 10, 11.7, 12.7, 19, 12.7, 19, 3.7, 20, 3.7],'arrows':'1x'})#### 
        #links.append({'name':'C_G','location':[13.7, 8, 15, 8],'arrows':'1x'}) 
        # changed C_G to bidirectional
        links.append({'name':'C_G','location':[13.7, 8, 15, 8],'arrows':'2x'})
        links.append({'name':'Y_Z','location':[21, 9.5, 22, 9.5],'arrows':'1x'}) 
        links.append({'name':'Z_22','location':[23.3, 6, 24, 6],'arrows':'1x'}) 
        links.append({'name':'Z_23','location':[23.3, 9.5, 24, 9.5],'arrows':'1x'}) 
        links.append({'name':'Z_24','location':[23.3, 11.5, 24, 11.5],'arrows':'1x'}) 
        links.append({'name':'G_D','location':[15.5, 7.5, 15.5, 5.5, 14, 5.5],'arrows':'1x'}) 
        links.append({'name':'Z_X','location':[22.5, 10, 22.5, 11.5, 21, 11.5],'arrows':'1x'}) 
        links.append({'name':'Z_21','location':[23, 9.5, 23.3,9.5,23.3, 3.5, 24, 3.5],'arrows':'1x'})#### 
        links.append({'name':'C_W','location':[12.9, 7.5, 12.9, 1.9, 18.7, 1.9, 18.7, 5.8, 20, 5.8],'arrows':'1x'})
        links.append({'name':'X_W','location':[20, 11.1, 19.3, 11.1, 19.3, 6.4,20, 6.4],'arrows':'1x'})  
        links.append({'name':'D_W','location':[13.5, 5, 13.5, 2.5, 17, 2.5,17, 6, 20, 6],'arrows':'1x'}) 
        links.append({'name':'Right_Left','location':[25.3, 7.7, 27, 7.7, 27, 14.6,1, 14.6, 1, 7,1.9, 7],'arrows':'1x'}) 
        links.append({'name':'2_4','location':[6, 1.5, 7.5, 1.5, 7.5, 3],'arrows':'1y'})
        links.append({'name':'3_4','location':[6, 5.5, 7.5, 5.5, 7.5, 4],'arrows':'1y'})
        links.append({'name':'6_8','location':[6, 8.5, 7.5, 8.5, 7.5, 10],'arrows':'1y'})
        links.append({'name':'7_8','location':[6, 12.5, 7.5, 12.5, 7.5, 11],'arrows':'1y'})
        links.append({'name':'A_V','location':[11.3, 6, 11.3, 1, 20.5, 1, 20.5, 3],'arrows':'1y'})  
        links.append({'name':'B_X','location':[11.3, 10, 11.3, 13.3, 20.3, 13.3, 20.3, 12],'arrows':'1y'})  
        #links.append({'name':'D_C','location':[13.5, 6, 13.5, 7.5],'arrows':'1y'}) 
        links.append({'name':'D_C','location':[13.5, 6, 13.5, 7.5],'arrows':'2y'}) 
        # Changed C_D to bidirectional 
        links.append({'name':'V_W','location':[20.5, 4, 20.5, 5.5],'arrows':'1y'}) 
        links.append({'name':'W_Y','location':[20.5, 6.5, 20.5, 9],'arrows':'1y'})  
        links.append({'name':'X_Y','location':[20.5, 11, 20.5, 10],'arrows':'1y'}) 
        # X to C added
        links.append({'name':'X_C','location':[20, 11.2, 12.1, 11.2,12.1,8.25,12.7,8.25],'arrows':'1x'}) 
        # changed to C_Y
        #links.append({'name':'Y_C','location':[20, 9.5, 17, 9.5, 17, 12.5, 12.9, 12.5, 12.9, 8.5],'arrows':'1y'})
        links.append({'name':'C_Y','location':[12.9, 8.5, 12.9, 12.5, 17, 12.5, 17, 9.5, 20, 9.5],'arrows':'1y'})  
        links.append({'name':'V_Z','location':[21, 3.5, 22.5, 3.5, 22.5, 9],'arrows':'1y'})   
        links.append({'name':'24_X','location':[25, 11.5, 25.3, 11.5,25.3, 3.5, 25.3, 13.3, 
        20.7, 13.3, 20.7, 12],'arrows':'1y'})  
        links.append({'name':'C_V','location':[12.8, 7.5, 12.8, 1.6,19, 1.6,19, 3.3,20, 3.3],'arrows':'1y'})   
        links.append({'name':'21_','location':[25, 3.5, 25.3, 3.5],'arrows':'0'})
        links.append({'name':'22_','location':[25, 6, 25.3, 6],'arrows':'0'})
        links.append({'name':'23_','location':[25, 9.5, 25.3, 9.5],'arrows':'0'})
        links.append({'name':'15_','location':[1.9, 3.5, 1.9, 10.5],'arrows':'0'})
        links.append({'name':'23_24','location':[23.3, 11.5, 23.3, 9.5],'arrows':'0'})
        links.append({'name':'F_C','location':[13.5, 8.5, 13.5, 10],'arrows':'2y'})
        links.append({'name':'G_H','location':[15.5, 8.5, 15.5, 10],'arrows':'2y'})
        links.append({'name':'G_H','location':[14, 10.5, 15, 10.5],'arrows':'2x'})
        links.append({'name':'C_H','location':[13.7, 8.5, 15, 10],'arrows':'slope'})
        n=0
        for box in Boxes:
            box['available']=True
            count=0
            for name in box['name']:
                if len(box['name'])>1:
                    count+=1
                if count<=1:
                    temp=box['location']
                    for m in range(4):
                        temp[m]=temp[m]*dx
                    box['location']=temp
                    frame.canvas.create_rectangle(box['location'],fill='pink',width=2)
                    count=1
                else:
                    break
            n+=1
            loc=box['location']
            x1=loc[0]+0.5*dx
            y1=loc[1]+0.5*dx
            frame.canvas.create_text(x1,y1,anchor="center",text=box['name'],
            font=("Times New Roman",24),tags='text'+str(n))
        
        for box in Boxes:
            if capacity[box['name']] != 10e5:
                for item in range(0,capacity[box['name']]):
                    v0=box['location'][0]+item*(dx/capacity[box['name']])
                    v1=box['location'][1]
                    v2=box['location'][0]+(item+1)*(dx/capacity[box['name']])
                    v3=box['location'][3]
                    frame.canvas.create_rectangle(v0,v1,v2,v3,fill='',width=0.5)
                    space[(box['name'],item)]=[v0,v1,v2,v3]
            else:
                space[(box['name'],0)]=box['location']
        
       
        for m in range(1,4):
            frame.canvas.create_rectangle(1.5*dx+(m-1)*8.5*dx,0.5*dx,
            9.4*dx+(m-1)*8.5*dx,14*dx, fill="",dash=(5,5),width=2)

        for cache in Cache:
            cache['visible']=True
            temp=cache['location']
            for m in range(4):
                temp[m]=temp[m]*dx
            cache['location']=temp
            if cache['visible']==True:
                frame.canvas.create_rectangle(cache['location'],fill='silver',width=2,dash=[15,15])
       
        a1=[dx/3,dx/3,dx/15]
        count1=0
        count2=0
        count3=0
        for link in links:
            count=0
            for name in link['name']:
                if len(link['name'])>1:
                    count+=1
                if count<=1:
                    temp=link['location']
                    for m in range(len(temp)):
                        temp[m]=temp[m]*dx
                    link['location']=temp
                    loc=link['location']
                    m=0
                    while (m+3)<len(temp):
                        if link['arrows']=='1x' and (m+3)==(len(temp)-1):
                            count1+=1
                            frame.canvas.create_line(loc[m],loc[m+1],loc[m+2],loc[m+3],fill='black',width=2,
                            arrow="last",arrowshape=a1,tags='link_1x_'+str(count1))
                            m=m+2
                        elif link['arrows']=='1y' and (m+3)==(len(temp)-1):
                            count2+=1
                            frame.canvas.create_line(loc[m],loc[m+1],loc[m+2],loc[m+3],fill='black',width=2,
                            arrow="last",arrowshape=a1,tags='link_1y_'+str(count2))
                            m=m+2
                        elif link['arrows']=='2y':
                            count3+=1
                            frame.canvas.create_line(loc[m],loc[m+1],loc[m+2],loc[m+3],fill='black',width=2,
                            arrow="both",arrowshape=a1,tags='link_2y_'+str(count3))
                            m=m+2
                        elif link['arrows']=='2x':
                            frame.canvas.create_line(loc[m],loc[m+1],loc[m+2],loc[m+3],fill='black',width=2,
                            arrow="both",arrowshape=a1,tags='link_2x')
                            m=m+2
                        elif link['arrows']=='slope':
                            frame.canvas.create_line(loc[m],loc[m+1],loc[m+2],loc[m+3],fill='black',width=2,
                            arrow="both",arrowshape=a1,tags='link_slope')
                            m=m+2
                        else:
                            frame.canvas.create_line(loc[m],loc[m+1],loc[m+2],loc[m+3],fill='black',width=2,
                            tags='link_0')
                            m=m+2
                            
                    count=1                
                else:
                    break
     
    #3.3 entity animation
            
    def show (self,i,j,k,server,generation):
        if i[1]['stimuli']==0:
            color='gray'
        elif i[1]['color']==-999:
            color='white'

        else:
            color=color_changer(i[1]['color'][0],i[1]['color'][1],i[1]['color'][2])

        self.save_dic[(i[0],k,generation,'0')]=self.frame.canvas.create_oval(30,self.h/2,50,self.h/2+20,fill=color,tags=(i[0],k,generation))
        self.save_dic[(i[0],k,generation,'0' ,'text')]=self.frame.canvas.create_text(40, self.h/2+10,anchor='center',text=i[0],font=("Times New Roman",10,"bold"),tags=(i[0],k,generation,'text'))
        self.save_dic_copy[(i[0],k,generation,'0')]=self.frame.canvas.create_oval(30,self.h/2,50,self.h/2+20,fill=color,tags=(i[0],k))
        self.save_dic_copy[(i[0],k,generation,'0' ,'text')]=self.frame.canvas.create_text(40, self.h/2+10,anchor='center',text=i[0],font=("Times New Roman",10,"bold"),tags=(i[0],k,generation,'text'))
        self.frame.canvas.update()
        time.sleep(0.1)
        self.frame.canvas.delete((i[0],k,generation))
        self.frame.canvas.delete((i[0],k,'text'))
  
    def enter (self,resource,server,connection,i,j,k,generation):
        
        if i[1]['stimuli']==0:
            color='gray'
        elif i[1]['color']==-999:
            color='white'
        else:
            color=color_changer(i[1]['color'][0],i[1]['color'][1],i[1]['color'][2])
     
        circle_r = self.circle_r
        #if the server is full, move the entitiy to wating room
        if resource.count==self.Capacity[server]:     
            self.loc_dic[(server,i[0],k,generation)]=-1  #loc_dic[full/not full,space] full=-1, not full=0
            for cache in self.Cache:
                if cache['name']==connection:
                    v0 = cache['location'][0]
                    v1 = cache['location'][1]
            x=v0
            y=v1+self.dx/2-circle_r
            self.save_dic[(i[0],k,server,generation)]=self.frame.canvas.create_oval(x, y, x + 2*circle_r, y + 2*circle_r,fill=color)
            self.save_dic[(i[0],k,server ,generation,'text')]=self.frame.canvas.create_text(x+circle_r, y+circle_r,anchor='center',text=i[0],font=("Times New Roman",10,"bold"))
            time.sleep(0.1)
            self.frame.canvas.update()        
        elif resource.count<self.Capacity[server]:   
            if self.Capacity[server] !=10e5:
                #if server is not full before the entity enters
                
                for item in range(self.Capacity[server]):
                    if (server,item) not in self.occupy_dic:
                        v0 = self.space[(server,item)][0]
                        v1 = self.space[(server,item)][1]        
                        x=v0
                        y=v1+self.dx/2-circle_r
                        
                        self.entity_loc[(i[0],k,server,generation)]=[x,y,color]
                        self.loc_dic[(server,i[0],k,generation)]=item
                        break 
            elif self.Capacity[server] ==10e5:
                
                self.loc_dic[(server,i[0],k,generation)]=0
                v0 = self.space[(server,0)][0]
                v1 = self.space[(server,0)][1]
            
                x=v0
                y=v1+self.dx/2-circle_r
                
                self.entity_loc[(i[0],k,server,generation)]=[x,y,color]
    
    def leave(self,i,j,k,server):
        
        if self.Capacity[server]!=10e5:
            self.occupy_dic.pop((server,self.loc_dic[(server,i[0])]))
        self.frame.canvas.coords( self.save_dic[(i[0],k,'0')],[self.w+1, self.w+1, self.w+1, self.w+1])
        self.frame.canvas.coords( self.save_dic[(i[0],k,'0','text')],[self.w+1, self.w+1])
        
    
    def add (self,server,i,j,k,generation):
        if i[1]['stimuli']==0:
            color='gray'
        elif i[1]['color']==-999:
            color='white'
        else:
            color=color_changer(i[1]['color'][0],i[1]['color'][1],i[1]['color'][2])
        circle_r=self.circle_r
        if  self.loc_dic[(server,i[0],k,generation)]!=-1:
            x=self.entity_loc[(i[0],k,server,generation)][0]
            y=self.entity_loc[(i[0],k,server,generation)][1]
            
            self.frame.canvas.update()
            self.save_dic[(i[0],k,server,generation)]=self.frame.canvas.create_oval(x, y, x + 2*circle_r, y + 2*circle_r, fill=color)
            self.save_dic[(i[0],k,server,generation,'text')]=self.frame.canvas.create_text(x+circle_r,y+circle_r,anchor="center",text=i[0],font=("Times New Roman",10,"bold"))
            self.occupy_dic[(server,self.loc_dic[(server,i[0],k,generation)])]=(i[0],k,generation)
            time.sleep(0.1)
            self.frame.canvas.update()
        else:
            for item in range(self.Capacity[server]):
                if (server,item) not in self.occupy_dic:
                    v0 = self.space[(server,item)][0]
                    v1 = self.space[(server,item)][1]
                    self.loc_dic[server,i[0],k,generation]=item       
                    x=v0
                    y=v1+self.dx/2-circle_r
                    self.frame.canvas.coords( self.save_dic[(i[0],k,server,generation)],[self.w+1, self.w+1, self.w+1, self.w+1])
                    self.frame.canvas.coords( self.save_dic[(i[0],k,server,generation,'text')],[self.w+1, self.w+1])
                    self.frame.canvas.update()
                    self.save_dic[(i[0],k,server,generation)]=self.frame.canvas.create_oval(x, y, x + 2*circle_r, y + 2*circle_r, fill=color)
                    self.save_dic[(i[0],k,server,generation,'text')]=self.frame.canvas.create_text(x+circle_r,y+circle_r,anchor="center",text=i[0],font=("Times New Roman",10,"bold"))
                    time.sleep(0.1)
                    self.frame.canvas.update()
                    break
            self.occupy_dic[(server,item)]=(i[0],k,generation)
    
    def delete (self,i,j,k,server,generation):
        if self.Capacity[server]!=10e5:
            if (server,self.loc_dic[(server,i[0],k,generation)]) in self.occupy_dic:
                self.occupy_dic.pop((server,self.loc_dic[(server,i[0],k,generation)]))
        entity_del =  self.save_dic[(i[0],k,server,generation)]
        entity_num_del = self.save_dic[(i[0],k,server,generation,'text')]
        self.frame.canvas.delete(entity_del)
        self.frame.canvas.delete(entity_num_del)
        time.sleep(0.1)
        self.frame.canvas.update()
                
    
    #3.4 model reaction animation GUI
    

    def judge_result(self,i,j,k,judge):
        dx=self.dx
        self.frame.canvas.create_rectangle(26.5*dx,5*dx,29.5*dx,6*dx,tag='ji_rec')
        if ji_result_dic[(i[0],k)]=='T':
            if judge=='color':
                self.frame.canvas.create_text(28*dx,5.5*dx,anchor='center',text='identical color',font=("Times New Roman",15,"bold"),tag='ji_text')
            elif judge=='text' :
                self.frame.canvas.create_text(28*dx,5.5*dx,anchor='center',text='identical text',font=("Times New Roman",15,"bold"),tag='ji_text')
        elif ji_result_dic[(i[0],k)]=='F':
            if judge=='color':
                self.frame.canvas.create_text(28*dx,5.5*dx,anchor='center',text='different color',font=("Times New Roman",15,"bold"),tag='ji_text')
            elif judge=='text':
                self.frame.canvas.create_text(28*dx,5.5*dx,anchor='center',text='different text',font=("Times New Roman",15,"bold"),tag='ji_text')
        self.frame.canvas.update()
        time.sleep(1)
        self.frame.canvas.delete('ji_rec')
        self.frame.canvas.delete('ji_text')
        self.frame.canvas.update()
        
        
    def look_at_signal(self,i,j,k,eye_loc):
        dx=self.dx

        self.frame.canvas.create_text(28.5*dx,10*dx,anchor='center',text='Eye Location: '+str(eye_loc),font=("Times New Roman",15,"bold"),tag='look_text',fill='red')
        self.frame.canvas.update()
        time.sleep(0.1)

        self.frame.canvas.delete('look_text')
        self.frame.canvas.update()
        
        
#3.4 model reaction animation GUI

def color_changer(a,b,c):
    return "#"+"".join([i[2:] if len(i[2:])>1 else '0'+i[2:] for i in [hex(a),hex(b),hex(c)]])

# if 'Press_button' in task_info_dic.values():
#     class reaction_press_button:
#         N=load_var(path+'/N.txt')
#         root = tk.Tk()
#         w=root.winfo_screenwidth()/2
#         h=root.winfo_screenheight()/5
#         frame=myCanvas(root,w,h)
#         frame.canvas.pack(fill="both",expand=True)
#         root.title('Reaction')
#         root.geometry('%dx%d+%d+%d'%(w,h,0,root.winfo_screenheight()/1.7))
#         color_list=[(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(255,128,0)]

#         if N==1:
#             frame.canvas.create_rectangle(w/2-80,h/2-18,w/2+80,h/2+18,fill='red',outline='red')
#         else:
#             for c in range(N):
#                 color=color_list[c]
#                 frame.canvas.create_rectangle(w/(N+1)*c+30,h/2-18,w/(N+1)*c+150,h/2+18,fill=color_changer(color[0],color[1],color[2]))
  
#         def add_button (self,i):
            
#             if self.N==1:
#                 self.frame.canvas.create_rectangle(self.w/2-80,self.h/2-18,self.w/2+80,self.h/2+18,fill='gray',outline='gray',tag='button_rec')
#                 self.frame.canvas.update()
#                 time.sleep(0.5)
#                 self.frame.canvas.delete('button_rec')
#                 self.frame.canvas.update()
#             else:
#                 for item in range(self.N):
#                     if i[1]['color']==color_list[item]:
#                         self.frame.canvas.create_rectangle(self.w/(N+1)*item+30,self.h/2-18,self.w/(N+1)*item+150,self.h/2+18,fill='gray',outline='gray',tag='button_rec')
#                         self.frame.canvas.update()
#                         break
                    
                        
#                 time.sleep(0.5)
#                 self.frame.canvas.delete('button_rec')
#                 self.frame.canvas.update()
try:
    if 'Press_button' in task_info_dic.values():
        class reaction_press_button:
            N = load_var(path + '/N.txt')  # Assuming load_var and path are defined elsewhere
            root = tk.Tk()
            w = root.winfo_screenwidth() / 2
            h = root.winfo_screenheight() / 5
            frame = myCanvas(root, w, h)  # Assuming myCanvas is defined elsewhere
            frame.canvas.pack(fill="both", expand=True)
            root.title('Reaction')
            root.geometry('%dx%d+%d+%d' % (w, h, 0, root.winfo_screenheight() / 1.7))
            color_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (255, 128, 0)]

            if N == 1:
                frame.canvas.create_rectangle(w / 2 - 80, h / 2 - 18, w / 2 + 80, h / 2 + 18, fill='red', outline='red')
            else:
                for c in range(N):
                    color = color_list[c]
                    frame.canvas.create_rectangle(w / (N + 1) * c + 30, h / 2 - 18, w / (N + 1) * c + 150, h / 2 + 18,
                                                  fill=color_changer(color[0], color[1], color[2]))

            def add_button(self, i):
                if self.N == 1:
                    self.frame.canvas.create_rectangle(self.w / 2 - 80, self.h / 2 - 18, self.w / 2 + 80, self.h / 2 + 18,
                                                       fill='gray', outline='gray', tag='button_rec')
                    self.frame.canvas.update()
                    time.sleep(0.5)
                    self.frame.canvas.delete('button_rec')
                    self.frame.canvas.update()
                else:
                    for item in range(self.N):
                        if i[1]['color'] == color_list[item]:
                            self.frame.canvas.create_rectangle(self.w / (N + 1) * item + 30, self.h / 2 - 18,
                                                               self.w / (N + 1) * item + 150, self.h / 2 + 18, fill='gray',
                                                               outline='gray', tag='button_rec')
                            self.frame.canvas.update()
                            break

                    time.sleep(0.5)
                    self.frame.canvas.delete('button_rec')
                    self.frame.canvas.update()

except NameError as e:
    # Check if the error message contains 'task_info_dic' to be more specific
    if 'task_info_dic' in str(e):
        messagebox.showerror("Error", "task_info_dic is not defined. Please define it before proceeding.")
        print('Back to menu')
        GUI_User_Main().root.mainloop()
    else:
        raise  # Re-raise the exception if it's not the one we're looking for

if'Count' in task_info_dic.values():
    class Reaction_count:

        root = tk.Tk()
        w=root.winfo_screenwidth()/2
        h=root.winfo_screenheight()/5
        frame=myCanvas(root,w,h)
        frame.canvas.pack(fill="both",expand=True)
        root.title('Reaction')
        root.geometry('%dx%d+%d+%d'%(w,h,0,root.winfo_screenheight()/1.7))           
        
        frame.canvas.create_text(w/2,h/4,text='Current count: ',font=("Times New Roman",18))

        frame.canvas.create_text(w/6*5,20,text='trial #: ',font=("Times New Roman",15))

        def show(self,start_num,end_num):
            self.frame.canvas.create_text(100,20,text='Count from %s to %s'%(start_num,end_num),font=("Times New Roman",18,"bold"),tag='count')

        def count_num (self,current):
            
            self.frame.canvas.create_text(self.w/2,self.h/2,text=str(current),font=("Times New Roman",18),fill='red',tag='current_count')
            self.frame.canvas.update()
            time.sleep(0.1)
            self.frame.canvas.delete('current_count')
        
        def trial(self,trial):
            self.frame.canvas.create_text(self.w/8*7,20,text=trial,font=("Times New Roman",15),tag='trial')
            self.frame.canvas.update()
            #time.sleep(0.1)
            #self.frame.canvas.delete('trial')
            
        def delete(self):
            self.frame.canvas.delete('trial')
            self.frame.canvas.delete('count') 

if 'Cal_single_digit_num' in task_info_dic.values():
    class Reaction_calsingledig:
        root = tk.Tk()
        w=root.winfo_screenwidth()/2
        h=root.winfo_screenheight()/5
        frame=myCanvas(root,w,h)
        frame.canvas.pack(fill="both",expand=True)
        root.title('Reaction')
        root.geometry('%dx%d+%d+%d'%(w,h,0,root.winfo_screenheight()/1.7))    

       # if operation=='Add (+)':
            #text='+'
        #elif operation=='Subtract (-)':
            #text='-'
        #elif operation=='Multiplication (*)':
           # text='*'
        #else:
            #='/'
        #frame.canvas.create_text(w/2,h/2,text=text,font=("Times New Roman",18,"bold"))
            #frame.canvas.create_text(w/2,h/4,text='Current count: ',font=("Times New Roman",18))  
        
        def first_num(self,first_num):
            self.frame.canvas.create_text(self.w/2-20,self.h/2,text=str(first_num),font=("Times New Roman",18),fill='red',tag='first_num')
            self.frame.canvas.update()
        
        def second_num(self,second_num):
            self.frame.canvas.create_text(self.w/2+20,self.h/2,text=str(second_num),font=("Times New Roman",18),fill='blue',tag='second_num')
            self.frame.canvas.update()
            
        def result(self,i):
            
            self.frame.canvas.create_text(self.w/2+60,self.h/2,text=' = '+str(i),font=("Times New Roman",18),tag='result')
            self.frame.canvas.update()
            time.sleep(0.2)
            
        def delete(self):

            self.frame.canvas.delete('first_num')

            self.frame.canvas.delete('second_num')

            self.frame.canvas.delete('result')
        
if 'Tracking_1D' in task_info_dic.values():
    class Reaction_track1D:
        
        #global h,w
        root = tk.Tk()
        w=root.winfo_screenwidth()/2
        h=root.winfo_screenheight()/5
        frame=myCanvas(root,w,h)
        frame.canvas.pack(fill="both",expand=True)
        root.title('Reaction_track1D')
        root.geometry('%dx%d+%d+%d'%(w,h,0,root.winfo_screenheight()/1.7))    
        frame.canvas.create_line(w/5,h/2,w/5*4,h/2,fill='black',width=3)
        origin=w/5
        length=w/5*3
        target=w/5
        #user=w/5+track1D_curse_loc/100*w/5*3
        r=5
        t=frame.canvas.create_oval(target-r, h/2-r,target+r,h/2+r,fill='red',outline='red',tag='target')
        #frame.canvas.create_oval(user-r, h/2-r,user+r,h/2+r,fill='black',outline='black',tag='user')
        
        
        def target_move(self,direction):
            global target_loc
            target_loc=0
            r=5
            h=self.h
            w=self.w
            #self.frame.canvas.create_oval(target-r, h/2-r,target+r,h/2+r,fill='red',outline='red',tag='target')
                          
            self.frame.canvas.move('target',direction*track1D_amp_dic[track1D_amp],0)
            target_loc=target_loc+track1D_amp_dic[track1D_amp]
            #time.sleep(0.05)
    
            self.frame.canvas.update()
            return target_loc
                                
        def user_click(self,user):
             
            r=5
            h=self.h
            
            self.frame.canvas.coords('user',user-r, h/2-r,user+r,h/2+r)
            
            self.frame.canvas.update()

if 'Tracking_2D' in task_info_dic.values():
    class Reaction_track2D:
        
        #global h,w
        root = tk.Tk()
        w=root.winfo_screenwidth()/4
        h=root.winfo_screenheight()/2
        frame=myCanvas(root,w,h)
        frame.canvas.pack(fill="both",expand=True)
        root.title('Reaction_track2D')
        root.geometry('%dx%d+%d+%d'%(w,h,0,root.winfo_screenheight()/2.5))
        length=w/5*3
        frame.canvas.create_line(w/5,h/7*6,w/5*4,h/7*6,fill='black',width=3)
        frame.canvas.create_line(w/5,h/7*6-w/5*3,w/5,h/7*6,fill='black',width=3)
        origin_x=w/5
        origin_y=h/7*6
        #target_x=track2D_target_loc_x/100*length+origin_x
        #target_y=origin_y-track2D_target_loc_y/100*length
        #cursor_x=track2D_cursor_loc_x/100*length+origin_x
        #cursor_y=origin_y-track2D_cursor_loc_y/100*length
        #user=w/5+track1D_curse_loc/100*w/5*3
        r=5
        #target=frame.canvas.create_oval(target_x-r, target_y-r,target_x+r,target_y+r,fill='red',outline='red',tag='target')
       # frame.canvas.create_oval(cursor_x-r, cursor_y-r,cursor_x+r,cursor_y+r,fill='black',outline='black',tag='user')
        
        
        def target_move(self,x):
            
            r=5
            h=self.h
            w=self.w
            #self.frame.canvas.create_oval(target-r, h/2-r,target+r,h/2+r,fill='red',outline='red',tag='target')
           
            if x==1:    
                self.frame.canvas.move('target',1*track2D_amp_dic[track2D_amp],0)
            elif x==-1:
                self.frame.canvas.move('target',-1*track2D_amp_dic[track2D_amp],0)
            elif x==2:
                self.frame.canvas.move('target',0,1*track2D_amp_dic[track2D_amp])
            elif x==-2:
                self.frame.canvas.move('target',0,-1*track2D_amp_dic[track2D_amp])
                     
            #target_loc=target_loc+track2D_amp_dic[track2D_amp]
            #time.sleep(0.05)
    
            self.frame.canvas.update()
            
                
                
        def user_click(self,x,y):
             
            r=5
            h=self.h
            
            self.frame.canvas.coords('user',x, y,x+2*r,y+2*r)
            
            self.frame.canvas.update()

if 'Static_2DTracing' in task_info_dic.values():
    class Reaction_static_2DTracing:
        win = tk.Tk()
        X, Y = ag.size()
        W=1300
        H=600
        winSize = str(W)+"x"+str(H)
        winPos = winSize + "+" + str((X - W) // 2)
        winPos += "+" + str((Y - H) // 2)
        win.geometry(winPos)
        #win.resizable(False, False)
        title = u'desktop resolution：' + str(X) + "x" + str(Y)
        title += ' ' * 5 + u'window size：' + winSize
        win.title(title)
        win.update()
        frame=myCanvas(win, win.winfo_width(), 600)
        frame.canvas.pack(side="top")
     
        x0,y0=W/2,280   # origin
        if static2D_shape=='Sin':
            xmax=math.pi*2       # The maximum value of the independent variable, if it exceeds the maximum value of the abscissa, it will be truncated
            xmin=-xmax
            w1,w2=100,100 
            w,h=xmax*w1+x0,H/2    # The positive maximum value of the horizontal and vertical axes
        elif static2D_shape=='Exp':
            xmax=5
            xmin=-5
            w1,w2=100,10 # w1, w2 are the magnifications of independent variables and function values on the horizontal and vertical axes
            w,h=xmax*w1+x0,H    # The positive maximum value of the horizontal and vertical axes
            x0=W/2
            y0=H/6*5
        elif static2D_shape=='Ln':
            xmax=10
            xmin=0.5
            w1,w2=100,100 # w1, w2 are the magnifications of independent variables and function values on the horizontal and vertical axes
            w,h=xmax*w1+x0,H    # The positive maximum value of the horizontal and vertical axes
            x0=W/6
            y0=H/6*5
            
        coord = x0-w,y0,x0+w,y0
        frame.canvas.create_line(coord,fill='black')
        coord = x0,y0-h,x0,y0+h
        frame.canvas.create_line(coord,fill='black')
        fx1 = lambda x : math.sin(x)
        step=0.001
        for x in npar(xmin,xmax+step,step):
            if static2D_shape=='Sin':
                y = math.sin(x)
            elif static2D_shape=='Exp':
                y=math.exp(x)
            if static2D_shape=='Ln':
                y = math.log(x)
                
            coord = x0+w1*x,y0-w2*y,x0+w1*x+1,y0-w2*y+1
            if abs(x*w1)<w and abs(y*w2)<h:
                frame.canvas.create_line(coord,fill='blue')
        frame.canvas.update()
          
        r=5
        x=(static2D_target_loc_x/100)*(xmax-xmin)+xmin
        if static2D_shape=='Sin':
            y=math.sin(x)
        elif static2D_shape=='Exp':
            y=math.exp(x)
        elif static2D_shape=='Ln':
            y=math.log(x)
  
        coord=x0+w1*x-r,y0-w2*y-r,x0+w1*x+r,y0-w2*y+r
        target=frame.canvas.create_oval(coord,fill='red',outline='red',tag='target')
        
        cursor_x=x0+w1*((static2D_cursor_loc_x/100)*(xmax-xmin)+xmin)
        if static2D_shape=='Sin':
            cursor_y=y0-w2*math.sin((static2D_cursor_loc_x/100)*(xmax-xmin)+xmin)
        elif static2D_shape=='Exp':
            cursor_y=y0-w2*math.exp((static2D_cursor_loc_x/100)*(xmax-xmin)+xmin)
        elif static2D_shape=='Ln':
            cursor_y=y0-w2*math.log((static2D_cursor_loc_x/100)*(xmax-xmin)+xmin)
        coord_cursor=cursor_x-r,cursor_y-r,cursor_x+r,cursor_y+r
        cursor=frame.canvas.create_oval(coord_cursor,fill='black',outline='black',tag='cursor')
        frame.canvas.update()
        
        def target_move (self):
            
            amp=1*static2D_amp_dic[static2D_amp]
            r=5
            x_right=(self.frame.canvas.coords(self.target)[0]+amp-self.x0+r)/self.w1
            x_left=(self.frame.canvas.coords(self.target)[0]-amp-self.x0+r)/self.w1
            if x_right>=Reaction_static_2DTracing().xmax:
                direction=-1              
            elif x_left<=Reaction_static_2DTracing().xmin:
                direction=1               
            else:
                direction=direction_static2D[-1]               
            if direction==1:
                x=x_right
                x_move=1*amp
            elif direction==-1:
                x=x_left
                x_move=-1*amp
            direction_static2D.append(direction)
            if static2D_shape=='Sin':
                y=self.y0-math.sin(x)*self.w2-r
            elif static2D_shape=='Exp':
                y=self.y0-math.exp(x)*self.w2-r
            elif static2D_shape=='Ln':
                y=self.y0-math.log(x)*self.w2-r
            y_move=y-(self.frame.canvas.coords(self.target)[1])
            self.frame.canvas.move('target',x_move,y_move)
            self.frame.canvas.update()
        
        def user_click(self,x,y):
             
            r=5           
            self.frame.canvas.coords('cursor',x, y,x+2*r,y+2*r)            
            self.frame.canvas.update()

class myCanvas_scroll(tk.Frame):
    def __init__(self, root,w,h):
        self.root = root
        self.w = w
        self.h = h
        self.canvas = tk.Canvas(root, width=self.w, height=self.h,scrollregion=(0, 0, 5000, 5000))
        scrollbar = tk.Scrollbar(self.root, orient="horizontal", command=self.canvas.xview,width=3)
        scrollbary = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview,width=3)
        self.canvas.config(xscrollcommand=scrollbar.set)
        self.canvas.config(yscrollcommand=scrollbary.set)
        scrollbar.pack(side="bottom", fill="x")
        scrollbary.pack(side='right',fill='y')
        self.canvas.pack( fill=tk.BOTH, expand=tk.YES)
        root.bind('<Configure>', self.resize)
    def resize(self, event):
        wscale=event.width/self.w
        hscale=event.height/self.h
        h_font=self.h/36
        arrow_1=self.w/91
        arrow_2=arrow_1
        arrow_3=self.h/256
        if wscale>1.05 or wscale<0.95 or hscale>1.05 or hscale<0.95:
            for m in range(1,25):
                self.canvas.itemconfig('text'+str(m),font=("Times New Roman",int(h_font*hscale)))
            for m in range(1,29):
                self.canvas.itemconfig('link_1x_'+str(m),arrowshape=[arrow_1*wscale,arrow_2*wscale,arrow_3*hscale])
            for m in range(1,17):
                self.canvas.itemconfig('link_1y_'+str(m),arrowshape=[arrow_1*hscale,arrow_2*hscale,arrow_3*wscale])
            for m in range(1,3):
                self.canvas.itemconfig('link_2y_'+str(m),arrowshape=[arrow_1*hscale,arrow_2*hscale,arrow_3*wscale])
            self.canvas.itemconfig('link_2x', arrowshape=[arrow_1*wscale,arrow_2*wscale,arrow_3*hscale])
            self.canvas.itemconfig('link_slope',arrowshape=[arrow_1*wscale,arrow_2*wscale,arrow_3*hscale])

            self.canvas.scale('all',0,0,wscale,hscale)
            self.w=event.width
            self.h=event.height
            self.canvas.pack(fill=tk.BOTH, expand=tk.YES)

if 'Dynamic_1D' in task_info_dic.values():
    class Reaction_dynamic1D:
        
        #global h,w
        root = tk.Tk()
        w=root.winfo_screenwidth()/2
        h=root.winfo_screenheight()/5
        frame=myCanvas_scroll(root,w,h)
        frame.canvas.pack(fill="both",expand=True)
        root.title('Reaction_dynamic1D')
        root.geometry('%dx%d+%d+%d'%(w,h,0,root.winfo_screenheight()/1.7))    
        frame.canvas.create_line(w/5,h/2,5*w,h/2,fill='black',width=3)
        target=w/5
        length=5*w-target
        user=w/5+dynamic1D_cursor_loc/100*length
        r=5
        target=frame.canvas.create_oval(target-r, h/2-r,target+r,h/2+r,fill='red',outline='red',tag='target')
        user=frame.canvas.create_oval(user-r, h/2-r,user+r,h/2+r,fill='black',outline='black',tag='user')
        
        # Bind the function to the scrollbar
        #scrollbar.config(command=on_scroll)
        
        def target_move(self,target):
            global target_loc
            target_loc=0
            r=5
            h=self.h
            w=self.w
            #self.frame.canvas.create_oval(target-r, h/2-r,target+r,h/2+r,fill='red',outline='red',tag='target')
                          
            self.frame.canvas.move('target',1*dynamic1D_amp_dic[dynamic1D_amp],0)
            target_loc=target_loc+dynamic1D_amp_dic[dynamic1D_amp]
            #time.sleep(0.05)
    
            self.frame.canvas.update()
            return target_loc
                                
        def user_click(self,user):
             
            r=5
            h=self.h
            
            self.frame.canvas.coords('user',user[0], user[1],user[2],user[3])
            
            self.frame.canvas.update()
            
        def scroll (self,move):
            self.frame.canvas.xview_moveto(move)   

if 'Dynamic_2D' in task_info_dic.values():
    class Reaction_dynamic2D:
        
        #global h,w
        root = tk.Tk()
        X, Y = ag.size()
        w=1300
        h=600
        winSize = str(w)+"x"+str(h)
        winPos = winSize + "+" + str((X - w) // 2)
        winPos += "+" + str((Y - h) // 2)
        root.geometry(winPos)
        frame=myCanvas_scroll(root,w,h)
        frame.canvas.pack(fill="both",expand=True)
        root.title('Reaction_dynamic2D')
        
        x0,y0=15,280   # origin
        if dynamic2D_shape=='Sin':
            xmax=math.pi*100      # The maximum value of the independent variable, if it exceeds the maximum value of the abscissa, it will be truncated
            xmin=0
            w1,w2=100,100 
            w,h=xmax*w1+x0,h/2  # The positive maximum value of the horizontal and vertical axes
        elif dynamic2D_shape=='Exp':
            xmax=100
            xmin=0
            w1,w2=500,10 # w1, w2 are the magnifications of independent variables and function values on the horizontal and vertical axes
            w,h=xmax*w1+x0,h    # The positive maximum value of the horizontal and vertical axes
            x0=15
            y0=h/6
        elif dynamic2D_shape=='Ln':
            xmax=10
            xmin=0.5
            w1,w2=100,100 # w1, w2 are the magnifications of independent variables and function values on the horizontal and vertical axes
            w,h=xmax*w1+x0,h    # The positive maximum value of the horizontal and vertical axes
            x0=w/6
            y0=h/6*5
            
        coord = x0,y0,x0+2*w,y0
        frame.canvas.create_line(coord,fill='black')
        coord = x0,y0-h,x0,y0+h
        frame.canvas.create_line(coord,fill='black')
        fx1 = lambda x : math.sin(x)
        step=0.001
        for x in npar(xmin,xmax+step,step):
            if dynamic2D_shape=='Sin':
                y = math.sin(x)
            elif dynamic2D_shape=='Exp':
                y=-math.exp(x)
            if dynamic2D_shape=='Ln':
                y = math.log(x)
                
            coord = x0+w1*x,y0-w2*y,x0+w1*x+1,y0-w2*y+1
            if abs(x*w1)<w and abs(y*w2)<h:
                frame.canvas.create_line(coord,fill='blue')
        frame.canvas.update()
          
        r=5
        x=(dynamic2D_target_loc_x/100)*(xmax-xmin)+xmin
        if dynamic2D_shape=='Sin':
            y=math.sin(x)
        elif dynamic2D_shape=='Exp':
            y=-math.exp(x)
        elif dynamic2D_shape=='Ln':
            y=math.log(x)
  
        coord=x0+w1*x-r,y0-w2*y-r,x0+w1*x+r,y0-w2*y+r
        target=frame.canvas.create_oval(coord,fill='red',outline='red',tag='target')
        
        cursor_x=x0+w1*((dynamic2D_cursor_loc_x/100)*(xmax-xmin)+xmin)
        if dynamic2D_shape=='Sin':
            cursor_y=y0-w2*math.sin((dynamic2D_cursor_loc_x/100)*(xmax-xmin)+xmin)
        elif dynamic2D_shape=='Exp':
            cursor_y=y0+w2*math.exp((dynamic2D_cursor_loc_x/100)*(xmax-xmin)+xmin)
        elif dynamic2D_shape=='Ln':
            cursor_y=y0-w2*math.log((dynamic2D_cursor_loc_x/100)*(xmax-xmin)+xmin)
        coord_cursor=cursor_x-r,cursor_y-r,cursor_x+r,cursor_y+r
        cursor=frame.canvas.create_oval(coord_cursor,fill='black',outline='black',tag='cursor')
        frame.canvas.update()
        

        # Bind the function to the scrollbar
        #scrollbar.config(command=on_scroll)
        
        def target_move (self):
            
            amp=1*dynamic2D_amp_dic[dynamic2D_amp]
            r=5
            '''
            x_right=(self.frame.canvas.coords(self.target)[0]+amp-self.x0+r)/self.w1
            x_left=(self.frame.canvas.coords(self.target)[0]-amp-self.x0+r)/self.w1
            if x_right>=Reaction_dynamic2D().xmax:
                direction=-1              
            elif x_left<=Reaction_dynamic2D().xmin:
                direction=1               
            else:
                direction=direction_dynamic2D[-1]               
            if direction==1:
                x=x_right
                x_move=1*amp
            elif direction==-1:
                x=x_left
                x_move=-1*amp
            direction_dynamic2D.append(direction)
            '''
            x=(self.frame.canvas.coords(self.target)[0]+amp+r-self.x0)/self.w1
            if dynamic2D_shape=='Sin':
                y=self.y0-math.sin(x)*self.w2-r
            elif dynamic2D_shape=='Exp':
                y=self.y0+math.exp(x)*self.w2-r
            elif dynamic2D_shape=='Ln':
                y=self.y0-math.log(x)*self.w2-r
            
            x_move=amp
            y_move=y-(self.frame.canvas.coords(self.target)[1])
            self.frame.canvas.move('target',x_move,y_move)
            self.frame.canvas.update()
        
        def user_click(self,x,y):
             
            r=5           
            self.frame.canvas.coords('cursor',x, y,x+2*r,y+2*r)            
            self.frame.canvas.update()
            
        def scroll_x (self,move):
            self.frame.canvas.xview_moveto(move)  
            
        def scroll_y (self,move):
            self.frame.canvas.yview_moveto(move)  


# -------------------------
# ENGINE
# -------------------------


#Section4 Engine 


#4.1 Engine parameters


#define ppt, cpt, mpt

#ppt = (-1) * 16 * math.log(1-random.uniform(0,1)) + 17
#cpt = (-1) * 22 * math.log(1-random.uniform(0,1)) + 13
#mpt = (-1) * 14 * math.log(1-random.uniform(0,1)) + 10

ppt=1000
cpt=35
mpt=24
dummy= 1000


#BE and the entity records

#define operator index
BE_dic = {}
BE_dic[11] = 'See'
BE_dic[31] = 'Hear'
BE_dic[101] = 'Store_to_WM'
BE_dic[111] = 'Choice'
BE_dic[211] ='Press_button'
BE_dic[201] = 'Look_at'
BE_dic[121] = 'Judge_identity'
BE_dic[123] = 'Judge_magnitude'
BE_dic[130] = 'Count'
BE_dic[135] = 'Cal_single_digit_num'
BE_dic[321] = 'Look_for'
BE_dic[322] = 'Tracking_1D'
 #0: noise 1: stimuli; 2:visual 3:auditory; 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified
 #10: red 11: blue
attribute_dic={}
attribute_dic[0]='noise'
attribute_dic[1]='stimuli'
attribute_dic[2]= 'visual'
attribute_dic[3]='auditory'
attribute_dic[4]='spatial'
attribute_dic[5]='verbal'
attribute_dic[6]='both spatial and verbal'
attribute_dic[7]='unknown'



#4.2 data record for specific BE 


color_list=[(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(255,128,0)]
text_list=['A','B','C','D','E','F','G','H']
STW_record = {}    
copy_dic={}
eyefixation_dic={} 
neweyefixation = [0,0]
communication_signal=0
eyefixation=[0,0]
entity_info={}
forced_exit_dic={}
ji_store_dic={}
jm_store_dic={}
ji_result_dic={}
jm_result_dic={}
count_num_dic={}
cal_sd_num_dic={}
cal_sd_result_dic={}

look_for_ls=[[(0,0),'a',(255,0,0)],\
                    [(1,1),'b',(0,255,0)],\
                       [(2,2),'c',(0,0,255)] ]
n_look_for_ls=len(look_for_ls)

#target=eval(input('target item[loc,text,color]:'))
#process user input of define task


direction_track1D=1
direction_static2D=[1]
direction_dynamic2D=[1]

track1D_freq_dic={'Slow':10,'Medium':50,'Quick':100}
track1D_amp_dic={'Small':1,'Medium':10,'Large':20}
track2D_freq_dic={'Slow':10,'Medium':50,'Quick':100}
track2D_amp_dic={'Small':10,'Medium':20,'Large':50}
static2D_freq_dic={'Slow':10,'Medium':50,'Quick':100}
static2D_amp_dic={'Small':1,'Medium':10,'Large':20}
dynamic1D_freq_dic={'Slow':10,'Medium':50,'Quick':100}
dynamic1D_amp_dic={'Small':1,'Medium':10,'Large':20}
dynamic2D_freq_dic={'Slow':10,'Medium':50,'Quick':100}
dynamic2D_amp_dic={'Small':1,'Medium':10,'Large':20}
start_time=0

#4.3 data record for sjourn time, used in plot section

sojourn_time_dic = {}
rt_dic ={1:[],2:[],3:[],4:[],5:[]}
rt_mean_dic={1:[],2:[],3:[],4:[],5:[]}
rt_var_dic={1:[],2:[],3:[],4:[],5:[]}

rmse_dic={}
rmse_var_dic={}
rmse_list=[]


#4.4 retrieve/ save data from GUI, which is used in engine part  

Task_dic ={}
tbd_list=load_var(path+'/tbd_list.txt')
anim=load_var(path+'/anim.txt')
SIMTIME=load_var(path+'/simtime.txt')

task_info_dic=load_var(path+'/task_info_dic.txt')
Tasklist_dic={}
for item in range(1,6):
    Task_dic[item]=[]
for j in range(1,6):
    order=[]
    if task_info_dic[(1,j)]!='':
        k=eval(task_info_dic[(1,j)])
        for i in range(2,18):
            if task_info_dic[(i,2*j-1)]!='':
                Task_dic[k].append((task_info_dic[(i,2*j-1)],eval(task_info_dic[(i,2*j)])))
        for item in Task_dic[k]:
            order.append(item[1])
        max_order=max(order)
        Tasklist_dic[k]=[[] for item in range(max_order)]
        for item in range(max_order):
            for t in Task_dic[k]:
                if t[1]==item+1:
                    Tasklist_dic[k][item].append(t[0])









#4.6 Engine core/ engine ignition


def main(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):
    
    #if the entity is of a certain task included by the user, get the correspondant task
        
    j=Tasklist_dic[k]
    
    #entity information
    entity_info[(i[0],k,generation)]=[]
    if attribute['stimuli']==0:
        entity_info[(i[0],k,generation)].append('noise')
    else:
        for item in attribute.keys() :
            if item=='stimuli' or item=='type' or item=='info':
                entity_info[(i[0],k,generation)].append(attribute_dic[attribute[item]])
            else:
                entity_info[(i[0],k,generation)].append(attribute[item])
    #entity_info[(i[0],k)].append(j)
    
    #activate operators 
    step_num=len(Tasklist_dic[k])
    for step in range(step_num):
        if len(Tasklist_dic[k][step])==1:
            a=Tasklist_dic[k][step][0]

            yield env.process(eval(a)(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))
                            
        elif len(Tasklist_dic[k][step])==2:
            a=Tasklist_dic[k][step][0]
            b=Tasklist_dic[k][step][1]
            
            yield env.process(eval(a)(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation)) & env.process(eval(b)(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))

            #yield env.process(A)&env.process(B)
                    
        elif len(Tasklist_dic[k][step])==3:
            a=Tasklist_dic[k][step][0]
            b=Tasklist_dic[k][step][1]
            c=Tasklist_dic[k][step][2]

          
            A=eval(a)(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation)
            
            B=eval(b)(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation)                          
   
            C=eval(c)(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation)
            yield env.process(A) and env.process(B) and env.process(C)
    

    if attribute['stimuli']!=0:
        sojourn_time_dic[(i[0],k,generation)]='%.2fmsec'%(env.now-arrival_time)
        rt_dic[k].append (env.now - arrival_time)

        rt_mean_dic[k].append(np.mean(rt_dic[k]))
        rt_var_dic[k].append(np.std(rt_dic[k]))
        
    #For look for: when target is found, function will be interrupted, 
    #thus the time record for look for is manipulated in the 'look for' class
        
          
    print('sojourn time for entity%s: %.2fmsec'%((i[0],k,generation),env.now-arrival_time))
    
    

#4.7 MEs




#4.8 entity generation




#Section5 Plot

class Plot:
    # root = tk.Tk()
    # root.title('Plot')
    # root.geometry('1400x500')  # Increase the height to accommodate the button
    # root.config(bg='#fff')

    # length = len(Tasklist_dic)

    # f = Figure(figsize=(5, 4), dpi=100)
    # ave_plot = f.add_subplot(211)
    # sd_plot = f.add_subplot(212)

    # data_plot = FigureCanvasTkAgg(f, master=root)
    # data_plot.draw()
    # data_plot.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # def __init__(self):
    #     self.canvas = tk.Canvas(self.root, width=1300, height=350, bg="white")
    #     self.canvas.update()

    #     # Create a frame for the button
    #     self.button_frame = tk.Frame(self.root, bg='#fff')
    #     self.button_frame.pack(side=tk.BOTTOM, fill=tk.X)

    #     self.back_button = tk.Button(self.button_frame, text="Back to Menu", command=self.go_back_to_menu)
    #     self.back_button.pack(side=tk.RIGHT, padx=10, pady=10)

    # def go_back_to_menu(self):
    #     self.root.destroy()
    #     GUI_User_Main().run()

    root = tk.Tk()
    root.title('Plot')
    root.geometry('1400x500')
    root.config(bg='#fff')
    
    # Initialize the plotting area once for all instances.
    f = Figure(figsize=(5, 4), dpi=100)
    ave_plot = f.add_subplot(211)
    sd_plot = f.add_subplot(212)
    data_plot = FigureCanvasTkAgg(f, master=root)
    data_plot.draw()
    data_plot.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def __init__(self):
        self.canvas = tk.Canvas(self.root, width=1300, height=350, bg="white")
        self.canvas.update()
        
        # Only create and pack the button frame and button once. To resolve the issue that there are two buttons appearing.
        if not hasattr(Plot, 'button_frame'):
            Plot.button_frame = tk.Frame(self.root, bg='#fff')
            Plot.button_frame.pack(side=tk.BOTTOM, fill=tk.X)
            Plot.back_button = tk.Button(Plot.button_frame, text="Back to Menu", command=self.go_back_to_menu)
            Plot.back_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def go_back_to_menu(self):
        self.root.destroy()
        # GUI_User_Main().root.mainloop()
        # main_function()
        if 'Press_button' in task_info_dic.values():
            reaction_press_button().root.destroy()
        if 'Count' in task_info_dic.values():
            Reaction_count().root.destroy()
        if 'Cal_single_digit_num' in task_info_dic.values():
            Reaction_calsingledig().root.destroy()
        if 'Tracking_1D' in task_info_dic.values():
            Reaction_track1D().root.destroy()
        if 'Tracking_2D' in task_info_dic.values():
            Reaction_track2D().root.destroy()
        if 'Static_2DTracing' in task_info_dic.values():
            Reaction_static_2DTracing().win.destroy()
        if 'Dynamic_1D' in task_info_dic.values():
            Reaction_dynamic1D().root.destroy()
        if 'Dynamic_2D' in task_info_dic.values():
            Reaction_dynamic2D().root.destroy()
        if anim == 1:
            Structure_and_Animation().root.destroy()

        python = sys.executable
        os.execl(python, python, *sys.argv)
    def tick(self):
        self.ave_plot.cla()
        self.ave_plot.set_xlabel("Number of Stimuli")
        self.ave_plot.set_ylabel("Mean of Sojourn Time")

        for (key, value) in rt_mean_dic.items():
            if value:
                self.ave_plot.step(
                    [index for (index, waits) in enumerate(value, start=1)],
                    [waits for (index, waits) in enumerate(value, start=1)],
                    label=key, marker='.'
                )

        self.ave_plot.legend()

        self.sd_plot.cla()
        self.sd_plot.set_xlabel("Number of Stimuli")
        self.sd_plot.set_ylabel("Standard Deviation of Sojourn Time")

        for (key, value) in rt_var_dic.items():
            if value:
                self.sd_plot.step(
                    [index for (index, waits) in enumerate(value, start=1)],
                    [waits for (index, waits) in enumerate(value, start=1)],
                    label=key, marker='.'
                )

        self.sd_plot.legend()

        self.data_plot.draw()
        self.canvas.update()

    def RMSE(self):
        self.ave_plot.cla()
        self.ave_plot.set_xlabel("Response Number")
        self.ave_plot.set_ylabel("RMSE")

        self.ave_plot.step(
            [t for (t, waits) in rmse_dic.items()],
            [waits for (t, waits) in rmse_dic.items()],
            'b.-'
        )

        self.sd_plot.cla()
        self.sd_plot.set_xlabel("Response Number")
        self.sd_plot.set_ylabel("Standard Deviation of RT")
        self.sd_plot.step(
            [t for (t, waits) in rmse_var_dic.items()],
            [waits for (t, waits) in rmse_var_dic.items()],
            'b.-'
        )

        self.data_plot.draw()
        self.canvas.update()



def create_clock(env):
    while True:
        yield env.timeout(10)
        Plot().tick(env.now)  
        print('Current time:', env.now )

if 'Tracking_1D' in task_info_dic.values() or 'Tracking_2D' in task_info_dic.values() or 'Static_2DTracing' in task_info_dic.values():
    Plot().RMSE()
else:
    Plot().tick()
    print('no tracking task')
# Plot().root.mainloop()




if anim==1:
    Structure_and_Animation().root.mainloop()



if 'Press_button' in task_info_dic.values():
    reaction_press_button().root.mainloop()
if 'Count' in task_info_dic.values():
    Reaction_count().root.mainloop()
if 'Cal_single_digit_num' in task_info_dic.values():
    Reaction_calsingledig().root.mainloop()
if 'Tracking_1D' in task_info_dic.values() :
    Reaction_track1D().root.mainloop()
if 'Tracking_2D' in task_info_dic.values():
    Reaction_track2D().root.mainloop()
if 'Static_2DTracing' in task_info_dic.values():
    Reaction_static_2DTracing().win.mainloop()
if 'Dynamic_1D' in task_info_dic.values():
    Reaction_dynamic1D().root.mainloop()
if 'Dynamic_2D' in task_info_dic.values():
    Reaction_dynamic2D().root.mainloop()


#print(sojourn_time_dic)
#print(entity_info)
