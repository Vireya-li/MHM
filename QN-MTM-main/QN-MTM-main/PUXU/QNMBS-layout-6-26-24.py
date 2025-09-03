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
        self.h = int(self.root.winfo_screenheight()*2.3)  # Adjust the scaling factor as needed
        self.canvas = tkinter.Canvas(root, width=self.w, height=self.h)
        self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
        root.bind('<Configure>', self.resize)
    def resize(self, event):
      wscale = event.width / self.w
      hscale = event.height / self.h

      h_font = self.h / 36
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
    Capacity['9']=5
    Capacity['10']=5
    Capacity['11']=5
    Capacity['12']=5
    Capacity['A']=4
    Capacity['B']=4
    Capacity['C']=5
    Capacity['D']=10e5
    Capacity['E']=1
    Capacity['F']=1
    Capacity['G']=10e5
    Capacity['H'] = 10e5  #unknown
    Capacity['K'] = 10e5
    Capacity['O'] = 10e5
    Capacity['S'] = 10e5
    Capacity['T'] = 10e5
    Capacity['W']=1
    Capacity['X'] = 10e5  #unknown
    Capacity['Y']=2
    Capacity['Z']=5
    Capacity['V']=10e5    #unknown
    Capacity['21']=1     #mouth
    Capacity['22'] = 1   #eye
    Capacity['23']=1     #lefthand
    Capacity['24']=1     #righthand
    Capacity['25']=1
    Capacity['26']=1
    Capacity['27']=1
    Capacity['31']=1
    Capacity['32']=1
    Capacity['33']=1
    Capacity['34']=1
    Capacity['51L']=1
    Capacity['52L']=1
    Capacity['53L']=1
    Capacity['54L']=1
    Capacity['51R']=1
    Capacity['52R']=1
    Capacity['53R']=1
    Capacity['54R']=1
    Capacity['41L']=1
    Capacity['42L']=1
    Capacity['43L']=1
    Capacity['44L']=1
    Capacity['41R']=1
    Capacity['42R']=1
    Capacity['43R']=1
    Capacity['44R']=1
    Capacity['101']=1
    Capacity['102']=1
    Capacity['103']=1
    Capacity['104']=1
    Capacity['105']=1
    Capacity['106']=1
    Capacity['61L']=1
    Capacity['62L']=1
    Capacity['63L']=1
    Capacity['64L']=1
    Capacity['65L']=1
    Capacity['61R']=1
    Capacity['62R']=1
    Capacity['63R']=1
    Capacity['64R']=1
    Capacity['65R']=1

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
    Boxes.append({'name':'9','location':[5, 14,6, 15]})
    Boxes.append({'name':'10','location':[5, 16,6, 17]})
    Boxes.append({'name':'11','location':[5, 18,6, 19]})
    Boxes.append({'name':'12','location':[5, 20,6, 21]})
    Cache.append({'name':'0_5','location':[2.5,10,3,11]})
    Cache.append({'name':'5_6','location':[4.5,8,5,9]})
    Cache.append({'name':'5_7','location':[4.5,12,5,13]})
    Cache.append({'name':'6_8','location':[7,9.5,8,10]})
    Cache.append({'name':'7_8','location':[7,11,8,11.5]})
    Cache.append({'name':'0_9','location':[4.5,14,5,15]})
    Cache.append({'name':'0_10','location':[4.5,16,5,17]})
    Cache.append({'name':'0_11','location':[4.5,18,5,19]})
    Cache.append({'name':'0_12','location':[4.5,20,5,21]})
     
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
    Cache.append({'name':'KOST_C','location':[12.7,8.5,13.2,9]})

    Boxes.append({'name':'D','location':[13, 5, 14, 6]})
    Cache.append({'name':'G_D','location':[14,5,14.5,6]})
    Cache.append({'name':'C_D','location':[13.3,6,13.7,6.4]})

    Boxes.append({'name':'E','location':[13.5, 18, 14.5, 19]})
    Cache.append({'name':'_E','location':[13,18,13.5,19]})


    Boxes.append({'name':'F','location':[13, 10, 14, 11]})
    Cache.append({'name':'C_F','location':[13,9.5,14,10]})
    Cache.append({'name':'H_F','location':[14,10,14.4,11]})

    Boxes.append({'name':'H','location':[15, 10, 16, 11]})
    Cache.append({'name':'C_H','location':[14.6,9.5,15,10]})
    Cache.append({'name':'G_H','location':[15,9.5,16,10]})
    Cache.append({'name':'F_H','location':[14.6,10,15,11]})
    Cache.append({'name':'E_H','location':[15,11,16,11.5]})


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
    Cache.append({'name':'B_X','location':[20,12,21,12.5]})
    #Cache.append({'name':'21_X','location':[20.5,12,21,12.5]})
    Cache.append({'name':'Z_X','location':[21,11,21.5,12]})
    Cache.append({'name':'A_X','location':[19.5,11.3,20,12]})

    Boxes.append({'name':'Z','location':[22, 9, 23, 10]})
    Cache.append({'name':'V_Z','location':[22,8.5,23,9]})
    Cache.append({'name':'Y_Z','location':[21.5,9,22,10]})
    Cache.append({'name':'E_Z','location':[22.6,10,23,10.5]})

    Boxes.append({'name':'K','location':[10.2, 14, 11.2, 15]})
    Cache.append({'name':'9_K','location':[9.7,14,10.2,15]})

    Boxes.append({'name':'O','location':[10.2, 16, 11.2, 17]})
    Cache.append({'name':'10_O','location':[9.7,16,10.2,17]})


    Boxes.append({'name':'S','location':[10.2, 18, 11.2, 19]})
    Cache.append({'name':'11_S','location':[9.7,18,10.2,19]})


    Boxes.append({'name':'T','location':[10.2, 20, 11.2, 21]})
    Cache.append({'name':'12_T','location':[9.7,20,10.2,21]})


    Boxes.append({'name':'51L','location':[7, 30, 8, 31]})
    Cache.append({'name':'_51','location':[7,29.7,8,30]})
    Cache.append({'name':'51_','location':[7,31,8,31.3]})

    Boxes.append({'name':'52L','location':[7, 32, 8, 33]})
    Cache.append({'name':'_52','location':[7,31.7,8,32]})
    Cache.append({'name':'52_','location':[7,33,8,33.3]})
    Cache.append({'name':'_52_','location':[8,32,8.3,33]})


    Boxes.append({'name':'53L','location':[7, 34, 8, 35]})
    Cache.append({'name':'_53','location':[7,33.7,8,34]})
    Cache.append({'name':'53_','location':[7,35,8,35.3]})
    Cache.append({'name':'_53_','location':[8,34,8.3,35]})

    Boxes.append({'name':'54L','location':[7, 36, 8, 37]})
    Cache.append({'name':'_54','location':[7,35.7,8,36]})
    Cache.append({'name':'_54_','location':[8,36,8.3,37]})
    #Cache.append({'name':'53_','location':[7,35,8,35.3]})

    Boxes.append({'name':'51R','location':[17, 30, 18, 31]})
    Cache.append({'name':'_51','location':[17,29.7,18,30]})
    Cache.append({'name':'51_','location':[17,31,18,31.3]})

    Boxes.append({'name':'52R','location':[17, 32, 18, 33]})
    Cache.append({'name':'_52','location':[17,31.7,18,32]})
    Cache.append({'name':'52_','location':[17,33,18,33.3]})
    Cache.append({'name':'_52_','location':[16.7,32,17,33]})

    Boxes.append({'name':'53R','location':[17, 34, 18, 35]})
    Cache.append({'name':'_53','location':[17,33.7,18,34]})
    Cache.append({'name':'53_','location':[17,35,18,35.3]})
    Cache.append({'name':'_53_','location':[16.7,34,17,35]})

    Boxes.append({'name':'54R','location':[17, 36, 18, 37]})
    Cache.append({'name':'_54','location':[17,35.7,18,36]})
    Cache.append({'name':'_54_','location':[16.7,36,17,37]})

    Boxes.append({'name':'41L','location':[4.5, 26, 5.5, 27]})
    Cache.append({'name':'_41','location':[4.5,25.7,5.5,26]})
    Cache.append({'name':'41_','location':[4.5,27,5.5,27.3]})

    Boxes.append({'name':'42L','location':[4.5, 28, 5.5, 29]})
    Cache.append({'name':'_42','location':[4.5,27.7,5.5,28]})
    Cache.append({'name':'42_','location':[4.5,29,5.5,29.3]})
    Cache.append({'name':'_42_','location':[5.5,28,5.7,29]})

    Boxes.append({'name':'43L','location':[4.5, 30, 5.5, 31]})
    Cache.append({'name':'_43','location':[4.5,29.7,5.5,30]})
    Cache.append({'name':'43_','location':[4.5,31,5.5,31.3]})
    Cache.append({'name':'_43_','location':[5.5,30,5.7,31]})


    Boxes.append({'name':'44L','location':[4.5, 32, 5.5, 33]})
    Cache.append({'name':'_44','location':[4.5,31.7,5.5,32]})
    Cache.append({'name':'44_','location':[4.5,33,5.5,33.3]})
    Cache.append({'name':'_44_','location':[5.5,32,5.7,33]})

    Boxes.append({'name':'41R','location':[19.5, 26, 20.5, 27]})
    Cache.append({'name':'_41','location':[19.5,25.7,20.5,26]})
    Cache.append({'name':'41_','location':[19.5,27,20.5,27.3]})

    Boxes.append({'name':'42R','location':[19.5, 28, 20.5, 29]})
    Cache.append({'name':'_42','location':[19.5,27.7,20.5,28]})
    Cache.append({'name':'42_','location':[19.5,29,20.5,29.3]})
    Cache.append({'name':'_42_','location':[19.3,28,19.5,29]})

    Boxes.append({'name':'43R','location':[19.5, 30, 20.5, 31]})
    Cache.append({'name':'_43','location':[19.5,29.7,20.5,30]})
    Cache.append({'name':'43_','location':[19.5,31,20.5,31.3]})
    Cache.append({'name':'_43_','location':[19.3,30,19.5,31]})

    Boxes.append({'name':'44R','location':[19.5, 32, 20.5, 33]})
    Cache.append({'name':'_44','location':[19.5,31.7,20.5,32]})
    Cache.append({'name':'44_','location':[19.5,33,20.5,33.3]})
    Cache.append({'name':'_44_','location':[19.3,32,19.5,33]})

    Boxes.append({'name':'65L','location':[0.3, 35.1, 1.3, 35.9]})#
    Cache.append({'name':'_65L','location':[0.3,34.8,1.3,35.1]})

    Boxes.append({'name':'64L','location':[1.5, 35.1, 2.5, 35.9]})
    Cache.append({'name':'_64L','location':[1.5,34.8,2.5,35.1]})
    
    Boxes.append({'name':'63L','location':[2.7, 35.1, 3.7, 35.9]})
    Cache.append({'name':'_63L','location':[2.7,34.8,3.7,35.1]})
    
    Boxes.append({'name':'62L','location':[3.9, 35.1, 4.9, 35.9]})
    Cache.append({'name':'_62L','location':[3.9,34.8,4.9,35.1]})

    Boxes.append({'name':'61L','location':[5.4, 35.1, 6.4, 35.9]})
    Cache.append({'name':'_61L','location':[5.4,34.8,6.4,35.1]})

    Boxes.append({'name':'61R','location':[18.65, 35.1, 19.65, 35.9]})
    Cache.append({'name':'_61R','location':[18.65,34.8,19.65,35.1]})

    
    Boxes.append({'name':'62R','location':[20.15, 35.1, 21.15, 35.9]})
    Cache.append({'name':'_62R','location':[20.15,34.8,21.15,35.1]})

    Boxes.append({'name':'63R','location':[21.35, 35.1, 22.35, 35.9]})
    Cache.append({'name':'_63R','location':[21.35,34.8,22.35,35.1]})

    Boxes.append({'name':'64R','location':[22.55, 35.1, 23.55, 35.9]})
    Cache.append({'name':'_64R','location':[22.55,34.8,23.55,35.1]})

    Boxes.append({'name':'65R','location':[23.75, 35.1, 24.75, 35.9]})
    Cache.append({'name':'_65R','location':[23.75,34.8,24.75,35.1]})

    Boxes.append({'name':'101','location':[9.14, 34.6, 10.14, 35.4]})
    Cache.append({'name':'_101','location':[9.14,34.3,10.14,34.6]})

    Boxes.append({'name':'102','location':[10.28, 34.6, 11.28, 35.4]})
    Cache.append({'name':'_102','location':[10.28,34.3,11.28,34.6]})

    Boxes.append({'name':'103','location':[11.42, 34.6, 12.43, 35.4]})
    Cache.append({'name':'_103','location':[11.42,34.3,12.43,34.6]})

    Boxes.append({'name':'104','location':[12.56, 34.6, 13.56, 35.4]})
    Cache.append({'name':'_104','location':[12.56,34.3,13.56,34.6]})

    Boxes.append({'name':'105','location':[13.7, 34.6, 14.7, 35.4]})
    Cache.append({'name':'_105','location':[13.7,34.3,14.7,34.6]})

    Boxes.append({'name':'106','location':[14.84, 34.6, 15.84, 35.4]})
    Cache.append({'name':'_106','location':[14.84,34.3,15.84,34.6]})



    Boxes.append({'name':'21','location':[7.5, 23.7, 8.5, 24.7]})
    Cache.append({'name':'_21_','location':[7.5,23.2,8.5,23.7]})

    Boxes.append({'name':'22','location':[9, 23.7, 10, 24.7]})
    Cache.append({'name':'_22_','location':[9,23.2,10,23.7]})

    Boxes.append({'name':'23','location':[10.5, 23.7, 11.5, 24.7]})
    Cache.append({'name':'_23_','location':[10.5,23.2,11.5,23.7]})

    Boxes.append({'name':'24','location':[12, 23.7, 13, 24.7]})
    Cache.append({'name':'_24_','location':[12,23.2,13,23.7]})

    Boxes.append({'name':'25','location':[13.5, 23.7, 14.5, 24.7]})
    Cache.append({'name':'_25_','location':[13.5,23.2,14.5,23.7]})

    Boxes.append({'name':'26','location':[15, 23.7, 16, 24.7]})
    Cache.append({'name':'_26_','location':[15,23.2,16,23.7]})

    Boxes.append({'name':'27','location':[16.5, 23.7, 17.5, 24.7]})
    Cache.append({'name':'_27_','location':[16.5,23.2,17.5,23.7]})

    Boxes.append({'name':'31','location':[12, 26, 13, 27]})
    Cache.append({'name':'_31','location':[12,25.7,13,26]})
    Cache.append({'name':'31_','location':[12,27,13,27.3]})

    Boxes.append({'name':'32','location':[12, 28, 13, 29]})
    Cache.append({'name':'_32','location':[12,27.7,13,28]})
    Cache.append({'name':'32_','location':[12,29,13,29.3]})
    Cache.append({'name':'_32_','location':[13,28,13.3,29]})

    Boxes.append({'name':'33','location':[12, 30, 13, 31]})
    Cache.append({'name':'_33','location':[12,29.7,13,30]})
    Cache.append({'name':'33_','location':[12,31,13,31.3]})
    Cache.append({'name':'_33_','location':[13,30,13.3,31]})

    Boxes.append({'name':'34','location':[12, 32, 13, 33]})
    Cache.append({'name':'_34','location':[12,31.7,13,32]})
    Cache.append({'name':'_34_','location':[13,32,13.3,33]})
    #Cache.append({'name':'34_','location':[12,33,13,33.3]})

    #Cache.append({'name':'Z_21','location':[23.5,3,24,4]})
    #Cache.append({'name':'Z_22','location':[23.5,5.5,24,6.5]})
    #Cache.append({'name':'Z_23','location':[23.5,9,24,10]})
    #Cache.append({'name':'Z_24','location':[23.5,11,24,12]})

    links=list()
    links.append({'name':'enter_1','location':[1.9, 7, 0.9, 7],'arrows':'1x'})
    links.append({'name':'enter_2','location':[0.9, 12.5, 1.9, 12.5],'arrows':'1x'})
    links.append({'name':'enter_3','location':[1.9, 19.5, 0.9, 19.5],'arrows':'1x'})
    links.append({'name':'enter_4','location':[0.9, 25.5, 1.9, 25.5],'arrows':'1x'})
    links.append({'name':'0_1','location':[1.9, 3.5, 3,  3.5],'arrows':'1x'}) 
    links.append({'name':'0_9','location':[1.9, 14.5, 5,  14.5],'arrows':'1x'}) 
    links.append({'name':'0_10','location':[1.9, 16.5, 5,  16.5],'arrows':'1x'}) 
    links.append({'name':'0_11','location':[1.9, 18.5, 5,  18.5],'arrows':'1x'})
    links.append({'name':'0_12','location':[1.9, 20.5, 5,  20.5],'arrows':'1x'})
    links.append({'name':'9_K','location':[6, 14.5, 10.2,  14.5],'arrows':'1x'})
    links.append({'name':'10_O','location':[6, 16.5, 10.2,  16.5],'arrows':'1x'})
    links.append({'name':'11_S','location':[6, 18.5, 10.2,  18.5],'arrows':'1x'})
    links.append({'name':'12_T','location':[6, 20.5, 10.2,  20.5],'arrows':'1x'})

    ####
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

    ###

    #links.append({'name':'Z_24','location':[23.3, 11.5, 24, 11.5],'arrows':'1x'}) 
    links.append({'name':'G_D','location':[15.5, 7.5, 15.5, 5.5, 14, 5.5],'arrows':'1x'}) 
    links.append({'name':'Z_X','location':[22.5, 10, 22.5, 11.5, 21, 11.5],'arrows':'1x'}) 
    #links.append({'name':'Z_21','location':[23, 9.5, 23.3,9.5,23.3, 3.5, 24, 3.5],'arrows':'1x'})#### 
    links.append({'name':'C_W','location':[12.9, 7.5, 12.9, 1.9, 18.7, 1.9, 18.7, 5.8, 20, 5.8],'arrows':'1x'})
    links.append({'name':'X_W','location':[20, 11.1, 19.3, 11.1, 19.3, 6.4,20, 6.4],'arrows':'1x'})  
    links.append({'name':'D_W','location':[13.5, 5, 13.5, 2.5, 17, 2.5,17, 6, 20, 6],'arrows':'1x'}) 
    #links.append({'name':'Right_Left','location':[25.3, 7.7, 27, 7.7, 27, 14.6,1, 14.6, 1, 7,1.9, 7],'arrows':'1x'}) 
    links.append({'name':'2_4','location':[6, 1.5, 7.5, 1.5, 7.5, 3],'arrows':'1y'})
    links.append({'name':'3_4','location':[6, 5.5, 7.5, 5.5, 7.5, 4],'arrows':'1y'})
    links.append({'name':'6_8','location':[6, 8.5, 7.5, 8.5, 7.5, 10],'arrows':'1y'})
    links.append({'name':'7_8','location':[6, 12.5, 7.5, 12.5, 7.5, 11],'arrows':'1y'})
    links.append({'name':'A_V','location':[11.3, 6, 11.3, 1, 20.5, 1, 20.5, 3],'arrows':'1y'})  
    links.append({'name':'B_X','location':[11.3, 10, 11.3, 13.3, 20.3, 13.3, 20.3, 12],'arrows':'1y'})  
    links.append({'name':'D_C','location':[13.5, 6, 13.5, 7.5],'arrows':'1y'}) 
    # Changed C_D to bidirectional
    links.append({'name':'C_D','location':[13.5, 7.5, 13.5, 6],'arrows':'1y'}) 
    links.append({'name':'V_W','location':[20.5, 4, 20.5, 5.5],'arrows':'1y'}) 
    links.append({'name':'W_Y','location':[20.5, 6.5, 20.5, 9],'arrows':'1y'})  
    links.append({'name':'X_Y','location':[20.5, 11, 20.5, 10],'arrows':'1y'})  
    # X to C
    links.append({'name':'X_C','location':[20, 11.2, 12.1, 11.2,12.1,8.25,12.7,8.25],'arrows':'1x'}) 
    #links.append({'name':'Y_C','location':[20, 9.5, 17, 9.5, 17, 12.5, 12.9, 12.5, 12.9, 8.5],'arrows':'1y'})  
    links.append({'name':'C_Y','location':[12.9, 8.5, 12.9, 12.5, 17, 12.5, 17, 9.5, 20, 9.5],'arrows':'1y'})
    links.append({'name':'V_Z','location':[21, 3.5, 22.5, 3.5, 22.5, 9],'arrows':'1y'})   
    #links.append({'name':'24_X','location':[25, 11.5, 25.3, 11.5,25.3, 3.5, 25.3, 13.3, 
    #20.7, 13.3, 20.7, 12],'arrows':'1y'})  
    links.append({'name':'C_V','location':[12.8, 7.5, 12.8, 1.6,19, 1.6,19, 3.3,20, 3.3],'arrows':'1y'})   
    #links.append({'name':'_27','location':[17, 23, 17, 22],'arrows':'2y'})
    #links.append({'name':'_21','location':[8, 22, 8, 23.5],'arrows':'2y'})

    links.append({'name':'F_C','location':[13.5, 8.5, 13.5, 10],'arrows':'2y'})
    links.append({'name':'G_H','location':[15.5, 8.5, 15.5, 10],'arrows':'2y'})


    links.append({'name':'_21','location':[8, 22, 8, 23.7],'arrows':'2y'})#
    #links.append({'name':'21_','location':[8, 23, 8, 22],'arrows':'1y'})#
    links.append({'name':'_22','location':[9.5, 22, 9.5, 23.7],'arrows':'2y'})
    #inks.append({'name':'22_','location':[9.5, 23, 9.5, 22],'arrows':'1y'})
    links.append({'name':'_23','location':[11, 22, 11, 23.7],'arrows':'2y'})
    #links.append({'name':'23_','location':[11, 23.5, 11, 22],'arrows':'1y'})
    links.append({'name':'_24','location':[12.5, 22, 12.5, 23.7],'arrows':'2y'})
    #links.append({'name':'24_','location':[12.5, 23.5, 12.5, 22],'arrows':'1y'})
    links.append({'name':'_25','location':[14, 22, 14, 23.7],'arrows':'2y'})
    #links.append({'name':'25_','location':[14, 23.5, 14, 22],'arrows':'1y'})
    links.append({'name':'_26','location':[15.5, 22, 15.5, 23.7],'arrows':'2y'})
    #links.append({'name':'26_','location':[15.5, 23.5, 15.5, 22],'arrows':'1y'})
    #links.append({'name':'_27','location':[17, 22, 17, 23],'arrows':'2y'})
    links.append({'name':'27_','location':[17, 22, 17, 23.7],'arrows':'2y'})
    #links.append({'name':'_27','location':[17, 23.5, 17, 22],'arrows':'1y'})

    links.append({'name':'15_','location':[1.9, 3.5, 1.9, 10.5],'arrows':'0'})
    #links.append({'name':'23_24','location':[23.3, 11.5, 23.3, 9.5],'arrows':'0'})
    #links.append({'name':'F_C','location':[13.5, 8.5, 13.5, 10],'arrows':'2y'})
    #links.append({'name':'G_H','location':[15.5, 8.5, 15.5, 10],'arrows':'2y'})
    links.append({'name':'G_C','location':[14, 10.5, 15, 10.5],'arrows':'2x'})
    links.append({'name':'C_H','location':[13.7, 8.5, 15, 10],'arrows':'slope'})

    #links.append({'name':'G_C','location':[15, 8, 13.7, 8],'arrows':'1x'}) 
    links.append({'name':'Y_Z','location':[21, 9.5, 22, 9.5],'arrows':'1x'}) 
    #links.append({'name':'Z_22','location':[23.3, 6, 24, 6],'arrows':'1x'}) 
    links.append({'name':'Z_right','location':[23, 9.5, 24, 9.5],'arrows':'1x'}) 
    links.append({'name':'right_down','location':[24, 9.5, 24, 21.5],'arrows':'0'})#################
    links.append({'name':'down_left','location':[24, 21.5, 12.5, 21.5],'arrows':'1x'})
    links.append({'name':'left_down','location':[12.5, 21.5, 12.5, 22],'arrows':'0'})#
    links.append({'name':'down_left_2','location':[12.5, 22, 1.9, 22],'arrows':'1x'})
    links.append({'name':'down_right','location':[12.5, 22, 17, 22],'arrows':'1x'})
    links.append({'name':'left_up','location':[1.9, 22, 1.9, 7],'arrows':'0'})
    links.append({'name':'up_down','location':[1.9, 22, 1.9, 26],'arrows':'0'})

    links.append({'name':'K_right','location':[11.2, 14.5, 11.7,  14.5],'arrows':'1x'})
    links.append({'name':'O_right','location':[11.2, 16.5, 11.7,  16.5],'arrows':'1x'})
    links.append({'name':'S_right','location':[11.2, 18.5, 11.7,  18.5],'arrows':'1x'})
    links.append({'name':'T_right','location':[11.2, 20.5, 11.7,  20.5],'arrows':'1x'})
    links.append({'name':'KOST','location':[11.7, 14.5, 11.7,  20.5],'arrows':'0'})
    links.append({'name':'S_E','location':[11.7, 18.5, 13.5,  18.5],'arrows':'1x'})

    links.append({'name':'E_right','location':[14.5, 18.5, 24,  18.5],'arrows':'1x'})
    links.append({'name':'E_up','location':[12.8, 18.5, 12.8,  8.5],'arrows':'2y'})
    links.append({'name':'E_H','location':[15.5, 18.5,15.5,  11],'arrows':'1y'})
    links.append({'name':'H_E','location':[15.5,  11,15.5, 18.5],'arrows':'1y'})
    links.append({'name':'E_Z','location':[22.75, 18.5,22.75,  10],'arrows':'1y'})

    links.append({'name':'connection','location':[6.5, 22, 6.5, 25],'arrows':'1y'})
    links.append({'name':'connection_','location':[6.5, 25, 6.5, 22],'arrows':'1y'})
    links.append({'name':'connection2','location':[1.9, 25, 20, 25],'arrows':'2x'})
    links.append({'name':'connection3','location':[18.3, 21.5, 18.3, 25],'arrows':'1y'})

    links.append({'name':'_41L','location':[5, 25, 5, 26],'arrows':'2y'})
    links.append({'name':'42_41L','location':[5, 27, 5, 28],'arrows':'2y'})
    links.append({'name':'43_42L','location':[5, 29, 5, 30],'arrows':'2y'})
    links.append({'name':'44_43L','location':[5, 31, 5, 32],'arrows':'2y'})
    links.append({'name':'44_L','location':[5, 33, 5, 34],'arrows':'2y'})
    links.append({'name':'6L','location':[0.8, 34, 6.2, 34],'arrows':'0'})
    links.append({'name':'_61L','location':[0.8, 34, 0.8,35.1],'arrows':'2y'})
    links.append({'name':'_62L','location':[2, 34, 2,35.1],'arrows':'2y'})
    links.append({'name':'_63L','location':[3.2, 34, 3.2,35.1],'arrows':'2y'})
    links.append({'name':'_64L','location':[4.4, 34, 4.4,35.1],'arrows':'2y'})
    links.append({'name':'_65L','location':[6.2, 34, 6.2,35.1],'arrows':'2y'})
    links.append({'name':'4L','location':[6, 34, 6,25],'arrows':'2y'})
    links.append({'name':'42L_','location':[5.5, 28.5, 6,28.5],'arrows':'2y'})
    links.append({'name':'43-L_','location':[5.5,30.5, 6,30.5],'arrows':'2y'})
    links.append({'name':'44L_','location':[5.5, 32.5, 6,32.5],'arrows':'2y'})

    links.append({'name':'_41R','location':[20, 25, 20, 26],'arrows':'2y'})
    links.append({'name':'42_41R','location':[20, 27, 20, 28],'arrows':'2y'})
    links.append({'name':'43_42R','location':[20, 29, 20, 30],'arrows':'2y'})
    links.append({'name':'44_43R','location':[20, 31, 20, 32],'arrows':'2y'})
    links.append({'name':'44_R','location':[20, 33, 20, 34],'arrows':'2y'})
    links.append({'name':'6R','location':[18.85, 34, 24.25, 34],'arrows':'0'})
    links.append({'name':'_61R','location':[18.85, 34, 18.85,35.1],'arrows':'2y'})
    links.append({'name':'_62R','location':[20.65, 34, 20.65,35.1],'arrows':'2y'})
    links.append({'name':'_63R','location':[21.85, 34, 21.85,35.1],'arrows':'2y'})
    links.append({'name':'_64R','location':[23.05, 34, 23.05,35.1],'arrows':'2y'})
    links.append({'name':'_65R','location':[24.25, 34, 24.25,35.1],'arrows':'2y'})
    links.append({'name':'4R','location':[19, 34, 19,25],'arrows':'2y'})
    links.append({'name':'42R_','location':[19, 28.5, 19.5,28.5],'arrows':'2y'})
    links.append({'name':'43R_','location':[19,30.5, 19.5,30.5],'arrows':'2y'})
    links.append({'name':'44R_','location':[19, 32.5, 19.5,32.5],'arrows':'2y'})

    links.append({'name':'_51L','location':[7.5, 25, 7.5, 30],'arrows':'2y'})
    links.append({'name':'52_51L','location':[7.5, 31, 7.5, 32],'arrows':'2y'})
    links.append({'name':'53_52L','location':[7.5, 33, 7.5, 34],'arrows':'2y'})
    links.append({'name':'54_53L','location':[7.5, 35, 7.5, 36],'arrows':'2y'})
    links.append({'name':'52L_','location':[8, 32.5, 9,32.5],'arrows':'2x'})
    links.append({'name':'53L_','location':[8,34.5, 9,34.5],'arrows':'2x'})
    links.append({'name':'54L_','location':[8, 36.5, 9,36.5],'arrows':'2x'})
    links.append({'name':'5L','location':[9, 36.5, 9,25],'arrows':'2y'})

    links.append({'name':'_51R','location':[17.5, 25, 17.5, 30],'arrows':'2y'})
    links.append({'name':'52_51R','location':[17.5, 31, 17.5, 32],'arrows':'2y'})
    links.append({'name':'53_52R','location':[17.5, 33, 17.5, 34],'arrows':'2y'})
    links.append({'name':'54_53R','location':[17.5, 35, 17.5, 36],'arrows':'2y'})
    links.append({'name':'52R_','location':[17 ,32.5, 16,32.5],'arrows':'2x'})
    links.append({'name':'53R_','location':[17,34.5, 16,34.5],'arrows':'2x'})
    links.append({'name':'54R_','location':[17, 36.5, 16,36.5],'arrows':'2x'})
    links.append({'name':'5R','location':[16, 36.5, 16,25],'arrows':'2y'})

    links.append({'name':'_31','location':[12.5, 26, 12.5, 25],'arrows':'2y'})
    links.append({'name':'32_31','location':[12.5, 27, 12.5, 28],'arrows':'2y'})
    links.append({'name':'33_32','location':[12.5, 29, 12.5, 30],'arrows':'2y'})
    links.append({'name':'34_33','location':[12.5, 31, 12.5, 32],'arrows':'2y'})
    links.append({'name':'32_','location':[13 ,28.5, 14,28.5],'arrows':'2x'})
    links.append({'name':'33_','location':[13,30.5, 14,30.5],'arrows':'2x'})
    links.append({'name':'34_','location':[13, 32.5, 14,32.5],'arrows':'2x'})
    links.append({'name':'3*','location':[14, 32.5, 14,25],'arrows':'2y'})

    links.append({'name':'_101','location':[9.7, 34.5, 9.7,33.5],'arrows':'2y'})
    links.append({'name':'_102','location':[10.9, 34.5, 10.9,33.5],'arrows':'2y'})
    links.append({'name':'_103','location':[11.9, 34.5, 11.9,33.5],'arrows':'2y'})
    links.append({'name':'_104','location':[13.06, 34.5, 13.06,33.5],'arrows':'2y'})
    links.append({'name':'_105','location':[14.2, 34.5, 14.2,33.5],'arrows':'2y'})
    links.append({'name':'_106','location':[15.34, 34.5, 15.34,33.5],'arrows':'2y'})
    links.append({'name':'100','location':[9.7, 33.5, 15.34,33.5],'arrows':'0'})
    links.append({'name':'_100','location':[11, 25, 11,33.5],'arrows':'1y'})
    links.append({'name':'100_','location':[10.5, 33.5, 10.5,25],'arrows':'1y', 'dash': (5, 2)})




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
                if box['name'] in ['101', '102', '103', '104', '105', '106']:
                    frame.canvas.create_rectangle(box['location'], fill='pink', width=2, dash=(5, 5))  # Dashed edges
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
        9.4*dx+(m-1)*8.5*dx,21.2*dx, fill="",dash=(5,5),width=2)

    for cache in Cache:
        cache['visible']=True
        temp=cache['location']
        for m in range(4):
            temp[m]=temp[m]*dx
        cache['location']=temp
        if cache['visible']==True:
            frame.canvas.create_rectangle(cache['location'],fill='silver',width=2,dash=[15,15])
   
    #a1=[dx/3,dx/3,dx/15]
    a1=[dx/5,dx/5,dx/15]
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
                dash = link.get('dash', None)#
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
                        arrow="last",arrowshape=a1,tags='link_1y_'+str(count2), dash=dash)#
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
    #root.after(t,refreshCanvas)
    frame.canvas.addtag_all('all')    
    root.mainloop()
    
if __name__ == '__main__':
    main()
