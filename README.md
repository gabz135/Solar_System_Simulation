# CSim_Final_Project

## Files in the Project

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

## How to Use

Use the main.py file to run the desired part of the simulation. You can choose which parts you want to run by commenting/uncommenting the function call lines shown at the end of the file.






1. Does the code have to be compatible with different units of data? Because grid is preset.
2. Is it ok for planet circles to have the same radius? and for x y axis to be preset to a certain value?
3. Is it ok for energy graphs to appear consecutively?
4. Why does big num_timesteps lead to bad orbital period?
5. How to do report?