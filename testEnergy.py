'''This file contains tests for the conservation of energy in an n-body simulation.
'''
import numpy as np
from Particle import Particle
from Simulation import (
    Sun,
    Mercury,
    Venus,
    Earth,
    Mars,
    Jupiter,
    Saturn,
    Uranus,
    Neptune,
)

"""
    Let's test if the kinetic energy of the Solar System is conserved.
    We will calculate the kinetic energy before and after one year of planetary motion.
"""
bodies = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]
initialKineticEnergy = []
finalKineticEnergy = []

deltaT = 86400  # one day in seconds
#Simulate the motion of bodies using the Euler method
for i in range(365):
    for body in bodies:
        initialKineticEnergy.append(body.kineticEnergy())
        body.updateGravitationalAcceleration(bodies)
        body.updateEulAlg(deltaT)
        finalKineticEnergy.append(body.kineticEnergy())

print(
    "Kinetic Energy of the Solar System at the start of the simulation is %s J."
    % sum(initialKineticEnergy),
    "Kinetic Energy of the Solar System at the end of the simulation is %s J."
    % sum(finalKineticEnergy),
    "Percentage difference is %s %%"
    % ((sum(initialKineticEnergy) - sum(finalKineticEnergy)) / sum(finalKineticEnergy)),
    sep="\n",
)
