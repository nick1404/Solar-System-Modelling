'''This file contains a simulation of motion of single body in a uniform gravitational field.
   This simulation is performed for both the Euler and the Euler-Cromer algorithms.
'''
from Particle import Particle
import matplotlib.pyplot as plt
import math
import numpy as np


# initialise the Bodies
Ball_Euler = Particle(
    position=np.array([0, 100, 0]),
    velocity=np.array([20, 50, 0]),
    acceleration=np.array([0, -10, 0]),  # g=-10 m/s^2 in y-direction
    name="Ball (Euler Algorithm)",
    mass=500.0,
)

Ball_EulerCromer = Particle(
    position=np.array([0, 100, 0]),
    velocity=np.array([20, 50, 0]),
    acceleration=np.array([0, -10, 0]),  # g=-10 m/s^2 in y-direction
    name="Ball (Euler-Cromer Algorithm)",
    mass=500.0,
)

Data = {}

for Ball in [Ball_Euler, Ball_EulerCromer]:
    time = 0  # initial time stamp
    deltaT = 1e-3  # time steps of 1ms

    times = []
    y = []

    # run simulation until ball hits the ground
    while Ball.position[1] > 0.0:
        # store the time stamps
        times.append(time)

        # store the y-position
        y.append(Ball.position[1])

        # update the time
        time += deltaT

        # update the positions and velocities
        if Ball.name == "Ball (Euler Algorithm)":
            Ball.updateEulAlg(deltaT)
        elif Ball.name == "Ball (Euler-Cromer Algorithm)":
            Ball.updateEulCromerAlg(deltaT)

    # Append the data from each algorithm to the mian dictionary for plottinng
    Data[Ball.name] = [times, y]

# Plot the ball trajectory from the equation of its parabolic motion
fig = plt.figure(figsize=(10, 7))
x = np.linspace(0, 12, 11708)
coeffs = [-5, 50, 100]
y = coeffs[0] * x ** 2 + coeffs[1] * x + coeffs[2]
plt.scatter(
    x, y, label="Analytically determined trajectory of the ball", marker="1", s=2
)

# Plot the ball trajectory from each algorithm
markers = [".", "v"]
for (key, value), m in zip(Data.items(), markers):
    plt.scatter(
        value[0], value[1], marker=m, label="Trajectory of a {}".format(key), s=1
    )

plt.xlabel("time (s)")
plt.ylabel("y-position (m)")
plt.legend(loc=1)
plt.savefig("plots/Ball_1D_Trajectory.pdf")
plt.show()
