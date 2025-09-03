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
    Cache = list()

    Boxes.append({'name':'51L','location':[7.0, 20.0, 8.0, 21.0]})
    Cache.append({'name':'_51','location':[7.0, 19.7, 8.0, 20.0]})
    Cache.append({'name':'51_','location':[7.0, 21.0, 8.0, 21.3]})

    Boxes.append({'name':'52L','location':[7.0, 22.0, 8.0, 23.0]})
    Cache.append({'name':'_52','location':[7.0, 21.7, 8.0, 22.0]})
    Cache.append({'name':'52_','location':[7.0, 23.0, 8.0, 23.299999999999997]})
    Cache.append({'name':'_52_','location':[8.0, 22.0, 8.3, 23.0]})


    Boxes.append({'name':'53L','location':[7.0, 24.0, 8.0, 25.0]})
    Cache.append({'name':'_53','location':[7.0, 23.700000000000003, 8.0, 24.0]})
    Cache.append({'name':'53_','location':[7.0, 25.0, 8.0, 25.299999999999997]})
    Cache.append({'name':'_53_','location':[8.0, 24.0, 8.3, 25.0]})

    Boxes.append({'name':'54L','location':[7.0, 26.0, 8.0, 27.0]})
    Cache.append({'name':'_54','location':[7.0, 25.700000000000003, 8.0, 26.0]})
    Cache.append({'name':'_54_','location':[8.0, 26.0, 8.3, 27.0]})
    #Cache.append({'name':'53_','location':[7.0, 25.0, 8.0, 25.299999999999997]})

    Boxes.append({'name':'51R','location':[17.0, 20.0, 18.0, 21.0]})
    Cache.append({'name':'_51','location':[17.0, 19.7, 18.0, 20.0]})
    Cache.append({'name':'51_','location':[17.0, 21.0, 18.0, 21.3]})

    Boxes.append({'name':'52R','location':[17.0, 22.0, 18.0, 23.0]})
    Cache.append({'name':'_52','location':[17.0, 21.7, 18.0, 22.0]})
    Cache.append({'name':'52_','location':[17.0, 23.0, 18.0, 23.299999999999997]})
    Cache.append({'name':'_52_','location':[16.7, 22.0, 17.0, 23.0]})

    Boxes.append({'name':'53R','location':[17.0, 24.0, 18.0, 25.0]})
    Cache.append({'name':'_53','location':[17.0, 23.700000000000003, 18.0, 24.0]})
    Cache.append({'name':'53_','location':[17.0, 25.0, 18.0, 25.299999999999997]})
    Cache.append({'name':'_53_','location':[16.7, 24.0, 17.0, 25.0]})

    Boxes.append({'name':'54R','location':[17.0, 26.0, 18.0, 27.0]})
    Cache.append({'name':'_54','location':[17.0, 25.700000000000003, 18.0, 26.0]})
    Cache.append({'name':'_54_','location':[16.7, 26.0, 17.0, 27.0]})

    Boxes.append({'name':'41L','location':[4.5, 16.0, 5.5, 17.0]})
    Cache.append({'name':'_41','location':[4.5, 15.7, 5.5, 16.0]})
    Cache.append({'name':'41_','location':[4.5, 17.0, 5.5, 17.3]})

    Boxes.append({'name':'42L','location':[4.5, 18.0, 5.5, 19.0]})
    Cache.append({'name':'_42','location':[4.5, 17.7, 5.5, 18.0]})
    Cache.append({'name':'42_','location':[4.5, 19.0, 5.5, 19.3]})
    Cache.append({'name':'_42_','location':[5.5, 18.0, 5.7, 19.0]})

    Boxes.append({'name':'43L','location':[4.5, 20.0, 5.5, 21.0]})
    Cache.append({'name':'_43','location':[4.5, 19.7, 5.5, 20.0]})
    Cache.append({'name':'43_','location':[4.5, 21.0, 5.5, 21.3]})
    Cache.append({'name':'_43_','location':[5.5, 20.0, 5.7, 21.0]})


    Boxes.append({'name':'44L','location':[4.5, 22.0, 5.5, 23.0]})
    Cache.append({'name':'_44','location':[4.5, 21.7, 5.5, 22.0]})
    Cache.append({'name':'44_','location':[4.5, 23.0, 5.5, 23.299999999999997]})
    Cache.append({'name':'_44_','location':[5.5, 22.0, 5.7, 23.0]})

    Boxes.append({'name':'41R','location':[19.5, 16.0, 20.5, 17.0]})
    Cache.append({'name':'_41','location':[19.5, 15.7, 20.5, 16.0]})
    Cache.append({'name':'41_','location':[19.5, 17.0, 20.5, 17.3]})

    Boxes.append({'name':'42R','location':[19.5, 18.0, 20.5, 19.0]})
    Cache.append({'name':'_42','location':[19.5, 17.7, 20.5, 18.0]})
    Cache.append({'name':'42_','location':[19.5, 19.0, 20.5, 19.3]})
    Cache.append({'name':'_42_','location':[19.3, 18.0, 19.5, 19.0]})

    Boxes.append({'name':'43R','location':[19.5, 20.0, 20.5, 21.0]})
    Cache.append({'name':'_43','location':[19.5, 19.7, 20.5, 20.0]})
    Cache.append({'name':'43_','location':[19.5, 21.0, 20.5, 21.3]})
    Cache.append({'name':'_43_','location':[19.3, 20.0, 19.5, 21.0]})

    Boxes.append({'name':'44R','location':[19.5, 22.0, 20.5, 23.0]})
    Cache.append({'name':'_44','location':[19.5, 21.7, 20.5, 22.0]})
    Cache.append({'name':'44_','location':[19.5, 23.0, 20.5, 23.299999999999997]})
    Cache.append({'name':'_44_','location':[19.3, 22.0, 19.5, 23.0]})

    Boxes.append({'name':'65L','location':[0.3, 25.1, 1.3, 25.9]})#
    Cache.append({'name':'_65L','location':[0.3, 24.799999999999997, 1.3, 25.1]})

    Boxes.append({'name':'64L','location':[1.5, 25.1, 2.5, 25.9]})
    Cache.append({'name':'_64L','location':[1.5, 24.799999999999997, 2.5, 25.1]})
    
    Boxes.append({'name':'63L','location':[2.7, 25.1, 3.7, 25.9]})
    Cache.append({'name':'_63L','location':[2.7, 24.799999999999997, 3.7, 25.1]})
    
    Boxes.append({'name':'62L','location':[3.9, 25.1, 4.9, 25.9]})
    Cache.append({'name':'_62L','location':[3.9, 24.799999999999997, 4.9, 25.1]})

    Boxes.append({'name':'61L','location':[5.4, 25.1, 6.4, 25.9]})
    Cache.append({'name':'_61L','location':[5.4, 24.799999999999997, 6.4, 25.1]})

    Boxes.append({'name':'61R','location':[18.65, 25.1, 19.65, 25.9]})
    Cache.append({'name':'_61R','location':[18.65, 24.799999999999997, 19.65, 25.1]})

    
    Boxes.append({'name':'62R','location':[20.15, 25.1, 21.15, 25.9]})
    Cache.append({'name':'_62R','location':[20.15, 24.799999999999997, 21.15, 25.1]})

    Boxes.append({'name':'63R','location':[21.35, 25.1, 22.35, 25.9]})
    Cache.append({'name':'_63R','location':[21.35, 24.799999999999997, 22.35, 25.1]})

    Boxes.append({'name':'64R','location':[22.55, 25.1, 23.55, 25.9]})
    Cache.append({'name':'_64R','location':[22.55, 24.799999999999997, 23.55, 25.1]})

    Boxes.append({'name':'65R','location':[23.75, 25.1, 24.75, 25.9]})
    Cache.append({'name':'_65R','location':[23.75, 24.799999999999997, 24.75, 25.1]})

    Boxes.append({'name':'101','location':[9.14, 24.6, 10.14, 25.4]})
    Cache.append({'name':'_101','location':[9.14, 24.299999999999997, 10.14, 24.6]})

    Boxes.append({'name':'102','location':[10.28, 24.6, 11.28, 25.4]})
    Cache.append({'name':'_102','location':[10.28, 24.299999999999997, 11.28, 24.6]})

    Boxes.append({'name':'103','location':[11.42, 24.6, 12.43, 25.4]})
    Cache.append({'name':'_103','location':[11.42, 24.299999999999997, 12.43, 24.6]})

    Boxes.append({'name':'104','location':[12.56, 24.6, 13.56, 25.4]})
    Cache.append({'name':'_104','location':[12.56, 24.299999999999997, 13.56, 24.6]})

    Boxes.append({'name':'105','location':[13.7, 24.6, 14.7, 25.4]})
    Cache.append({'name':'_105','location':[13.7, 24.299999999999997, 14.7, 24.6]})

    Boxes.append({'name':'106','location':[14.84, 24.6, 15.84, 25.4]})
    Cache.append({'name':'_106','location':[14.84, 24.299999999999997, 15.84, 24.6]})



    Boxes.append({'name':'21','location':[7.5, 11.7, 8.5, 12.7]})
    Cache.append({'name':'_21_','location':[7.5, 11.2, 8.5, 11.7]})

    Boxes.append({'name':'22','location':[9.0, 11.7, 10.0, 12.7]})
    Cache.append({'name':'_22_','location':[9.0, 11.2, 10.0, 11.7]})

    Boxes.append({'name':'23','location':[10.5, 11.7, 11.5, 12.7]})
    Cache.append({'name':'_23_','location':[10.5, 11.2, 11.5, 11.7]})

    Boxes.append({'name':'24','location':[12.0, 11.7, 13.0, 12.7]})
    Cache.append({'name':'_24_','location':[12.0, 11.2, 13.0, 11.7]})

    Boxes.append({'name':'25','location':[13.5, 11.7, 14.5, 12.7]})
    Cache.append({'name':'_25_','location':[13.5, 11.2, 14.5, 11.7]})

    Boxes.append({'name':'26','location':[15.0, 11.7, 16.0, 12.7]})
    Cache.append({'name':'_26_','location':[15.0, 11.2, 16.0, 11.7]})

    Boxes.append({'name':'27','location':[16.5, 11.7, 17.5, 12.7]})
    Cache.append({'name':'_27_','location':[16.5, 11.2, 17.5, 11.7]})

    Boxes.append({'name':'31','location':[12.0, 16.0, 13.0, 17.0]})
    Cache.append({'name':'_31','location':[12.0, 15.7, 13.0, 16.0]})
    Cache.append({'name':'31_','location':[12.0, 17.0, 13.0, 17.3]})

    Boxes.append({'name':'32','location':[12.0, 18.0, 13.0, 19.0]})
    Cache.append({'name':'_32','location':[12.0, 17.7, 13.0, 18.0]})
    Cache.append({'name':'32_','location':[12.0, 19.0, 13.0, 19.3]})
    Cache.append({'name':'_32_','location':[13.0, 18.0, 13.3, 19.0]})

    Boxes.append({'name':'33','location':[12.0, 20.0, 13.0, 21.0]})
    Cache.append({'name':'_33','location':[12.0, 19.7, 13.0, 20.0]})
    Cache.append({'name':'33_','location':[12.0, 21.0, 13.0, 21.3]})
    Cache.append({'name':'_33_','location':[13.0, 20.0, 13.3, 21.0]})

    Boxes.append({'name':'34','location':[12.0, 22.0, 13.0, 23.0]})
    Cache.append({'name':'_34','location':[12.0, 21.7, 13.0, 22.0]})
    Cache.append({'name':'_34_','location':[13.0, 22.0, 13.3, 23.0]})
    #Cache.append({'name':'34_','location':[12.0, 23.0, 13.0, 23.299999999999997]})

    #Cache.append({'name':'Z_21','location':[23.5, -7.0, 24.0, -6.0]})
    #Cache.append({'name':'Z_22','location':[23.5, -4.5, 24.0, -3.5]})
    #Cache.append({'name':'Z_23','location':[23.5, -1.0, 24.0, 0.0]})
    #Cache.append({'name':'Z_24','location':[23.5, 1.0, 24.0, 2.0]})

    links=list()

    links.append({'name':'_21','location':[8.0, 10, 8.0, 11.7],'arrows':'2y'})#
    #links.append({'name':'21_','location':[8.0, 13.0, 8.0, 12.0],'arrows':'1y'})#
    links.append({'name':'_22','location':[9.5, 10, 9.5, 11.7],'arrows':'2y'})
    #inks.append({'name':'22_','location':[9.5, 13.0, 9.5, 12.0],'arrows':'1y'})
    links.append({'name':'_23','location':[11.0, 10, 11.0, 11.7],'arrows':'2y'})
    #links.append({'name':'23_','location':[11.0, 13.5, 11.0, 12.0],'arrows':'1y'})
    links.append({'name':'_24','location':[12.5, 10, 12.5, 11.7],'arrows':'2y'})
    #links.append({'name':'24_','location':[12.5, 13.5, 12.5, 12.0],'arrows':'1y'})
    links.append({'name':'_25','location':[14.0, 10, 14.0, 11.7],'arrows':'2y'})
    #links.append({'name':'25_','location':[14.0, 13.5, 14.0, 12.0],'arrows':'1y'})
    links.append({'name':'24_25','location':[13.25, 10, 13.25, 15],'arrows':'2y'})
    links.append({'name':'_26','location':[15.5, 10, 15.5, 11.7],'arrows':'2y'})
    #links.append({'name':'26_','location':[15.5, 13.5, 15.5, 12.0],'arrows':'1y'})
    #links.append({'name':'_27','location':[17.0, 12.0, 17.0, 13.0],'arrows':'2y'})
    links.append({'name':'27_','location':[17.0, 10, 17.0, 11.7],'arrows':'2y'})
    #links.append({'name':'_27','location':[17.0, 13.5, 17.0, 12.0],'arrows':'1y'}
   
    #links.append({'name':'Z_right','location':[23.0, -0.5, 24.0, -0.5],'arrows':'1x'}) 
    #links.append({'name':'right_down','location':[24.0, -0.5, 24.0, 11.5],'arrows':'0'})#################
    #links.append({'name':'down_left','location':[24.0, 11.5, 12.5, 11.5],'arrows':'1x'})
    links.append({'name':'left_down','location':[12.5, 7, 12.5, 10.0],'arrows':'2y'})#
    links.append({'name':'down_left_2','location':[12.5, 10, 8, 10],'arrows':'1x'})
    links.append({'name':'down_right','location':[12.5, 10, 17.0, 10],'arrows':'1x'})
    #links.append({'name':'left_up','location':[1.9, 12.0, 1.9, -3.0],'arrows':'0'})
    #links.append({'name':'up_down','location':[1.9, 12.0, 1.9, 16.0],'arrows':'0'})

    #links.append({'name':'E_right','location':[14.5, 8.5, 24.0, 8.5],'arrows':'1x'})
    #links.append({'name':'E_up','location':[12.8, 8.5, 12.8, -1.5],'arrows':'2y'})
    #links.append({'name':'E_H','location':[15.5, 8.5, 15.5, 1.0],'arrows':'1y'})
    #links.append({'name':'H_E','location':[15.5, 1.0, 15.5, 8.5],'arrows':'1y'})
    #links.append({'name':'E_Z','location':[22.75, 8.5, 22.75, 0.0],'arrows':'1y'})

    links.append({'name':'connection','location':[6.5, 10.0, 6.5, 15.0],'arrows':'2y'})
    #links.append({'name':'connection_','location':[6.5, 15.0, 6.5, 12.0],'arrows':'1y'})
    links.append({'name':'connection2','location':[5, 15.0, 20.0, 15.0],'arrows':'2x'})
    links.append({'name':'connection3','location':[18.3, 10, 18.3, 15.0],'arrows':'2y'})

    links.append({'name':'_41L','location':[5.0, 15.0, 5.0, 16.0],'arrows':'2y'})
    links.append({'name':'42_41L','location':[5.0, 17.0, 5.0, 18.0],'arrows':'2y'})
    links.append({'name':'43_42L','location':[5.0, 19.0, 5.0, 20.0],'arrows':'2y'})
    links.append({'name':'44_43L','location':[5.0, 21.0, 5.0, 22.0],'arrows':'2y'})
    links.append({'name':'44_L','location':[5.0, 23.0, 5.0, 24.0],'arrows':'2y'})
    links.append({'name':'6L','location':[0.8, 24.0, 6.2, 24.0],'arrows':'0'})
    links.append({'name':'_61L','location':[0.8, 24.0, 0.8, 25.1],'arrows':'2y'})
    links.append({'name':'_62L','location':[2.0, 24.0, 2.0, 25.1],'arrows':'2y'})
    links.append({'name':'_63L','location':[3.2, 24.0, 3.2, 25.1],'arrows':'2y'})
    links.append({'name':'_64L','location':[4.4, 24.0, 4.4, 25.1],'arrows':'2y'})
    links.append({'name':'_65L','location':[6.2, 24.0, 6.2, 25.1],'arrows':'2y'})
    links.append({'name':'4L','location':[6.0, 24.0, 6.0, 15.0],'arrows':'2y'})
    links.append({'name':'42L_','location':[5.5, 18.5, 6.0, 18.5],'arrows':'2y'})
    links.append({'name':'43-L_','location':[5.5, 20.5, 6.0, 20.5],'arrows':'2y'})
    links.append({'name':'44L_','location':[5.5, 22.5, 6.0, 22.5],'arrows':'2y'})

    links.append({'name':'_41R','location':[20.0, 15.0, 20.0, 16.0],'arrows':'2y'})
    links.append({'name':'42_41R','location':[20.0, 17.0, 20.0, 18.0],'arrows':'2y'})
    links.append({'name':'43_42R','location':[20.0, 19.0, 20.0, 20.0],'arrows':'2y'})
    links.append({'name':'44_43R','location':[20.0, 21.0, 20.0, 22.0],'arrows':'2y'})
    links.append({'name':'44_R','location':[20.0, 23.0, 20.0, 24.0],'arrows':'2y'})
    links.append({'name':'6R','location':[18.85, 24.0, 24.25, 24.0],'arrows':'0'})
    links.append({'name':'_61R','location':[18.85, 24.0, 18.85, 25.1],'arrows':'2y'})
    links.append({'name':'_62R','location':[20.65, 24.0, 20.65, 25.1],'arrows':'2y'})
    links.append({'name':'_63R','location':[21.85, 24.0, 21.85, 25.1],'arrows':'2y'})
    links.append({'name':'_64R','location':[23.05, 24.0, 23.05, 25.1],'arrows':'2y'})
    links.append({'name':'_65R','location':[24.25, 24.0, 24.25, 25.1],'arrows':'2y'})
    links.append({'name':'4R','location':[19.0, 24.0, 19.0, 15.0],'arrows':'2y'})
    links.append({'name':'42R_','location':[19.0, 18.5, 19.5, 18.5],'arrows':'2y'})
    links.append({'name':'43R_','location':[19.0, 20.5, 19.5, 20.5],'arrows':'2y'})
    links.append({'name':'44R_','location':[19.0, 22.5, 19.5, 22.5],'arrows':'2y'})

    links.append({'name':'_51L','location':[7.5, 15.0, 7.5, 20.0],'arrows':'2y'})
    links.append({'name':'52_51L','location':[7.5, 21.0, 7.5, 22.0],'arrows':'2y'})
    links.append({'name':'53_52L','location':[7.5, 23.0, 7.5, 24.0],'arrows':'2y'})
    links.append({'name':'54_53L','location':[7.5, 25.0, 7.5, 26.0],'arrows':'2y'})
    links.append({'name':'52L_','location':[8.0, 22.5, 9.0, 22.5],'arrows':'2x'})
    links.append({'name':'53L_','location':[8.0, 24.5, 9.0, 24.5],'arrows':'2x'})
    links.append({'name':'54L_','location':[8.0, 26.5, 9.0, 26.5],'arrows':'2x'})
    links.append({'name':'5L','location':[9.0, 26.5, 9.0, 15.0],'arrows':'2y'})

    links.append({'name':'_51R','location':[17.5, 15.0, 17.5, 20.0],'arrows':'2y'})
    links.append({'name':'52_51R','location':[17.5, 21.0, 17.5, 22.0],'arrows':'2y'})
    links.append({'name':'53_52R','location':[17.5, 23.0, 17.5, 24.0],'arrows':'2y'})
    links.append({'name':'54_53R','location':[17.5, 25.0, 17.5, 26.0],'arrows':'2y'})
    links.append({'name':'52R_','location':[17.0, 22.5, 16.0, 22.5],'arrows':'2x'})
    links.append({'name':'53R_','location':[17.0, 24.5, 16.0, 24.5],'arrows':'2x'})
    links.append({'name':'54R_','location':[17.0, 26.5, 16.0, 26.5],'arrows':'2x'})
    links.append({'name':'5R','location':[16.0, 26.5, 16.0, 15.0],'arrows':'2y'})

    links.append({'name':'_31','location':[12.5, 16.0, 12.5, 15.0],'arrows':'2y'})
    links.append({'name':'32_31','location':[12.5, 17.0, 12.5, 18.0],'arrows':'2y'})
    links.append({'name':'33_32','location':[12.5, 19.0, 12.5, 20.0],'arrows':'2y'})
    links.append({'name':'34_33','location':[12.5, 21.0, 12.5, 22.0],'arrows':'2y'})
    links.append({'name':'32_','location':[13.0, 18.5, 14.0, 18.5],'arrows':'2x'})
    links.append({'name':'33_','location':[13.0, 20.5, 14.0, 20.5],'arrows':'2x'})
    links.append({'name':'34_','location':[13.0, 22.5, 14.0, 22.5],'arrows':'2x'})
    links.append({'name':'3*','location':[14.0, 22.5, 14.0, 15.0],'arrows':'2y'})

    links.append({'name':'_101','location':[9.7, 24.5, 9.7, 23.5],'arrows':'2y'})
    links.append({'name':'_102','location':[10.9, 24.5, 10.9, 23.5],'arrows':'2y'})
    links.append({'name':'_103','location':[11.9, 24.5, 11.9, 23.5],'arrows':'2y'})
    links.append({'name':'_104','location':[13.06, 24.5, 13.06, 23.5],'arrows':'2y'})
    links.append({'name':'_105','location':[14.2, 24.5, 14.2, 23.5],'arrows':'2y'})
    links.append({'name':'_106','location':[15.34, 24.5, 15.34, 23.5],'arrows':'2y'})
    links.append({'name':'100','location':[9.7, 23.5, 15.34, 23.5],'arrows':'0'})
    links.append({'name':'_100','location':[11.0, 15.0, 11.0, 23.5],'arrows':'1y'})
    links.append({'name':'100_','location':[10.5, 23.5, 10.5, 15.0],'arrows':'1y', 'dash': (5, 2)})




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
    
    
    
    # Comment out or remove this section
# for m in range(1,4):
#     frame.canvas.create_rectangle(1.5*dx+(m-1)*8.5*dx,0.5*dx,
#     9.4*dx+(m-1)*8.5*dx,21.2*dx, fill="",dash=(5,5),width=2)

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
