"""
Pendulum plot
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
g = 9.81
l = 1.0
b = 0.0  # Damping

# Initial conditions
x0 = 2.0
v0 = 0.0
t0 = 0.0

# Simulation time, timestep and time
t_max = 20.0
dt = 0.01

t_array = np.arange(t0, t_max, dt)

# Initial state
state = np.array([x0, v0])

# Euler solution
x_euler = np.zeros(t_array.shape)
v_euler = np.zeros(t_array.shape)

# Verlet solution
x_verlet = np.zeros(t_array.shape)
v_verlet = np.zeros(t_array.shape)

# Energy
energy_euler = np.zeros(t_array.shape)
energy_verlet = np.zeros(t_array.shape)

# Euler
for i, t in enumerate(t_array):

    if i == 0:
        continue

    # State
    x_euler[i] = state[0]
    v_euler[i] = state[1]

    # Energy
    energy_euler[i] = 0.5 * l * v_euler[i]**2 + g * l * (1.0 - np.cos(x_euler[i]))

    # Euler step
    state = state + dt * np.array([v_euler[i-1], - (g/l) * np.sin(x_euler[i-1]) - b * v_euler[i-1]])

# Verlet
for i, t in enumerate(t_array):

    if i == 0:
        continue

    # State
    x_verlet[i] = state[0]
    v_verlet[i] = state[1]

    # Energy
    energy_verlet[i] = 0.5 * l * v_verlet[i]**2 + g * l * (1.0 - np.cos(x_verlet[i]))

    # Verlet step
    x_next = 2.0 * state[0] - state[1] * dt + (g/l) * np.sin(state[0]) * dt**2 - state[1] * dt
    v_next = (x_next - state[0]) / (2.0 * dt)

    state = np.array([x_next, v_next])

# Plot
fig, ax = plt.subplots(3, 1, sharex=True)

ax[0].plot(t_array, x_euler, label='Euler')
ax[0].plot(t_array, x_verlet, label='Verlet')
ax[0].set_ylabel('Angle [rad]')
ax[0].legend()

ax[1].plot(t_array, v_euler, label='Euler')
ax[1].plot(t_array, v_verlet, label='Verlet')
ax[1].set_ylabel('Velocity [rad/s]')
ax[1].legend()

ax[2].plot(t_array, energy_euler, label='Euler')
ax[2].plot(t_array, energy_verlet, label='Verlet')
ax[2].set_xlabel('Time [s]')
ax[2].set_ylabel('Energy [J]')
ax[2].legend()


plt.show()