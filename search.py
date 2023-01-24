
import os

from hillclimber import HILL_CLIMBER
from parallelHillClimber import PARALLEL_HILL_CLIMBER

if __name__ == '__main__':

    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    phc.Show_Best()