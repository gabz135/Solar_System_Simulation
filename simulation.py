import json
from body import Body
from constants import G
from numpy.linalg import norm

class Simulation():
    
    def __init__(self, input_file):
        with open(input_file) as f:
            input_data = json.load(f)
        
        self.timestep = input_data["timestep"]
        self.num_timesteps = input_data["num_timesteps"]
        self.tot_energy_list = []
        self.body_list = []
        self.patch_list = []

        #adding all the bodies to body_list.
        for body in input_data["bodies"]:
            self.body_list.append(Body(body["name"], body["mass"], body["orbital_radius"], body["colour"]))


    #the following 3 functions are helper functions that will be used later on in run_simulation() to update velocities.
    def _update_positions(self):
        for body in self.body_list:
            #creating local variables for values to make the position formula clearer
            current_position = body.position_list[-1]
            current_velocity = body.velocity_list[-1]
            current_acceleration = body.acceleration_list[-1]
            previous_acceleration = body.acceleration_list[-2]

            position = current_position + (current_velocity * self.timestep) + (1/6 * ((4 * current_acceleration) - previous_acceleration) * self.timestep * (self.timestep))
            body.position_list.append(position)

    def _update_accelerations(self):
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
        for body in self.body_list:
            #creating local variables for values to ake velocity formula clearer
            current_velocity = body.velocity_list[-1]
            next_acceleration = body.acceleration_list[-1]
            current_acceleration = body.acceleration_list[-2]
            previous_acceleration = body.acceleration_list[-3]

            velocity = current_velocity + (1/6 * ((2 * next_acceleration) + (5 * current_acceleration) - (previous_acceleration)) * self.timestep)
            body.velocity_list.append(velocity)


    def _calc_tot_energy(self):
        pass

    def run_simulation(self):
        #initialise the first 2 values of acceleration for all bodies
        self._update_accelerations()
        for body in self.body_list:
            body.acceleration_list.append(body.acceleration_list[0])

        for i in range(self.num_timesteps):
            self._update_positions()
            self._update_accelerations()
            self._update_velocities()
        
        self._calc_tot_energy()

        

    def _animate(self, i):
        pass

    def animate_simulation(self):
        pass