# Note: It should be noted that due to Bertrand's theorem, changing the power of the orbit means that there will not be
#       a stable orbit (at least a non-circular one, but after several hours of modifications and tweaks, I couldn't
#       even find an unstable orbit. So, I did the next best thing and added a non-inverse square term to the equation
#       and actually got something interesting. 

from vpython import *
import numpy as np

au = 1.496e11   # Distance from Earth to Sun in meters (Actual)

# Create Bodies (Play God)
Sun = sphere(pos=vector(0, 0, 0), radius=1e10, color=color.yellow)   # radius=1e10
Earth = sphere(pos=vector(au, 0, 0), radius=5e9, color=color.cyan, make_trail=True)   # radius=5e9
scene.autoscale = 0

# Define Constants (Play God v2)
d1 = 0.39*au   # Distance from Mercury to Sun in meters
d2 = 30*au   # Distance of Neptune from Sun in meters
G = 6.67e-11   # Gravitational Constant dim= L^(3)M^(-1)T^(-2)
d = 1
Earth.m = 5.972e24   # Mass of Earth
Sun.m = 1.989e30   # Mass of Sun (Actual)
# Earth.m = 1
# Sun.m = 1
r = vec(au, 0, 0)   # Initial Position of Earth


# Define  Velocities and Momenta
Earth.v = vec(0, np.sqrt(G*Sun.m/mag(r)), 0)   # Linear Velocity of Earth
# Earth.v = vec(0, 1, 0)
Earth.p = Earth.m * Earth.v   # Linear Momentum of Earth

Sun.v = vec(0, 0, 0)   # Sun Velocity
Sun.p = Sun.m * Sun.v   # Sun Momentum

dt = 40  # Time Step

while True:
    R = Earth.pos - Sun.pos
    Fg = (G * (3*Sun.m * Earth.m) / mag(R)**3 * R) - (((mag(Earth.p) / mag(R))**2) / (Earth.m * mag(R)**4)) * R

    Earth.p = -Fg * dt + Earth.p

    Earth.v = Earth.p / Earth.m

    Earth.pos = Earth.pos + Earth.v * dt


