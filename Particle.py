'''This file contains the Particle class that initiates all properties relating to a particle
   and holds methods that update its position, velocity, gravitation acceleration, momentum and kinetic energy.
'''
import numpy as np

class Particle:

    G = 6.67408e-20 # gravitation constant

    def __init__(
        self,
        position=np.array([0, 0, 0], dtype=float),
        velocity=np.array([0, 0, 0], dtype=float),
        acceleration=np.array([0, -10, 0], dtype=float),
        name="Ball",
        mass=1.0,
    ):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.name = name
        self.mass = mass

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration
        )

    def updateEulAlg(self, deltaT):
        """Use Euler algorithm to update particle's velocity and position
           after time deltaT has passed."""
        self.position += self.velocity * deltaT
        self.velocity += self.acceleration * deltaT

    def updateEulCromerAlg(self, deltaT):
        """Use Euler - Cromer algorithm to update particle's velocity and position
           after time deltaT has passed."""
        self.velocity += self.acceleration * deltaT
        self.position += self.velocity * deltaT

    def updateVerletAlg(self, deltaT, bodies):
        """Use Verlet algorithm to update particle's velocity and position
           after time deltaT has passed."""  
           
        def updateAccelerationVerlet(bodies):
            """Calculate and store the new acceleration (a_{n+1}) due to gravity (in 3 dimensions) of itself
            due to the other objects (in the "bodies" list) given their current relative positions."""
            new_acceleration = np.array([0, 0, 0], dtype=float)
            for body in bodies:

                # Make sure that the current object is not the same as the one in the list
                if self.name == body.name:
                    continue
                
                r = np.sqrt(
                    (self.position[0] - body.position[0]) ** 2
                    + (self.position[1] - body.position[1]) ** 2
                    + (self.position[2] - body.position[2]) ** 2
                )
                acceleration = np.array([0, 0, 0], dtype=float)
                for j in range(0, 3):
                #     new_acceleration[j] += (-(self.G * body.mass * (self.position[j] - body.position[j]))/((r**2)*r))
                    acceleration[j] = (-self.G * body.mass) * (self.position[j] - body.position[j]) /(r ** 3)
                    
                new_acceleration += acceleration
            return new_acceleration
        
        self.position = self.position + self.velocity * deltaT + 1/2 * self.acceleration * (deltaT ** 2)
        # new_acceleration = updateAcceleration(bodies)
        new_acceleration = updateAccelerationVerlet(bodies)
        
        self.velocity = self.velocity + 1/2 * (new_acceleration + self.acceleration) * deltaT
    
    def updateRungeKuttaAlg(self, deltaT, bodies):
        '''
        '''
        def updateAcceleration(position):
            '''Inner function to calculate acceleration on a body'''
            total_acceleration = np.array([0, 0, 0], dtype=float)
            for body in bodies:

                # Make sure that the current object is not the same as the one in the list
                if self.name == body.name:
                    continue

                position_difference = np.sqrt(
                    (position[0] - body.position[0]) ** 2
                    + (position[1] - body.position[1]) ** 2
                    + (position[2] - body.position[2]) ** 2
                )
                acceleration = (
                    # ((-self.G * body.mass) / np.dot((position - body.position), (position - body.position))**1.5) * (position - body.position)
                    ((-self.G * body.mass) / position_difference ** 2)
                    * (position - body.position)
                    / position_difference
                )
                total_acceleration += acceleration
            return total_acceleration
        
        k1_v = updateAcceleration(self.position)
        k1_r = self.velocity
        k2_v = updateAcceleration(self.position + k1_r * deltaT/2)
        k2_r = self.velocity + k1_v * deltaT/2
        k3_v = updateAcceleration(self.position + k2_r * deltaT/2)
        k3_r = self.velocity + k2_v * deltaT/2
        k4_v = updateAcceleration(self.position + k3_r * deltaT)
        k4_r = self.velocity + k3_v * deltaT
        
        self.velocity += deltaT/6 * (k1_v + 2*k2_v + 2*k3_v + k4_v)
        self.position += deltaT/6 * (k1_r + 2*k2_r + 2*k3_r + k4_r)
        
    def updateGravitationalAcceleration(self, bodies):
        """Calculate and store the acceleration due to gravity (in 3 dimensions) of itself
        due to the other objects (in the "bodies" list) given their current relative positions."""
        self.acceleration = np.array([0, 0, 0], dtype=float)
        for body in bodies:

            # Make sure that the current object is not the same as the one in the list
            if self.name == body.name:
                continue

            position_difference = np.sqrt(
                (self.position[0] - body.position[0]) ** 2
                + (self.position[1] - body.position[1]) ** 2
                + (self.position[2] - body.position[2]) ** 2
            )
            acceleration = (
                ((-self.G * body.mass) / position_difference ** 2)
                * (self.position - body.position)
                / position_difference
            )
            self.acceleration += acceleration

    def kineticEnergy(self):
        """Calculates the kinetic energy of the body."""
        v = np.linalg.norm(self.velocity)
        return 1 / 2 * self.mass * v ** 2
    
    def linearMomentum(self):
        '''Calculates the linear momentum of the body'''
        v = np.linalg.norm(self.velocity)
        return self.mass * v
    
    def angularMomentum(self):
        '''Calculates the angular momentum of the body'''
        lin_mom_vect = self.mass * self.velocity
        ang_mom_vect = np.cross(self.position, lin_mom_vect)
        return np.linalg.norm(ang_mom_vect)