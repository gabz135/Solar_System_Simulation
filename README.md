# Solar System Simulation

A Python-based N-body simulation modelling the motion of planets under gravitational forces. The project implements the Beeman integration method and compares its energy conservation with the Direct Euler and Euler-Cromer methods.

The simulation can be configured with different planets, timesteps and simulation durations, and includes an animation for visualising planetary motion. System energy is also calculated to evaluate the accuracy and stability of the numerical integration methods.

## Features

- N-body gravitational simulation of planetary motion
- Beeman integration method
- Comparison with Direct Euler and Euler-Cromer integration methods
- System energy calculation and analysis
- Animated visualisation of planetary motion
- Configurable planets, timestep and simulation duration

## Project Structure

| File | Description |
|------|-------------|
| `main.py` | Entry point for running simulations and experiments. |
| `simulation.py` | Contains the core simulation logic, including running the simulation, collecting results and animating planetary motion. |
| `body.py` | Defines the `Body` class and stores the properties of planets and other bodies in the simulation. |
| `simulationDirectEuler.py` | Implements the Direct Euler integration method for comparison. |
| `simulationEulerCromer.py` | Implements the Euler-Cromer integration method for comparison. |
| `constants.py` | Stores physical constants used throughout the simulation. |
| `simulation_data.json` | Stores configuration data including planets, timestep and number of timesteps. |
| `system_energy.txt` | Stores the calculated system energy produced by the simulation. |
| `README.md` | Project documentation and instructions for running and configuring the simulation. |

## Getting Started

### Requirements

- Python 3

### Running the Simulation

The simulation can be run using:

    python main.py

The desired parts of the simulation can be selected by commenting or uncommenting the corresponding function calls at the end of `main.py`.

Some parts of the program, such as the animation, must be closed before the next part of the program can run.

## Configuration

The simulation can be configured through `simulation_data.json`.

### Adding or Removing Planets

To change the number of planets, edit `simulation_data.json` and add or remove the relevant planetary data.

If additional planets are added, the x and y limits used by the animation may also need to be adjusted in the `animate_simulation` method of the `Simulation` class.

### Timestep and Simulation Duration

The timestep and number of timesteps can also be changed in `simulation_data.json`.

## Units

The simulation is designed to work with astronomical units (AU), Earth masses and Earth years.

To use a different unit system, the following values need to be updated:

- `constants.py` - gravitational constant `G` and the Sun's mass
- `simulation_data.json` - planetary data and timestep
- `simulation.py` - x and y limits used by the animation

## Course Context

This project was developed as part of the University of Edinburgh's Computer Simulation course.