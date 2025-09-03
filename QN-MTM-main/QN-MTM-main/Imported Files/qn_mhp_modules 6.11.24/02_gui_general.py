

#Section 1 codes are now in _init_.py 
#Section 2 is for GUI codes; this module contains #2.1 and #2.2 of QN-MHP 4/26/24 (L30-687)

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
#2.3 codes are now in gui_be.py


