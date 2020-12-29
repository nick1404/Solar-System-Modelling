This repository contains the source code for the final PHYS281 project, the simulation of the time-evolution of the Solar System. 

**Contents:**

- **Particle.py** -- Contains the particle class with all its methods that are used to simulate the motion of bodies;
- **Simulation.py** -- Sets up the initial conditions of the bodies in the Solar System and performs iterations of Euler/Euler-Cromer method to generate the data that can be plotted in **plotSimulationSolSyst.py**;
- **plotSimulation2Sat.py** -- A test file that simulates a 3-body system (2 satellites orbiting the Earth) and plots their trajectories;
-  **plotSimulationSolSyst.py** -- Takes in a binary data file and produces a plot of the orbits of a n-body system;
- **Simulation1Body.py** -- A test file that uses the Euler/Euler-Cromer method to plot a trajectory of a single body due to a constant gravitational field;
- **Simulation2Body.py** -- A test file that uses the Euler-Cromer method to simulate a 2-body system (a satellite orbiting the Earth) and plots their trajectories;
- **testEnergy.py** -- A test file that checks for the conservation of energy in an n-body simulation (Solar System);
- **testMomentum.py** -- A test file that checks for both conservation of both linear and angular momenta in an n-body simulation (Solar System).


**How to run the simulation of the Solar System:**

1. In the **Simulation.py**, choose a desired numerical method that updates the positions and velocities in each iteration. Also you can choose the time step and the duration of the simulation.
2. The simulation data is saved to a binary (.npy) data file, which you can load into the **plotSimulationSolSyst.py** to produce visualisations of the planetary orbits around the Sun.