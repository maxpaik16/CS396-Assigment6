import random

import pyrosim.pyrosim as pyrosim


def Create_World():
    pyrosim.Start_SDF('world.sdf')

    pyrosim.Send_Cube(
                    name="Box",
                    pos=[-2, 2, .5],
                    size=[1, 1, 1]
                )

    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(
                    name="LinkTorso",
                    pos=[0, 0, 1.5],
                    size=[1, 1, 1]
                )

    pyrosim.Send_Joint(
        name="LinkTorso_LinkBackLeg",
        parent="LinkTorso",
        child="LinkBackLeg",
        type="revolute",
        position=[-.5, 0, 1]
    )

    pyrosim.Send_Cube(
                    name="LinkBackLeg",
                    pos=[-.5, 0, -.5],
                    size=[1, 1, 1]
                )

    pyrosim.Send_Joint(
        name="LinkTorso_LinkFrontLeg",
        parent="LinkTorso",
        child="LinkFrontLeg",
        type="revolute",
        position=[.5, 0, 1]
    )

    pyrosim.Send_Cube(
                    name="LinkFrontLeg",
                    pos=[.5, 0, -.5],
                    size=[1, 1, 1]
                )

    pyrosim.End()

def Create_Brain():
    pyrosim.Start_NeuralNetwork('brain.nndf')

    pyrosim.Send_Sensor_Neuron(name=0, linkName='LinkTorso')
    pyrosim.Send_Sensor_Neuron(name=1, linkName='LinkBackLeg')
    pyrosim.Send_Sensor_Neuron(name=2, linkName='LinkFrontLeg')

    pyrosim.Send_Motor_Neuron(name=3, jointName='LinkTorso_LinkBackLeg')
    pyrosim.Send_Motor_Neuron(name=4, jointName='LinkTorso_LinkFrontLeg')

    for i in range(3):
        for j in range(2):
            pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j+3, weight=random.random() * 2 - 1)

    pyrosim.End()


if __name__ == '__main__':
    Create_World()
    Create_Robot()
    Create_Brain()
