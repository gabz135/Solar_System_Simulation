from simulation import Simulation
from simulationDirectEuler import SimulationDirectEuler
from simulationEulerCromer import SimulationEulerCromer

def run_main_simulation(simulation_testing):
    """Runs Section 3: Simulation of the project.

    Parameters
    ----------
    simulation_testing : Simulation
        An instance of the Simulation class with a populated positions list for quick calculations.
    """
    simulation_testing.animate_simulation()
    simulation_testing.display_sim_orbital_periods()
    simulation_testing.calc_store_tot_energy()


def run_experiment_1(simulation_exp1):
    """Runs Section 4.1: Experiment 1 of the project.

    Parameters
    ----------
    simulation_testing : Simulation
        An instance of the Simulation class with a populated positions list for quick calculations.
    """
    simulation_exp1.compare_orbital_periods()


def run_experiment_2(simulation_exp2):
    """Runs Section 4.2: Experiment 2 of the project.

    Parameters
    ----------
    simulation_testing : Simulation
        An instance of the Simulation class with a populated positions list for quick calculations.
    """
    simulation_exp2.calc_store_tot_energy()

    simulation_euler_cromer = SimulationEulerCromer("simulation_data.json")
    simulation_euler_cromer.run_simulation()
    simulation_euler_cromer.calc_store_tot_energy()

    simulation_direct_euler = SimulationDirectEuler("simulation_data.json")
    simulation_direct_euler.run_simulation()
    simulation_direct_euler.calc_store_tot_energy()

    simulation_exp2.graph_total_energy()
    simulation_euler_cromer.graph_total_energy()
    simulation_direct_euler.graph_total_energy()


def run_experiment_4(simulation_exp4):
    """Runs Section 4.4: Experiment 4 of the project.

    Parameters
    ----------
    simulation_testing : Simulation
        An instance of the Simulation class with a populated positions list for quick calculations.
    """
    simulation_exp4.detect_planetary_alignment() #could supply a value to change the number of planets from the default 5


#Main program
simulation_test = Simulation("simulation_data.json")
simulation_test.run_simulation()

run_main_simulation(simulation_test)
run_experiment_1(simulation_test)
run_experiment_2(simulation_test)
run_experiment_4(simulation_test)