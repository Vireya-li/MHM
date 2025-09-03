#----------------------- 
#Section3 Structure and Animation (This file contains only Section 3.4 for BE-specific animation functions)

#3.1 structure and animation window definition (now in qn_mhp_layout.py)
#3.2 structure and animation (now in qn_mhp_layout.py)     
#3.3 entity animation (now in animation_general.py)
import tkinter as tk
import time
import pyautogui as ag
import math
from numpy import arange as npar



# Import other custom modules using absolute imports
from tkinter import messagebox
from gui_general_2 import saved, load_var, save_var, path, GUI_User_Main
from gui_for_be_3 import operation, track1D_curse_loc, track2D_target_loc_x, track2D_target_loc_y, track2D_cursor_loc_x, track2D_cursor_loc_y, track1D_amp, track2D_amp,N, static2D_shape,static2D_target_loc_x, static2D_cursor_loc_x, dynamic2D_shape, static2D_amp, dynamic1D_cursor_loc, dynamic1D_amp, dynamic2D_target_loc_x, dynamic2D_cursor_loc_x, dynamic2D_amp
from qn_mhp_layout_4 import Structure_and_Animation, myCanvas
from animation_general_5 import show, enter, leave, add, delete
from model_core_7 import QN_MHP, env, Tasklist_dic, sojourn_time_dic, rt_mean_dic, rt_var_dic, rmse_dic, rmse_var_dic, ji_result_dic, task_info_dic, color_list, track1D_amp_dic, track2D_amp_dic, static2D_amp_dic, direction_static2D, dynamic1D_amp_dic, dynamic2D_amp_dic
from behavior_elements_8 import *
from plot_9 import Plot
            
   
    
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


#Section4 Engine (now in separate files)


