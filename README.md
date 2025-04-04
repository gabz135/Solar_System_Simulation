# CSim_Final_Project #

## Files in the Project ##

### 1. `main.py`
**Purpose:** This file runs the tests for everything the project requires, including the simulation and experiments.

### 2. `simulation.py`
**Purpose:** This file contains the main `Simulation` class, which handles the core simulation logic for the project. It includes methods for initializing the simulation, running it, and collecting results.

### 3. `body.py`
**Purpose:** This file contains the main `Body` class, which creates and stores the data for all the bodies/planets used in the simulation.

### 4. `simulationDirectEuler.py`
**Purpose:** This file contains the main `SimulationDirectEuler` class, which is used to compare the energy values for different integration methods.

### 5. `simulationEulerCromer.py`
**Purpose:** This file contains the main `SimulationEulerCromer` class, which is used to compare the energy values for different integration methods.

### 6. `constants.py`
**Purpose:** This file contains some constant values to allow easy access to them from anywhere in the project.

### 7. `simulation_data.json`
**Purpose:** This file contains the timestep, number of timesteps and planets data that are used in the simulation.

### 8. `system_energy.txt`
**Purpose:** This file is the output of calculating the system energy and writing it to file. Data gets overwritten when simulaiton is rerun.

### 9. `README.md`
**Purpose:** This file provides documentation for the project, explaining its purpose and how to use it.

---

## How to Use ##

Use the main.py file to run the desired part of the simulation. You can choose which parts you want to run by commenting/uncommenting the function call lines shown at the end of the file. 
P.S. the next part of the program will not run until the previous is closed. So for example, when the animation plays it has to be closed befire the other parts of the program will run.

## Notes ##
1. To change the number of planets edit simulation_data.json and add more planet data to it.
2. The number of timesteps and length of timestep can also be changed from the simulation_data.json file.
3. If the number of planets is expanded, the x and y limit values will also have to be changed to show the added planets in the animation. This can be done by editing the limit values in the `animate_simulation` method in the `Simulation` class
4. The code works best in the units of AU, Earth masses and Earth years. To use a different unit system minimal changes will need to be made to the following files: 
    - `constants.py` change the value of G and sun_mass
    - `simulation_data.json` change planets and timestep data
    - `simulation.py` change the x and y limits of the animation  


<STYLE>
    * {
        background-color: #FFFFAA;
        color:            #080808;
    }
    code {
        color: #435588;
        background-color: #D5D58477;
    }
</STYLE>