
import numpy as np
import pyrosim.pyrosim as pyrosim
import os

import time
import random
import constants as c


class SOLUTION:

    def __init__(self, ID):
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights *= 2
        self.weights -= 1
        self.myID = ID
        self.num_joints = random.randint(1, 10)

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Robot()
        self.Create_Brain()

        os.system('python simulate.py {} {} 2&>1 &'.format(directOrGUI, self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists('fitness{}.txt'.format(self.myID)):
            time.sleep(.01)
        with open('fitness{}.txt'.format(self.myID), 'r') as f:
            self.fitness = float(f.read())
        # print(self.fitness)
        os.system('rm {}'.format('fitness{}.txt'.format(self.myID)))

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Robot()
        self.Create_Brain()
        os.system('python simulate.py {} {} &'.format(directOrGUI, self.myID))

    def Create_World(self):
        pyrosim.Start_SDF('world.sdf')

        pyrosim.End()

        while not os.path.exists('world.sdf'):
            time.sleep(.01)

    def Create_Robot(self):
        pyrosim.Start_URDF("body.urdf")

        lastsize = [random.random(), random.random(), random.random()]
        lastpos = [0, 0, lastsize[2] / 2]
        pyrosim.Send_Cube(
            name="Link1",
            pos=lastpos,
            size=lastsize
        )

        """for i in range(self.num_joints):
            # make joint
            pyrosim.Send_Joint(
                name="Link{}_Link{}".format(i, i + 1),
                parent="Link{}".format(i),
                child="Link{}".format(i + 1),
                type="revolute",
                position=[0, -.5, 1],
                jointAxis="1 0 0"
            )


            # make next link

            pass"""

        pyrosim.End()

        while not os.path.exists('body.urdf'):
            time.sleep(.01)

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork('brain{}.nndf'.format(self.myID))

        num_sensors = 0
        for i in range(self.num_joints + 1):
            if random.random() > .5:
                pyrosim.Send_Sensor_Neuron(name=num_sensors, linkName='Link{}'.format(i))
                num_sensors += 1

        for i in range(self.num_joints):
            pyrosim.Send_Motor_Neuron(name=i + num_sensors, jointName='Link{}_Link{}'.format(i - 1, i))

        self.weights = np.random.rand(num_sensors, self.num_joints)

        for i in range(num_sensors):
            for j in range(self.num_joints):
                pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j + num_sensors, weight=self.weights[i, j])

        pyrosim.End()

        while not os.path.exists('brain{}.nndf'.format(self.myID)):
            time.sleep(.01)

    def Mutate(self):
        row = random.randint(0, c.numSensorNeurons - 1)
        column = random.randint(0, c.numMotorNeurons - 1)

        self.weights[row, column] = 2 * random.random() - 1

    def Set_ID(self, val):
        self.myID = val

