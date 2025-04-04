import json
from body import Body
from constants import G
from numpy.linalg import norm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math
import os


class Simulation():
    """The main class which is used for the performing the different parts of the simulation.
    """    
    def __init__(self, input_file):
        """Simulation class constructor which takes a data file and extracts simulation data as well as planets data.

        Parameters
        ----------
        input_file : json
            stores simulation data such as timestep and num_timesteps and planets data.
        """
        with open(input_file) as f:
            input_data = json.load(f)
        
        self.timestep = input_data["timestep"]
        self.num_timesteps = input_data["num_timesteps"]
        self.tot_energy_list = []
        self.body_list = []
        self.patch_list = [] #used for animating planets in the solar system

        #adding all the bodies to body_list.
        for body in input_data["bodies"]:
            self.body_list.append(Body(body["name"], body["mass"], body["orbital_radius"], body["colour"]))


    #the following 3 functions are helper functions that will be used later on in run_simulation() to update velocities.
    def _update_positions(self):
        """Updates the position of all bodies using Beeman method.
        """
        for body in self.body_list:
            #creating local variables for values to make the position formula clearer
            current_position = body.position_list[-1]
            current_velocity = body.velocity_list[-1]
            current_acceleration = body.acceleration_list[-1]
            previous_acceleration = body.acceleration_list[-2]

            position = (current_position + (current_velocity * self.timestep) + 
                        (1/6 * ((4 * current_acceleration) - previous_acceleration) * self.timestep * (self.timestep)))
            body.position_list.append(position)

    def _update_accelerations(self):
        """Updates the acceleration of all bodies - acceleration formula is independent of Integration method.
        """
        for i in range(len(self.body_list)):
            sum = 0
            for j in range(len(self.body_list)):
                if i == j:
                    continue
                position_ji = self.body_list[i].position_list[-1] - self.body_list[j].position_list[-1]
                mag_position_ji = norm(position_ji)
                sum += (self.body_list[j].mass * position_ji) / (mag_position_ji * mag_position_ji * mag_position_ji)

            acceleration = -G * sum
            self.body_list[i].acceleration_list.append(acceleration)

    def _update_velocities(self):
        """Updates the velocity of all bodies using Beeman method.
        """
        for body in self.body_list:
            #creating local variables for values to ake velocity formula clearer
            current_velocity = body.velocity_list[-1]
            next_acceleration = body.acceleration_list[-1]
            current_acceleration = body.acceleration_list[-2]
            previous_acceleration = body.acceleration_list[-3]

            velocity = current_velocity + (1/6 * ((2 * next_acceleration) + (5 * current_acceleration) - (previous_acceleration)) * self.timestep)
            body.velocity_list.append(velocity)


    def calc_store_tot_energy(self):
        """Calculates the total energy of system at a regular interval and saves that data to file.
        """
        frequency = 50 #calculates the energy every frequency number of timesteps. if changed, change it in the graphing function too.

        i = 0
        while i < self.num_timesteps:
            kinetic_energy = 0
            potential_energy = 0
            for body_i in self.body_list:
                #caculating kinetic energy:
                mag_velocity = norm(body_i.velocity_list[i])
                kinetic_energy += (1/2) * body_i.mass * (mag_velocity * mag_velocity)

                #calculating potential energy:
                for body_j in self.body_list:
                    if body_i == body_j:
                        continue
                    mag_position_ij = norm(body_j.position_list[i] - body_i.position_list[i])
                    potential_energy += (G * body_i.mass * body_j.mass) / mag_position_ij

            potential_energy = potential_energy * (-1/2) #to fix double counting problem

            self.tot_energy_list.append(kinetic_energy + potential_energy)
            i += frequency 

        #writing the total energy of the system to file:
        with open("system_energy.txt", "w") as writefile:
            writefile.write("Below is the total energy of the system calculated at a regular inteval: \n")

            for energy in self.tot_energy_list:
                writefile.write(str(energy) + "\n")


    def run_simulation(self):
        """Uses Beeman method to update positions of all bodies for length of simulation and writes total energy to file.
        """
        #initialise the first 2 values of acceleration for all bodies
        self._update_accelerations()
        for body in self.body_list:
            body.acceleration_list.append(body.acceleration_list[0])

        for i in range(self.num_timesteps):
            self._update_positions()
            self._update_accelerations()
            self._update_velocities()

        
    def _animate(self, i):
        """Returns the positions of planets for the given value of i. 

        Parameters
        ----------
        i : int
            the current frame number from FuncAnimation.

        Returns
        -------
        list of patches Circle objects
            stores the list of patches Circle for each planet for the given frame.
        """
        for j in range (len(self.body_list)):
            self.patch_list[j].center = tuple(map(float, self.body_list[j].position_list[i]))
        return self.patch_list
 
    def animate_simulation(self):
        """Animates the simulation of the solar system.
        """
        fig = plt.figure()
        ax = plt.axes()

        for i in range(len(self.body_list)):
            position = tuple(map(float, self.body_list[i].position_list[0]))
            radius = 0.2
            colour = self.body_list[i].colour

            current_body_circle = plt.Circle(position, radius, color=colour, animated=True)
            self.patch_list.append(ax.add_patch(current_body_circle))

        ax.axis('scaled')
        #x and y-axis are in the unit of AU
        ax.set_xlim(-6, 6)
        ax.set_ylim(-6, 6)

        plt.xlabel("x position (AU)")
        plt.ylabel("y position (AU)")

        numFrames = self.num_timesteps
        self.anim = FuncAnimation(fig, self._animate, numFrames, repeat=False, interval=20, blit=True)

        plt.show()
    
    def display_sim_orbital_periods(self):
        output_string = "" #will be used to format planet data for printing
        for body in self.body_list:
            if body.name == "sun":
                continue
            
            full_orbit_timestep = body.check_orbital_period(self.timestep)
            output_string += body.name + ": " + str(round(body.orbital_period, 4)) + " Earth years \t"
            if not full_orbit_timestep:
                output_string += "\tIncomplete cycle for given number of timesteps \n"
            else:
                output_string += "Full orbital cycle at timestep " + str(full_orbit_timestep) + "\n"
        
        #printing data about orbital periods
        width = os.get_terminal_size().columns
        heading = "ORBITAL PERIODS OF PLANETS IN EARTH YEARS"
        print()
        print(heading.center(width))
        print()

        print(output_string)
        print()


    def compare_orbital_periods(self):
        """Compares the orbital periods of the planets in the simulation to the actual orbital periods from NASA
        """
        #Stores actual periods in a dictionary to be able to access the values with the name of planet.
        #Periods are in Earth years.
        NASA_orbital_periods = {
            "mercury" : 0.241,
            "venus" : 0.615,
            "earth" : 1,
            "moon" : 0.0748,
            "mars" : 1.88,
            "jupiter" : 11.9,
            "saturn" : 29.4,
            "uranus" : 83.7,
            "neptune" : 163.7,
            "pluto" : 247.9
        }

        output_string = "" #will be used to format output to print
        for body in self.body_list:
            if body.name == "sun":
                continue
            body.check_orbital_period(self.timestep)
            percentage_difference = (abs(NASA_orbital_periods[body.name] - body.orbital_period) / 
                                     NASA_orbital_periods[body.name] * 100)
            
            output_string += body.name + ": \n"
            output_string += ("Actual orbital period: " + str(NASA_orbital_periods[body.name]) + "\t" + 
                              "Simulation orbital period: " + str(round(body.orbital_period,3)) + "\n" +
                              "Percentage difference: " + str(round(percentage_difference,3)) + "% \n\n")
            
        #printing the comparison of orbital periods
        width = os.get_terminal_size().columns
        heading = "COMPARISON OF SIMULATION AND ACTUAL ORBITAL PERIODS"
        print()
        print(heading.center(width))
        print()

        print(output_string)
        print()


    def graph_total_energy(self):
        """Graphs the total energy of the system against time.
        """
        plt.plot(self.tot_energy_list, marker='o', linestyle='-')

        #fixes the offset of time to make it accurate
        current_xticks = plt.xticks()[0]
        plt.xticks(current_xticks, (current_xticks * 50) * self.timestep) #50 is the frequeny at which energy was calculated

        plt.xlabel("Time (years)")
        plt.ylabel(r"Energy Value ($M_{\oplus} \cdot \frac{\text{AU}^2}{\text{yr}^2}$)")
        plt.title("Total energy of system over timesteps")

        plt.show()


    def detect_planetary_alignment(self, num_planets=5):
        """Detects the planetary alignments for a supplied number of planets and outputs the timesteps at which they happened.

        Parameters
        ----------
        num_planets : int
            The number of planets for which the planetary alignments should be counted.
        """
        alignment_occurences = []
        for i in range(self.num_timesteps):
            relative_angles = np.zeros(num_planets)
            for j in range(1, (num_planets + 1)): #to calculate relative angles for all bodies
                relative_x = self.body_list[j].position_list[i][0] - self.body_list[0].position_list[i][0]
                relative_y = self.body_list[j].position_list[i][1] - self.body_list[0].position_list[i][1]
                relative_angles[j-1] = math.atan2(relative_y, relative_x)
            
            angles_average = relative_angles.mean()
            tolerance = 5 * (math.pi / 180) #to convert the 5 degrees to radians

            is_in_range_pi = np.all((relative_angles >= angles_average - tolerance) & 
                                    (relative_angles <= angles_average + tolerance))
            if is_in_range_pi:
                alignment_occurences.append(i)
            else: #making angles between 0 and 2pi and rechecking
                relative_angles_2pi = np.zeros(num_planets)
                for j in range(len(relative_angles)): #making a secondary array with angles between 0 and 2pi
                    relative_angles_2pi[j] = relative_angles[j] if relative_angles[j] > 0 else relative_angles[j] + 2 * math.pi

                angles_average_2pi = relative_angles_2pi.mean()
                is_in_range_2pi = np.all((relative_angles_2pi >= angles_average_2pi - tolerance) & 
                                         (relative_angles_2pi <= angles_average_2pi + tolerance))
                
                if is_in_range_2pi:
                    alignment_occurences.append(i)
        
        #printing data about planetary alignments
        width = os.get_terminal_size().columns
        heading = "OCCURENCES OF PLANETARY ALIGNMENTS"
        print()
        print(heading.center(width))
        print()

        print("There has been planetary alignments at the following timesteps: ")
        output = ""
        for occurence in alignment_occurences:
            output += "- " + str(occurence) + " -"
        print(output)
        print()