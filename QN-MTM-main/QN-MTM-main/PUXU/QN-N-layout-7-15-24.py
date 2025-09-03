from itertools import count
from pickle import FALSE
import tkinter 
import os
from tkinter import font
from turtle import color
from queue import Queue

class myCanvas(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.w = self.root.winfo_screenwidth()  # Adjust the scaling factor as needed
        self.h = int(self.root.winfo_screenheight()*2.5)  # Adjust the scaling factor as needed
        self.canvas = tkinter.Canvas(root, width=self.w, height=self.h)
        self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
        root.bind('<Configure>', self.resize)
    def resize(self, event):
      wscale = event.width / self.w
      hscale = event.height / self.h

      h_font = self.h / 72
      arrow_1 = self.w / 91
      arrow_2 = arrow_1
      arrow_3 = self.h / 256
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

    Capacity = {}
    Capacity['DLPFC']=10e5
    Capacity['SMA']=10e5
    Capacity['PreM']=10e5
    Capacity['CMAs']=10e5
    Capacity['PMC']=10e5
    Capacity['PSS']=10e5
    Capacity['PPAC']=10e5
    Capacity['SSS']=10e5
    Capacity['SV']=10e5
    Capacity['PV']=10e5
    Capacity['SA']=10e5
    Capacity['PA']=10e5
    Capacity['PO']=10e5
    Capacity['SO']=10e5
    Capacity['T6']=10e5
    Capacity['T1']=10e5
    Capacity['T2']=10e5
    Capacity['T3']=10e5
    Capacity['T4']=10e5
    Capacity['T5']=10e5
    Capacity['LS']=10e5
    Capacity['BG']=10e5
    Capacity['HT']=10e5
    Capacity['RF']=10e5
    Capacity['CB']=10e5
    Capacity['RN']=10e5
    Capacity['A']=10e5
    Capacity['B']=10e5
    Capacity['C']=10e5
    Capacity['D']=10e5
    Capacity['E']=10e5
    Capacity['F']=10e5
    Capacity['G']=10e5
    Capacity['H']=10e5
    Capacity['I']=10e5
    Capacity['J']=10e5
    Capacity['K']=10e5
    Capacity['L']=10e5
    Capacity['CN-II']=10e5
    Capacity['CN-III,IV,VI']=10e5
    Capacity['CN-I']=10e5
    Capacity['CN-V,VII']=10e5
    Capacity['CN-VIII-Vestibular']=10e5
    Capacity['CN-VIII-Cochlear']=10e5
    Capacity['CN-IX,X']=10e5
    Capacity['CN-XI,XII']=10e5
    Capacity['PiMd']=10e5
    Capacity['BS-SMN']=10e5










    space={}

    frame=myCanvas(root)
    frame.canvas.pack(fill="both",expand=True)
    #generate the rectangles and text
    Boxes=list()
    Boxes.append({'name':'DLPFC','location':[8,4,9,5]})
    Boxes.append({'name':'SMA','location':[11,2,12,3]})
    Boxes.append({'name':'PreM','location':[11,4,12,5]})
    Boxes.append({'name':'CMAs','location':[11,6,12,7]})
    Boxes.append({'name':'PMC','location':[14,2,15,3]})
    Boxes.append({'name':'PSS','location':[16,2,17,3]})
    Boxes.append({'name':'PPAC','location':[19,2,20,3]})
    Boxes.append({'name':'SSS','location':[16.5,4,17.5,5]})
    Boxes.append({'name':'SV','location':[21,4,22,5]})
    Boxes.append({'name':'PV','location':[23,6,24,7]})
    Boxes.append({'name':'SA','location':[19,7,20,8]})
    Boxes.append({'name':'PA','location':[17,7,18,8]})
    Boxes.append({'name':'PO','location':[6,8,7,9]})
    Boxes.append({'name':'SO','location':[8,8,9,9]})
    Boxes.append({'name':'T6','location':[6,11,7,12]})
    Boxes.append({'name':'T1','location':[6,12.5,7,13.5]})
    Boxes.append({'name':'T2','location':[7.25,12.5,8.25,13.5]})
    Boxes.append({'name':'T3','location':[8.5,12.5,9.5,13.5]})
    Boxes.append({'name':'T4','location':[9.75,12.5,10.75,13.5]})
    Boxes.append({'name':'T5','location':[11,12.5,12,13.5]})
    Boxes.append({'name':'LS','location':[12.5,12.5,13.5,13.5]})
    Boxes.append({'name':'BG','location':[14.5,12.5,15.5,13.5]})
    Boxes.append({'name':'HT','location':[6,15,7,16]})
    Boxes.append({'name':'RF','location':[12.5,16,13.1,18]})
    Boxes.append({'name':'CB','location':[13.2,18,14.25,24]})
    Boxes.append({'name':'RN','location':[17,16,18,17]})
    Boxes.append({'name':'A','location':[11,16.5,12,17.5]})
    Boxes.append({'name':'B','location':[11,17.8,12,18.8]})
    Boxes.append({'name':'C','location':[7.25,20,8.25,21]})
    Boxes.append({'name':'D','location':[15.5,20,16.5,21]})
    Boxes.append({'name':'E','location':[7.25,22,8.25,23]})
    Boxes.append({'name':'F','location':[9.75,24,10.75,25]})
    Boxes.append({'name':'G','location':[11.5,24,12.5,25]})
    Boxes.append({'name':'H','location':[7.25,25,8.25,26]})
    Boxes.append({'name':'I','location':[15.5,25,16.5,26]})
    Boxes.append({'name':'J','location':[7.25,27,8.25,28]})
    Boxes.append({'name':'K','location':[7.25,29,8.25,30]})
    Boxes.append({'name':'L','location':[9.5,29,10.5,30]})
    Boxes.append({'name':'CN-II','location':[3,16,3,16]})
    Boxes.append({'name':'CN-III,IV,VI','location':[3,17.5,3,17.5]})
    Boxes.append({'name':'CN-I','location':[3,7,3,7]})
    Boxes.append({'name':'CN-V,VII','location':[3,19,3,19]})
    Boxes.append({'name':'CN-VIII-Vestibular','location':[3,21,3,21]})
    Boxes.append({'name':'CN-VIII-Cochlear','location':[3,23,3,23]})
    Boxes.append({'name':'CN-IX,X','location':[3,24.5,3,24.5]})
    Boxes.append({'name':'CN-XI,XII','location':[3,26.5,3,26.5]})
    Boxes.append({'name':'PiMd','location':[18,26,19,27]})
    Boxes.append({'name':'BS-SMN','location':[20,17,21,26]})




    Cache=list()
    links=list()
    links.append({'name':'PPAC_DLPFC','location':[19.3,2, 19.3,1, 8.7,1, 8.7,4],'arrows':'1y'}) 
    links.append({'name':'DLPFC_SMA','location':[9,4.25,10,4.25, 10, 2.5, 11, 2.5 ],'arrows':'1x'}) 
    links.append({'name':'DLPFC_PreM','location':[9,4.5, 11,4.5 ],'arrows':'1x'}) 
    links.append({'name':'DLPFC_CMAs','location':[9,4.75, 10, 4.75,10, 6.5, 11, 6.5 ],'arrows':'1x'}) 
    links.append({'name':'SMA_PMC','location':[12,2.25, 14,2.25 ],'arrows':'1x'}) 
    links.append({'name':'PreM_PMC','location':[12,4.5, 12.5,4.5 , 12.5, 2.5, 14,2.5],'arrows':'1x'}) 
    links.append({'name':'CMAs_PMC','location':[12,6.5, 13,6.5, 13, 2.75, 14, 2.75 ],'arrows':'1x'}) 
    links.append({'name':'PSS_PMC','location':[16,2.5, 15,2.5 ],'arrows':'1x'}) 
    links.append({'name':'PSS_SSS','location':[17,2.5, 17.25,2.5 , 17.25, 4],'arrows':'1y'}) 
    links.append({'name':'SSS_PPAC','location':[17.5, 4.5, 18,4.5 , 18, 2.5, 19,2.5],'arrows':'1x'}) 
    links.append({'name':'SV_PPAC','location':[21.5,4, 21.5,2.5 , 20, 2.5],'arrows':'1x'}) 
    links.append({'name':'PV_SV','location':[23.5,6, 23.5,4.5 , 22, 4.5],'arrows':'1x'}) 
    links.append({'name':'SA_PPAC','location':[19.5,7, 19.5, 3],'arrows':'1y'}) 
    links.append({'name':'PA_SA','location':[18,7.5, 19,7.5],'arrows':'1x'}) 
    links.append({'name':'PO_SO','location':[7,8.5, 8,8.5],'arrows':'1x'})
    links.append({'name':'PO_T6','location':[6.33,9, 6.33,11],'arrows':'1y'})
    links.append({'name':'T6_SO','location':[6.66,11, 6.66,9.5, 8.5, 9.5, 8.5,9],'arrows':'1y'})
    links.append({'name':'HT_T1','location':[6.5,15, 6.5,13.5],'arrows':'2y'})
    links.append({'name':'T2_PMC','location':[7.75,12.5, 7.75,10, 14.33, 10, 14.33,3],'arrows':'1y'})
    links.append({'name':'PMC_T2','location':[7.75,10, 7.75,12.5],'arrows':'1y'})
    links.append({'name':'SO_LS','location':[9,8.5, 13,8.5, 13,12.5],'arrows':'1y'})
    links.append({'name':'T3_PSS','location':[9,12.5, 9,11.5, 16.2,11.5, 16.2, 3],'arrows':'1y'})
    links.append({'name':'T4_PV','location':[10.25,12.5, 10.25,11, 23.5,11, 23.5, 7],'arrows':'1y'})
    links.append({'name':'T5_PA','location':[11.5,12.5, 11.5,10.5, 17.5,10.5, 17.5, 8],'arrows':'1y'})
    links.append({'name':'BG_right','location':[15.5,13,22,13],'arrows':'2x'})
    links.append({'name':'BG_LS','location':[13.5,12.8,14.5,12.8],'arrows':'2x'})
    links.append({'name':'PMC_down','location':[14.66,3,14.66,10,19.5,10, 19.5,13],'arrows':'1y'})
    links.append({'name':'T2_CB','location':[7.55,19, 13.2,19],'arrows':'1x'})
    links.append({'name':'CB_T2','location':[7.55,19, 7.55,13.5],'arrows':'1y'})
    links.append({'name':'T2_BG','location':[7.85,13.5, 7.85,15.5, 15.2,15.5,15.2,13.5],'arrows':'1y'})
    links.append({'name':'BG_T2','location':[7.85,15.5, 7.85,13.5],'arrows':'1y'})
    links.append({'name':'T2_LS','location':[8,13.5, 8,15, 12.7,15, 12.7,13.5],'arrows':'1y'})
    links.append({'name':'LS_T2','location':[8,15, 8,13.5],'arrows':'1y'})
    links.append({'name':'LS_RF','location':[13,16, 13,13.5],'arrows':'2y'})
    links.append({'name':'LS_CB','location':[13.4,18, 13.4,13.5],'arrows':'2y'})
    links.append({'name':'RF_BG','location':[13.1,16, 13.7,16, 13.7, 13.2, 14.5, 13.2],'arrows':'1x'})
    links.append({'name':'BG_RF','location':[13.7,16, 13.1,16],'arrows':'1x'})
    links.append({'name':'CB_RF','location':[13.1,16.5, 14,16.5, 14, 18],'arrows':'1y'})
    links.append({'name':'RF_CB','location':[14,16.5, 13.1,16.5],'arrows':'1x'})
    links.append({'name':'CB_RN','location':[14.25,19, 15.5,19, 15.5, 19, 15.5,16.5,17,16.5],'arrows':'1x'})
    links.append({'name':'RN_CB','location':[15.5,19, 14.25,19],'arrows':'1x'})
    links.append({'name':'BG_CB','location':[14.2,18, 14.2,16, 15, 16, 15, 13.5],'arrows':'1y'})
    links.append({'name':'CB_BG','location':[14.2,16, 14.2,18],'arrows':'1y'})
    links.append({'name':'CB_BG','location':[14.2,16, 14.2,18],'arrows':'1y'})  
    links.append({'name':'_PO','location':[3,8.5, 6,8.5],'arrows':'1x'})  
    links.append({'name':'_A','location':[3,17, 11,17],'arrows':'1x'})  
    links.append({'name':'A_','location':[11,17.3, 3,17.3],'arrows':'1x'}) 
    links.append({'name':'_T4','location':[10.25,17, 10.25,13.5],'arrows':'1y'}) 
    links.append({'name':'_C','location':[3,20.5, 7.25,20.5],'arrows':'2x'}) 
    links.append({'name':'_E','location':[3,22.5, 7.25,22.5],'arrows':'1x'}) 
    links.append({'name':'_H','location':[3,25.5, 7.25,25.5],'arrows':'2x'})
    links.append({'name':'_J','location':[7.25,27.5, 3,27.5],'arrows':'1x'})
    links.append({'name':'_F','location':[3,24.5, 9.75,24.5],'arrows':'1x'})
    links.append({'name':'_K','location':[3,32, 7.75,32, 7.75, 30],'arrows':'1y'})
    links.append({'name':'_L','location':[10,37, 10, 30],'arrows':'1y'})
    links.append({'name':'C_T3','location':[8.25,20.2, 8.6, 20.2, 8.6, 13.5],'arrows':'1y'})
    links.append({'name':'E_T3','location':[8.25,22.2, 8.7, 22.2, 8.7, 13.5],'arrows':'1y'})
    links.append({'name':'H_T3','location':[8.25,25.5, 8.8, 25.5, 8.8, 13.5],'arrows':'1y'})
    links.append({'name':'K_T3','location':[8.25,29.5, 9, 29.5, 9, 13.5],'arrows':'1y'})
    links.append({'name':'L_T3','location':[9.5,29.5, 9.3, 29.5, 9.3, 13.5],'arrows':'1y'})
    links.append({'name':'F_G','location':[10.75,24.5, 11.5,24.5],'arrows':'1x'})
    links.append({'name':'C_CB','location':[8.25,20.5, 13.2,20.5],'arrows':'2x'})
    links.append({'name':'E_CB','location':[8.25,22.5, 13.2,22.5],'arrows':'2x'})
    links.append({'name':'K_CB','location':[9,23.8, 13.2,23.8],'arrows':'1x'})
    links.append({'name':'G_B','location':[11.75,24, 11.75,18.8],'arrows':'1y'})
    links.append({'name':'B_T5','location':[12,18, 12.4,18, 12.4, 12.75, 12, 12.75],'arrows':'1x'})
    links.append({'name':'_down','location':[18,13,18,15],'arrows':'1y'})
    links.append({'name':'V1','location':[17.5,15,18.5,15],'arrows':'0'})
    links.append({'name':'_RN','location':[17.5,15,17.5,16],'arrows':'1y'})
    links.append({'name':'RN_down','location':[17.5,17,17.5,37],'arrows':'1y'})
    links.append({'name':'CB_D','location':[14.25,20.5,15.5,20.5],'arrows':'1x'})
    links.append({'name':'RN_D','location':[17.5,20.5,16.5,20.5],'arrows':'1x'})
    links.append({'name':'D_down','location':[16,21,16,23],'arrows':'1y'})
    links.append({'name':'RN_I','location':[17.5,25.5,16.5,25.5],'arrows':'1x'})
    links.append({'name':'I_down','location':[16,26,16,28],'arrows':'1y'})
    links.append({'name':'_PiMd','location':[18.5,15,18.5,26],'arrows':'1y'})
    links.append({'name':'PiMd_down','location':[18.5,27, 18.5,37],'arrows':'1y'})
    links.append({'name':'CB_BS-SMN','location':[14.25,23.5, 20,23.5],'arrows':'2x'})
    links.append({'name':'B_S_1','location':[20,18, 19,18],'arrows':'2x'})
    links.append({'name':'B_S_2','location':[20,25, 19,25],'arrows':'2x'})
    links.append({'name':'B_S_3','location':[21,18, 22,18],'arrows':'2x'})
    links.append({'name':'B_S_4','location':[21,25, 22,25],'arrows':'2x'})
    links.append({'name':'down2','location':[22,13, 22,15],'arrows':'1y'})
    links.append({'name':'V2','location':[20.5,15, 23.5,15],'arrows':'0'})
    links.append({'name':'_BS-SMN','location':[20.5,15, 20.5,17],'arrows':'1y'})
    links.append({'name':'down_2','location':[ 23.5,15, 23.5, 37],'arrows':'1y'})
    links.append({'name':'BS-SMN_down','location':[20.5,26, 20.5,37],'arrows':'1y'})
    links.append({'name':'BS_1','location':[20.5,27, 21.5,27],'arrows':'1x'})
    links.append({'name':'BS_2','location':[20.5,28, 19.5,28],'arrows':'1x'})
    links.append({'name':'BS_3','location':[20.5,29, 19.5,29],'arrows':'1x'})
    links.append({'name':'BS_4','location':[20.5,30, 21.5,30],'arrows':'1x'})

    links.append({'name':'_1','location':[23.5,27, 22.5,27],'arrows':'1x'})
    links.append({'name':'_2','location':[23.5,28, 24.5,28],'arrows':'1x'})
    links.append({'name':'_3','location':[23.5,29, 22.5,29],'arrows':'1x'})
    links.append({'name':'_4','location':[23.5,30, 24.5,30],'arrows':'1x'})

    links.append({'name':'_5','location':[23.5,18, 24.5,18],'arrows':'1x'})
    links.append({'name':'_6','location':[23.5,19, 22.5,19],'arrows':'1x'})
    links.append({'name':'_7','location':[23.5,20, 24.5,20],'arrows':'1x'})



    n=0
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
                if box['name'] == 'PiMd':
                 frame.canvas.create_rectangle(box['location'], fill='pink', width=2, dash=(4, 2))
                else:
                 frame.canvas.create_rectangle(box['location'],fill='pink',width=2)
                count=1
            else:
                break
        n+=1
        loc=box['location']
        x1=loc[0]+0.5*dx
        y1=loc[1]+0.5*dx
        frame.canvas.create_text(x1,y1,anchor="center",text=box['name'],
        font=("Times New Roman",8),tags='text'+str(n))
    
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


     
    
    frame.canvas.update
    frame.canvas.pack()
    #root.after(t,refreshCanvas)
    frame.canvas.addtag_all('all')    
    root.mainloop()
    
if __name__ == '__main__':
    main()
