
#Section5 Plot
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import os

# Import other custom modules using absolute imports
from qn_mhp_layout_4 import Structure_and_Animation
from animation_general_5 import show, enter, leave, add, delete
from animation_be_6 import Reaction_dynamic1D, Reaction_dynamic2D
from model_core_7 import QN_MHP, env, Tasklist_dic, sojourn_time_dic, rt_mean_dic, rt_var_dic, rmse_dic, rmse_var_dic
from behavior_elements_8 import *

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