
import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import os
import constants as c

from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:

    def __init__(self, ID):
        self.robotID = p.loadURDF('body.urdf')
        self.nn = NEURAL_NETWORK('brain{}.nndf'.format(ID))
        self.myID = ID
        os.system('rm brain{}.nndf'.format(self.myID))

    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, step):
        for sensor in self.sensors.values():
            sensor.Get_Value(step)

    def Prepare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName, self.robotID)

    def Act(self, step):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = bytes(self.nn.Get_Motor_Neurons_Joint(neuronName), encoding='utf8')
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle)

    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotID, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        with open('fitnesstmp{}.txt'.format(self.myID), 'w') as f:
            f.write(str(xCoordinateOfLinkZero))

        os.system('mv {} {}'.format('fitnesstmp{}.txt'.format(self.myID), 'fitness{}.txt'.format(self.myID)))