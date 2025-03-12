import numpy as np
import math
from constants import G

class Body():

    def __init__(self, name, mass, orbital_radius, colour):
        self.name = name
        self.mass = mass
        self.orbital_radius = orbital_radius
        self.colour = colour

        self.orbital_period = 0

        self.acceleration_list = []
        self.position_list = []
        self.velocity_list = []

        #assigning inital values for position and velocity lists.
        self.position_list.append(np.array([self.orbital_radius,0]))

        sun_mass = 1.989e30
        velocity_mag = math.sqrt((G * sun_mass) / self.orbital_radius) 
        #IMPORTANT division by 0 here. for now i will ensure that the 
        #sun has orbital radius 0 but this will need to be fixed. initially sun had 0.0 orbital radius.
        self.velocity_list.append(np.array([0,velocity_mag]))

    def check_orbital_period(self):
        pass
