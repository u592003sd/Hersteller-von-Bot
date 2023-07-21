#This script is for farmers cum attackers.
from random import randint
from numpy import sign

def ActRobot(robot):
        h_mov=0
        v_mov=0
        my_sig=robot.GetYourSignal()
        if len(robot.GetCurrentBaseSignal())>7 and my_sig[my_sig.index("_")+1]==1: #When target base not given
            return randint(1,4)
        
        if len(robot.GetCurrentBaseSignal())>7 and my_sig[my_sig.index("_")+1]==2: 
            w_a=[robot.investigate_up(),robot.investigate_down(),robot.investigate_left(),robot.investigate_right()]
            dr_cr={0:(0,-1),1:(0,1),2:(-1,0),3:(1,0)} #dr_cr: Used when enemy base is found and we have to calculate its co-ordinates.
            for i in range(len(w_a)):
                if w_a[i]=="enemy":
                    if robot.GetVirus() > 1000:
                        robot.DeployVirus(200)    
                elif w_a[i]=="enemy-base":
                    pos=robot.GetPosition()
                    pos=list(pos)
                    pos[0],pos[1]=dr_cr[i][0],dr_cr[i][1]
                    pos=tuple(pos)
                    robot.setSignal(f"{pos}")
        else: #When target base given 
            pos=list(robot.GetPosition())
            trg_pos_tup=eval(robot.GetCurrentBaseSignal())
            trg_pos=[trg_pos_str[0],trg_pos_str[1]]
            if (trg_pos[0]-pos[0])!=0:
                h_mov=3-sign(trg_pos[0]-pos[0])
                return h_mov
            if (trg_pos[1]-pos[1])!=0:
                v_mov=2+sign(trg_pos[1]-pos[1])
                return v_mov
            
        


def ActBase(base):
        '''
        Add your code here
    
        '''
        if base.GetElixir() > 500:
            n=len(base.GetListOfSignals())
            pur=1
            if (n+1)%3==0:
                pur=2
            base.create_robot(f'{n+1}_{pur}_(20,{n})')
        L=base.GetListOfSignals()
        for sig in L:
            if len(sig)<=7:
                base.SetYourSignal(sig)
                break  
        #return


''' in the first "if" section, for enemy base we have used correction terms
to add to the robot's co-ordinates to get target position co-ords. Then we have
set the robot's signal to the coordinates. Later we'll gather all the robot
signals and see if one of them contains '(' to check for target position detection.

in the second section, we have taken coords of both robot and enemy base. Now
we have to search for a method to execute left and right turns by one "if", and
up and down by another "if".

pur variable is to denote the purpose of the robot.
1: farmer
2: setter than attacker

the coordinates in the signal show the target base
'''
