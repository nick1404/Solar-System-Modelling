'''This file contains a simulation of motion of two bodies (a satellite and the Earth) due to a each other's gravitational fields.
   This simulation is performed for the Euler-Cromer algorithm.
'''
import numpy as np
from Particle import Particle
import matplotlib.pyplot as plt

earthMass = 5.97237e24  # kg
earthRadius = 6371  # km
Earth = Particle(
    position=np.array([0, 0, 0]),
    velocity=np.array([0, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Earth",
    mass=earthMass,
)
satPosition = earthRadius + (35786)
satVelocity = np.sqrt(
    Earth.G * Earth.mass / satPosition
)  # from centrifugal force = gravitational force
Satellite = Particle(
    position=[satPosition, 0, 0],
    velocity=[0, satVelocity, 0],
    acceleration=np.array([0, 0, 0]),
    name="Satellite",
    mass=100.0,
)

sat_x = []
sat_y = []
earth_x = []
earth_y = []
# A for loop over 2000 iterations in which the accelerations, positions and velocities of the Earth and Satellite are updated
for iter in range(20000):
    Satellite.updateGravitationalAcceleration([Satellite, Earth])
    Earth.updateGravitationalAcceleration([Satellite, Earth])
    Satellite.updateEulCromerAlg(6)  # time step of 6 seconds
    Earth.updateEulCromerAlg(6)
    sat_x.append(Satellite.position[0])
    sat_y.append(Satellite.position[1])
    earth_x.append(Earth.position[0])
    earth_y.append(Earth.position[1])

# Plot the data
fig = plt.figure(figsize=(7, 7))
plt.scatter(sat_x, sat_y, label="Satellite", s=1)
plt.scatter(earth_x, earth_y, label="Earth", s=1)
plt.xlabel("Position in x-direction (km)")
plt.ylabel("Position in y-direction (km)")
plt.legend()
plt.savefig("plots/Earth_1_Sat.pdf")
plt.show()
