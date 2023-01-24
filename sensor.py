import constants as c
import numpy as np

import pyrosim.pyrosim as pyrosim

class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.NUM_STEPS)

    def Get_Value(self, step):
        self.values[step] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        with open('data/{}Values.npy'.format(self.linkName), 'wb') as f:
            np.save(f, self.values)