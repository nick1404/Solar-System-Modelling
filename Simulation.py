"""This file sets the initial conditions for the bodies in the Solar System and iterates the positions, velocities and accelerations of each body
   a chosen number of times. It outputs the data that can be used for plotting the orbits to a binary file.
"""
import numpy as np
import copy
from Particle import Particle

"""
    This simulation will model the evolution of the Solar System over a time period of 1 year (starting from 1 Jan 2020).
    The origin of the coordinate system is the barycenter of the Solar System.
    All distances are in km, velocities are in km/s. Mass is in kg.
"""
sunMass = 1988500e24
mercuryMass = 3.302e23
venusMass = 48.685e23
earthMass = 5.97219e24
marsMass = 6.4171e23
jupiterMass = 1898.13e24
saturnMass = 5.6834e26
uranusMass = 86.813e24
neptuneMass = 1.024e26  # from Google not NASA

Sun = Particle(
    position=np.array(
        [-5.682653841092885e05, 1.112997165528592e06, 3.445256675517594e03]
    ),
    velocity=np.array(
        [-1.446153643855376e-02, -3.447507130430867e-03, 3.988611997595555e-04]
    ),
    acceleration=np.array([0, 0, 0]),
    name="Sun",
    mass=sunMass,
)
Mercury = Particle(
    position=np.array(
        [-1.004302793346122e07, -6.782848247285485e07, -4.760889633162629e06]
    ),
    velocity=np.array(
        [3.847265155592926e01, -4.158689546981208e00, -3.869763647804497e00]
    ),
    acceleration=np.array([0, 0, 0]),
    name="Mercury",
    mass=mercuryMass,
)
Venus = Particle(
    position=np.array(
        [1.076209595805564e08, 8.974122818036491e06, -6.131976661929069e06]
    ),
    velocity=np.array(
        [-2.693485084259549e00, 3.476650462014290e01, 6.320912271467272e-01]
    ),
    acceleration=np.array([0, 0, 0]),
    name="Venus",
    mass=venusMass,
)
Earth = Particle(
    position=np.array(
        [-2.545323708273825e07, 1.460913442868109e08, -2.726527903765440e03]
    ),
    velocity=np.array(
        [-2.986338200235307e01, -5.165822246700293e00, 1.135526860257752e-03]
    ),
    acceleration=np.array([0, 0, 0]),
    name="Earth",
    mass=earthMass,
)
Mars = Particle(
    position=np.array(
        [-1.980535522170065e08, -1.313944334060654e08, 2.072245594990239e06]
    ),
    velocity=np.array(
        [1.439273929359666e01, -1.805004074289640e01, -7.312485979614864e-01]
    ),
    acceleration=np.array([0, 0, 0]),
    name="Mars",
    mass=marsMass,
)
Jupiter = Particle(
    position=np.array(
        [7.814210740178683e07, -7.769489405106364e08, 1.474081608751178e06]
    ),
    velocity=np.array(
        [1.283931035247975e01, 1.930357070566108e00, -2.952599473712843e-01]
    ),
    acceleration=np.array([0, 0, 0]),
    name="Jupiter",
    mass=jupiterMass,
)
Saturn = Particle(
    position=np.array(
        [5.674914809473343e08, -1.388366463018738e09, 1.549265783457875e06]
    ),
    velocity=np.array(
        [8.406493531200095e00, 3.627774839464044e00, -3.983651341797232e-01]
    ),
    acceleration=np.array([0, 0, 0]),
    name="Saturn",
    mass=saturnMass,
)
Uranus = Particle(
    position=np.array(
        [2.426731532276310e09, 1.703392504032894e09, -2.511215084173620e07]
    ),
    velocity=np.array(
        [-3.962351584219718e00, 5.256523421272158e00, 7.095167477538000e-02]
    ),
    acceleration=np.array([0, 0, 0]),
    name="Uranus",
    mass=uranusMass,
)
Neptune = Particle(
    position=np.array(
        [4.374094274093674e09, -9.514049067425712e08, -8.121317847458720e07]
    ),
    velocity=np.array(
        [1.118822506695780e00, 5.342644352002246e00, -1.362606261073369e-01]
    ),
    acceleration=np.array([0, 0, 0]),
    name="Neptune",
    mass=neptuneMass,
)

# A for loop that calculates the accelerations, positions and velocities of the bodies in the Solar System over 100 years
bodies = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]
Data = []
deltaT = 3600  # one hour in seconds

for i in range(8766):  # Update every hour over 1 year
    dataPerPlanetPerDay = []
    for body in bodies:
        body.updateGravitationalAcceleration(bodies)
        body.updateEulCromerAlg(deltaT)
        dataPerPlanetPerDay.append(copy.deepcopy(body))

    Data.append(dataPerPlanetPerDay)

# Save the simulation data to a binary file
np.save("simulations/Solar_System_1Year_EulerCromer", Data, allow_pickle=True)
