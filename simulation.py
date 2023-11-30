import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Wave parameters
K = 0.1  # Wavenumber (smaller for a larger scale)
w = 1.0  # Angular frequency
phi = 0  # Phase
A = 0.1  # Amplitude (smaller for a smaller amplitude)

# Simulation parameters
x = np.linspace(-50, 50, 100)  # x coordinates (larger for a larger scale)
y = np.linspace(-50, 50, 100)  # y coordinates (larger for a larger scale)
X, Y = np.meshgrid(x, y)  # Creates a 2D grid

# Gerstner wave function
def gerstner_wave(X, Y, t):
    r = np.sqrt(X**2 + Y**2)  # Distance to the center
    Z = A * np.cos(K*r - w*t + phi)
    return Z

# Create the 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Update function for the animation
def update(t):
    ax.clear()
    Z = gerstner_wave(X, Y, t)
    ax.plot_surface(X, Y, Z, cmap='ocean')

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 100), interval=100)

# Save the animation as a video
ani.save('wave.mp4', writer='ffmpeg')

plt.show()
