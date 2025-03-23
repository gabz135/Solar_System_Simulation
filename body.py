import numpy as np
import math
from constants import G, sun_mass

class Body():
    """Creates Body objects for celestial bodies to use in the simulation.
    """
    def __init__(self, name, mass, orbital_radius, colour):
        """Body class constructor which initialises body data as well as calculate initial position and velocity.

        Parameters
        ----------
        name : str
            stores name of the Body object
        mass : float
            stores mass of the Body object in the unit of Earth masses
        orbital_radius : float
            stores the orbital radius of the Body object in the unit of AU
        colour : str
            stores the colour of the Body object
        """
        self.name = name
        self.mass = mass
        self.orbital_radius = orbital_radius
        self.colour = colour

        self.orbital_period = 0

        self.acceleration_list = []
        self.position_list = []
        self.velocity_list = []

        #assigning inital value for position list:
        self.position_list.append(np.array([self.orbital_radius,0]))

        #assigning inital value for velocity list:
        velocity_mag = math.sqrt((G * sun_mass) / self.orbital_radius) if self.orbital_radius != 0 else 0
        self.velocity_list.append(np.array([0,velocity_mag]))
    
    def check_orbital_period(self, timestep):
        """Calculates the orbital period for the current object.

        Parameters
        ----------
        timestep : float
            The simulation's timestep.
        """
        num_orbits = 0
        full_orbit_timesteps = [] #will record all timesteps where a planet completes a full orbit
        for i  in range(1, len(self.position_list)):
            previous_angle = math.atan2(self.position_list[i-1][1], self.position_list[i-1][0])
            current_angle = math.atan2(self.position_list[i][1], self.position_list[i][0])
            if abs(current_angle - previous_angle) > math.pi:
                num_orbits += 1
                full_orbit_timesteps.append(i)

        time = len(self.position_list) * timestep #the first part is equivelant to num_timesteps as the list will be the length of num_timesteps
        self.orbital_period = time / num_orbits if num_orbits != 0 else 0
        return False if not full_orbit_timesteps else full_orbit_timesteps[0]