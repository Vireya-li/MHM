

# -------------------------
# ENGINE
# -------------------------


#Section4 Engine 


#4.1-4.6 (now in separate file)

#This file contains the basic BEs: the first part and the "count" in 4.7 (BE definitions) 
#The compound BEs (the second part of 4.7) and 4.8 (entity generation for BEs) are now in separate files



#4.7 BEs (this file contains only the first part + the count BE)


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


