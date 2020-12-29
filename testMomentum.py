'''This file contains tests of both linear and angular momenta conservation in an n-body simulation.
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

"""Test the angular momentum of the Earth wrt to the center of the Sun.
   The origin is at the center of the Sun.
"""
earthMass = 5.97237e24  # https://en.wikipedia.org/wiki/Earth
earthRadius = 6.37810 * 1e6  # https://en.wikipedia.org/wiki/Earth
earthSunDistance = 149.597e9  # m
earthTimePeriod = 365 * 24 * 3600  # s
earthVelocity = 2 * np.pi * earthSunDistance / earthTimePeriod
earthAngularMomentum = earthMass * earthVelocity * earthSunDistance

earthPositionVector = [
    -2.488497169862896e07,
    1.449783471212823e08,
    -6.171784579284489e03,
]
earthVelocityVector = [
    -2.984892046591452e01,
    -5.162374739569864e00,
    7.366656604983479e-04,
]

Earth = Particle(
    position=np.array([x * 1000 for x in earthPositionVector]),
    velocity=np.array([x * 1000 for x in earthVelocityVector]),
    acceleration=np.array([0, 0, 0]),
    name="Earth",
    mass=earthMass,
)

print(
    "The theoretical value of the angular momentum of the Earth is %s kg m^2 s^(-1)."
    % (round(earthAngularMomentum, 3)),
    "The value obtained in the simulation is %s kg m^2 s^(-1)."
    % (round(Earth.angularMomentum(), 3)),
    sep="\n",
)
print(
    "Percentage difference is %s %%."
    % (
        round(
            (earthAngularMomentum - Earth.angularMomentum())
            / earthAngularMomentum
            * 100,
            3,
        )
    )
)

"""
    Now let's test if the overall angular momentum of the Solar System is conserved.
    We will calculate the total angular momentum before and after one year of planetary motion.
"""
bodies = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]
initialAngularMomentum = []
finalAngularMomentum = []
initialLinearMomentum = []
finalLinearMomentum = []

deltaT = 86400  # one day in seconds
for i in range(365):
    for body in bodies:
        initialAngularMomentum.append(body.angularMomentum())
        initialLinearMomentum.append(body.linearMomentum())
        body.updateGravitationalAcceleration(bodies)
        body.updateEulerAlg(deltaT)
        finalAngularMomentum.append(body.angularMomentum())
        finalLinearMomentum.append(body.linearMomentum())

print(
    "Angular momentum of the Solar System at the start of the simulation is %s kg m^2 s^(-1)."
    % sum(initialAngularMomentum),
    "Angular momentum of the Solar System %s kg m^2 s^(-1)."
    % sum(finalAngularMomentum),
    "Percentage difference is %s %%"
    % (
        (sum(initialAngularMomentum) - sum(finalAngularMomentum))
        / sum(finalAngularMomentum)
        * 100
    ),
    sep="\n",
)
print(
    "Linear momentum of the Solar System at the start of the simulation is %s kg m^2 s^(-1)."
    % sum(initialLinearMomentum),
    "Linear momentum of the Solar System %s kg m^2 s^(-1)." % sum(finalLinearMomentum),
    "Percentage difference is %s %%"
    % (
        (sum(initialLinearMomentum) - sum(finalLinearMomentum))
        / sum(finalLinearMomentum)
        * 100
    ),
    sep="\n",
)
