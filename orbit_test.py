from vpython import *
import numpy as np

# Create Bodies (Play God)
Sun = sphere(pos=vector(0, 0, 0), radius=1e10, color=color.yellow)
Earth = sphere(pos=vector(1.5e11, 0, 0), radius=5e9, color=color.cyan, make_trail=True)
scene.autoscale = 0

# Define Constants (Play God v2)
G = 6.67e-11
Sun.m = 1.989e30
Earth.m = 5.972e24
r = vec(1.5e11, 0, 0)

# Define  Velocities and Momenta
Earth.v = vec(0, np.sqrt(G*Sun.m/mag(r)), 0)
Earth.p = Earth.m * Earth.v

Sun.v = vec(0, 0, 0)
Sun.p = Sun.m * Sun.v

dt = 10

while True:
    R = Earth.pos - Sun.pos
    Fg = G * (Sun.m * Earth.m) / mag(R)**3 * R

    Earth.p = -Fg * dt + Earth.p

    Earth.v = Earth.p / Earth.m

    Earth.pos = Earth.pos + Earth.v *dt


