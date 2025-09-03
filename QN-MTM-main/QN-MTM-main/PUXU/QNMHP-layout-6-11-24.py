from itertools import count
from pickle import FALSE
import tkinter 
import os
from tkinter import font
from turtle import color
from queue import Queue



class myCanvas(tkinter.Frame):
    def __init__(self, root):
        self.root = root
        self.w = self.root.winfo_screenwidth()
        self.h = self.root.winfo_screenheight()
        self.canvas = tkinter.Canvas(root, width=self.w, height=self.h)
        self.canvas.pack( fill=tkinter.BOTH, expand=tkinter.YES)
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
            self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)


def main():
    root = tkinter.Tk()
    w=root.winfo_screenwidth()
    h=root.winfo_screenheight()
    dx = w//30 

    # Copied from QNMHP_layout_only
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


    frame=myCanvas(root)
    frame.canvas.pack(fill="both",expand=True)
    #generate the rectangles and text
    Boxes=list()
    Boxes.append({'name':'1','location':[3,3,4,4]})
    Boxes.append({'name':'2','location':[5, 1, 6, 2]})
    Boxes.append({'name':'3','location':[5, 5, 6, 6]})
    Boxes.append({'name':'4','location':[7, 3, 8, 4]})
    Cache=list()
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
    links.append({'name':'A_C','location':[11.5, 7.75, 12.7, 7.75],'arrows':'1x'}) 
    links.append({'name':'C_B','location':[11.5, 8, 11.5, 9],'arrows':'1y'})
    #links.append({'name':'B_C','location':[11.5, 8.25, 12.7, 8.25],'arrows':'1x'}) 
    links.append({'name':'B_C','location':[11.5, 8, 12.7, 8],'arrows':'1x'}) 
    links.append({'name':'B_W','location':[11.5, 10, 11.5, 13, 19.2, 13, 19.2, 6.2, 20, 6.2],'arrows':'1x'}) 
    links.append({'name':'B_V','location':[11.7, 10, 11.7, 12.7, 19, 12.7, 19, 3.7, 20, 3.7],'arrows':'1x'})#### 
    # changed C_G to bidirectional
    links.append({'name':'C_G','location':[13.7, 8, 15, 8],'arrows':'2x'}) 
    # add G_C
    #links.append({'name':'G_C','location':[15, 8, 13.7, 8],'arrows':'1x'}) 
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
    links.append({'name':'D_C','location':[13.5, 6, 13.5, 7.5],'arrows':'2y'}) 
    # Changed C_D to bidirectional
    #links.append({'name':'C_D','location':[13.5, 7.5, 13.5, 6],'arrows':'1y'}) 
    links.append({'name':'V_W','location':[20.5, 4, 20.5, 5.5],'arrows':'1y'}) 
    links.append({'name':'W_Y','location':[20.5, 6.5, 20.5, 9],'arrows':'1y'})  
    links.append({'name':'X_Y','location':[20.5, 11, 20.5, 10],'arrows':'1y'})  
    # X to C
    links.append({'name':'X_C','location':[20, 11.2, 12.1, 11.2,12.1,8.25,12.7,8.25],'arrows':'1x'}) 
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
    
    #Copied from QNMHP-4-26-24: line 224 - 234
    #To add capacity bars for some servers
    
    for box in Boxes:
            if Capacity[box['name']] != 10e5:
                for item in range(0,Capacity[box['name']]):
                    v0=box['location'][0]+item*(dx/Capacity[box['name']])
                    v1=box['location'][1]
                    v2=box['location'][0]+(item+1)*(dx/Capacity[box['name']])
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
    # print(count1)
    # print(count2)
    # print(count3)
    
   
    # control the refresh time interval
    t=50
    # generate j balls one time(greater than 0)
    j=150
    #R1,R2,R3,R4 servers
    #Q_R1,Q_R2_R1,Q_R3_R1,Q_R4_R2,Q_R4_R3 the queue room corresponding to each server
    Q_R1=Queue(maxsize=0)
    Q_R2_R1=Queue(maxsize=0)
    Q_R3_R1=Queue(maxsize=0)
    Q_R4_R2=Queue(maxsize=0)
    Q_R4_R3=Queue(maxsize=0)
    R1=Queue(maxsize=0)    
    R2=Queue(maxsize=0)    
    R3=Queue(maxsize=0)    
    R4=Queue(maxsize=j)
    for m in range(1,j+1):
        temp=Cache[0]
        if m%2==1:
            frame.canvas.create_oval(temp['location'],fill='red',tags='ball_'+str(m))
        else:
            frame.canvas.create_oval(temp['location'],fill='green',tags='ball_'+str(m))
        Q_R1.put(m)
    cache1=Cache[1]
    cache2=Cache[2]
    cache3=Cache[3]
    cache4=Cache[4]
    def  refreshCanvas():
        flag_R1=True
        flag_R1R2=True
        flag_R1R3=True
        flag_R2=True
        flag_R3=True
        flag_R24=True
        flag_R34=True
        while R4.full()==True:
            # for m in range(R4.qsize()):
            #     print(R4.get())
            break
            #os._exit(0)
        if Q_R1.empty()==False and R1.empty()==True:
            temp=Q_R1.get()
            R1.put(temp)
            flag_R1=False
            temp1=Boxes[0]
            frame.canvas.coords('ball_'+str(temp),temp1['location'])
        if R1.empty()==False and flag_R1==True:
            temp=R1.get()
            if temp%2==0:
                frame.canvas.coords('ball_'+str(temp),cache1['location'])
                Q_R2_R1.put(temp)
                flag_R1R2=False
            else:
                frame.canvas.coords('ball_'+str(temp),cache2['location'])
                Q_R3_R1.put(temp)
                flag_R1R3=False
        if Q_R2_R1.empty()==False and flag_R1R2==True and R2.empty()==True:
            temp=Q_R2_R1.get()
            temp1=Boxes[1]
            frame.canvas.coords('ball_'+str(temp),temp1['location'])
            R2.put(temp)
            flag_R2=False
        if Q_R3_R1.empty()==False and flag_R1R3==True and R3.empty()==True:
            temp=Q_R3_R1.get()
            temp1=Boxes[2]
            frame.canvas.coords('ball_'+str(temp), temp1['location'])
            R3.put(temp)
            flag_R3=False
        if R2.empty()==False and flag_R2==True and Q_R4_R2.empty()==True:
            temp=R2.get()
            frame.canvas.coords('ball_'+str(temp),cache3['location'])
            Q_R4_R2.put(temp)
            flag_R24=False
        if R3.empty()==False and flag_R3==True and Q_R4_R3.empty()==True:
            temp=R3.get()
            frame.canvas.coords('ball_'+str(temp),cache4['location'])
            Q_R4_R3.put(temp)
            flag_R34=False
        if flag_R34==True and Q_R4_R3.empty()==False:
            temp=Q_R4_R3.get()
            temp1=Boxes[3]
            frame.canvas.coords('ball_'+str(temp),temp1['location'])
            R4.put(temp)
        if flag_R24==True and Q_R4_R2.empty()==False:
            temp=Q_R4_R2.get()
            temp1=Boxes[3]
            frame.canvas.coords('ball_'+str(temp),temp1['location'])
            R4.put(temp)
        frame.canvas.update
        root.after(t,refreshCanvas)              
    
    frame.canvas.update
    frame.canvas.pack()
    root.after(t,refreshCanvas)
    frame.canvas.addtag_all('all')    
    root.mainloop()
    
if __name__ == '__main__':
    main()
