from vpython import *
import numpy as np

au = 1.496e11   # Distance from Earth to Sun in meters (Actual)
erad = 5e9
# au = 30
# Create Bodies
Sun = sphere(pos=vector(0, 0, 0), radius=2*erad, color=color.yellow)   # radius=1e10
Earth = sphere(pos=vector(au, 1, 1), radius=erad, color=color.blue, make_trail=True)   # radius=5e9
Venus = sphere(pos=vector(0.72*au, 1, 1), radius=0.95*erad, color=color.orange, make_trail=True)
Mercury = sphere(pos=vector(0.39*au, 1, 1), radius=0.38*erad, color=color.green, make_trail=True)
Mars = sphere(pos=vector(1.5*au, 1, 1), radius=0.53*erad, color=color.red, make_trail=True)
Jupiter = sphere(pos=vector(5.2*au, 1, 1), radius=1.5*erad, color=color.purple, make_trail=True)
scene.autoscale = 0

# Define Constants (Play God v2)
G = 6.67e-11   # Gravitational Constant dim= L^(3)M^(-1)T^(-2)

Earth.m = 5.972e24   # Mass of Earth Kg
Sun.m = 1.989e30   # Mass of Sun Kg
Venus.m = 4.867e24   # Mass of Venus Kg
Mercury.m = 3.285e23   # Mass of Mercury in Kg
Mars.m = 6.39e23   # Mass of Mars in Kg
Jupiter.m = 1.9e27   # Mass of Jupiter in Kg

rE = vec(au, 1, 1)   # Initial Position of Earth
rV = vec(0.72*au, 1, 1)   # Initial Position of Venus
rm = vec(0.39*au, 1, 1)   # Initial Position of Mercury
rM = vec(1.5*au, 1, 1)   # Initial Position of Mars
rJ = vec(5.2*au, 1, 1)   # Initial Position of Jupiter

# Define  Velocities and Momenta
Earth.v = vec(0, np.sqrt(G*Sun.m/mag(rE)), 0)   # Linear Velocity of Earth
Venus.v = vec(0, np.sqrt(G*Sun.m/mag(rV)), 0)   # Linear Velocity of Venus
Mercury.v = vec(0, np.sqrt(G*Sun.m/mag(rm)), 0)   # Linear Velocity of Mercury
Mars.v = vec(0, np.sqrt(G*Sun.m/mag(rM)), 0)   # Linear Velocity of Mars
Jupiter.v = vec(0, np.sqrt(G*Sun.m/mag(rJ)), 0)

Earth.p = Earth.m * Earth.v   # Linear Momentum of Earth
Venus.p = Venus.m * Venus.v   # Linear Momentum of Venus
Mercury.p = Mercury.m * Mercury.v   # Linear Momentum of Mercury
Mars.p = Mars.m * Mars.v   # Linear Momentum of Mars
Jupiter.p = Jupiter.m * Jupiter.v   # Linear Momentum of Jupiter

Sun.v = vec(0, 0, 0)   # Sun Velocity
Sun.p = Sun.m * Sun.v   # Sun Momentum

Po = 365.25*24*60*60   # 1 Earth year converted into seconds
Earth.omega = 2*np.pi/Po   # Change in Earth's angle with respect to the Sun in 1/sec
Venus.omega = 2*np.pi/(0.616*Po)   # Change in Venus's angle with respect to the Sun in 1/sec
Mercury.omega = 2*np.pi/(0.25*Po)   # Change in Mercury's angle with respect to the Sun in 1/sec
Mars.omega = 2*np.pi/(1.88*Po)   # Change in Mars's angle with respect to the Sun in 1/sec
Jupiter.omega = 2*np.pi/(11.86*Po)   # Change in Jupiter's angle with respect to the Sun in 1/sec

G1 = (Earth.m * mag(rE)**3 * Earth.omega**2) / (Sun.m * Earth.m)   # Gravitational Constant for Earth
G2 = (Venus.m * mag(rV)**4 * Venus.omega**2) / (Sun.m * Venus.m)   # Gravitational Constant for Venus
G3 = (Mercury.m * mag(rm)**2 * Mercury.omega**2) / (Sun.m * Mercury.m)   # Gravitational Constant for Mercury
G4 = (Mars.m * Mars.omega**2) / (Sun.m * Mars.m)   # Gravitational Constant for Mars
G5 = (Jupiter.m * mag(rJ)**5 * Jupiter.omega**2) / (Sun.m * Jupiter.m)   # Gravitational Constant for Jupiter

dt = 1200  # Time Step (Use dt = 120 for detailed behavior of inner planets, Use dt = 1200 for behavior of Jupiter)

# Redundant stuff which I am afraid to remove due to irrational fear of breaking the entire thing
time = 517425600
thetas = 4*np.pi


# Define Phase Space Diagrams:
Mercury_phase_space = graph(title='Earth Phase Diagram', xtitle='Position', ytitle='Velocity', fast=True)
Mercury_phase_space_curve = gcurve(graph=Mercury_phase_space, color=color.green, size=0.1)

Venus_phase_space = graph(title='Earth Phase Diagram', xtitle='Position', ytitle='Velocity', fast=True)
Venus_phase_space_curve = gcurve(graph=Venus_phase_space, color=color.orange, size=0.1)

Earth_phase_space = graph(title='Earth Phase Diagram', xtitle='Position', ytitle='Velocity', fast=True)
Earth_phase_space_curve = gcurve(graph=Earth_phase_space, color=color.blue, size=0.1)

Mars_phase_space = graph(title='Earth Phase Diagram', xtitle='Position', ytitle='Velocity', fast=True)
Mars_phase_space_curve = gcurve(graph=Mars_phase_space, color=color.red, size=0.1)

Jupiter_phase_space = graph(title='Earth Phase Diagram', xtitle='Position', ytitle='Velocity', fast=True)
Jupiter_phase_space_curve = gcurve(graph=Jupiter_phase_space, color=color.purple, size=0.1)

#time = 0
while True:
    
    # Phase Space Diagrams (Comment this out if your computer begins smoking)
    Mercury_phase_space_curve.plot(pos=(Mercury.pos.x, np.sqrt(Mercury.v.x ** 2 + Mercury.v.y ** 2)))
    Venus_phase_space_curve.plot(pos=(Venus.pos.x, np.sqrt(Venus.v.x ** 2 + Venus.v.y ** 2))
    Earth_phase_space_curve.plot(pos=(Earth.pos.x, np.sqrt(Earth.v.x ** 2 + Earth.v.y ** 2)))
    Mars_phase_space_curve.plot(pos=(Mars.pos.x, np.sqrt(Mars.v.x ** 2 + Mars.v.y ** 2)))
    Jupiter_phase_space_curve.plot(pos=(Jupiter.pos.x, np.sqrt(Jupiter.v.x ** 2 + Jupiter.v.y ** 2)))

    # Position Vectors:
    R1 = Earth.pos - Sun.pos   # Position of Earth relative to Sun
    L1 = mag(R1)
    R2 = Venus.pos - Sun.pos   # Position of Venus relative to Sun
    L2 = mag(R2)
    R3 = Mercury.pos - Sun.pos   # Position of Mercury relative to Sun
    L3 = mag(R3)
    R4 = Mars.pos - Sun.pos   # Position of Mars relative to Sun
    L4 = mag(R4)
    R5 = Jupiter.pos - Sun.pos   # Position of Jupiter relative to Sun
    L5 = mag(R5)

    Fg1 = (Earth.m * Sun.m * R1 * G1)/L1**3   # Inverse Square Orbit (1/r**2)
    Fg2 = (Venus.m * Sun.m * R2 * G2)/L2**4   # Inverse Cube (1/r**3)
    Fg3 = (Mercury.m * Sun.m * R3 * G3)/L3**2  # Inverse Power (1/r)
    Fg4 = (Mars.m * Sun.m * R4 * G4)   # Linear Power Orbit (r)
    Fg5 = (Jupiter.m * Sun.m * R5 * G5)/L5**5   # Inverse 4th Power Spiral (1/r**4)

    # Momentum Update:
    Earth.p = -Fg1 * dt + Earth.p
    Venus.p = -Fg2 * dt + Venus.p
    Mercury.p = -Fg3 * dt + Mercury.p
    Mars.p = -Fg4 * dt + Mars.p
    Jupiter.p = -Fg5 * dt + Jupiter.p

    # Velocity Update:
    Earth.v = Earth.p / Earth.m
    Venus.v = Venus.p / Venus.m
    Mercury.v = Mercury.p / Mercury.m
    Mars.v = Mars.p / Mars.m
    Jupiter.v = Jupiter.p / Jupiter.m

    # Position Update:
    Earth.pos = Earth.pos + Earth.v * dt
    Venus.pos = Venus.pos + Venus.v * dt
    Mercury.pos = Mercury.pos + Mercury.v * dt
    Mars.pos = Mars.pos + Mars.v * dt
    Jupiter.pos = Jupiter.pos + Jupiter.v * dt

    time = time + dt

    if Jupiter.pos.mag > 10*au:
        break



#   Bertrand's Theorem states that the only two functions for which there exists a stable equilibrium is that of an
#   inverse square law and that of a linear power (Earth and Mars in the code respectively). Every other power results
#   in some sort of eventual spiral into the void (Venus), spiral into doom (Jupiter), or whatever the heck Mercury is
#   doing...




