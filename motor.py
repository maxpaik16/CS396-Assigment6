
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p

import numpy as np

class MOTOR:

    def __init__(self, jointName, bodyID):
        self.jointName = jointName
        self.bodyID = bodyID

    def Set_Value(self, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=self.bodyID,
            jointName=bytes(self.jointName),
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.MAX_FORCE
        )
