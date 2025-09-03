

# -------------------------
# ENGINE
# -------------------------
import random
import simpy
import math
import numpy as np
import sys

# Import other custom modules using absolute imports
from qn_mhp_layout_4 import Structure_and_Animation
from animation_general_5 import show, enter, leave, add, delete
from gui_general_2 import saved, load_var, save_var, path, GUI_User_Main
from behavior_elements_8 import *
from plot_9 import Plot


#Section4 Engine 
#This file now contains only Sections 4.1-4.6 of QM-MHP 4/26/24) (L3205-3640)
#Sections 4.7-4.8 now in separate file

#4.1 Engine parameters


#define ppt, cpt, mpt

#ppt = (-1) * 16 * math.log(1-random.uniform(0,1)) + 17
#cpt = (-1) * 22 * math.log(1-random.uniform(0,1)) + 13
#mpt = (-1) * 14 * math.log(1-random.uniform(0,1)) + 10

ppt=33
cpt=35
mpt=24


#BE and the entity records (Q: should these be moved to be closer to BEs? These are not model parameters)

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



#4.2 data record for specific BE (Q: should these be moved to be closer to BEs?)


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

#4.3 data record for sojourn time, used in plot section (Q: move elsewhere?)

sojourn_time_dic = {}
rt_dic ={1:[],2:[],3:[],4:[],5:[]}
rt_mean_dic={1:[],2:[],3:[],4:[],5:[]}
rt_var_dic={1:[],2:[],3:[],4:[],5:[]}

rmse_dic={}
rmse_var_dic={}
rmse_list=[]


#4.4 retrieve/ save data from GUI, which is used in engine part  (Q: move elsewhere?)

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


#4.5 Servers (These are core components of model)

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
    
    

#4.7 BEs (for defining the various Behavior Elements; now in separate file)
#4.8 entity generation for BEs (now in separate file)


#Section5 Plot (now in separate file)

