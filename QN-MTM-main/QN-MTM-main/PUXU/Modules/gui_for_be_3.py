

#2.3 BE Specific GUI
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random
import simpy
import sys
import math
import numpy as np
import pyautogui as ag
import os
import time
import pickle
import shutil

# Import other custom modules using absolute imports
from gui_general_2 import saved, load_var, save_var, path, GUI_User_Main
from qn_mhp_layout_4 import Structure_and_Animation
from animation_general_5 import show, enter, leave, add, delete
from model_core_7 import QN_MHP, env, main, Tasklist_dic, sojourn_time_dic, rt_mean_dic, rt_var_dic, rmse_dic, rmse_var_dic
from behavior_elements_8 import *
from plot_9 import Plot


#This file contains only BE-specific GUI (Section 2.3) (L689-2092) of QN-MHP 4/26/24
# need to import related modules/files!!
# need to be imported into related modules/files!!

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
# all other codes are now in separate module files

