
            
#This file contains only the second part of BE: the compound BEs



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



#4.8 entity generation (now in separate file)

