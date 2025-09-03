
# This file is Section 4.8 Entity Generation of the single file version

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


#Section5 Plot

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