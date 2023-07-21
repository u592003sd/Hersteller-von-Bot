from random import randint
from numpy import sign

def ActRobot(robot):
        h_mov=0
        v_mov=0
        if "(" not in str(robot.GetYourSignal()):
            w_a=[robot.investigate_up(),robot.investigate_down(),robot.investigate_left(),robot.investigate_right()]
            dr_cr={0:(0,-1),1:(0,1),2:(-1,0),3:(1,0)} #dr_cr: Used when enemy base is found and we have to calculate its co-ordinates.
            for i in range(4):
                if w_a[i]=="enemy":
                    if robot.GetVirus() > 1000:
                        robot.DeployVirus(200)    
                elif w_a[i]=="enemy-base":
                    pos=robot.GetPosition()
                    pos=list(pos)
                    pos[0],pos[1]=dr_cr[i][0],dr_cr[i][1]
                    pos=tuple(pos)
                    robot.setSignal(f"{pos}")

        else:
            pos=list(robot.GetPosition())
            trg_pos_str=robot.GetYourSignal()
            trg_pos=[trg_pos_str[1],trg_pos_str[3]]
            if (trg_pos[0]-pos[0])!=0:
                h_mov=3-sign(trg_pos[0]-pos[0])
                return h_mov
            if (trg_pos[1]-pos[1])!=0:
                v_mov=2+sign(trg_pos[1]-pos[1])
                return v_mov
            
        return randint(1,4)


def ActBase(base):
        '''
        Add your code here
    
        '''
        if base.GetElixir() > 500:
                base.create_robot('')
                        
        #return


''' in the first "if" section, for enemy base we have used correction terms
to add to the robot's co-ordinates to get target position co-ords. Then we have
set the robot's signal to the coordinates. Later we'll gather all the robot
signals and see if one of them contains '(' to check for target position detection.

in the second section, we have taken coords of both robot and enemy base. Now
we have to search for a method to execute left and right turns by one "if", and
up and down by another "if". '''
