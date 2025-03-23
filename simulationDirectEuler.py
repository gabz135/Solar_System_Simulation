from simulation import Simulation

class SimulationDirectEuler(Simulation):
    """Used in Experiment 2 for comparison. Uses the Direct Euler instead of Beeman method for position calculations.

    Parameters
    ----------
    Simulation : Simluation
        Parent class with all the functionality for the Simulation but allows us to use different calculation method here.
    """
    def _update_positions(self):
        """Updates the position of all bodies using Direct Euler method.
        """
        for body in self.body_list:
            #creating local variables for values to make the position formula clearer
            current_position = body.position_list[-1]
            current_velocity = body.velocity_list[-1]

            position = current_position + (current_velocity * self.timestep)
            body.position_list.append(position)
    
    def _update_velocities(self):
        """Updates the velocities of all bodies using Direct Euler method.
        """
        for body in self.body_list:
            #creating local variables for values to make velocity formula clearer
            current_velocity = body.velocity_list[-1]
            current_acceleration = body.acceleration_list[-1]

            velocity = current_velocity + (current_acceleration * self.timestep)
            body.velocity_list.append(velocity)
    
    def run_simulation(self):
        """Uses Direct Euler method to update positions of all bodies for length of simulation and writes total energy to file.
        """
        for i in range(self.num_timesteps):
            self._update_accelerations()
            self._update_positions()
            self._update_velocities()