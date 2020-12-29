'''This file is a test file of a 3-body simulation. It takes input from a binary data file and plots the positions of two satellites around the Earth.
'''
import matplotlib.pyplot as plt
import numpy as np
import Simulation

#Load in the data file
Data = np.load("ThreeBodyTest.npy", allow_pickle=True)


earth_x = [items[1].position[0] for items in Data]
earth_y = [items[1].position[1] for items in Data]
earth_z = [items[1].position[2] for items in Data]

satellite_1_x = [items[2].position[0] for items in Data]
satellite_1_y = [items[2].position[1] for items in Data]
satellite_1_z = [items[2].position[2] for items in Data]

satellite_2_x = [items[3].position[0] for items in Data]
satellite_2_y = [items[3].position[1] for items in Data]
satellite_2_z = [items[3].position[2] for items in Data]

#Plot the orbits
plt.plot(satellite_1_x, satellite_1_y, label="Satellite 1")
plt.plot(satellite_2_x, satellite_2_y, label="Satellite 2")
plt.plot(earth_x, earth_y, marker='.', label="Earth")
plt.legend()

plt.savefig('plots/Solar_System_1.pdf')
plt.show()
