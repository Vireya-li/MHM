

# -------------------------
# ENGINE
# -------------------------


#Section4 Engine 
import random
import math
import numpy as np
import sys
import time
from random import expovariate, randint

# Import other custom modules using absolute imports
from gui_general_2 import anim, load_var, path
from gui_for_be_3 import N, hear_entity_dic, see_entity_dic, judgei_target_dic, length_count, ji_result_dic, color_dic, operation, track1D_response, track2D_response, static2D_response, dynamic1D_amp, dynamic1D_response,  operation, track1D_curse_loc, track2D_target_loc_x, track2D_target_loc_y, track2D_cursor_loc_x, track2D_cursor_loc_y, track1D_amp, track2D_amp,N, static2D_cursor_loc_x, dynamic1D_cursor_loc, dynamic1D_amp, dynamic2D_cursor_loc_x, dynamic2D_response
from qn_mhp_layout_4 import Structure_and_Animation
from animation_general_5 import show, enter, leave, add, delete
from animation_be_6 import Reaction_calsingledig, reaction_press_button, Reaction_count, Reaction_track1D, Reaction_track2D, Reaction_static_2DTracing, Reaction_dynamic1D, Reaction_dynamic2D
from model_core_7 import QN_MHP, ppt, server2, server3,j,k, track2D_freq_dic, track2D_freq, static2D_freq_dic, static2D_freq, dynamic2D_freq_dic, dynamic2D_freq, copy_dic, Tasklist_dic, server6, server7, serverA, serverB, cpt, ji_store_dic, jm_result_dic, jm_store_dic, task_info_dic, cal_sd_num_dic, cal_sd_result_dic, mpt, eyefixation_dic, entity_info, attribute_dic, look_for_ls, n_look_for_ls, count_num_dic, rmse_list, rmse_dic, rmse_var_dic, SIMTIME, start_time, track1D_freq_dic, track1D_freq,track1D_amp_dic, track1D_amp, env, dynamic1D_freq_dic, dynamic1D_freq, dynamic1D_amp_dic, track2D_amp_dic, color_list,main
from plot_9 import Plot



#4.1-4.6 (now in separate file)

#This file contains 4.7 (BE definitions) and 4.8 (entity generation for BEs) 



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

#4.8 entity generation (for specific BEs) 

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


#Section5 Plot (now in separate file)

