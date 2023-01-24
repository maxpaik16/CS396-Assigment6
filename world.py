

import pybullet as p


class WORLD:

    def __init__(self):
        p.loadSDF('world.sdf')
        self.planeID = p.loadURDF('plane.urdf')