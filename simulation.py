
import pybullet as p
import pybullet_data
import time
import numpy as np
import random

import constants as c

import pyrosim.pyrosim as pyrosim

from world import WORLD
from robot import ROBOT


class SIMULATION:

    def __init__(self, directOrGUI, solutionID):
        if directOrGUI == 'DIRECT':
            self.physicsClient = p.connect(p.DIRECT)
        elif directOrGUI == 'GUI':
            self.physicsClient = p.connect(p.GUI)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.GRAVITY_X, c.GRAVITY_Y, c.GRAVITY_Z)

        self.myID = solutionID

        self.world = WORLD()
        self.robot = ROBOT(self.myID)

        pyrosim.Prepare_To_Simulate(self.robot.robotID)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def Run(self):
        for i in range(c.NUM_STEPS):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            # time.sleep(c.SLEEP_TIME)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()


if __name__ == '__main__':
    pass
