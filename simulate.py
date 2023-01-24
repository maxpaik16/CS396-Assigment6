
from simulation import SIMULATION
import sys

if __name__ == '__main__':
    directOrGUI = sys.argv[1]
    solutionID = sys.argv[2]
    simulation = SIMULATION(directOrGUI, solutionID)
    simulation.Run()
    simulation.Get_Fitness()