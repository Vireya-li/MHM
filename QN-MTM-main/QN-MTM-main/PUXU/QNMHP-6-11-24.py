
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

import os
import time

import pickle
import shutil
from tkinter import Button

from tkinter import messagebox


#Section2

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


#Main menu UI
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
            text='QN-MHP Software',
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
        self.Button_start=tk.Button(self.root,text='Start',font=('',20),command=self.root.destroy)
        self.Button_start.place(x=450,y=400,width=100,height=40)
        
    def task_event(self):
        GUI_task_def_step1().root.mainloop()
        
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



#define task UI
class GUI_task_def_step1:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Define Task step1: define task number, BE, and order')
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
        tk.Label(self.root,text='Step1: set task number, choose the behavior elements in each task and their corresponding order',font=('bold',14),anchor='w')\
            .grid(row = 0,column=0,pady=10,columnspan=10,sticky='w')
        #tk.Label(self.root,text='Step2: click the Apply button, and click the b_e button in the automatically generated task list to open the setting interface of the selected b_e',font=('bold',14))\
            #.grid(row = 19,column=0,pady=3,columnspan=18,sticky='w')
        self.l_tn= tk.Label(self.root,text='Task No.',font=('bold',14),relief='ridge',width=8)
        self.l_tn.grid(row = 1,column=0,pady=1,padx=1)
        self.l_order=tk.Label(self.root,text='Behavior\n Elements\n and \n Order',font=('bold',14),relief='ridge',height=32)
        self.l_order.grid(row = 2,column=0,rowspan=16,pady=1)
        
        #Combobox
        self.combobox={}
        global tbd_list
        tbd_list=['TBD1','TBD2','TBD3']
        save_var(tbd_list, path+'/tbd_list.txt')
        for r in range(2,18):
            for c in range(1,11):
                if c%2==0: #choose order
                    self.value = tk.StringVar()
                    '''
                    if saved==1:
                        self.value.set(load_var(path+'task_info_dic.txt')[(r,c)])
                    else:
                        self.value.set('')
                    '''
                    value_order = ['',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
                    self.combobox[(r,c)] = ttk.Combobox(
                        master = self.root,
                        width=2,
                        state='readonly',
                        cursor='arrow',
                        values=value_order,
                        #textvariable=self.value,
                        font=('bold',10)
                        )
                    self.combobox[(r,c)].bind('<<ComboboxSelected>>',self.pick)
                    self.combobox[(r,c)].grid(row=r,column=c)   
                    
                    if saved==1 and load_var(path+'/task_info_dic.txt')[(r,c)]!='':
                        self.combobox[(r,c)].current(eval(load_var(path+'/task_info_dic.txt')[(r,c)]))
                    else:
                        self.combobox[(r,c)].current(0)
                      
                        
                else: #choose behavior elements
                    self.value = tk.StringVar()
                    value_be = ['','See','Hear','Store_to_WM','Choice','Judge_identity',\
                                'Count','Cal_single_digit_num','Press_button','Look_at',\
                                    'Look_for','Tracking_1D','Tracking_2D','Static_2DTracing',\
                                        'Dynamic_1D','Dynamic_2D','UD_ST','UD_BE']
                    self.combobox[(r,c)] = ttk.Combobox(
                        master = self.root,
                        width=18,
                        state='readonly',
                        cursor='arrow',
                        values=value_be,  
                        font=('bold',10)
                        )
                    self.combobox[(r,c)].bind('<<ComboboxSelected>>',self.pick)
                    self.combobox[(r,c)].grid(row=r,column=c)
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
        operator_name_list = ['See','Hear','TBD','TBD','TBD','Store_to_WM','Choice',\
                 'Judge_identity','Count','Cal_single_digit_num','Press_button','Look_at','Look_for','Tracking_1D',\
                     'Dynamic_1D','Dynamic_2D','TBD','TBD']

        self.Button_next=tk.Button(self.root,text='Next: BE Specification',font=16,command=self.next_event)
        self.Button_next.grid(row=18,column=2,columnspan=3,pady=30,ipady=3)
        self.Button_save=tk.Button(self.root,text='Save and Back to Main Menu',font=16,command=self.root.destroy)
        self.Button_save.grid(row=18,column=7,columnspan=3,pady=30,ipady=3)

        for c in range(1,6):
            self.value = tk.StringVar()
            self.value.set('')
            value_tn = ['',1,2,3,4,5]
            self.combobox[(1,c)] = ttk.Combobox(
                master = self.root,
                state='readonly',
                cursor='arrow',
                values=value_tn, 
                width=28
                )
            self.combobox[(1,c)].bind('<<ComboboxSelected>>',self.pick)
            self.combobox[(1,c)].grid(row=1,column=2*c-1,padx=0.5,columnspan=2)
            
            if saved==1 and load_var(path+'/task_info_dic.txt')[(1,c)]!='':
                self.combobox[(1,c)].current(eval(load_var(path+'/task_info_dic.txt')[(1,c)]))
                print(self.combobox[(1,c)].get())
            else:
                self.combobox[(1,c)].current(0)
            
 
    #get combobox user input    
    def pick(self,*arg):
        global task_info_dic,task_info_dic_f
        task_info_dic={}
        for r in range(1,18):
            if r==1:
                for c in range(1,6):
                    task_info_dic[(r,c)]=self.combobox[(r,c)].get()
            else:                    
                for c in range(1,11):
                    task_info_dic[(r,c)]=self.combobox[(r,c)].get()
        task_info_dic_f=save_var(task_info_dic,path+'/task_info_dic.txt')

    
    def next_event(self):
        global task_info_dic,task_info_dic_f
        task_info_dic={}
        for r in range(1,18):
            if r==1:
                for c in range(1,6):
                    task_info_dic[(r,c)]=self.combobox[(r,c)].get()
            else:                    
                for c in range(1,11):
                    task_info_dic[(r,c)]=self.combobox[(r,c)].get()
        task_info_dic_f=save_var(task_info_dic,path+'/task_info_dic.txt')
        GUI_task_def_step2().root.mainloop()
        
                                       
class GUI_task_def_step2:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Define Task step2: BE Specification')
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
        tk.Label(self.root,text='Step2: click the BE button in the automatically generated task list to open the setting interface of the selected BE',font=('bold',14))\
            .grid(row = 0,column=0,pady=3,columnspan=18,sticky='w')
        
        self.button={}
        self.l_tn= tk.Label(self.root,text='Task No.',font=('bold',15),height=2)
        self.l_tn.grid(row = 1,column=0,pady=3,padx=3)
        column_=1
        for c in range(1,6):
            if task_info_dic[(1,c)]!='':
                if task_info_dic[(1,c)]=='1':
                    self.task_no='1'
                    tk.Label(self.root,text=task_info_dic[(1,c)],font=14).grid(row=1,column=column_)
                    row_=2
                    for r in range(2,18):
                        if task_info_dic[(r,2*c-1)]!='':
                            if task_info_dic[(r,2*c-1)]=='See':
                                self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.see_event1,width=18)
                            elif task_info_dic[(r,2*c-1)]=='Hear':
                                self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.hear_event1,width=18)
                            elif task_info_dic[(r,2*c-1)]=='Judge_identity':
                                self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.judgei_event1,width=18)  
                            elif task_info_dic[(r,2*c-1)]=='Look_at':
                                self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.lookat_event1,width=18)  
                            elif task_info_dic[(r,2*c-1)]=='Choice':
                                self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.choice_event1,width=18)  
                            elif task_info_dic[(r,2*c-1)]=='Count':
                                self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.count_event1,width=18)                           
                            elif task_info_dic[(r,2*c-1)]=='Cal_single_digit_num':
                                self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.cal_single_digit_num_event1,width=18)
                            elif task_info_dic[(r,2*c-1)]=='Look_for':
                                self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.lookfor_event1,width=18)  
                            elif task_info_dic[(r,2*c-1)]=='Tracking_1D':
                                self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.track1D_event1,width=18)  
                            elif task_info_dic[(r,2*c-1)]=='Tracking_2D':
                                self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.track2D_event1,width=18)                             
                            elif task_info_dic[(r,2*c-1)]=='Static_2DTracing':
                                self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.static_tracing_event1,width=18)          
                            elif task_info_dic[(r,2*c-1)]=='Dynamic_1D':
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.dynamic1D_event1,width=18)
                            elif task_info_dic[(r,2*c-1)]=='Dynamic_2D':
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.dynamic2D_event1,width=18) 
                            elif task_info_dic[(r,2*c-1)]=='TBD1':
                                self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.tbd1_event1,width=18)    
                            elif task_info_dic[(r,2*c-1)]=='TBD2':
                                self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.tbd2_event1,width=18)  
                            elif task_info_dic[(r,2*c-1)]=='TBD3':
                                self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.tbd3_event1,width=18)                      
                            else:
                                self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,width=18)
                            self.button[(r,2*c-1)].grid(row=row_,column=column_)        
                            row_+=1
                if task_info_dic[(1,c)]=='2':
                     self.task_no='2'
                     tk.Label(self.root,text=task_info_dic[(1,c)],font=14).grid(row=1,column=column_)
                     row_=2
                     for r in range(2,18):
                         if task_info_dic[(r,2*c-1)]!='':
                             if task_info_dic[(r,2*c-1)]=='See':
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.see_event2,width=18)
                             elif task_info_dic[(r,2*c-1)]=='Hear':
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.hear_event2,width=18)
                             elif task_info_dic[(r,2*c-1)]=='Judge_identity':
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.judgei_event2,width=18)  
                             elif task_info_dic[(r,2*c-1)]=='Look_at':
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.lookat_event2,width=18)  
                             elif task_info_dic[(r,2*c-1)]=='Choice':
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.choice_event2,width=18)  
                             elif task_info_dic[(r,2*c-1)]=='Count':
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.count_event2,width=18)
                             elif task_info_dic[(r,2*c-1)]=='Cal_single_digit_num':
                                self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.cal_single_digit_num_event2,width=18)  
                             elif task_info_dic[(r,2*c-1)]=='Look_for':
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.lookfor_event2,width=18) 
                             elif task_info_dic[(r,2*c-1)]=='Tracking_1D':
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.track1D_event2,width=18)  
                             elif task_info_dic[(r,2*c-1)]=='Tracking_2D':
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.track2D_event2,width=18)                             
                             elif task_info_dic[(r,2*c-1)]=='Static_2DTracing':
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.static_tracing_event2,width=18)  
                             elif task_info_dic[(r,2*c-1)]=='Dynamic_1D':
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.dynamic1D_event2,width=18)     
                             elif task_info_dic[(r,2*c-1)]=='Dynamic_2D':
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.dynamic2D_event2,width=18)     
                             elif task_info_dic[(r,2*c-1)]=='TBD1':
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.tbd1_event2,width=18)    
                             elif task_info_dic[(r,2*c-1)]=='TBD2':
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.tbd2_event2,width=18)  
                             elif task_info_dic[(r,2*c-1)]=='TBD3':
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,command=self.tbd3_event2,width=18)                      
                             else:
                                 self.button[(r,2*c-1)]=tk.Button(self.root,text=task_info_dic[(r,2*c-1)],font=16,height=1,width=18)
                             self.button[(r,2*c-1)].grid(row=row_,column=column_)        
                             row_+=1
                column_+=2
            self.Button_save=tk.Button(self.root,text='Save and Back to Step1',font=16,command=self.root.destroy)
            self.Button_save.place(x=700,y=700,width=230,height=50)
            
    
    #BE data record as part of task def step2, have important broad effect.
    #Currently for 2 tasks, can be expanded to 5 (currect) or more (in future)
    def see_event1(self):
        GUI_BE_See('1').root.mainloop()
    def hear_event1(self):
        GUI_BE_Hear('1').root.mainloop()
    def choice_event1(self):
        GUI_BE_Choice('1').root.mainloop()
    def judgei_event1(self):
        GUI_BE_Judgei('1').root.mainloop()
    def lookat_event1(self):
        GUI_BE_Lookat('1').root.mainloop()
    def lookfor_event1(self):
        GUI_BE_Lookfor('1').root.mainloop()
    def cal_single_digit_num_event1(self):
        GUI_BE_Cal_single_digit_num('1').root.mainloop()
    def count_event1(self):
        GUI_BE_Count('1').root.mainloop()
    def track1D_event1(self):
        GUI_BE_track1D('1').root.mainloop()
    def track2D_event1(self):
        GUI_BE_track2D('1').root.mainloop()
    def static_tracing_event1(self):
        GUI_BE_static_tracing('1').root.mainloop()
    def dynamic1D_event1(self):
        GUI_BE_dynamic1D('1').root.mainloop()
    def dynamic2D_event1(self):
        GUI_BE_dynamic2D('1').root.mainloop()


    def see_event2(self):
        GUI_BE_See('2').root.mainloop()
    def hear_event2(self):
        GUI_BE_Hear('2').root.mainloop()
    def choice_event2(self):
        GUI_BE_Choice('2').root.mainloop()
    def count_event2(self):
        GUI_BE_Count('2').root.mainloop()
    def judgei_event2(self):
        GUI_BE_Judgei('2').root.mainloop()
    def cal_single_digit_num_event2(self):
        GUI_BE_Cal_single_digit_num('2').root.mainloop()
    def lookat_event2(self):
        GUI_BE_Lookat('2').root.mainloop()
    def lookfor_event2(self):
        GUI_BE_Lookfor('2').root.mainloop()
    def count_event2(self):
        GUI_BE_Count('2').root.mainloop()
    def track1D_event2(self):
        GUI_BE_track1D('2').root.mainloop()
    def track2D_event2(self):
        GUI_BE_track2D('2').root.mainloop()
    def static_tracing_event2(self):
        GUI_BE_static_tracing('2').root.mainloop()
    def dynamic1D_event2(self):
        GUI_BE_dynamic1D('2').root.mainloop()
    def dynamic2D_event2(self):
        GUI_BE_dynamic2D('2').root.mainloop()

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

#2.3 BE Specific GUI

see_entity_dic={}
hear_entity_dic={}
class GUI_BE_See:
    def __init__(self,task_no):
    
        self.root = tk.Tk()    
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=1100    #window width
        wh=320  #window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.root.title('BE Specification: See')
        self.root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        self.task_no=task_no
        
        
        self.See()
        
        
    def See(self):

        #title Lable
        tk.Label(self.root,text='Choose the entitie(s) to be processed in See and set the corresponding parameters',font=('bold',14))\
            .grid(row = 0,column=0,pady=3,columnspan=10,sticky='w')
        title_ls=['Entity','First Arrival Time (msec)','IAT(msec)','Occurences']
        for c in range(1,5):
            tk.Label(self.root,text=title_ls[c-1],font=('bold',14),width=22,relief='sunken')\
                .grid(row = 1, column=c)
        for r in range(2,6):
            tk.Label(self.root,text=str(r-1),font=('bold',14),width=5,relief='sunken')\
                .grid(row = r, column=0)
        self.see={}
        value_see = ['','Color(s)','Text','Item(s)']
        for r in range(2,6):
            self.see[(r,1,self.task_no)] = ttk.Combobox(
                master = self.root,
                width=30,
                state='readonly',
                cursor='arrow',
                values=value_see, 
                font=('bold',10)
                )
            self.see[(r,1,self.task_no)].bind('<<ComboboxSelected>>',self.pick)
            self.see[(r,1,self.task_no)].grid(row=r,column=1)
            if saved==1 and load_var(path+'/see_entity_dic.txt')[(r,1,self.task_no)]!='':
                for item in range(len(value_see)):
                    if load_var(path+'/see_entity_dic.txt')[(r,1,self.task_no)]==value_see[item]:
                        self.see[(r,1,self.task_no)].current(item)
            else:
                self.see[(r,1,self.task_no)].current(0)
            
       
        for r in range(2,6):
            for c in range(2,5):
                self.see[(r,c,self.task_no)]=tk.Entry(self.root,width=30)
                self.see[(r,c,self.task_no)].grid(row=r,column=c)
                if saved==1:
                    self.see[(r,c,self.task_no)].insert(0,load_var(path+'/see_entity_dic.txt')[(r,c,self.task_no)])
        
        
        self.Button_ok=tk.Button(self.root,text='Save and Back to Step2',font=16,command=self.entry_event)
        self.Button_ok.grid(row=8,rowspan=3,column=3,columnspan=2,pady=30,ipady=3)
            
    def pick(self,*arg):
        for r in range(2,6):
            see_entity_dic[(r,1,self.task_no)]=self.see[(r,1,self.task_no)].get()
        save_var(see_entity_dic, path+'/see_entity_dic.txt')
            
       
    # def entry_event(self):
    #     if saved == 1:
    #        see_entity_dic.update(load_var(path+'/see_entity_dic.txt'))
    #        for r in range(2,6):
    #            see_entity_dic[(r,1,self.task_no)]=self.see[(r,1,self.task_no)].get()
    #        for r in range(2,6):
    #            for c in range(2,5):
    #                see_entity_dic[(r,c,self.task_no)]=self.see[(r,c,self.task_no)].get()
    #        save_var(see_entity_dic, path+'/see_entity_dic.txt')
            
    #     else:            
    #         for r in range(2,6):
    #             see_entity_dic[(r,1,self.task_no)]=self.see[(r,1,self.task_no)].get()
                         
    #         for r in range(2,6):
    #             for c in range(2,5):
    #                 see_entity_dic[(r,c,self.task_no)]=self.see[(r,c,self.task_no)].get()
    #         save_var(see_entity_dic, path+'/see_entity_dic.txt')
        
      
    #     self.root.destroy()

    def entry_event(self):
        try:
            # Validate entry fields only if any field in a row is filled
            for r in range(2, 6):
                row_filled = any(self.see[(r, c, self.task_no)].get().strip() for c in range(2, 5))
                if row_filled:
                    for c in range(2, 5):
                        val_str = self.see[(r, c, self.task_no)].get().strip()
                        if val_str == "":
                            raise ValueError(f"Please fill all required fields in row {r}.")
                        if not val_str.isdigit() or int(val_str) <= 0:
                            raise ValueError(f"Please enter a positive integer at row {r}, column {c}.")
            
            # If validation passes, update dictionary and save variables
            for r in range(2, 6):
                see_entity_dic[(r, 1, self.task_no)] = self.see[(r, 1, self.task_no)].get()
                for c in range(2, 5):
                    see_entity_dic[(r, c, self.task_no)] = self.see[(r, c, self.task_no)].get() if self.see[(r, c, self.task_no)].get().strip() else None
            save_var(see_entity_dic, path+'/see_entity_dic.txt')
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




class GUI_BE_Hear:
    def __init__(self,task_no):
    
        self.root = tk.Tk()    
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=1100    #window width
        wh=320   #window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.root.title('Hear')
        self.root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        self.task_no=task_no
        self.Hear()
        
    def Hear(self):
        #title Lable
        tk.Label(self.root,text='Choose the entitie(s) to be processed in Hear and set the corresponding parameters',font=('bold',14))\
            .grid(row = 0,column=0,pady=3,columnspan=10,sticky='w')
        title_ls=['Entity','First Arrival Time (msec)','IAT(msec)','Occurences']
        for c in range(1,5):
            tk.Label(self.root,text=title_ls[c-1],font=('bold',14),width=22,relief='sunken')\
                .grid(row = 1, column=c)
        for r in range(2,6):
            tk.Label(self.root,text=str(r-1),font=('bold',14),width=5,relief='sunken')\
                .grid(row = r, column=0)
        self.hear={}
        value_hear = ['','Color(s)','Text','Item(s)']
        for r in range(2,6):
            self.hear[(r,1,self.task_no)] = ttk.Combobox(
                master = self.root,
                width=30,
                state='readonly',
                cursor='arrow',
                values=value_hear, 
                font=('bold',10)
                )
            self.hear[(r,1,self.task_no)].bind('<<ComboboxSelected>>',self.pick)
            self.hear[(r,1,self.task_no)].grid(row=r,column=1)
            
            if saved==1 and load_var(path+'/hear_entity_dic.txt')[(r,1,self.task_no)]!='':
                for item in range(len(value_hear)):
                    if load_var(path+'/hear_entity_dic.txt')[(r,1,self.task_no)]==value_hear[item]:
                        self.hear[(r,1,self.task_no)].current(item)
            else:
                self.hear[(r,1,self.task_no)].current(0)
            
        for r in range(2,6):
            for c in range(2,5):
                self.hear[(r,c,self.task_no)]=tk.Entry(self.root,width=30)
                self.hear[(r,c,self.task_no)].grid(row=r,column=c)
                if saved==1:
                    self.hear[(r,c,self.task_no)].insert(0,load_var(path+'/hear_entity_dic.txt')[(r,c,self.task_no)])
        
        
        self.Button_ok=tk.Button(self.root,text='OK',font=16,command=self.entry_event)
        self.Button_ok.grid(row=8,rowspan=3,column=4,columnspan=1,pady=30,ipady=3,ipadx=7)
            
    def pick(self,*arg):
        for r in range(2,6):
            hear_entity_dic[(r,1,self.task_no)]=self.hear[(r,1,self.task_no)].get()
            
    # def entry_event(self):
        
    #     if saved == 1:
    #        hear_entity_dic.update(load_var(path+'/hear_entity_dic.txt'))
    #        for r in range(2,6):
    #            hear_entity_dic[(r,1,self.task_no)]=self.hear[(r,1,self.task_no)].get()
    #        save_var(hear_entity_dic, path+'/hear_entity_dic.txt')
    #        for r in range(2,6):
    #            for c in range(2,5):
    #                hear_entity_dic[(r,c,self.task_no)]=self.hear[(r,c,self.task_no)].get()
    #        save_var(hear_entity_dic, path+'/hear_entity_dic.txt')
    #     else:
    #         for r in range(2,6):
    #             hear_entity_dic[(r,1,self.task_no)]=self.hear[(r,1,self.task_no)].get()
    #         save_var(hear_entity_dic, path+'/hear_entity_dic.txt')
    #         for r in range(2,6):
    #             for c in range(2,5):
    #                 hear_entity_dic[(r,c,self.task_no)]=self.hear[(r,c,self.task_no)].get()
    #         save_var(hear_entity_dic, path+'/hear_entity_dic.txt')
    #     self.root.destroy()     

    def entry_event(self):
        try:
            # Validate entry fields only if any field in a row is filled
            for r in range(2, 6):
                row_filled = any(self.hear[(r, c, self.task_no)].get().strip() for c in range(2, 5))
                if row_filled:
                    for c in range(2, 5):
                        val_str = self.hear[(r, c, self.task_no)].get().strip()
                        if val_str == "":
                            raise ValueError(f"Please fill all required fields in row {r}.")
                        if not val_str.isdigit() or int(val_str) <= 0:
                            raise ValueError(f"Please enter a positive integer at row {r}, column {c}.")
            
            # If validation passes, update dictionary and save variables
            for r in range(2, 6):
                hear_entity_dic[(r, 1, self.task_no)] = self.hear[(r, 1, self.task_no)].get()
                for c in range(2, 5):
                    hear_entity_dic[(r, c, self.task_no)] = self.hear[(r, c, self.task_no)].get() if self.hear[(r, c, self.task_no)].get().strip() else None
            save_var(hear_entity_dic, path+'/hear_entity_dic.txt')
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


class GUI_BE_Choice:
    def __init__(self,task_no):
    
        self.root = tk.Tk()    
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=560   #window width
        wh=170   #window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.root.title('BE Specification: choice')
        self.root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        self.task_no=task_no
        self.Choice()
        
    def Choice(self):
        self.choice={}
        tk.Label(self.root,text='Input Choice Number: ',font=("Times New Roman",20)).grid(row=0,column=0,padx=30,pady=10)
        
        self.choice[self.task_no]=tk.Entry(self.root,width=15)
        self.choice[self.task_no].grid(row=0,column=1,ipady=3) 
        if saved==1:
            self.choice[self.task_no].insert(0,load_var(path+'/N.txt'))
       
        self.Button_ok=tk.Button(self.root,text='Save and Back to Step2',font=16,command=self.entry_event)
        self.Button_ok.grid(row=2,rowspan=3,column=1,columnspan=2,pady=30,ipady=3)
    #Ziqi's modification of type checking        
    def entry_event(self):
        global N
        try:
            N = int(self.choice[self.task_no].get())
            if N <= 0:
                raise ValueError
            save_var(N, path+'/N.txt')
            self.root.destroy()
        except ValueError:
            self.show_error_message()
            return
            
    def show_error_message(self):
        error_window = tk.Toplevel(self.root)
        error_window.title("Error")
        error_window.geometry("300x100")
        error_label = tk.Label(error_window, text="Please enter a positive integer for the choice number.", font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()

class GUI_BE_Lookat:
    def __init__(self,task_no):
    
        self.root = tk.Tk()    
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=550    #window width
        wh=170   #window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.root.title('Look_At')
        self.root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        self.task_no=task_no
        self.Lookat()
        
    def Lookat(self):
        self.lookat={}
        tk.Label(self.root,text='Input initial eye location: ',font=("Times New Roman",20)).grid(row=0,column=0,padx=30,pady=10)
        
        self.lookat[self.task_no]=tk.Entry(self.root,width=15)
        self.lookat[self.task_no].grid(row=0,column=1,ipady=3)
       
        self.Button_ok=tk.Button(self.root,text='OK',font=16,command=self.entry_event)
        self.Button_ok.grid(row=2,rowspan=3,column=4,columnspan=1,pady=30,ipady=3,ipadx=7)
    #Ziqi's modification of type checking        
    def entry_event(self):
        global eyeloc_ini
        try:
            eyeloc_ini = {}
            eyeloc_ini[eval(self.task_no)] = int(self.lookat[self.task_no].get())
            if eyeloc_ini[eval(self.task_no)] < 0 or eyeloc_ini[eval(self.task_no)] > 100:
                raise ValueError
            self.root.destroy()
        except ValueError:
            self.show_error_message()
            return #Ziqi's edition
            
    def show_error_message(self):
        error_window = tk.Toplevel(self.root)
        error_window.title("Error")
        error_window.geometry("300x100")
        error_label = tk.Label(error_window, text="Please enter an integer between 0 and 100 for the initial eye location.", font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()
    
class GUI_BE_Judgei:
    def __init__(self,task_no):
    
        self.root = tk.Tk()    
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=500    #window width
        wh=200   #window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.root.title('Judge_Identity')
        self.root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        self.task_no=task_no
        self.Judgei()
        
    def Judgei(self):
        self.judge_i={}
        self.judge_v={}
        tk.Label(self.root,text='Choose the identity to be judged',font=("Times New Roman",15)).grid(row=0,column=0,pady=10,padx=10)
        tk.Label(self.root,text='Choose the value of the target identity',font=("Times New Roman",15)).grid(row=1,column=0,pady=10)
        
        self.identity_var = tk.StringVar(self.root)
        self.judge_i[self.task_no] = ttk.Combobox(self.root,textvariable=self.identity_var,values = ['Text','Color'])
        self.judge_i[self.task_no].grid(row=0,column=1)
        if saved==1:
            for item in range(2):
                if load_var(path+'/judgei_target_dic.txt')[self.task_no]['identity']==['Text','Color'][item]:
                    self.judge_i[self.task_no].current(item)
        
        else:
            self.identity_var.trace_add('write',self.update_options)
        
        self.value_var = tk.StringVar(self.root)
        
        options_text = ['a', 'b', 'c']
        options_color = ['red', 'green','blue','yellow']
        
        if saved == 1:
            self.judge_v[self.task_no] = ttk.Combobox(self.root,textvariable=self.value_var,values=options_color+options_text)
        else:   
            self.judge_v[self.task_no] = ttk.Combobox(self.root,textvariable=self.value_var,values=[])
        self.judge_v[self.task_no].grid(row=1,column=1)
               
        if saved==1:
            for item in range(len(options_color)):
                if load_var(path+'/judgei_target_dic.txt')[self.task_no]['value']==options_color[item]:
                    self.judge_v[self.task_no].current(item)
            for item in range(len(options_text)):
                if load_var(path+'/judgei_target_dic.txt')[self.task_no]['value']==options_text[item]:
                    self.judge_v[self.task_no].current(item)
       
        self.Button_ok=tk.Button(self.root,text='OK',font=16,command=self.entry_event)
        self.Button_ok.grid(row=2,rowspan=3,column=4,columnspan=1,pady=30,ipady=3,ipadx=7)
            
    def update_options(self,*args):
        selected_identity = self.identity_var.get()
        self.value_var.set('')
        self.judge_v[self.task_no]['values']=[]
        if selected_identity == 'Text':
            options = ['a', 'b', 'c']
        elif selected_identity == 'Color':
            options = ['red', 'green','blue','yellow']
            
        self.judge_v[self.task_no]['values'] = options
            
    
    def pick(self,*arg):
        global judgei_target_dic
        judgei_target_dic={}
        judgei_target_dic[self.task_no]={}
        judgei_target_dic[self.task_no]['identity']=self.judge_i[self.task_no].get()
            
    def entry_event(self):
        global judgei_target_dic
        judgei_target_dic={}
        judgei_target_dic[self.task_no]={}
        judgei_target_dic[self.task_no]['identity']=self.judge_i[self.task_no].get()
        judgei_target_dic[self.task_no]['value']=self.judge_v[self.task_no].get()
        save_var(judgei_target_dic, path+'/judgei_target_dic.txt')
        self.root.destroy()

class GUI_BE_Count:
    def __init__(self,task_no):  
        self.root = tk.Tk()    
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=500      #window width
        wh=300      #window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.root.title('Define Count Parameters')
        self.root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        self.v=tk.IntVar()
        self.interface()
        
    def interface(self):
        #title Lable

        title_ls=['Count Length (Integer 1-10)']
        self.stimuli={}
        for r in range(1,2):
            tk.Label(self.root,text=title_ls[r-1],font=('bold',14),width=22,relief='flat',anchor='w')\
                .grid(row = r, column=0,columnspan=3,pady=20,padx=10)
                 
       
        for r in range(1,2):
            self.stimuli[(r,4)]=tk.Entry(self.root,width=22)
            self.stimuli[(r,4)].grid(row=r,column=4,columnspan=2)
            if saved==1:
                self.stimuli[(r,4)].insert(0,load_var(path+'/countstimuli.txt')[(r,4)])
                
        self.Button_save=tk.Button(self.root,text='Save and back to Step2',font=('bold',15),bg='white',command=self.entry_event)
        
        self.Button_save.grid(row=7,column=2,columnspan=4,ipadx=5,pady=30,ipady=10)
       
    #Ziqi's modification of type checking.
    def entry_event(self):
        global length_count, n_tiral_count, mean_count, sd_count, stimuli_dic, N_count
        try:
            stimuli_dic = {}
            for r in range(1,2):
                length_count = int(self.stimuli[(r,4)].get())
                if length_count <= 0 or length_count > 10:
                    raise ValueError
            save_var(stimuli_dic, path+'/countstimuli.txt')
            self.root.destroy()
        except ValueError:
            self.show_error_message()
            return #Ziqi's edition
            
    def show_error_message(self):
        error_window = tk.Toplevel(self.root)
        error_window.title("Error")
        error_window.geometry("300x100")
        error_label = tk.Label(error_window, text="Please enter an integer between 1 and 10 for the count length.", font=("Arial", 12))
        error_label.pack(pady=20)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()

class GUI_BE_Cal_single_digit_num:
    def __init__(self,task_no):  
        self.root = tk.Tk()    
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=800    #window width
        wh=350   #window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.root.title('Define Cal_single_digit_num Parameters')
        self.root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        self.v=tk.IntVar()
        self.task_no=task_no
        self.interface()
        
    def interface(self):
        #title Lable
        
        arith_ls=['Choose arithmetic operations']

        self.arith={}
     
        
        value_arith=['Add (+)','Subtract (-)','Multiplication (*)','Division (/)']
        self.arith[(0,4)] = ttk.Combobox(
           master = self.root,
           state='readonly',
           cursor='arrow',
           values=value_arith, 
           )
        self.arith[(0,4)] .grid(row=0,column=4,columnspan=3)
        
        if saved==1:
            for item in range(len(value_arith)):
                if load_var(path+'/arith.txt')[(0,4)]==value_arith[item]:
                    self.arith[(0,4)].current(item)
        
        r=0
        tk.Label(self.root,text=arith_ls[r],font=('bold',14),width=50,relief='flat',anchor='w')\
            .grid(row = r, column=0,columnspan=3,pady=20,padx=10)
        
        if saved==1:
            self.arith[(r,4)].insert(0,load_var(path+'/arith.txt')[(r,4)])
        self.Button_next=tk.Button(self.root,text='Save and back to step2',font=('bold',15),bg='white',command=self.start_event)
        self.Button_next.grid(row=2,column=4,columnspan=1,ipadx=12,pady=15,ipady=3)
        
           
    def start_event(self):
        
        global operation
        arith_dic={}
        r=0
        arith_dic[(r,4)]=self.arith[(r,4)].get()
        save_var(arith_dic, path+'/arith.txt')
        operation=self.arith[(0,4)].get()

        self.root.destroy()

color_dic={'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,255),\
          'yellow':(255,255,0), 'cyan':(0,255,255),'megenta':(255,0,255)
          }

    
look_for_ls=[[(0,0),'a','red'],\
                    [(1,1),'b','green'],\
                       [(2,2),'c','blue'] ]
class GUI_BE_Lookfor:
    def __init__(self,task_no):
    
        self.root = tk.Tk()    
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=1000    #window width
        wh=550#window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.root.title('Look_For')
        self.root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        self.task_no=task_no
        global judgei_target_dic       
        judgei_target_dic={}
        judgei_target_dic[self.task_no]={}
        self.Lookfor()
        
    def Lookfor(self):

        '''
        self.list_button=tk.Button(self.root,text='1.Open the list of all the items',font=("Times New Roman",15),command=self.lookfor_list)           
        self.list_button.pack(pady=30)
        '''
        
        
        self.judge_i={}

        tk.Label(self.root,text='1. Choose the identity to be judged',font=("Times New Roman",15)).pack()        
        
        value_identity=['Text','Color']
        self.judge_i[self.task_no]=ttk.Combobox(
            master=self.root,
            width=15,
            height=5,
            state='readonly',
            cursor='arrow',
            values=value_identity, 
            font=('bold',10)
            )
        self.judge_i[self.task_no].bind('<<ComboboxSelected>>',self.judge_identity)
        self.judge_i[self.task_no].pack(pady=30)
        
        if saved==1 and load_var(path+'/judgei_target_dic.txt')!='':
            for item in range(len(value_identity)):
                if load_var(path+'/judgei_target_dic.txt')[self.task_no]['identity']==value_identity[item]:
                    self.judge_i[self.task_no].current(item)
                    judgei_target_dic[self.task_no]['identity']=value_identity[item]

        tk.Button(self.root,text='2. Choose the value of the target identity:',font=("Times New Roman",15),command=self.target_button).pack(pady=30)
        
        tk.Button(self.root,text='Save',font=("Times New Roman",15),command=self.save).pack(pady=30)
        
    def lookfor_list(self):
        window=tk.Toplevel(self.root)
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=500    #window width
        wh=1000#window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        window.title('Look_For List')
        window.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        window.mainloop()
        
    def text(self):
        judgei_target_dic[self.task_no]['identity']='Text'
        self.window=tk.Toplevel(self.root)
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=500    #window width
        wh=200#window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.window.title('Choose Text Target')
        self.window.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        self.value_target=[]
        tk.Label(self.window,text='2. Choose Text Target', font=("Times New Roman",15)).pack(pady=30)
        for item in look_for_ls:
            self.value_target.append(item[1])
        self.judge_v={}
        self.judge_v[self.task_no]=ttk.Combobox(
            master=self.window,
            width=15,
            height=5,
            state='readonly',
            cursor='arrow',
            values=self.value_target, 
            font=('bold',10)
            )
        self.judge_v[self.task_no].bind('<<ComboboxSelected>>',self.judge_target_text)
        self.judge_v[self.task_no].pack()
        
        if saved==1 and load_var(path+'/judgei_target_dic.txt')!='':
            for item in range(len(self.value_target)):
                if load_var(path+'/judgei_target_dic.txt')[self.task_no]['value']==self.value_target[item]:
                    self.judge_v[self.task_no].current(item)
                    judgei_target_dic[self.task_no]['value']=self.value_target[item]
        
        ok=tk.Button(self.window, text='OK',font=("Times New Roman",15),command=self.ok)
        ok.pack(pady=30)
        
        
    def color(self):
        judgei_target_dic[self.task_no]['identity']='Color'
        self.window=tk.Toplevel(self.root)
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=500    #window width
        wh=200#window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.window.title('2. Choose Color Target')
        self.window.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        
        tk.Label(self.window,text='2. Choose Color Target', font=("Times New Roman",15)).pack(pady=30)
        self.value_target=[]
        for item in look_for_ls:
            self.value_target.append(item[2])
        self.judge_v={}
        self.judge_v[self.task_no]=ttk.Combobox(
            master=self.window,
            width=15,
            height=5,
            state='readonly',
            cursor='arrow',
            values=self.value_target, 
            font=('bold',10)
            )
        self.judge_v[self.task_no].bind('<<ComboboxSelected>>',self.judge_target_color)
        self.judge_v[self.task_no].pack()
        
        if saved==1 and load_var(path+'/judgei_target_dic.txt')!='':
            for item in range(len(self.value_target)):
                if load_var(path+'/judgei_target_dic.txt')[self.task_no]['value']==self.value_target[item]:
                    self.judge_v[self.task_no].current(item)
                    judgei_target_dic[self.task_no]['value']=self.value_target[item]
        
        ok=tk.Button(self.window,text='OK',font=("Times New Roman",15),command=self.ok)
        ok.pack(pady=30)
        
        
    def judge_identity(self,*arg):
        judgei_target_dic[self.task_no]['identity']=self.judge_i[self.task_no].get()
        
    
    def target_button(self):
        if judgei_target_dic[self.task_no]['identity']=='Text':
            self.text()
        else:
            self.color()
    
    def judge_target_text(self,*arg):
   
        judgei_target_dic[self.task_no]['value']=self.judge_v[self.task_no].get()
    
    
    
    def judge_target_color(self,*arg):  
               
        judgei_target_dic[self.task_no]['value']=self.judge_v[self.task_no].get()
        
    def ok (self):
        save_var(judgei_target_dic, path+'/judgei_target_dic.txt')
        self.window.destroy()
        
    def save (self):
        self.root.destroy()
        

class GUI_BE_track1D:
    def __init__(self,task_no):
    
        self.root = tk.Tk()    
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=500    #window width
        wh=500 #window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.root.title('Tracking_1D')
        self.root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        self.task_no=task_no
        tk.Label(self.root,text='Enter curse starting location: (An integer in 1-100) ',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        self.track1D_curse_loc={}
        
        self.track1D_curse_loc[self.task_no]=tk.Entry(self.root,width=20)
        self.track1D_curse_loc[self.task_no].pack(anchor='w',padx=10)
        if saved==1:
            self.track1D_curse_loc[self.task_no].insert(0,str(load_var(path+'/track1D_curse_loc.txt')))
        tk.Label(self.root,text='Select target movement track1D_freq:',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        
        value_track1D_freq = ['Slow','Medium','Quick']
        
        self.track1D_freq={}
        self.track1D_freq[self.task_no] = ttk.Combobox(
            master = self.root,
            state='readonly',
            cursor='arrow',
            width=22,
            values=value_track1D_freq, 
            )
        #self.stimulitype.bind('<<ComboboxSelected>>',self.pick)
        self.track1D_freq[self.task_no].pack(anchor='w',padx=10)
        
        if saved==1:
            for item in range(len(value_track1D_freq)):
                if load_var(path+'/track1D_freq.txt')==value_track1D_freq[item]:
                    self.track1D_freq[self.task_no].current(item)
        
        
        tk.Label(self.root,text='Select target movement track1D_amp:',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        
        value_track1D_amp = ['Small','Medium','Large']
        self.track1D_amp={}
        self.track1D_amp[self.task_no] = ttk.Combobox(
            master = self.root,
            state='readonly',
            cursor='arrow',
            width=22,
            values=value_track1D_amp, 
            )
        #self.stimulitype.bind('<<ComboboxSelected>>',self.pick)
        self.track1D_amp[self.task_no].pack(anchor='w',padx=10)
        
        if saved==1:
            for item in range(len(value_track1D_amp)):
                if load_var(path+'/track1D_amp.txt')==value_track1D_amp[item]:
                    self.track1D_amp[self.task_no].current(item)
        
        tk.Label(self.root,text='Select response method:',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        
        value_track1D_response = ['Click mouse','Press keyboard']
        
        self.track1D_response={}
        self.track1D_response[self.task_no] = ttk.Combobox(
            master = self.root,
            state='readonly',
            cursor='arrow',
            width=22,
            values=value_track1D_response, 
            )
        #self.stimulitype.bind('<<ComboboxSelected>>',self.pick)
        self.track1D_response[self.task_no].pack(anchor='w',padx=10)
        
        if saved==1:
            for item in range(len(value_track1D_response)):
                if load_var(path+'/track1D_response.txt')==value_track1D_response[item]:
                    self.track1D_response[self.task_no].current(item)
        
        self.Button_ok=tk.Button(self.root,text='OK',font=16,command=self.entry_event)
        self.Button_ok.pack()
    #Ziqi's modification of type checking    
    def entry_event(self):
        global track1D_curse_loc, track1D_freq, track1D_amp, track1D_response
        try:
            track1D_curse_loc = int(self.track1D_curse_loc[self.task_no].get())
            if track1D_curse_loc < 1 or track1D_curse_loc > 100:
                raise ValueError
            save_var(track1D_curse_loc, path+'/track1D_curse_loc.txt')
            
            track1D_freq = self.track1D_freq[self.task_no].get()
            save_var(track1D_freq, path+'/track1D_freq.txt')
            
            track1D_amp = self.track1D_amp[self.task_no].get()
            save_var(track1D_amp, path+'/track1D_amp.txt')
            
            track1D_response = self.track1D_response[self.task_no].get()
            save_var(track1D_response, path+'/track1D_response.txt')
            
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
        
class GUI_BE_track2D:
    def __init__(self,task_no):
    
        self.root = tk.Tk()    
        sw=self.root.winfo_screenwidth()        #screen width
        sh=self.root.winfo_screenheight()       #screen height
        ww=500    #window width
        wh=700 #window height
        x=(sw-ww)/2  #window coordinate (left_up point)
        y=(sh-wh)/2  #window coordinate
        self.root.title('Tracking_2D')
        self.root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))
        self.task_no=task_no
        tk.Label(self.root,text='Enter cursor starting location (x): (An integer in 0-100) ',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        self.track2D_cursor_loc_x={}
        
        self.track2D_cursor_loc_x[self.task_no]=tk.Entry(self.root,width=20)
        self.track2D_cursor_loc_x[self.task_no].pack(anchor='w',padx=10)
        if saved==1:
            self.track2D_cursor_loc_x[self.task_no].insert(0,str(load_var(path+'/track2D_cursor_loc_x.txt')))
        
        tk.Label(self.root,text='Enter cursor starting location (y): (An integer in 0-100) ',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        self.track2D_cursor_loc_y={}
        
        self.track2D_cursor_loc_y[self.task_no]=tk.Entry(self.root,width=20)
        self.track2D_cursor_loc_y[self.task_no].pack(anchor='w',padx=10)
        if saved==1:
            self.track2D_cursor_loc_y[self.task_no].insert(0,str(load_var(path+'/track2D_cursor_loc_y.txt')))
        
        tk.Label(self.root,text='Enter initial target location (x): (An integer in 0-100) ',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        self.track2D_target_loc_x={}
        
        self.track2D_target_loc_x[self.task_no]=tk.Entry(self.root,width=20)
        self.track2D_target_loc_x[self.task_no].pack(anchor='w',padx=10)
        if saved==1:
            self.track2D_target_loc_x[self.task_no].insert(0,str(load_var(path+'/track2D_target_loc_x.txt')))
            
        
        tk.Label(self.root,text='Enter initial target location (y): (An integer in 0-100) ',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        self.track2D_target_loc_y={}
        
        self.track2D_target_loc_y[self.task_no]=tk.Entry(self.root,width=20)
        self.track2D_target_loc_y[self.task_no].pack(anchor='w',padx=10)
        if saved==1:
            self.track2D_target_loc_y[self.task_no].insert(0,str(load_var(path+'/track2D_target_loc_y.txt')))
        
        tk.Label(self.root,text='Select target movement track2D_freq:',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        
        value_track2D_freq = ['Slow','Medium','Quick']
        
        self.track2D_freq={}
        self.track2D_freq[self.task_no] = ttk.Combobox(
            master = self.root,
            state='readonly',
            cursor='arrow',
            width=22,
            values=value_track2D_freq, 
            )
        #self.stimulitype.bind('<<ComboboxSelected>>',self.pick)
        self.track2D_freq[self.task_no].pack(anchor='w',padx=10)
        
        if saved==1:
            for item in range(len(value_track2D_freq)):
                if load_var(path+'/track2D_freq.txt')==value_track2D_freq[item]:
                    self.track2D_freq[self.task_no].current(item)
        
        
        tk.Label(self.root,text='Select target movement track2D_amp:',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        
        value_track2D_amp = ['Small','Medium','Large']
        self.track2D_amp={}
        self.track2D_amp[self.task_no] = ttk.Combobox(
            master = self.root,
            state='readonly',
            cursor='arrow',
            width=22,
            values=value_track2D_amp, 
            )
        #self.stimulitype.bind('<<ComboboxSelected>>',self.pick)
        self.track2D_amp[self.task_no].pack(anchor='w',padx=10)
        
        if saved==1:
            for item in range(len(value_track2D_amp)):
                if load_var(path+'/track2D_amp.txt')==value_track2D_amp[item]:
                    self.track2D_amp[self.task_no].current(item)
        
        tk.Label(self.root,text='Select response method:',font=("Times New Roman",15)).pack(anchor='w',pady=20,padx=10)
        
        value_track2D_response = ['Click mouse','Press keyboard']
        
        self.track2D_response={}
        self.track2D_response[self.task_no] = ttk.Combobox(
            master = self.root,
            state='readonly',
            cursor='arrow',
            width=22,
            values=value_track2D_response, 
            )
        #self.stimulitype.bind('<<ComboboxSelected>>',self.pick)
        self.track2D_response[self.task_no].pack(anchor='w',padx=10)
        
        if saved==1:
            for item in range(len(value_track2D_response)):
                if load_var(path+'/track2D_response.txt')==value_track2D_response[item]:
                    self.track2D_response[self.task_no].current(item)
        
        self.Button_ok=tk.Button(self.root,text='OK',font=16,command=self.entry_event)
        self.Button_ok.pack()
    #Ziqi's modification of type checking    
    def entry_event(self):
        global track2D_target_loc_x, track2D_target_loc_y, track2D_cursor_loc_x, track2D_cursor_loc_y, track2D_freq, track2D_amp, track2D_response
        try:
            track2D_target_loc_x = int(self.track2D_target_loc_x[self.task_no].get())
            if track2D_target_loc_x < 0 or track2D_target_loc_x > 100:
                raise ValueError
            save_var(track2D_target_loc_x, path+'/track2D_target_loc_x.txt')
            
            track2D_target_loc_y = int(self.track2D_target_loc_y[self.task_no].get())
            if track2D_target_loc_y < 0 or track2D_target_loc_y > 100:
                raise ValueError
            save_var(track2D_target_loc_y, path+'/track2D_target_loc_y.txt')
            
            track2D_cursor_loc_x = int(self.track2D_cursor_loc_x[self.task_no].get())
            if track2D_cursor_loc_x < 0 or track2D_cursor_loc_x > 100:
                raise ValueError
            save_var(track2D_cursor_loc_x, path+'/track2D_cursor_loc_x.txt')
            
            track2D_cursor_loc_y = int(self.track2D_cursor_loc_y[self.task_no].get())
            if track2D_cursor_loc_y < 0 or track2D_cursor_loc_y > 100:
                raise ValueError
            save_var(track2D_cursor_loc_y, path+'/track2D_cursor_loc_y.txt')
            
            track2D_freq = self.track2D_freq[self.task_no].get()
            save_var(track2D_freq, path+'/track2D_freq.txt')
            
            track2D_amp = self.track2D_amp[self.task_no].get()
            save_var(track2D_amp, path+'/track2D_amp.txt')
            
            track2D_response = self.track2D_response[self.task_no].get()
            save_var(track2D_response, path+'/track2D_response.txt')
            
            self.root.destroy()
        except ValueError:
            self.show_error_message()
            return
            
    def show_error_message(self):
        error_window = tk.Toplevel(self.root)
        error_window.title("Error")
        error_window.geometry("300x100")
        error_label = tk.Label(error_window, text="Please enter an integer between 0 and 100 for the target and cursor locations.", font=("Arial", 12))
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

        if operation=='Add (+)':
            text='+'
        elif operation=='Subtract (-)':
            text='-'
        elif operation=='Multiplication (*)':
            text='*'
        else:
            text='/'
        frame.canvas.create_text(w/2,h/2,text=text,font=("Times New Roman",18,"bold"))
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
        user=w/5+track1D_curse_loc/100*w/5*3
        r=5
        t=frame.canvas.create_oval(target-r, h/2-r,target+r,h/2+r,fill='red',outline='red',tag='target')
        frame.canvas.create_oval(user-r, h/2-r,user+r,h/2+r,fill='black',outline='black',tag='user')
        
        
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
        target_x=track2D_target_loc_x/100*length+origin_x
        target_y=origin_y-track2D_target_loc_y/100*length
        cursor_x=track2D_cursor_loc_x/100*length+origin_x
        cursor_y=origin_y-track2D_cursor_loc_y/100*length
        #user=w/5+track1D_curse_loc/100*w/5*3
        r=5
        target=frame.canvas.create_oval(target_x-r, target_y-r,target_x+r,target_y+r,fill='red',outline='red',tag='target')
        frame.canvas.create_oval(cursor_x-r, cursor_y-r,cursor_x+r,cursor_y+r,fill='black',outline='black',tag='user')
        
        
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

ppt=33
cpt=35
mpt=24


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
    
    

#4.7 BEs


def See(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation):
    if attribute['type']==2:  
        global communication_signal,eyefixation
        if anim==1:
            #If visual entity arrives, Watch_for is enabled
            print('%.2fmsec, See operator is enabled by the arrival of visual entity #%s'%(env.now,(i[0],k)))
    
            #At server1: 
            #Visual input at server1: 
            #If receiving a communication signal from serverW, update eye fixation location
           
            if communication_signal == 1:
                eyefixation = neweyefixation
                communication_signal = 0   #updating ends, flip the communication signal sign
            #print('eye fixation input at server1: ',eyefixation)
            
            #if entity (i) is Noise, no entry 
            #(for now, no need to go to Server 2, TBD later)
    
            if attribute['stimuli'] == 0:
                print('entity', (i[0],k), 'is a noise')
            #if entity (i) is Visual Signal (of any kind): 
            else: 
                print('entity', (i[0],k), 'is a visual signal')
    
                Structure_and_Animation().enter(qn_mhp.server1, '1','0_1', i, j, k,generation)  
                Structure_and_Animation().add('1', i, j, k,generation)                
                yield env.timeout(ppt)  #use ppt time
                Structure_and_Animation().delete(i, j, k, '1',generation)
                
                outserver_dic[1] = 1 #send entity (i) to server 2&3
            
            #At server2 & 3: 
            #if receiving entity (i) from Server 1
            if outserver_dic[1] == 1:
                yield env.process(server2(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))\
                    &env.process(server3(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))              
                #outserver_dic[2]=outserver_dic[3] = 1 #send entity (i) to server 4
            
            #At server4
            #If receiving entity (i) from server 2&3
            if outserver_dic[2] == 1 and outserver_dic[3]==1:          
                with qn_mhp.server4.request() as request:                
                    yield request     
                    Structure_and_Animation().add('4', i, j, k,generation)             
                    yield env.timeout(ppt) #use ppt time   
                    Structure_and_Animation().delete(i, j, k, '4',generation)
                  
            #send entity to  Server A and/or B
            #depending on whether it is Spatial and/or Verbal 
                if attribute['info'] == 4:  #if spatial 
                    outserver_dic[4] = 1  #send to A
                elif attribute['info'] == 5:  #if verbal
                    outserver_dic[4] = 2  #send to B
                elif attribute['info'] == 6:  #if both
                    outserver_dic[4] = 3  #send to both A and B
                elif attribute['info'] == 7: #if unknown or unspecified (by the modeler)
                    prob = random.uniform(0,1)
                    if prob <=0.5:  #send Entity (i) to Server A or B with equal probability (p=0.5) (for now)
                        outserver_dic[4] = 1 #send to A              
                    else:
                        outserver_dic[4] = 2 #send to B 
                
                # At Server A or B (the one that receives Entity (i)):
                #upon receiving entity (i) from Server 4:
                if outserver_dic[4]!=0:
                    #(immediately) send entity (i) to Server C, and keep a copy of entity (i)
                    outserver_dic[101] = outserver_dic[102]=1       
                    copy_dic[i[0]] = attribute
            
                    Structure_and_Animation().enter(qn_mhp.serverC, 'C', '4_C', i, j, k, generation) 
                    Structure_and_Animation().add('C', i, j, k,generation)  
                    Structure_and_Animation().delete(i, j, k, 'C', generation)          
                print('%.2fmsec, See ends for entity #%s'%(env.now,(i[0],k))) 
        
        else:
            #If visual entity arrives, Watch_for is enabled
            print('%.2fmsec, See operator is enabled by the arrival of visual entity #%s'%(env.now,(i[0],k)))
        
            #At server1: 
            #Visual input at server1: 
            #If receiving a communication signal from serverW, update eye fixation location
    
            if communication_signal == 1:
                eyefixation = neweyefixation
                communication_signal = 0   #updating ends, flip the communication signal sign
            #print('eye fixation input at server1: ',eyefixation)
            
            #if entity (i) is Noise, no entry 
            #(for now, no need to go to Server 2, TBD later)
            if attribute['stimuli'] == 0:
                print('entity', (i[0],k), 'is a noise')
            #if entity (i) is Visual Signal (of any kind): 
            else: 
                print('entity', (i[0],k), 'is a visual signal')        
                yield env.timeout(ppt)  #use ppt time
        
                outserver_dic[1] = 1 #send entity (i) to server 2&3
            
            #At server2 & 3: 
            #if receiving entity (i) from Server 1
            if outserver_dic[1] == 1:
                if outserver_dic[1] == 1:
                    yield env.process(server2(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))\
                        &env.process(server3(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))              
                   
            #At server4
            #If receiving entity (i) from server 2&3
            if outserver_dic[2] == 1 and outserver_dic[3]==1:
            
                with qn_mhp.server4.request() as request:           
                    yield request            
                    yield env.timeout(ppt) #use ppt time   
                    
            #send entity to  Server A and/or B
            #depending on whether it is Spatial and/or Verbal 
                if attribute['info'] == 4:  #if spatial 
                    outserver_dic[4] = 1  #send to A
                elif attribute['info'] == 5:  #if verbal
                    outserver_dic[4] = 2  #send to B
                elif attribute['info'] == 6:  #if both
                    outserver_dic[4] = 3  #send to both A and B
                elif attribute['info'] == 7: #if unknown or unspecified (by the modeler)
                    prob = random.uniform(0,1)
                    if prob <=0.5:  #send Entity (i) to Server A or B with equal probability (p=0.5) (for now)
                        outserver_dic[4] = 1 #send to A              
                    else:
                        outserver_dic[4] = 2 #send to B 
                
                # At Server A or B (the one that receives Entity (i)):
                #upon receiving entity (i) from Server 4:
                if outserver_dic[4]!=0:
                    #(immediately) send entity (i) to Server C, and keep a copy of entity (i)
                    outserver_dic[101] = outserver_dic[102]=1       
                    copy_dic[i[0]] = attribute
                         
                print('%.2fmsec, See ends for entity #%s'%(env.now,(i[0],k))) 
        
            
        # in case user forgot to selcet 'Store to wm' BE
        if ['Store_to_WM']  not in Tasklist_dic[k]:
            yield env.process(Store_to_WM(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))
            
        
def Hear (qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):
    if attribute['type']==3:
        if anim==1:
          
           #If auditory entity arrives, Listen_to is enabled
           print('%.2fmsec, Hear operator is enabled by the arrival of entity #%s'%(env.now,(i[0],k)))
    
           #At server5: 
           #if entity (i) is Noise, no entry 
           #(for now, no need to go to Server 6, TBD later)
           if attribute['stimuli'] == 0:
               print('entity', (i[0],k), 'is a noise')
           #if entity (i) is Visual Signal (of any kind): 
           else: 
               print('entity', (i[0],k), 'is an auditory signal')
               
               Structure_and_Animation().enter(qn_mhp.server5, '5','0_5' ,i, j, k,generation)           
               Structure_and_Animation().add('5', i, j, k,generation)          
               yield env.timeout(ppt)  #use ppt time
               Structure_and_Animation().delete(i, j, k, '5',generation)
               
               outserver_dic[5] = 1 #send entity (i) to server 6&7
           
           #At server6 & 7: 
           #if receiving entity (i) from Server 5
           if outserver_dic[5] == 1:
               yield env.process(server6(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))\
                   &env.process(server7(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))              
           
           #At server8
           #If receiving entity (i) from server 6&7
           if outserver_dic[6] == 1 and outserver_dic[7]==1:
               
               with qn_mhp.server8.request() as request:              
                   yield request            
                   Structure_and_Animation().add('8', i, j, k,generation)              
                   yield env.timeout(ppt) #use ppt time
                   Structure_and_Animation().delete(i, j, k, '8',generation)
               
           #send entity to  Server A and/or B
           #depending on whether it is Spatial and/or Verbal 
               if attribute['info'] == 4:  #if spatial 
                   outserver_dic[8] = 1  #send to A
               elif attribute['info'] == 5:  #if verbal
                   outserver_dic[8] = 2  #send to B
               elif attribute['info'] == 6:  #if both
                   outserver_dic[8] = 3  #send to both A and B
               elif attribute['info'] == 7: #if unknown or unspecified (by the modeler)
                   prob = random.uniform(0,1)
                   if prob <=0.5:  #send Entity (i) to Server A or B with equal probability (p=0.5) (for now)
                       outserver_dic[8] = 1 #send to A               
                   else:
                       outserver_dic[8] = 2 #send to B 
                       
               # At Server A or B (the one that receives Entity (i)):
               #upon receiving entity (i) from Server 8:
               if outserver_dic[8]!=0:
                   #(immediately) send entity (i) to Server C, and keep a copy of entity (i)
                   outserver_dic[101] = outserver_dic[102]=1       
                   copy_dic[(i[0],k)] = attribute
                  
                   Structure_and_Animation().enter(qn_mhp.serverC, 'C', '4_C', i, j, k, generation) 
                   Structure_and_Animation().add('C', i, j, k,generation)  
                   Structure_and_Animation().delete(i, j, k, 'C', generation)
                   
               print('%.2fmsec, Hear ends for entity #%s'%(env.now,(i[0],k)))
    
    
        else:
           #If auditory entity arrives, Listen_to is enabled
           print('%.2fmsec, Hear operator is enabled by the arrival of auditory entity #%s'%(env.now,(i[0],k)))
       
           #At server5: 
           #if entity (i) is Noise, no entry 
           #(for now, no need to go to Server 6, TBD later)
           if attribute['stimuli'] == 0:
               print('entity', (i[0],k), 'is a noise')
           #if entity (i) is Visual Signal (of any kind): 
           else: 
               print('entity', (i[0],k), 'is an auditory signal')
                      
               yield env.timeout(ppt)  #use ppt time
    
               outserver_dic[5] = 1 #send entity (i) to server 6&7
           
           #At server6 & 7: 
           #if receiving entity (i) from Server 5
           if outserver_dic[5] == 1:
               yield env.process(server6(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))\
                   &env.process(server7(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))              
           
           #At server8
           #If receiving entity (i) from server 6&7
           if outserver_dic[6] == 1 and outserver_dic[7]==1:
               
               with qn_mhp.server8.request() as request:
                      
                   yield request
            
                   yield env.timeout(ppt) #use ppt time
                        
                   
           #send entity to  Server A and/or B
           #depending on whether it is Spatial and/or Verbal 
               if attribute['info'] == 4:  #if spatial 
                   outserver_dic[8] = 1  #send to A
               elif attribute['info'] == 5:  #if verbal
                   outserver_dic[8] = 2  #send to B
               elif attribute['info'] == 6:  #if both
                   outserver_dic[8] = 3  #send to both A and B
               elif attribute['info'] == 7: #if unknown or unspecified (by the modeler)
                   prob = random.uniform(0,1)
                   if prob <=0.5:  #send Entity (i) to Server A or B with equal probability (p=0.5) (for now)
                       outserver_dic[8] = 1 #send to A               
                   else:
                       outserver_dic[8] = 2 #send to B 
                       
               # At Server A or B (the one that receives Entity (i)):
               #upon receiving entity (i) from Server 8:
               if outserver_dic[8]!=0:
                   #(immediately) send entity (i) to Server C, and keep a copy of entity (i)
                   outserver_dic[101] = outserver_dic[102]=1       
                   copy_dic[(i[0],k)] = attribute
                   
               print('%.2fmsec, Hear ends for entity #%s'%(env.now,(i[0],k)))

        # in case user forgot to selcet 'Store to wm' BE
        if ['Store_to_WM']  not in Tasklist_dic[k]:
            yield env.process(Store_to_WM(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))
            

def Store_to_WM(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation):
    
    if j==  [['See'], ['Store_to_WM']] or j==[['Hear'], ['Store_to_WM']] or  j==[['See','Hear'], ['Store_to_WM']]:    #if the task is Rememebr in WM 
        prio=i[0]*-1
       
    else:
        prio=-10e5
        
    if anim==1:
        #Store_to_STM is enabled if receiving entity (i) from Server 4 and/or Server 8
        if outserver_dic[4] !=0 or outserver_dic[8]!=0:
            print('%.2fmsec, Store_to_STM operator is enabled by receiving entity #%s'%(env.now,(i[0],k)))
        
            if outserver_dic[4]==1 or outserver_dic[8]==1:  #if entity is sent to serverA
                #At serverA
                yield env.process(serverA(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, prio,generation))
                                     
            elif outserver_dic[4] == 2 or outserver_dic[8]==2: #if entity is sent to serverB            
                #At serverB
                yield env.process(serverB(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, prio,generation))
                                        
            elif outserver_dic[4] == 3 or outserver_dic[8]==3: #if entity is sent to both serverA &B
            
            #At serverA&B
                yield env.process(serverA(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, prio,generation))\
                    & env.process(serverB(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, prio,generation))

            print('%.2fmsec, Store_to_STM ends for entity #%s'%(env.now,(i[0],k)))
            
    else:
        #Store_to_STM is enabled if receiving entity (i) from Server 4 and/or Server 8
        if outserver_dic[4] !=0 or outserver_dic[8]!=0:
            print('%.2fmsec, Store_to_STM operator is enabled by receiving entity #%s'%(env.now,(i[0],k)))
        
            if outserver_dic[4]==1 or outserver_dic[8]==1:  #if entity is sent to serverA
        
                #At serverA
                yield env.process(serverA(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, prio,generation))
       
            elif outserver_dic[4] == 2 or outserver_dic[8]==2: #if entity is sent to serverB            
                #At serverB
                yield env.process(serverB(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, prio,generation))
                                 
            elif outserver_dic[4] == 3 or outserver_dic[8]==3: #if entity is sent to both serverA &B
            
            #At serverA&B
                yield env.process(serverA(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, prio,generation))\
                    & env.process(serverB(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, prio,generation))
                       
            print('%.2fmsec, Store_to_STM ends for entity #%s'%(env.now,(i[0],k)))
    

def Choice(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):
    
    if anim==1:
        #Choice is enabled if receiving entity (i) from Server A or B  
        if outserver_dic[101] == 1 and outserver_dic[102] == 1:
            print('%.2fmsec, Choice operator is enabled by receiving entity #%s'%(env.now,(i[0],k)))
            
            #At serverC  
            if outserver_dic[4]!=0 or outserver_dic[8]!=0:
                if outserver_dic[4]!=0:
                    Structure_and_Animation().enter(qn_mhp.serverC, 'C', '4_C', i, j, k,generation)
                else:
                    Structure_and_Animation().enter(qn_mhp.serverC, 'C', '8_C', i, j, k,generation)
                with qn_mhp.serverC.request() as request:               
                    yield request                
                    Structure_and_Animation().add('C', i, j, k,generation)                    
                    yield env.timeout(cpt)
                    Structure_and_Animation().delete(i, j, k, 'C',generation)
            
                #At serverF       
                #Use total time =cpt time + b* log2 (N) (N is the number of choices, b=50ms, for now) 
                b=150
                Structure_and_Animation().enter(qn_mhp.serverF, 'F', 'C_F', i, j, k,generation)
                with qn_mhp.serverF.request() as request:        
                    yield request                
                    Structure_and_Animation().add('F', i, j, k,generation)                
                    yield env.timeout(cpt+b*math.log(N,2))
                    Structure_and_Animation().delete(i, j, k, 'F',generation)
                                                
                #Send entity (i) (back) to Server C; At Server C,
                outserver_dic[103] = 1  #send entity (i) to W
                print('%.2fmsec, Choice ends for entity #%s'%(env.now,(i[0],k))) 
    
    else:    
        #Choice is enabled if receiving entity (i) from Server A or B  
        if outserver_dic[101] == 1 and outserver_dic[102] == 1:
            print('%.2fmsec, Choice operator is enabled by receiving entity #%s'%(env.now,(i[0],k)))
            
            #At serverC  
            with qn_mhp.serverC.request() as request:
                            
                yield request
                yield env.timeout(cpt)
                            
            
            #At serverF       
            #Use total time =cpt time + b* log2 (N) (N is the number of choices, b=50ms, for now) 
            b=150
            with qn_mhp.serverF.request() as request:
                    
                yield request
                
                yield env.timeout(cpt+b*math.log(N,2))
                
            #Send entity (i) (back) to Server C; At Server C,
            outserver_dic[103] = 1  #send entity (i) to W
            print('%.2fmsec, Choice ends for entity #%s'%(env.now,(i[0],k))) 


def Judge_identity (qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation):
    #judge= 'color'
    print('%.2fmsec,Judge_identity operator is enabled by receiving entity #%s'%(env.now,(i[0],k)))
    if anim==1:
        #Judge_identity is enabled if receiving entity (i) from Server A or B  
        #if outserver_dic[101] == 1 and outserver_dic[102] == 1:
            
        #At serverF
        # store its attributes
        ji_store_dic[(i[0]),k]=attribute
        #use cpt time (at least, for now, perhaps 150 msec is needed)
        Structure_and_Animation().enter(qn_mhp.serverF, 'F', '4_F', i, j, k,generation)
        with qn_mhp.serverF.request() as request:
            yield request
            Structure_and_Animation().add('F', i, j, k, generation)
            time.sleep(0.1)
            yield env.timeout(cpt)
            Structure_and_Animation().delete(i, j, k, 'F',generation)
        if judgei_target_dic[str(k)]['identity']=='Text':
            
            judge = 'text'
           
            if judgei_target_dic[str(k)]['value']==attribute['text']:
                ji_result_dic[(i[0],k)]='T'
                print('%.2fmsec,Judge_identity,target %s is found'%(env.now,judgei_target_dic[str(k)]['value']))
            else:
                  ji_result_dic[(i[0],k)]='F'
                  print('%.2fmsec,Judge_identity,target %s is not found'%(env.now,judgei_target_dic[str(k)]['value']))
  
                    
        elif judgei_target_dic[str(k)]['identity']=='Color':
            
            judge = 'color'
            for (key,value) in color_dic.items():
                if key == judgei_target_dic[str(k)]['value']:
                    color = value
            if color==attribute['color']:
                ji_result_dic[(i[0],k)]='T'
                print('%.2fmsec,Judge_identity,target %s is found'%(env.now,judgei_target_dic[str(k)]['value']))
            else:
                ji_result_dic[(i[0],k)]='F'
                print('%.2fmsec,Judge_identity,target %s is not found'%(env.now,judgei_target_dic[str(k)]['value']))


        Structure_and_Animation().judge_result(i, j, k, judge)
        
    elif anim==0:
        #Judge_identity is enabled if receiving entity (i) from Server A or B  
        #if outserver_dic[101] == 1 and outserver_dic[102] == 1:
            
        #At serverF
        # store its attributes
        ji_store_dic[(i[0]),k]=attribute
        #use cpt time (at least, for now, perhaps 150 msec is needed)       
        with qn_mhp.serverF.request() as request:
            yield request
            yield env.timeout(cpt)

        if judgei_target_dic[str(k)]['identity']=='Text':
            
            judge = 'text'
           
            if judgei_target_dic[str(k)]['value']==attribute['text']:
                ji_result_dic[(i[0],k)]='T'
                print('%.2fmsec,Judge_identity,target %s is found'%(env.now,judgei_target_dic[str(k)]['value']))
            else:
                  ji_result_dic[(i[0],k)]='F'
                  print('%.2fmsec,Judge_identity,target %s is not found'%(env.now,judgei_target_dic[str(k)]['value']))
  
                    
        elif judgei_target_dic[str(k)]['identity']=='Color':
            
            judge = 'color'
            
            if eval(judgei_target_dic[str(k)]['value'])==attribute['color']:
                ji_result_dic[(i[0],k)]='T'
                print('%.2fmsec,Judge_identity,target %s is found'%(env.now,judgei_target_dic[str(k)]['value']))
            else:
                ji_result_dic[(i[0],k)]='F'
                print('%.2fmsec,Judge_identity,target %s is not found'%(env.now,judgei_target_dic[str(k)]['value']))
                
                
def Judge_magnitude (qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation,dimension):
  
    print('%.2fmsec,Judge_magnitude operator is enabled by receiving entity #%s'%(env.now,(i[0],k)))
    if anim==1:
        #Judge_identity is enabled if receiving entity (i) from Server A or B  
        #if outserver_dic[101] == 1 and outserver_dic[102] == 1:
            
        #At serverF
        # store its attributes
        jm_store_dic[(i[0]),k]=attribute
        #use cpt time (at least, for now, perhaps 150 msec is needed)
        Structure_and_Animation().enter(qn_mhp.serverF, 'F', 'C_F', i, j, k,generation)
        with qn_mhp.serverF.request() as request:
            yield request
            Structure_and_Animation().add('F', i, j, k, generation)
            yield env.timeout(cpt)
            Structure_and_Animation().delete(i, j, k, 'F',generation)
        if 'Tracking_1D' in task_info_dic.values():   
            if attribute['eye_loc'][0]==attribute['eye_loc'][1]:
                jm_result_dic[(i[0],k)]='T'
                print('Cursor location = Target location')
            elif attribute['eye_loc'][0]<attribute['eye_loc'][1]:
                jm_result_dic[(i[0],k)]='Left'
                print('Cursor location > Target location')
            elif attribute['eye_loc'][0]>attribute['eye_loc'][1]:
                jm_result_dic[(i[0],k)]='Right'
                print('Cursor location < Target location')
            
        elif 'Tracking_2D' in task_info_dic.values():
            if dimension=='x':
                if attribute['eye_loc'][0]==attribute['eye_loc'][2]:
                    jm_result_dic[(i[0],k)]='T'
                    print('Cursor location_x = Target location_x')
                elif attribute['eye_loc'][0]<attribute['eye_loc'][2]:
                    jm_result_dic[(i[0],k)]='Left'
                    print('Cursor location_x > Target location_x')
                elif attribute['eye_loc'][0]>attribute['eye_loc'][2]:
                    jm_result_dic[(i[0],k)]='Right'
                    print('Cursor location_x < Target location_x')
            if dimension=='y':
                if attribute['eye_loc'][1]==attribute['eye_loc'][3]:
                    jm_result_dic[(i[0],k)]='T'
                    print('Cursor location_y = Target location_y')
                elif attribute['eye_loc'][1]<attribute['eye_loc'][3]:
                    jm_result_dic[(i[0],k)]='Left'
                    print('Cursor location_y > Target location_y')
                elif attribute['eye_loc'][1]>attribute['eye_loc'][3]:
                    jm_result_dic[(i[0],k)]='Right'
                    print('Cursor location_y < Target location_y')
            
                
        print('%.2fmsec,Judge_magnitude ends for entity #%s'%(env.now,(i[0],k)))
     
    elif anim==0:
        #Judge_identity is enabled if receiving entity (i) from Server A or B  
        #if outserver_dic[101] == 1 and outserver_dic[102] == 1:
            
        #At serverF
        # store its attributes
        ji_store_dic[(i[0]),k]=attribute
        #use cpt time (at least, for now, perhaps 150 msec is needed)
        with qn_mhp.serverF.request() as request:
            yield request
            yield env.timeout(cpt)
        if attribute['eye_loc'][0]==attribute['eye_loc'][1]:
            jm_result_dic[(i[0],k)]='T'
            print('Cursor location = Target location')
        elif attribute['eye_loc'][0]<attribute['eye_loc'][1]:
            jm_result_dic[(i[0],k)]='Left'
            print('Cursor location > Target location')
        elif attribute['eye_loc'][0]>attribute['eye_loc'][1]:
            jm_result_dic[(i[0],k)]='Right'
            print('Cursor location < Target location')
                 
        
        print('%.2fmsec,Judge_magnitude ends for entity #%s'%(env.now,(i[0],k)))


def Cal_single_digit_num(qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation):
    if anim== 1:
        #At serverF
        #Upon receiving entity#1 from Server A/B/C/… with attribute “number 1”,
        #Use cpt time,
        #Store entity#1’s “number 1” in related data structure of F;
        #Upon receiving entity#2 from Server A/B/C/… with attribute “number 2”,
        #Use cpt time,
        #Store entity#2’s “number 2” in related data structure of F
        Structure_and_Animation().enter(qn_mhp.serverF, 'F', 'C_F', i, j, k,generation)
        with qn_mhp.serverF.request() as request:
            yield request
            Structure_and_Animation().add('F', i, j, k, generation)
            yield env.timeout(cpt)
            Structure_and_Animation().delete(i, j, k, 'F', generation)
        if i[0]%2!=0:
            cal_sd_num_dic['num1']=attribute['cal_sd_num1']
            Reaction_calsingledig().first_num( cal_sd_num_dic['num1'])
            
        elif i[0]%2==0:
            cal_sd_num_dic['num2']=attribute['cal_sd_num2']
            Reaction_calsingledig().second_num(cal_sd_num_dic['num2'])
            #use cpt time
            # Generate New Entity#F(i) with attribute “Result”,
            #Use cpt time
            #Result = the corresponding arithmetic calculation result for Entity 1 and Entity 2
            #Use cpt time,
            #Store Result in related data structure
            Structure_and_Animation().enter(qn_mhp.serverF, 'F', 'C_F', i, j, k,generation)
            with qn_mhp.serverF.request() as request:
                yield request
                Structure_and_Animation().add('F', i, j, k, generation)
                yield env.timeout(2*cpt)
                Structure_and_Animation().delete(i, j, k, 'F',generation)
            
            if operation=='Add (+)':
                cal_sd_result_dic[i[0]]=cal_sd_num_dic['num1']+cal_sd_num_dic['num2']
                print('Result:',cal_sd_num_dic['num1'],'+',cal_sd_num_dic['num2'],'=',cal_sd_result_dic[i[0]])
            elif operation=='Subtract (-)':
                cal_sd_result_dic[i[0]]=(cal_sd_num_dic['num2']-cal_sd_num_dic['num1'])
                print('Result:',cal_sd_num_dic['num1'],'-',cal_sd_num_dic['num2'],'=',cal_sd_result_dic[i[0]])
            elif operation == 'Multiplication (*)':
                cal_sd_result_dic[i[0]]=(cal_sd_num_dic['num1']*cal_sd_num_dic['num2'])
                print('Result:',cal_sd_num_dic['num1'],'*',cal_sd_num_dic['num2'],'=',cal_sd_result_dic[i[0]])
            elif operation=='Division (/)':
                cal_sd_result_dic[i[0]]=(cal_sd_num_dic['num1']/cal_sd_num_dic['num2'])
                print('Result:',cal_sd_num_dic['num1'],'/',cal_sd_num_dic['num2'],'=',cal_sd_result_dic[i[0]])
            attribute['cal_sd_result']=cal_sd_result_dic[i[0]]   
            print('%.2fmsec, Cal_sigle_digit_num ends for entity #%s'%(env.now,(i[0],i[0]-1,k))) 
            Reaction_calsingledig().result(cal_sd_result_dic[i[0]])
            #Send entity#F1 to Server C
            #At serverC    
            Reaction_calsingledig().delete()
    elif anim==0:
        #At serverF
        #Upon receiving entity#1 from Server A/B/C/… with attribute “number 1”,
        #Use cpt time,
        #Store entity#1’s “number 1” in related data structure of F;
        #Upon receiving entity#2 from Server A/B/C/… with attribute “number 2”,
        #Use cpt time,
        #Store entity#2’s “number 2” in related data structure of F
        with qn_mhp.serverF.request() as request:
            yield request
            yield env.timeout(cpt)
        if i[0]==1:
            cal_sd_num_dic['num1']=attribute['cal_sd_num1']
        elif i[0]==2:
            cal_sd_num_dic['num2']=attribute['cal_sd_num2']
            #use cpt time
            # Generate New Entity#F(i) with attribute “Result”,
            #Use cpt time
            #Result = the corresponding arithmetic calculation result for Entity 1 and Entity 2
            #Use cpt time,
            #Store Result in related data structure
            with qn_mhp.serverF.request() as request:
                yield request
                yield env.timeout(3*cpt)
           
            if operation=='Add (+)':
                cal_sd_result_dic[i[0]]=cal_sd_num_dic['num1']+cal_sd_num_dic['num2']
            elif operation=='Subtract (-)':
                cal_sd_result_dic[i[0]](cal_sd_num_dic['num2']-cal_sd_num_dic['num1'])
            elif operation == 'Multiplication (*)':
                cal_sd_result_dic[i[0]](cal_sd_num_dic['num1']*cal_sd_num_dic['num2'])
            elif operation=='Division (/)':
                cal_sd_result_dic[i[0]](cal_sd_num_dic['num1']/cal_sd_num_dic['num2'])
            attribute['cal_sd_result']=cal_sd_result_dic[i[0]]   
            #Send entity#F1 to Server C
            #At serverC
    


def Press_button(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation):
    if anim==1:
        #Press_button is enabled if receiving entity (i) from Server C  
        if outserver_dic[103] == 1:
            print('%.2fmsec, Press_button operator is enabled by receiving entity #%s'%((i[0],k)))
               
            #At serverW:  
            Structure_and_Animation().enter(qn_mhp.serverW, 'W', 'F_W', i, j, k,generation)
            with qn_mhp.serverW.request() as request:
                yield request
                
                Structure_and_Animation().add('W', i, j, k,generation)
                
                yield env.timeout(mpt)  #use mpt time
                Structure_and_Animation().delete(i, j, k, 'W',generation)
                
            outserver_dic[201] = 1  #Send entity (i) to Server Y 
        
        #At serverY
        #If receiving entity (i) from Server W
        if outserver_dic[201] == 1:
            Structure_and_Animation().enter(qn_mhp.serverY, 'Y', 'W_Y', i, j, k,generation)
            with qn_mhp.serverY.request() as request:                         
                yield request                
                Structure_and_Animation().add('Y', i, j, k,generation)
                yield env.timeout(mpt) #Use mpt time
                Structure_and_Animation().delete(i, j, k, 'Y',generation)
                
            outserver_dic[202] = 1   #Send entity (i) to Server Z 
            
        #At serverZ
        #If receiving entity (i) from Server Y
        if outserver_dic[202] == 1:
            Structure_and_Animation().enter(qn_mhp.serverZ, 'Z', 'Y_Z', i, j, k,generation)
            with qn_mhp.serverZ.request() as request:
                
                yield request
                
                Structure_and_Animation().add('Z', i, j, k,generation)
                
                yield env.timeout(mpt) #Use mpt time
                Structure_and_Animation().delete(i, j, k, 'Z',generation)
                
            outserver_dic[203] = 1  #Send entity (i) to Finger Server  
        
        #At lefthand server
        #If receiving entity (i) from Server Z 
        if outserver_dic[203] == 1:
            Structure_and_Animation().enter(qn_mhp.lefthand, '22', 'Z_22', i, j, k,generation)
            with qn_mhp.lefthand.request() as request:
                
                yield request
                
                Structure_and_Animation().add('22', i, j, k,generation)
                
                yield env.timeout(20) # for now, use a constant, say 20 msec for “finger press physical action” time
                Structure_and_Animation().delete(i, j, k, '22',generation)
            if 'Press_button' in task_info_dic.values():        
                reaction_press_button().add_button(i)

            print('%.2fmsec, Press_button ends for entity #%s'%(env.now,(i[0],k)))
    
    else:
        #Press_button is enabled if receiving entity (i) from Server C  
        if outserver_dic[103] == 1:
            print('%.2fmsec, Press_button operator is enabled by receiving entity #%s'%(env.now,(i[0],k)))
               
            #At serverW:  
            with qn_mhp.serverW.request() as request:
             
                yield request
    
                yield env.timeout(mpt)  #use mpt time
          
            outserver_dic[201] = 1  #Send entity (i) to Server Y 
        
        #At serverY
        #If receiving entity (i) from Server W
        if outserver_dic[201] == 1:
            with qn_mhp.serverY.request() as request:
               
                yield request
             
                yield env.timeout(mpt) #Use mpt time
               
            outserver_dic[202] = 1   #Send entity (i) to Server Z 
            
        #At serverZ
        #If receiving entity (i) from Server Y
        if outserver_dic[202] == 1:
            with qn_mhp.serverZ.request() as request:
                        
                yield request
                yield env.timeout(mpt) #Use mpt time
          
            outserver_dic[203] = 1  #Send entity (i) to Finger Server  
        
        #At lefthand server
        #If receiving entity (i) from Server Z 
        if outserver_dic[203] == 1:
            with qn_mhp.lefthand.request() as request:
                         
                yield request
               
                yield env.timeout(20) # for now, use a constant, say 20 msec for “finger press physical action” time
                           
            print('%.2fmsec, Press_button ends for entity #%s'%(env.now,(i[0],k)))
        
    
def Look_at(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation):
    global communication_signal,neweyefixation
    
    if anim==1:
        #Look_At is enabled if receiving entity (i) from Server C(or any entity from CogNet, in general)
        #if outserver_dic[103] == 1:
        #print('%.2fmsec, Look_at operator is enabled by receiving entity #%s'%(env.now,(i,j,k)))
        yield env.timeout(0)
        print('%.2fmsec, Look_at operator is enabled by receiving entity #%s'%(env.now,(i[0],k)))  
        #At serverW: 
        Structure_and_Animation().enter(qn_mhp.serverW, 'W', 'C_W', i, j, k,generation)
        with qn_mhp.serverW.request() as request:           
            yield request           
            Structure_and_Animation().add('W', i, j, k, generation)         
            yield env.timeout(mpt)  #use mpt time           
        Structure_and_Animation().delete( i, j, k,'W',generation)      
        outserver_dic[201] = 1  #Send entity (i) to Server Y 
    
    #At serverY
    #If receiving entity (i) from Server W
    #At serverY
    #If receiving entity (i) from Server W
        if outserver_dic[201] == 1:
            Structure_and_Animation().enter(qn_mhp.serverY, 'Y', 'W_Y', i, j, k,generation)
            with qn_mhp.serverY.request() as request:              
                yield request              
                Structure_and_Animation().add('Y', i, j, k, generation)            
                yield env.timeout(mpt) #Use mpt time               
            Structure_and_Animation().delete( i, j, k,'Y',generation)          
            outserver_dic[202] = 1   #Send entity (i) to Server Z 
        
        if outserver_dic[202] == 1:
            Structure_and_Animation().enter(qn_mhp.serverZ, 'Z', 'Y_Z', i, j, k,generation)
            with qn_mhp.serverZ.request() as request:               
                yield request                
                Structure_and_Animation().add('Z', i, j, k, generation)               
                yield env.timeout(mpt) #Use mpt time                
            Structure_and_Animation().delete( i, j, k,'Z',generation)           
            outserver_dic[203] = 1  #Send entity (i) to Eye Server        
        
        #At Eye server
        #If receiving entity (i) from Server Z 
        if outserver_dic[203] == 1:
            #yield time
            # can use Normal Distribution (mean=30 msec, sd=10 msec)or 20, 30, 40 msec for short, medium, or long saccades)
            Structure_and_Animation().enter(qn_mhp.eyes, '23', 'Z_23', i, j, k,generation)
            with qn_mhp.eyes.request() as request:
                yield request                
                Structure_and_Animation().add('23', i, j, k, generation)              
                yield env.timeout(np.random.normal(30,10))                 
            Structure_and_Animation().delete(i, j, k, '23',generation)
                
            #Recording/updating new eye fixation location/direction   
    
            neweyefixation = attribute['eye_loc']  #set by programmer for now
            eyefixation_dic[(i[0],k)] = neweyefixation    
            #send a “communications signal,” Note: this signal is not an internal QN entity”to device/environment       
            communication_signal = 1
            print('%.2fmsec, Look_at ends for entity #%s'%(env.now,(i[0],k)))         

    else:
        #Look_At is enabled if receiving entity (i) from Server C(or any entity from CogNet, in general)
        print('%.2fmsec, Look_at operator is enabled by receiving entity #%s'%(env.now,(i[0],k)))  
        #At serverW:  
        with qn_mhp.serverW.request() as request:
        
            yield request
        
            yield env.timeout(mpt)  #use mpt time
   
        outserver_dic[201] = 1  #Send entity (i) to Server Y 
        
        #At serverY
        #If receiving entity (i) from Server W
        #At serverY
        #If receiving entity (i) from Server W
        if outserver_dic[201] == 1:
            with qn_mhp.serverY.request() as request:
             
                yield request
                
                yield env.timeout(mpt) #Use mpt time
     
            outserver_dic[202] = 1   #Send entity (i) to Server Z 
        
        if outserver_dic[202] == 1:
            with qn_mhp.serverZ.request() as request:
    
                
                yield request
                yield env.timeout(mpt) #Use mpt time
     
            outserver_dic[203] = 1  #Send entity (i) to Eye Server        
             
        #At Eye server
        #If receiving entity (i) from Server Z 
        if outserver_dic[203] == 1:
            #yield time
            # can use Normal Distribution (mean=30 msec, sd=10 msec)or 20, 30, 40 msec for short, medium, or long saccades)
            with qn_mhp.eyes.request() as request:               
                yield request    
                yield env.timeout(np.random.normal(30,10)) 
              
            #Recording/updating new eye fixation location/direction   
    
            neweyefixation = attribute['eye_loc']  #set by programmer for now
            eyefixation_dic[(i[0],k)] = neweyefixation    
            #send a “communications signal,” Note: this signal is not an internal QN entity”to device/environment       
            communication_signal = 1
            print('%.2fmsec, Look_at ends for entity #%s'%(env.now,(i[0],k)))   
            

def look_for(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,count,generation):
    #entity information
    entity_info[(i[0],k)]=[]
    if attribute['stimuli']==0:
        entity_info[(i[0],k)].append('noise')
    else:
        for item in attribute.keys() :
            if item=='stimuli' or item=='type' or item=='info':
                entity_info[(i[0],k)].append(attribute_dic[attribute[item]])
            else:
                entity_info[(i[0],k)].append(attribute[item])
    if count>n_look_for_ls:
        print('Target not found')
        env.process(look_for(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, count,generation)).interrupt()

    else:
        if attribute['stimuli']==1:
                       
            yield env.process(Look_at(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))
            yield env.process(See(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))
            yield env.process(Judge_identity(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))
            yield env.process(Store_to_WM(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))
            print(count,'item(s) have already be seen so far')
            if ji_result_dic[(i[0],k)]=='F':
                
                i[0]+=1    
                #update arival time
                arrival_time = env.now
                attribute = {'stimuli':1,'type':2,'info':6}         
                if len(look_for_ls)>1:
                    item=randint(1,len(look_for_ls)-1)
                elif len(look_for_ls)==1:
                    item=0
                attribute['eye_loc']=look_for_ls[item][0]
                attribute['color']=look_for_ls[item][2]
                attribute['text']=look_for_ls[item][1]  
               
                if len(look_for_ls)==0:
                    attribute['eye_loc']=-999
                    attribute['color']=-999
                    attribute['text']=-999  

                i[1]=attribute
                if attribute['stimuli']==1 and len(look_for_ls)!=0:
                    del look_for_ls[item]
                    count+=1
                if anim==1:
                    Structure_and_Animation().show(i, j, k, '0',generation)
                env.process(look_for(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, count,generation))
            
            elif ji_result_dic[(i[0],k)]=='T':
                print('entity found',(attribute['eye_loc'],attribute['text'],attribute['color']))
                env.process(look_for(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, count,generation)).interrupt('entity is already found')   
            '''
            print('sojourn time for entity%s: %.2fmsec'%((i[0],k,generation),env.now-arrival_time))  
            
            sojourn_time_dic[(i[0],k,generation)]='%.2fmsec'%(env.now-arrival_time)
            rt_dic[k].append (env.now - arrival_time)
    
            rt_mean_dic[k].append(np.mean(rt_dic[k]))
            rt_var_dic[k].append(np.std(rt_dic[k]))


            '''

def Count(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation):
    
    trial=i[0]
    Reaction_count().trial(trial)
   
            
    if anim==1:
        if outserver_dic[4] !=0 or outserver_dic[8]!=0:
            print('%.2fmsec, Count operator is enabled by receiving entity #%s'%(env.now,(i[0],k)),'\n','Start number:',\
                  attribute['Start'],'End number:',attribute['End'])
        
            count_num_dic['start_num']=attribute['Start']
            count_num_dic['end_num']=attribute['End']
            
            for item in range(count_num_dic['start_num'],count_num_dic['end_num']+1):
                Structure_and_Animation().enter(qn_mhp.serverF, 'F', 'C_F', i,j,k,generation)
                with qn_mhp.serverF.request() as request:
                    yield request
                    Structure_and_Animation().add('F', i,j,k, generation)
                    yield env.timeout(cpt)
                    Structure_and_Animation().delete(i,j,k, 'F', generation)
                    print('%.2fmsec'%(env.now),'current number is ',item)
                    Reaction_count().count_num(item)
                #Send entity#F(i) to Server C:
                Structure_and_Animation().enter(qn_mhp.serverC, 'C', 'F_C', i,j,k,generation)
                with qn_mhp.serverC.request() as request:
                    yield request
                    Structure_and_Animation().add('C', i,j,k, generation)
                    yield env.timeout(cpt)
                    current_num=item+1
                    Structure_and_Animation().delete(i,j,k, 'C', generation)                                   
                    
                if current_num>count_num_dic['end_num']:
                    break
                    print('%.2fmsec, Count ends for entity #%s'%(env.now,i[0]))
                    Reaction_count().delete()
    elif anim==0:
  
        #At serverF
        if outserver_dic[4] !=0 or outserver_dic[8]!=0:
            print('%.2fmsec, Count operator is enabled by receiving entity #%s'%(env.now,i[0]),'\n',\
                  attribute['Start'],'End number:',attribute['End'])
            count_num_dic['start_num']=attribute['Start']
            count_num_dic['end_num']=attribute['End']
            for item in range(count_num_dic['start_num'],count_num_dic['end_num']+1):
                with qn_mhp.serverF.request() as request:
                    yield request
                    yield env.timeout(cpt)
                    print('%.2fmsec'%(env.now),'current number is ',item)
    
                #Send entity#F(i) to Server C:                
                with qn_mhp.serverC.request() as request:
                    yield request
                    yield env.timeout(cpt)
                    current_num=item+1
                
                if current_num>count_num_dic['end_num']:
                    break
                    print('%.2fmsec, Count ends for entity #%s'%(env.now,i[0]))
    Reaction_count().delete()


def Tracking_1D(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation):
    #entity information
    
    entity_info[(i[0],k)]=[]
    if attribute['stimuli']==0:
        entity_info[(i[0],k)].append('noise')
    else:

        for item in attribute.keys() :
            if item=='stimuli' or item=='type' or item=='info':
                entity_info[(i[0],k)].append(attribute_dic[attribute[item]])
            else:
                entity_info[(i[0],k)].append(attribute[item])

    if attribute['stimuli']==1:
        re_count=0
        #calculate the square error at the start
        square_error=(Reaction_track1D().user-Reaction_track1D().target)**2
        rmse_list.append(square_error)
        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
        rmse_var_dic[re_count]=np.std(rmse_list)
        
        while env.now<SIMTIME:
            #Look at and see for cursor        
            yield env.process(Look_at(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))
            print('eye is on cursor: ',(attribute['eye_loc'][1],0))
            yield env.process(See(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
            
            #Look at and see for target
            position=Reaction_track1D().frame.canvas.coords(Reaction_track1D().t)
            attribute['eye_loc'][0]=(env.now-start_time)/track1D_freq_dic[track1D_freq]*track1D_amp_dic[track1D_amp]*100/Reaction_track1D().w*5/3
            yield env.process(Look_at(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))                     
            print('eye is on target: ',(attribute['eye_loc'][0],0))
            yield env.process(See(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
            
            #Judge magnitude
            yield env.process(Judge_magnitude(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation,'x'))
            
            
            #Mouse click                      
            if track1D_response=='Click mouse':
                
                #if track1D_amp=='Small' and track1D_freq=='Slow':
                #Fitt's Law for clicking
                a=1
                b=2
                W=2*Reaction_track1D().r
                cursor=attribute['eye_loc'][1]/100*Reaction_track1D().w/5*3
                target=attribute['eye_loc'][0]/100*Reaction_track1D().w/5*3
                A=abs(cursor-target)
                MT=a+b*math.log2(2*A/W)
                yield env.timeout(MT) 
                
                #show cursor after clicking 
                Reaction_track1D().user_click(position[0]+Reaction_track1D().r)
                #update cursor position
                attribute['eye_loc'][1]=position[0]*100*5/Reaction_track1D().w/3
                
                #update the postion of the target
                target_new=position=Reaction_track1D().frame.canvas.coords(Reaction_track1D().t)[0]
                
                #Calculate error                
                square_error=(target_new-target)**2
                
                re_count+=1
                
                #Calculate RMSE
                rmse_list.append(square_error)
                rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                rmse_var_dic[re_count]=np.std(rmse_list)
                            
            if track1D_response=='Press keyboard':
                step=5 #real world
                
                cursor=attribute['eye_loc'][1]/100*Reaction_track1D().w/5*3
                target=attribute['eye_loc'][0]/100*Reaction_track1D().w/5*3
                
                while True:
                    while cursor>=target:
                        yield env.process(Press_button(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
                        
                        #update cursor postion:
                        cursor=cursor-step
                        #show cursor
                        Reaction_track1D().user_click(cursor)
                        
                        #update target position
                        target=Reaction_track1D().frame.canvas.coords(Reaction_track1D().t)[0]
                        
                        re_count+=1
                        
                        #square error
                        square_error=(cursor-target)**2
                        #calculate RMSE
                        rmse_list.append(square_error)
                        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                        rmse_var_dic[re_count]=np.std(rmse_list)
                     
                    while cursor<target:
                        yield env.process(Press_button(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
                        
                        #update cursor postion:
                        cursor=cursor+step
                        #show cursor
                        Reaction_track1D().user_click(cursor)
                        
                        #update target position
                        target=Reaction_track1D().frame.canvas.coords(Reaction_track1D().t)[0]
                        
                        re_count+=1
                        
                        #square error
                        square_error=(cursor-target)**2
                        #calculate RMSE
                        rmse_list.append(square_error)
                        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                        rmse_var_dic[re_count]=np.std(rmse_list)
                
def Tracking_2D(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation):
    #entity information
    
    entity_info[(i[0],k)]=[]
    if attribute['stimuli']==0:
        entity_info[(i[0],k)].append('noise')
    else:

        for item in attribute.keys() :
            if item=='stimuli' or item=='type' or item=='info':
                entity_info[(i[0],k)].append(attribute_dic[attribute[item]])
            else:
                entity_info[(i[0],k)].append(attribute[item])

    if attribute['stimuli']==1:
        re_count=0
        #calculate the square error at the start
        square_error=(Reaction_track2D().target_x-Reaction_track2D().cursor_x)**2+\
            (Reaction_track2D().target_y-Reaction_track2D().cursor_y)**2
        rmse_list.append(square_error)
        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
        rmse_var_dic[re_count]=np.std(rmse_list)
        
        while env.now<SIMTIME:
            #Look at and see for cursor        
            yield env.process(Look_at(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))
            print('eye is on cursor: ',(attribute['eye_loc'][2],attribute['eye_loc'][3]))
            yield env.process(See(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
            
            #Look at and see for target
            position=Reaction_track2D().frame.canvas.coords(Reaction_track2D().target)
            attribute['eye_loc'][0]=(position[0]+Reaction_track2D().r-Reaction_track2D().origin_x)/Reaction_track2D().length*100
            attribute['eye_loc'][1]=(Reaction_track2D().origin_y-(position[1]+Reaction_track2D().r))/Reaction_track2D().length*100

            yield env.process(Look_at(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))                     
            print('eye is on target: ',(attribute['eye_loc'][0],attribute['eye_loc'][1]))
            yield env.process(See(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
            
            #Judge magnitude
            yield env.process(Judge_magnitude(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation,'x'))
            yield env.process(Judge_magnitude(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation,'y'))
            
            
            #Mouse click                      
            if track2D_response=='Click mouse':
                
                #if track1D_amp=='Small' and track1D_freq=='Slow':
                #Fitt's Law for clicking
                a=1
                b=2
                W=2*Reaction_track2D().r
                cursor_x=attribute['eye_loc'][2]/100*Reaction_track2D().length
                target_x=attribute['eye_loc'][0]/100*Reaction_track2D().length
                cursor_y=attribute['eye_loc'][3]/100*Reaction_track2D().length
                target_y=attribute['eye_loc'][1]/100*Reaction_track2D().length
                
                print(attribute['eye_loc'][0],attribute['eye_loc'][1])
                A=((cursor_x-target_x)**2+(cursor_y-target_y)**2)**0.5
                MT=a+b*math.log2(2*A/W)
                if MT>=0:
                    yield env.timeout(MT) 
                else:
                    yield env.timeout(0)
                
                #show cursor after clicking 
                Reaction_track2D().user_click(position[0],position[1])
                #update cursor position
                attribute['eye_loc'][2]=target_x*100/Reaction_track2D().length       
                attribute['eye_loc'][3]=target_y*100/Reaction_track2D().length 
                
                #update the postion of the target
                position_new=Reaction_track2D().frame.canvas.coords(Reaction_track2D().target)
                attribute['eye_loc'][0]=(position[0]+Reaction_track2D().r-Reaction_track2D().origin_x)/Reaction_track2D().length*100
                attribute['eye_loc'][1]=(Reaction_track2D().origin_y-(position[1]+Reaction_track2D().r))/Reaction_track2D().length*100
                '''
                for item in direction_track2D:
                    if item==1:
                        target_new_x=target_x+1*track2D_amp_dic[track2D_amp]
                        attribute['eye_loc'][0]+=1*track2D_amp_dic[track2D_amp]/Reaction_track2D().length*100
                    elif item==-1:
                        target_new_x=target_x-1*track2D_amp_dic[track2D_amp]
                        attribute['eye_loc'][0]-=1*track2D_amp_dic[track2D_amp]/Reaction_track2D().length*100
                    elif item==2:
                        target_new_y=target_y+1*track2D_amp_dic[track2D_amp]
                        attribute['eye_loc'][1]-=1*track2D_amp_dic[track2D_amp]/Reaction_track2D().length*100
                    elif item==-2:
                        target_new_y=target_y-1*track2D_amp_dic[track2D_amp]
                        attribute['eye_loc'][1]+=1*track2D_amp_dic[track2D_amp]/Reaction_track2D().length*100
                direction_track2D.clear()
                '''
                #Calculate error                
                square_error=(position_new[0]-position[0])**2+(position_new[1]-position[1])**2
                
                re_count+=1
                
                #Calculate RMSE
                rmse_list.append(square_error)
                rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                rmse_var_dic[re_count]=np.std(rmse_list)
                            
            if track2D_response=='Press keyboard':
                step=5 #real world
                
                cursor_x=attribute['eye_loc'][2]/100*Reaction_track2D().length+Reaction_track2D().origin_x
                cursor_y=Reaction_track2D().origin_y-attribute['eye_loc'][3]/100*Reaction_track2D().length
                target_x=position[0]+Reaction_track2D().r
                target_y=position[1]+Reaction_track2D().r
                
                while True:
                    while cursor_x>=target_x:
                        yield env.process(Press_button(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
                        
                        #update cursor postion:
                        cursor_x=cursor_x-step
                        #show cursor
                        Reaction_track2D().user_click(cursor_x-Reaction_track2D().r,cursor_y-Reaction_track2D().r)
                        
                        #update target position
                        position=Reaction_track2D().frame.canvas.coords(Reaction_track2D().target)
                        target_x=position[0]+Reaction_track2D().r
                        target_y=position[1]+Reaction_track2D().r
                        
                        re_count+=1
                        
                        #square error
                        square_error=(cursor_x-target_x)**2+(cursor_y-target_y)**2
                        #calculate RMSE
                        rmse_list.append(square_error)
                        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                        rmse_var_dic[re_count]=np.std(rmse_list)
                        
                        
                        
                    while cursor_x<target_x:
                        yield env.process(Press_button(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
                        
                        #update cursor postion:
                        cursor_x=cursor_x+step
                        #show cursor
                        Reaction_track2D().user_click(cursor_x-Reaction_track2D().r,cursor_y-Reaction_track2D().r)
                        
                        #update target position
                        position=Reaction_track2D().frame.canvas.coords(Reaction_track2D().target)
                        target_x=position[0]+Reaction_track2D().r
                        target_y=position[1]+Reaction_track2D().r
                        
                        re_count+=1
                        
                        #square error
                        square_error=(cursor_x-target_x)**2+(cursor_y-target_y)**2
                        #calculate RMSE
                        rmse_list.append(square_error)
                        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                        rmse_var_dic[re_count]=np.std(rmse_list)
                    
                    while cursor_y>=target_y:
                        yield env.process(Press_button(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
                        
                        #update cursor postion:
                        cursor_y=cursor_y-step
                        #show cursor
                        Reaction_track2D().user_click(cursor_x-Reaction_track2D().r,cursor_y-Reaction_track2D().r)
                        
                        #update target position
                        position=Reaction_track2D().frame.canvas.coords(Reaction_track2D().target)
                        target_x=position[0]+Reaction_track2D().r
                        target_y=position[1]+Reaction_track2D().r
                        
                        re_count+=1
                        
                        #square error
                        square_error=(cursor_x-target_x)**2+(cursor_y-target_y)**2
                        #calculate RMSE
                        rmse_list.append(square_error)
                        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                        rmse_var_dic[re_count]=np.std(rmse_list)
                        
                    while cursor_y<target_y:
                        yield env.process(Press_button(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
                        
                        #update cursor postion:
                        cursor_y=cursor_y+step
                        #show cursor
                        Reaction_track2D().user_click(cursor_x-Reaction_track2D().r,cursor_y-Reaction_track2D().r)
                        
                        #update target position
                        position=Reaction_track2D().frame.canvas.coords(Reaction_track2D().target)
                        target_x=position[0]+Reaction_track2D().r
                        target_y=position[1]+Reaction_track2D().r
                        
                        re_count+=1
                        
                        #square error
                        square_error=(cursor_x-target_x)**2+(cursor_y-target_y)**2
                        #calculate RMSE
                        rmse_list.append(square_error)
                        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                        rmse_var_dic[re_count]=np.std(rmse_list)

def Static_2DTracing(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation):
    entity_info[(i[0],k)]=[]
    if attribute['stimuli']==0:
        entity_info[(i[0],k)].append('noise')
    else:

        for item in attribute.keys() :
            if item=='stimuli' or item=='type' or item=='info':
                entity_info[(i[0],k)].append(attribute_dic[attribute[item]])
            else:
                entity_info[(i[0],k)].append(attribute[item])

    if attribute['stimuli']==1:
        re_count=0
        #calculate the square error at the start
        position0_target=Reaction_static_2DTracing().frame.canvas.coords(Reaction_static_2DTracing().target)
        position0_cursor=Reaction_static_2DTracing().frame.canvas.coords(Reaction_static_2DTracing().cursor)        
        square_error=(position0_cursor[0]-position0_target[0])**2+\
            (position0_cursor[1]-position0_target[1])**2
        rmse_list.append(square_error)
        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
        rmse_var_dic[re_count]=np.std(rmse_list)
        
        while env.now<SIMTIME:
            #Look at and see for cursor 
            position_cursor=Reaction_static_2DTracing().frame.canvas.coords(Reaction_static_2DTracing().cursor)
            yield env.process(Look_at(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))
            print('eye is on cursor: ',(attribute['eye_loc'][2],attribute['eye_loc'][3]))
            yield env.process(See(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
            
            #Look at and see for target
            position=Reaction_static_2DTracing().frame.canvas.coords(Reaction_static_2DTracing().target)
            attribute['eye_loc'][0]=(position[0]+Reaction_static_2DTracing().r-Reaction_static_2DTracing().x0)/Reaction_static_2DTracing().w1
            attribute['eye_loc'][1]=(Reaction_static_2DTracing().y0-(position[1]+Reaction_static_2DTracing().r))/Reaction_static_2DTracing().w2

            yield env.process(Look_at(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))                     
            print('eye is on target: ',(attribute['eye_loc'][0],attribute['eye_loc'][1]))
            yield env.process(See(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
            
            #Judge magnitude
            yield env.process(Judge_magnitude(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation,'x'))
            yield env.process(Judge_magnitude(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation,'y'))
            
            
            #Mouse click                      
            if static2D_response=='Click mouse':
                
                #if track1D_amp=='Small' and track1D_freq=='Slow':
                #Fitt's Law for clicking
                a=1
                b=2
                W=2*Reaction_static_2DTracing().r
                cursor_x=position_cursor[0]
                target_x=position[0]
                cursor_y=position_cursor[1]
                target_y=position[1]
                
                print(attribute['eye_loc'][0],attribute['eye_loc'][1])
                A=((cursor_x-target_x)**2+(cursor_y-target_y)**2)**0.5
                MT=a+b*math.log2(2*A/W)
                yield env.timeout(MT) 
                
                #show cursor after clicking 
                Reaction_static_2DTracing().user_click(position[0],position[1])
                #update cursor position
                attribute['eye_loc'][2]=attribute['eye_loc'][0]
                attribute['eye_loc'][3]=attribute['eye_loc'][1]
                
                #update the postion of the target
                position_new=Reaction_static_2DTracing().frame.canvas.coords(Reaction_static_2DTracing().target)
               
                #Calculate error                
                square_error=(position_new[0]-position[0])**2+(position_new[1]-position[1])**2
                
                re_count+=1
                
                #Calculate RMSE
                rmse_list.append(square_error)
                rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                rmse_var_dic[re_count]=np.std(rmse_list)
                            
            elif static2D_response=='Press keyboard':
                step=5 #real world
                
                position_cursor=Reaction_static_2DTracing().frame.canvas.coords(Reaction_static_2DTracing().cursor)
                cursor_x=position_cursor[0]-Reaction_static_2DTracing().r
                cursor_y=position_cursor[1]-Reaction_static_2DTracing().r
                target_x=position[0]-Reaction_static_2DTracing().r
                target_y=position[1]-Reaction_static_2DTracing().r
                
                while True:
                    while cursor_x>=target_x:
                        yield env.process(Press_button(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
                        
                        #update cursor postion:
                        cursor_x=cursor_x-step
                        #show cursor
                        Reaction_static_2DTracing().user_click(cursor_x,cursor_y)
                        
                        #update target position
                        position=Reaction_static_2DTracing().frame.canvas.coords(Reaction_static_2DTracing().target)
                        target_x=position[0]-Reaction_static_2DTracing().r
                        target_y=position[1]-Reaction_static_2DTracing().r
                        
                        re_count+=1
                        
                        #square error
                        square_error=(cursor_x-target_x)**2+(cursor_y-target_y)**2
                        #calculate RMSE
                        rmse_list.append(square_error)
                        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                        rmse_var_dic[re_count]=np.std(rmse_list)
                        
                        
                        
                    while cursor_x<target_x:
                        yield env.process(Press_button(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
                        
                        #update cursor postion:
                        cursor_x=cursor_x+step
                        #show cursor
                        Reaction_static_2DTracing().user_click(cursor_x,cursor_y)
                        
                        #update target position
                        position=Reaction_static_2DTracing().frame.canvas.coords(Reaction_static_2DTracing().target)
                        target_x=position[0]+Reaction_static_2DTracing().r
                        target_y=position[1]+Reaction_static_2DTracing().r
                        
                        re_count+=1
                        
                        #square error
                        square_error=(cursor_x-target_x)**2+(cursor_y-target_y)**2
                        #calculate RMSE
                        rmse_list.append(square_error)
                        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                        rmse_var_dic[re_count]=np.std(rmse_list)
                    
                    while cursor_y>=target_y:
                        yield env.process(Press_button(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
                        
                        #update cursor postion:
                        cursor_y=cursor_y-step
                        #show cursor
                        Reaction_static_2DTracing().user_click(cursor_x,cursor_y)
                        
                        #update target position
                        position=Reaction_track2D().frame.canvas.coords(Reaction_static_2DTracing().target)
                        target_x=position[0]-Reaction_static_2DTracing().r
                        target_y=position[1]-Reaction_static_2DTracing().r
                        
                        re_count+=1
                        
                        #square error
                        square_error=(cursor_x-target_x)**2+(cursor_y-target_y)**2
                        #calculate RMSE
                        rmse_list.append(square_error)
                        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                        rmse_var_dic[re_count]=np.std(rmse_list)
                        
                    while cursor_y<target_y:
                        yield env.process(Press_button(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
                        
                        #update cursor postion:
                        cursor_y=cursor_y+step
                        #show cursor
                        Reaction_static_2DTracing().user_click(cursor_x,cursor_y)
                        
                        #update target position
                        position=Reaction_static_2DTracing().frame.canvas.coords(Reaction_static_2DTracing().target)
                        target_x=position[0]-Reaction_static_2DTracing().r
                        target_y=position[1]-Reaction_static_2DTracing().r
                        
                        re_count+=1
                        
                        #square error
                        square_error=(cursor_x-target_x)**2+(cursor_y-target_y)**2
                        #calculate RMSE
                        rmse_list.append(square_error)
                        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                        rmse_var_dic[re_count]=np.std(rmse_list)

def Dynamic_1D(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation):
    #entity information
    
    entity_info[(i[0],k)]=[]
    if attribute['stimuli']==0:
        entity_info[(i[0],k)].append('noise')
    else:

        for item in attribute.keys() :
            if item=='stimuli' or item=='type' or item=='info':
                entity_info[(i[0],k)].append(attribute_dic[attribute[item]])
            else:
                entity_info[(i[0],k)].append(attribute[item])

    if attribute['stimuli']==1:
        re_count=0
        #calculate the square error at the start
        square_error=(Reaction_dynamic1D().user-Reaction_dynamic1D().target)**2
        rmse_list.append(square_error)
        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
        rmse_var_dic[re_count]=np.std(rmse_list)
        
        while env.now<SIMTIME:
            #Look at and see for cursor        
            yield env.process(Look_at(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))
            print('eye is on cursor: ',(attribute['eye_loc'][1],0))
            yield env.process(See(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))    
            #Look at and see for target
            attribute['eye_loc'][0]=(env.now-start_time)/dynamic1D_freq_dic[dynamic1D_freq]*track1D_amp_dic[dynamic1D_amp]*100/Reaction_dynamic1D().length
            yield env.process(Look_at(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))                     
            print('eye is on target: ',(attribute['eye_loc'][0],0))
            yield env.process(See(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
            target=Reaction_dynamic1D().frame.canvas.coords(Reaction_dynamic1D().target)
            #Judge magnitude
            yield env.process(Judge_magnitude(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation,'x'))
            
           
            #Mouse click                      
            if dynamic1D_response=='Click mouse':
                
                #if track1D_amp=='Small' and track1D_freq=='Slow':
                #Fitt's Law for clicking
                a=1
                b=2
                W=2*Reaction_dynamic1D().r
                cursor=Reaction_dynamic1D().frame.canvas.coords(Reaction_dynamic1D().user)[0]
                A=abs(cursor-target[0])
                MT=a+b*math.log2(2*A/W)
                yield env.timeout(MT) 
                
                #show cursor after clicking 
                Reaction_dynamic1D().user_click(target)
                #update cursor position
                attribute['eye_loc'][1]=target[0]*100*Reaction_dynamic1D().length+Reaction_dynamic1D().target
                
                #update the postion of the target
                target_new=Reaction_dynamic1D().frame.canvas.coords(Reaction_dynamic1D().target)[0]
                
                #Calculate error                
                square_error=(target_new-target[0])**2
                
                re_count+=1
                
                #Calculate RMSE
                rmse_list.append(square_error)
                rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                rmse_var_dic[re_count]=np.std(rmse_list)
                            
            if dynamic1D_response=='Press keyboard':
                step=5 #real world
                
                cursor=attribute['eye_loc'][1]/100*Reaction_dynamic1D().length
                target=attribute['eye_loc'][0]/100*Reaction_dynamic1D().length
                
                while cursor>=target:
                    yield env.process(Press_button(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
                    
                    #update cursor postion:
                    cursor=cursor-step
                    #show cursor
                    Reaction_dynamic1D().user_click(Reaction_dynamic1D().target+cursor)
                    
                    #update target position
                    target=(env.now-start_time)/dynamic1D_freq_dic[dynamic1D_freq]*dynamic1D_amp_dic[dynamic1D_amp]
                    
                    re_count+=1
                    
                    #square error
                    square_error=(cursor-target)**2
                    #calculate RMSE
                    rmse_list.append(square_error)
                    rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                    rmse_var_dic[re_count]=np.std(rmse_list)
                    
                  
                while cursor<target:
                    yield env.process(Press_button(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
                    
                    #update cursor postion:
                    cursor=cursor+step
                    #show cursor
                    Reaction_dynamic1D().user_click(Reaction_dynamic1D().target+cursor)
                    
                    #update target position
                    target=(env.now-start_time)/dynamic1D_freq_dic[dynamic1D_freq]*dynamic1D_amp_dic[dynamic1D_amp]
                    
                    re_count+=1
                    
                    #square error
                    square_error=(cursor-target)**2
                    #calculate RMSE
                    rmse_list.append(square_error)
                    rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                    rmse_var_dic[re_count]=np.std(rmse_list)    
            
            for t in range(18,0,-1):
                if Reaction_dynamic1D().frame.canvas.coords(Reaction_dynamic1D().target)[0]>=5000*t/10/2:
                    Reaction_dynamic1D().scroll(t/10/2)
                    break
            '''
            elif Reaction_dynamic1D().frame.canvas.coords(Reaction_dynamic1D().target)[0]>=2500:
                Reaction_dynamic1D().scroll(0.5)
                
            elif Reaction_dynamic1D().frame.canvas.coords(Reaction_dynamic1D().target)[0]>=1500:
                Reaction_dynamic1D().scroll(0.3)            
            elif Reaction_dynamic1D().frame.canvas.coords(Reaction_dynamic1D().target)[0]>=1000:
                Reaction_dynamic1D().scroll(0.2)
            elif Reaction_dynamic1D().frame.canvas.coords(Reaction_dynamic1D().target)[0]>=500:
                Reaction_dynamic1D().scroll(0.1)
            '''   

def Dynamic_2D(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation):
    #entity information
    
    entity_info[(i[0],k)]=[]
    if attribute['stimuli']==0:
        entity_info[(i[0],k)].append('noise')
    else:

        for item in attribute.keys() :
            if item=='stimuli' or item=='type' or item=='info':
                entity_info[(i[0],k)].append(attribute_dic[attribute[item]])
            else:
                entity_info[(i[0],k)].append(attribute[item])

    if attribute['stimuli']==1:
        re_count=0
        #calculate the square error at the start
        position0_target=Reaction_dynamic2D().frame.canvas.coords(Reaction_dynamic2D().target)
        position0_cursor=Reaction_dynamic2D().frame.canvas.coords(Reaction_dynamic2D().cursor)        
        square_error=(position0_cursor[0]-position0_target[0])**2+\
            (position0_cursor[1]-position0_target[1])**2
        rmse_list.append(square_error)
        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
        rmse_var_dic[re_count]=np.std(rmse_list)
        
        while env.now<SIMTIME:
            #Look at and see for cursor 
            position_cursor=Reaction_dynamic2D().frame.canvas.coords(Reaction_dynamic2D().cursor)
            yield env.process(Look_at(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))
            print('eye is on cursor: ',(attribute['eye_loc'][2],attribute['eye_loc'][3]))
            yield env.process(See(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
            
            #Look at and see for target
            position=Reaction_dynamic2D().frame.canvas.coords(Reaction_dynamic2D().target)
            attribute['eye_loc'][0]=(position[0]+Reaction_dynamic2D().r-Reaction_dynamic2D().x0)/Reaction_dynamic2D().w1
            attribute['eye_loc'][1]=(Reaction_dynamic2D().y0-(position[1]+Reaction_dynamic2D().r))/Reaction_dynamic2D().w2

            yield env.process(Look_at(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation))                     
            print('eye is on target: ',(attribute['eye_loc'][0],attribute['eye_loc'][1]))
            yield env.process(See(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
            
            #Judge magnitude
            yield env.process(Judge_magnitude(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation,'x'))
            yield env.process(Judge_magnitude(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation,'y'))
            
            
            #Mouse click                      
            if dynamic2D_response=='Click mouse':
                
                #if track1D_amp=='Small' and track1D_freq=='Slow':
                #Fitt's Law for clicking
                a=1
                b=2
                W=2*Reaction_dynamic2D().r
                cursor_x=position_cursor[0]
                target_x=position[0]
                cursor_y=position_cursor[1]
                target_y=position[1]
                
                print(attribute['eye_loc'][0],attribute['eye_loc'][1])
                A=((cursor_x-target_x)**2+(cursor_y-target_y)**2)**0.5
                MT=a+b*math.log2(2*A/W)
                yield env.timeout(MT) 
                
                #show cursor after clicking 
                Reaction_dynamic2D().user_click(position[0],position[1])
                #update cursor position
                attribute['eye_loc'][2]=attribute['eye_loc'][0]
                attribute['eye_loc'][3]=attribute['eye_loc'][1]
                
                #update the postion of the target
                position_new=Reaction_dynamic2D().frame.canvas.coords(Reaction_dynamic2D().target)
               
                #Calculate error                
                square_error=(position_new[0]-position[0])**2+(position_new[1]-position[1])**2
                
                re_count+=1
                
                #Calculate RMSE
                rmse_list.append(square_error)
                rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                rmse_var_dic[re_count]=np.std(rmse_list)
                            
            elif dynamic2D_response=='Press keyboard':
                step=5 #real world
                
                position_cursor=Reaction_dynamic2D().frame.canvas.coords(Reaction_dynamic2D().cursor)
                cursor_x=position_cursor[0]-Reaction_dynamic2D().r
                cursor_y=position_cursor[1]-Reaction_dynamic2D().r
                target_x=position[0]-Reaction_dynamic2D().r
                target_y=position[1]-Reaction_dynamic2D().r
                
                while True:
                    while cursor_x>=target_x:
                        yield env.process(Press_button(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
                        
                        #update cursor postion:
                        cursor_x=cursor_x-step
                        #show cursor
                        Reaction_dynamic2D().user_click(cursor_x,cursor_y)
                        
                        #update target position
                        position=Reaction_dynamic2D().frame.canvas.coords(Reaction_dynamic2D().target)
                        target_x=position[0]-Reaction_dynamic2D().r
                        target_y=position[1]-Reaction_dynamic2D().r
                        
                        re_count+=1
                        
                        #square error
                        square_error=(cursor_x-target_x)**2+(cursor_y-target_y)**2
                        #calculate RMSE
                        rmse_list.append(square_error)
                        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                        rmse_var_dic[re_count]=np.std(rmse_list)
                        
                        
                        
                    while cursor_x<target_x:
                        yield env.process(Press_button(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
                        
                        #update cursor postion:
                        cursor_x=cursor_x+step
                        #show cursor
                        Reaction_dynamic2D().user_click(cursor_x,cursor_y)
                        
                        #update target position
                        position=Reaction_dynamic2D().frame.canvas.coords(Reaction_dynamic2D().target)
                        target_x=position[0]+Reaction_dynamic2D().r
                        target_y=position[1]+Reaction_dynamic2D().r
                        
                        re_count+=1
                        
                        #square error
                        square_error=(cursor_x-target_x)**2+(cursor_y-target_y)**2
                        #calculate RMSE
                        rmse_list.append(square_error)
                        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                        rmse_var_dic[re_count]=np.std(rmse_list)
                    
                    while cursor_y>=target_y:
                        yield env.process(Press_button(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
                        
                        #update cursor postion:
                        cursor_y=cursor_y-step
                        #show cursor
                        Reaction_static_2DTracing().user_click(cursor_x,cursor_y)
                        
                        #update target position
                        position=Reaction_track2D().frame.canvas.coords(Reaction_static_2DTracing().target)
                        target_x=position[0]-Reaction_dynamic2D().r
                        target_y=position[1]-Reaction_dynamic2D().r
                        
                        re_count+=1
                        
                        #square error
                        square_error=(cursor_x-target_x)**2+(cursor_y-target_y)**2
                        #calculate RMSE
                        rmse_list.append(square_error)
                        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                        rmse_var_dic[re_count]=np.std(rmse_list)
                        
                    while cursor_y<target_y:
                        yield env.process(Press_button(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))
                        
                        #update cursor postion:
                        cursor_y=cursor_y+step
                        #show cursor
                        Reaction_dynamic2D().user_click(cursor_x,cursor_y)
                        
                        #update target position
                        position=Reaction_dynamic2D().frame.canvas.coords(Reaction_dynamic2D().target)
                        target_x=position[0]-Reaction_dynamic2D().r
                        target_y=position[1]-Reaction_dynamic2D().r
                        
                        re_count+=1
                        
                        #square error
                        square_error=(cursor_x-target_x)**2+(cursor_y-target_y)**2
                        #calculate RMSE
                        rmse_list.append(square_error)
                        rmse_dic[re_count] = (np.sum(rmse_list))**(1/2)/(re_count+1)
                        rmse_var_dic[re_count]=np.std(rmse_list)
            
            for t in range(19,0,-1):
                if Reaction_dynamic2D().frame.canvas.coords(Reaction_dynamic2D().target)[0]>=5000*t/10/2:
                    Reaction_dynamic2D().scroll_x(t/10/2)
                    break
                
            for t in range(19,0,-1):
                if Reaction_dynamic2D().frame.canvas.coords(Reaction_dynamic2D().target)[0]>=5000*(100-t)/10/2:
                    Reaction_dynamic2D().scroll_y(t/10/2)
                    break
            '''
            elif Reaction_dynamic1D().frame.canvas.coords(Reaction_dynamic1D().target)[0]>=2500:
                Reaction_dynamic1D().scroll(0.5)
                
            elif Reaction_dynamic1D().frame.canvas.coords(Reaction_dynamic1D().target)[0]>=1500:
                Reaction_dynamic1D().scroll(0.3)            
            elif Reaction_dynamic1D().frame.canvas.coords(Reaction_dynamic1D().target)[0]>=1000:
                Reaction_dynamic1D().scroll(0.2)
            elif Reaction_dynamic1D().frame.canvas.coords(Reaction_dynamic1D().target)[0]>=500:
                Reaction_dynamic1D().scroll(0.1)
            '''   



def time_stamp_track_1D(env):
   
    position = Reaction_track1D().frame.canvas.coords(Reaction_track1D().t)
    global direction_track1D
    if direction_track1D==1:
        if position[0]+1*track1D_amp_dic[track1D_amp]<=Reaction_track1D().origin+Reaction_track1D.length-Reaction_track1D().r:
            Reaction_track1D().target_move(1)
        else:
            Reaction_track1D().frame.canvas.move('target',Reaction_track1D().origin+Reaction_track1D.length-Reaction_track1D().r-position[0],0)
            direction_track1D=-1
    elif direction_track1D==-1:
        if position[0]-1*track1D_amp_dic[track1D_amp]>=Reaction_track1D().origin-Reaction_track1D().r:
            Reaction_track1D().target_move(direction_track1D)
        else:
            Reaction_track1D().frame.canvas.move('target',-(position[0]-(Reaction_track1D().origin-Reaction_track1D().r)),0)
            direction_track1D=1

    time.sleep(0.0000000005)
    yield env.timeout(0)     

def time_stamp_track_2D(env):

    direction=random.choice([-1,1,-2,2]) #-2: down 2: up -1: left 1: right
    position = Reaction_track2D().frame.canvas.coords(Reaction_track2D().target)
    
    #make sure the target point is within the coordinates
    if direction==1:
        if position[0]+1*track2D_amp_dic[track2D_amp]<=Reaction_track2D().origin_x+Reaction_track2D.length-Reaction_track2D().r:
            Reaction_track2D().frame.canvas.move('target',1*track2D_amp_dic[track2D_amp],0)           
        else:
            Reaction_track2D().frame.canvas.move('target',Reaction_track2D().origin_x+Reaction_track2D.length-Reaction_track2D().r-position[0],0)
    
    elif direction==-1:
        if position[0]-1*track2D_amp_dic[track2D_amp]>=Reaction_track2D().origin_x-Reaction_track2D().r:
            Reaction_track2D().frame.canvas.move('target',-1*track2D_amp_dic[track2D_amp],0)
            
        else:
            Reaction_track2D().frame.canvas.move('target',-(position[0]-(Reaction_track2D().origin_x-Reaction_track2D().r)),0)
            
    elif direction==2:
        if position[1]-1*track2D_amp_dic[track2D_amp]>=Reaction_track2D().origin_y-Reaction_track2D().length-Reaction_track2D().r:
            Reaction_track2D().frame.canvas.move('target',0,-1*track2D_amp_dic[track2D_amp])
            
        else:
            Reaction_track2D().frame.canvas.move('target',0,-(position[1]-(Reaction_track2D.origin_y-Reaction_track2D.length-Reaction_track2D.r)))
        
    elif direction==-2:
        if position[1]+1*track2D_amp_dic[track2D_amp]<=Reaction_track2D().origin_y-Reaction_track2D().r:
            Reaction_track2D().frame.canvas.move('target',0,1*track2D_amp_dic[track2D_amp])
            
        else:
            Reaction_track2D().frame.canvas.move('target',0,Reaction_track2D().origin_y-Reaction_track2D().r-position[1])
    
    
    time.sleep(0.0000000005)
    yield env.timeout(0) 

def time_stamp_static_2D(env):
    Reaction_static_2DTracing().target_move()
    time.sleep(0.0000000005)
    yield env.timeout(0) 

def time_stamp_dynamic_1D(env):
    Reaction_dynamic1D().target_move(0)
    time.sleep(0.0000000005)
    yield env.timeout(0)   
    
def time_stamp_dynamic_2D(env):
    Reaction_dynamic2D().target_move()
    time.sleep(0.0000000005)
    yield env.timeout(0) 

#4.8 entity generation

def see_color_en (env,k_see):
    qn_mhp = QN_MHP(env)
    generation='see_color_en'

    # initialization
    i = [0]
    index=0
    
    k=eval(k_see)
    
    yield env.timeout(see_color_fa)  
    #generate entities
    while True:
        if index<see_color_occur:
            #update entity index i
            index+=1
            i=[index]        
            #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
            #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
            #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
            #server index will be consistent with Hanning's code
            outserver_dic = {}
            for item in range(1,300):
                outserver_dic[item] = 0
            #update arival time
            arrival_time = env.now
            #update attibute 
            #i[0]:0: noise 1: stimuli; i[1][1]: 2:visual 3:auditory; i[1][2]: 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified
            #i[1][3]: color 
            
            #if only 'SEE' behavior element is chosen, generate visual entities
            if ['Choice'] in Tasklist_dic[k] or ['Store_to_WM','Choice'] in Tasklist_dic[k]:
                if load_var(path+'/N.txt')==1:
                    attribute = {'stimuli':1,'type':2,'info':randint(4,7),'color':(255,0,0)}  
                else:
                    attribute={'stimuli':1,'type':2,'info':randint(4,7),'color':color_list[randint(0, N-1)]}
            
            else:
                attribute={'stimuli':1,'type':2,'info':randint(4,7),'color':color_list[randint(0, len(color_list)-1)]}
 
            i.append(attribute)

            if anim==1:             
                Structure_and_Animation().show(i, j, k, '0',generation)

            env.process(main(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation)) 
            #yield env.timeout(expovariate(1/IAT))  # interval arriving time: lamda=1/50 msec           
            yield env.timeout(see_color_IAT)
        else:
            break
        
        

def hear_color_en (env,k_hear):
    qn_mhp = QN_MHP(env)
    generation='hear_color_en'

    # initialization
    i = [0]
    index=0
    
    k=eval(k_hear) 
   
    yield env.timeout(hear_color_fa)  
    #generate entities
    while True:
        if index<hear_color_occur:
            #update entity index i
            index+=1
            i=[index]        
            #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
            #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
            #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
            #server index will be consistent with Hanning's code
            outserver_dic = {}
            for item in range(1,300):
                outserver_dic[item] = 0
            #update arival time
            arrival_time = env.now
            #update attibute 
            #i[0]:0: noise 1: stimuli; i[1][1]: 2:visual 3:auditory; i[1][2]: 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified
            #i[1][3]: color 
            
            #if only 'SEE' behavior element is chosen, generate visual entities
            if ['Choice'] in Tasklist_dic[k]:
                if load_var(path+'/N.txt')==1:
                    attribute = {'stimuli':randint(0,1),'type':3,'info':randint(4,7),'color':(255,0,0)}  
                else:
                    attribute={'stimuli':randint(0,1),'type':3,'info':randint(4,7),'color':color_list[randint(0, N-1)]}
            
            else:
                attribute={'stimuli':randint(0,1),'type':3,'info':randint(4,7),'color':color_list[randint(0, len(color_list)-1)]}    
            i.append(attribute)
            
            if anim==1:             
                Structure_and_Animation().show(i, j, k, '0',generation)

            env.process(main(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation)) 
            #yield env.timeout(expovariate(1/IAT))  # interval arriving time: lamda=1/50 msec           
            yield env.timeout(hear_color_IAT)
        else:
            break

def see_text_en (env,k_see):
    qn_mhp = QN_MHP(env)
    generation='see_text_en'

    # initialization
    i = [0]
    index=0
    
    k=eval(k_see)
    
   
    yield env.timeout(see_text_fa)  
    #generate entities
    while True:
        if index<see_text_occur:
            #update entity index i
            index+=1
            i=[index]        
            #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
            #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
            #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
            #server index will be consistent with Hanning's code
            outserver_dic = {}
            for item in range(1,300):
                outserver_dic[item] = 0
            #update arival time
            arrival_time = env.now
            #update attibute 
            #i[0]:0: noise 1: stimuli; i[1][1]: 2:visual 3:auditory; i[1][2]: 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified
            #i[1][3]: color 
            
            #if only 'SEE' behavior element is chosen, generate visual entities
            attribute={}
            if 'Cal_single_digit_num' in task_info_dic.values():
                attribute={'stimuli':1, 'type':2, 'info':randint(4,7),'color':(255,255,255)}
                attribute['cal_sd_num1']=randint(1,9)
                attribute['cal_sd_num2']=randint(1,9)
                i.append(attribute)
            
            elif 'Count' in task_info_dic.values():
                a=randint(1,9)
                b=a+length_count-1
     
                attribute = {'stimuli':1,'type':2,'info':randint(4,7),'color':(255,255,255),'Start':a,'End':b}  
            
                
                i.append(attribute)
                Reaction_count().show(a, b)
            else:
                attribute = {'stimuli':randint(0,1),'type':2,'info':5,'color':-999}    
                i.append(attribute)
            if anim==1:             
                Structure_and_Animation().show(i, j, k, '0',generation)

            env.process(main(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation)) 
            #yield env.timeout(expovariate(1/IAT))  # interval arriving time: lamda=1/50 msec           
            yield env.timeout(see_text_IAT)
        else:
            break

def hear_text_en (env,k_hear):
    qn_mhp = QN_MHP(env)
    generation='hear_text_en'

    # initialization
    i = [0]
    index=0
    
    k=eval(k_hear) 
   
    yield env.timeout(hear_text_fa)  
    #generate entities
    while True:
        if index<hear_text_occur:
            #update entity index i
            index+=1
            i=[index]        
            #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
            #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
            #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
            #server index will be consistent with Hanning's code
            outserver_dic = {}
            for item in range(1,300):
                outserver_dic[item] = 0
            #update arival time
            arrival_time = env.now
            #update attibute 
            #i[0]:0: noise 1: stimuli; i[1][1]: 2:visual 3:auditory; i[1][2]: 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified
            #i[1][3]: color 
            
            #if only 'SEE' behavior element is chosen, generate visual entities
            
            attribute={}
            if 'Cal_single_digit_num' in task_info_dic.values():
                attribute={'stimuli':1, 'type':3, 'info':randint(4,7),'color':(255,255,255)}
                attribute['cal_sd_num1']=randint(1,9)
                attribute['cal_sd_num2']=randint(1,9)
                i.append(attribute)
            
            elif 'Count' in task_info_dic.values():
                a=randint(1,9)
                b=a+length_count-1
     
                attribute = {'stimuli':1,'type':3,'info':randint(4,7),'color':(255,255,255),'Start':a,'End':b}  
            
                
                i.append(attribute)
                Reaction_count().show(a, b)
            else:
                attribute = {'stimuli':randint(0,1),'type':2,'info':5,'color':-999}    
                i.append(attribute)
            
            
            if anim==1:             
                Structure_and_Animation().show(i, j, k, '0',generation)

            env.process(main(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,generation)) 
            #yield env.timeout(expovariate(1/IAT))  # interval arriving time: lamda=1/50 msec           
            yield env.timeout(hear_text_IAT)
        else:
            break

def Look_for_en(env):
    qn_mhp = QN_MHP(env)
    generation='look_for_en'

    # initialization
    i = [0]
    index=0
    count=0
    for item in judgei_target_dic:
        k=eval(item)
    yield env.timeout(0)  
    #generate entities


    #update entity index i
    index+=1
    i=[index]        
    #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
    #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
    #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
    #server index will be consistent with Hanning's code
    outserver_dic = {}
    for item in range(1,300):
        outserver_dic[item] = 0
    #update arival time
    arrival_time = env.now
    #update attibute 
    #0: noise 1: stimuli; 2:visual 3:auditory; 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified
    
    attribute = {'stimuli':1,'type':2,'info':6}
  
    if len(look_for_ls)>1:
        item=randint(1,len(look_for_ls)-1)
    elif len(look_for_ls)==1:
        item=0
    attribute['eye_loc']=look_for_ls[item][0]
    attribute['color']=look_for_ls[item][2]
    attribute['text']=look_for_ls[item][1]  

    
    if len(look_for_ls)==0:
        attribute['eye_loc']=-999
        attribute['color']=-999
        attribute['text']=-999  
            

    i.append(attribute)
    if attribute['stimuli']==1 and len(look_for_ls)!=0:
        del look_for_ls[item]
        count+=1
    print(i[1]['color'])
    if anim==1:
        Structure_and_Animation().show(i, j, k, '0',generation)
    env.process(look_for(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time,count,generation))   
      


def track1D_en(env):
    qn_mhp = QN_MHP(env)
    generation='track1D_en'

    # initialization
    i = [0]
    index=0
    count=0
    
    for item in task_info_dic:
        if task_info_dic[item]=='Tracking_1D':
            k=eval(task_info_dic[1,(item[1]+1)/2])
            
    #yield env.timeout(trace1D_fa)  
    #generate entities
    while True: 
        #if index<track1D_trial[k]:
            
        #update entity index i
        index+=1
        i=[index]        
        #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
        #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
        #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
        #server index will be consistent with Hanning's code
        outserver_dic = {}
        for item in range(1,300):
            outserver_dic[item] = 0
        #update arival time
        arrival_time = env.now
        #update attibute 
        #0: noise 1: stimuli; 2:visual 3:auditory; 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified
        
        target=0
        user=track1D_curse_loc
        
        attribute = {'stimuli':1,'type':2,'info':6}
        attribute['eye_loc']=[target,user]#[target,user]
        attribute['color']=(255,0,0)
        i.append(attribute)

        if anim==1:
            Structure_and_Animation().show(i, j, k, '0',generation)
        env.process(main(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))   
        #yield env.timeout(expovariate(1/IAT))  # interval arriving time: lamda=1/50 msec            
        
        yield env.timeout(10e5)
        #yield env.timeout(track1D_time[k]) 
            
def track2D_en(env):
    qn_mhp = QN_MHP(env)
    generation='track2D_en'

    # initialization
    i = [0]
    index=0
    count=0
    
    k=1
            
    #yield env.timeout(trace1D_fa)  
    #generate entities
    while True: 
        #if index<track1D_trial[k]:
            
        #update entity index i
        index+=1
        i=[index]        
        #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
        #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
        #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
        #server index will be consistent with Hanning's code
        outserver_dic = {}
        for item in range(1,300):
            outserver_dic[item] = 0
        #update arival time
        arrival_time = env.now
        #update attibute 
        #0: noise 1: stimuli; 2:visual 3:auditory; 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified
        
        target_x=track2D_target_loc_x
        target_y=track2D_target_loc_y
        user_x=track2D_cursor_loc_x
        user_y=track2D_cursor_loc_y
        
        attribute = {'stimuli':1,'type':2,'info':6}
        attribute['eye_loc']=[target_x,target_y,user_x,user_y]#[target,user]
        attribute['color']=-999
        i.append(attribute)

        if anim==1:
            Structure_and_Animation().show(i, j, k, '0',generation)
        env.process(main(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))   
        #yield env.timeout(expovariate(1/IAT))  # interval arriving time: lamda=1/50 msec            
        
        yield env.timeout(10e5)
        #yield env.timeout(track1D_time[k]) 

def static2D_en(env):
    qn_mhp = QN_MHP(env)
    generation='static2D_en'

    # initialization
    i = [0]
    index=0
    count=0
    
    k=1
            
    #yield env.timeout(trace1D_fa)  
    #generate entities
    while True: 
        #if index<track1D_trial[k]:
            
        #update entity index i
        index+=1
        i=[index]        
        #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
        #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
        #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
        #server index will be consistent with Hanning's code
        outserver_dic = {}
        for item in range(1,300):
            outserver_dic[item] = 0
        #update arival time
        arrival_time = env.now
        #update attibute 
        #0: noise 1: stimuli; 2:visual 3:auditory; 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified
        
        target_x=-Reaction_static_2DTracing().xmax
        target_y=math.sin(target_x)
        user_x=-Reaction_static_2DTracing().xmax+(2*Reaction_static_2DTracing().xmax*static2D_cursor_loc_x/100)
        user_y=math.sin(user_x)
        
        attribute = {'stimuli':1,'type':2,'info':6}
        attribute['eye_loc']=[target_x,target_y,user_x,user_y]#[target,user]
        attribute['color']=-999
        i.append(attribute)

        if anim==1:
            Structure_and_Animation().show(i, j, k, '0',generation)
        env.process(main(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))   
        #yield env.timeout(expovariate(1/IAT))  # interval arriving time: lamda=1/50 msec            
        
        yield env.timeout(10e5)
        #yield env.timeout(track1D_time[k]) 

def dynamic1D_en(env):
    qn_mhp = QN_MHP(env)
    generation='dynamic1D_en'

    # initialization
    i = [0]
    index=0
    count=0
    
    for item in task_info_dic:
        if task_info_dic[item]=='Dynamic_1D':
            print(task_info_dic[item[0],item[1]+1])
            
    #yield env.timeout(trace1D_fa)  
    #generate entities
    while True: 
        #if index<track1D_trial[k]:
            
        #update entity index i
        index+=1
        i=[index]        
        #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
        #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
        #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
        #server index will be consistent with Hanning's code
        outserver_dic = {}
        for item in range(1,300):
            outserver_dic[item] = 0
        #update arival time
        arrival_time = env.now
        #update attibute 
        #0: noise 1: stimuli; 2:visual 3:auditory; 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified
        
        target=0
        user=dynamic1D_cursor_loc
        
        attribute = {'stimuli':1,'type':2,'info':6}
        attribute['eye_loc']=[target,user]#[target,user]
        attribute['color']=(255,0,0)
        i.append(attribute)

        if anim==1:
            Structure_and_Animation().show(i, j, k, '0',generation)
        env.process(main(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))   
        #yield env.timeout(expovariate(1/IAT))  # interval arriving time: lamda=1/50 msec            
        
        yield env.timeout(10e5)
        #yield env.timeout(track1D_time[k]) 

def dynamic2D_en(env):
    qn_mhp = QN_MHP(env)
    generation='dynamic2D_en'

    # initialization
    i = [0]
    index=0
    count=0
    
    k=1
            
    #yield env.timeout(trace1D_fa)  
    #generate entities
    while True: 
        #if index<track1D_trial[k]:
            
        #update entity index i
        index+=1
        i=[index]        
        #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
        #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
        #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
        #server index will be consistent with Hanning's code
        outserver_dic = {}
        for item in range(1,300):
            outserver_dic[item] = 0
        #update arival time
        arrival_time = env.now
        #update attibute 
        #0: noise 1: stimuli; 2:visual 3:auditory; 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified
        
        target_x=-Reaction_dynamic2D().xmax
        target_y=math.sin(target_x)
        user_x=-Reaction_dynamic2D().xmax+(2*Reaction_dynamic2D().xmax*dynamic2D_cursor_loc_x/100)
        user_y=math.sin(user_x)
        
        attribute = {'stimuli':1,'type':2,'info':6}
        attribute['eye_loc']=[target_x,target_y,user_x,user_y]#[target,user]
        attribute['color']=-999
        i.append(attribute)

        if anim==1:
            Structure_and_Animation().show(i, j, k, '0',generation)
        env.process(main(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation))   
        #yield env.timeout(expovariate(1/IAT))  # interval arriving time: lamda=1/50 msec            
        
        yield env.timeout(10e5)
        #yield env.timeout(track1D_time[k]) 
        
def time_en_track1D (env):
    while True:
        yield env.timeout(track1D_freq_dic[track1D_freq]) 
        env.process(time_stamp_track_1D(env))
                   
def time_en_track2D (env):
    while True:
        yield env.timeout(track2D_freq_dic[track2D_freq])
        env.process(time_stamp_track_2D(env))
        
def time_en_static2D (env):
    while True:
        yield env.timeout(static2D_freq_dic[static2D_freq])
        env.process(time_stamp_static_2D(env))

def time_en_dynamic1D (env):
    while True:
        yield env.timeout(dynamic1D_freq_dic[dynamic1D_freq]) 
        env.process(time_stamp_dynamic_1D(env))
        
def time_en_dynamic2D (env):
    while True:
        yield env.timeout(dynamic2D_freq_dic[dynamic2D_freq]) 
        env.process(time_stamp_dynamic_2D(env))

if anim==1:
    Structure_and_Animation().background()

class entity_generation:
    if 'See' in task_info_dic.values() and 'Look_for' not in task_info_dic.values():
        for (r,c,no) in see_entity_dic:
            if see_entity_dic[(r,c,no)]=='Color(s)':
                global see_color_IAT, see_color_fa, see_color_occur
                see_color_fa=eval(see_entity_dic[(r,2,no)])
                see_color_IAT=eval(see_entity_dic[(r,3,no)])
                see_color_occur=eval(see_entity_dic[(r,4,no)])
                k_see=no
                env.process(see_color_en(env,k_see))
                
    if 'Hear' in task_info_dic.values():
        for (r,c,no) in hear_entity_dic:
            if hear_entity_dic[(r,c,no)]=='Color(s)':
                global hear_color_IAT, hear_color_fa, hear_color_occur
                hear_color_fa=eval(hear_entity_dic[(r,2,no)])
                hear_color_IAT=eval(hear_entity_dic[(r,3,no)])
                hear_color_occur=eval(hear_entity_dic[(r,4,no)])
                k_hear=no
                env.process(hear_color_en(env,k_hear))
                
    if 'See' in task_info_dic.values() and 'Look_for' not in task_info_dic.values():
        for (r,c,no) in see_entity_dic:
            if see_entity_dic[(r,c,no)]=='Text':
                global see_text_IAT, see_text_fa, see_text_occur
                see_text_fa=eval(see_entity_dic[(r,2,no)])
                see_text_IAT=eval(see_entity_dic[(r,3,no)])
                see_text_occur=eval(see_entity_dic[(r,4,no)])
                k_see=no
                env.process(see_text_en(env,k_see))
                
    if 'Hear' in task_info_dic.values():
        for (r,c,no) in hear_entity_dic:
            if hear_entity_dic[(r,c,no)]=='Text':
                global hear_text_IAT, hear_text_fa, hear_text_occur
                hear_text_fa=eval(hear_entity_dic[(r,2,no)])
                hear_text_IAT=eval(hear_entity_dic[(r,3,no)])
                hear_text_occur=eval(hear_entity_dic[(r,4,no)])
                k_hear=no
                env.process(hear_text_en(env,k_hear))
    

        
    if 'Look_for' in task_info_dic.values():
        env.process(Look_for_en(env))
    
    if 'Tracking_1D' in task_info_dic.values():
       
        start_time=env.now
        env.process(track1D_en(env))
        env.process(time_en_track1D(env))
        
    if 'Tracking_2D' in task_info_dic.values():
    
        start_time=env.now
        env.process(track2D_en(env))
        env.process(time_en_track2D(env))
    
    if 'Static_2DTracing' in task_info_dic.values():
        
        start_time=env.now
        env.process(static2D_en(env))
        env.process(time_en_static2D(env))

    if 'Dynamic_1D' in task_info_dic.values():
        start_time=env.now
        env.process(dynamic1D_en(env))
        env.process(time_en_dynamic1D(env))
        
    if 'Dynamic_2D' in task_info_dic.values():
        start_time=env.now
        env.process(dynamic2D_en(env))
        env.process(time_en_dynamic2D(env))
        
    env.run(until=SIMTIME)  #running time


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