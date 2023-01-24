
from solution import SOLUTION
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0

        for n in range(c.populationSize):
            self.parents[n] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        os.system('rm brain*.nndf')
        os.system('rm fitness*.txt')

    def Evolve(self):
        self.Evaluate(self.parents)


        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evaluate(self, solutions):
        for parent in solutions.values():
            parent.Start_Simulation('DIRECT')

        for parent in solutions.values():
            parent.Wait_For_Simulation_To_End()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}

        for i, parent in self.parents.items():

            child = copy.deepcopy(parent)
            child.Set_ID(self.nextAvailableID)
            self.children[i] = child
            self.nextAvailableID += 1

    def Mutate(self):
        for child in self.children.values():
            child.Mutate()

    def Select(self):
        for n in self.parents.keys():
            if self.children[n].fitness < self.parents[n].fitness:
                self.parents[n] = self.children[n]

    def Print(self):
        print('\n')
        for n in self.parents.keys():
            print("key: {}, child fitness: {}, parent fitness: {}".format(n, self.children[n].fitness, self.parents[n].fitness))

    def Show_Best(self):
        best_parent = self.parents[0]
        for parent in self.parents.values():
            if best_parent.fitness > parent.fitness:
                best_parent = parent

        best_parent.Start_Simulation('GUI')

