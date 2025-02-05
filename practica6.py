# Import necessary libraries
import ipywidgets as widgets
from IPython import display as display
import matplotlib.pyplot as plt
import numpy as np
def create_button():
    # Create the "Next Iteration" button widget
    button = widgets.Button(
        description='Next Iteration',
        disabled=False,
        button_style='',
        tooltip='Next Iteration',
        icon='check'
    )
    return button
# Define the search space limits
lower_limit = -20
upper_limit = 20
# Number of particles and dimensions for the 3D optimization problem
n_particles = 20
n_dimensions = 3
# Define Rosenbrock's function

def rosenbrock(x, y, z):
    a = 1.0
    b = 100.0
    c = 100.0
    return (a - x)**2 + b * (y - x**2)**2 + c * (z - y**2)**2
# Initialize particle positions and velocities in the 3D space
X = lower_limit + (upper_limit - lower_limit) * np.random.rand(n_particles, n_dimensions)
V = -(upper_limit - lower_limit) / 2 + (upper_limit - lower_limit) * np.random.rand(n_particles, n_dimensions)

# Initialize global and local fitness values
fitness_gbest = np.inf
fitness_lbest = np.full(n_particles, np.inf)
# Initialize global and local best positions
X_lbest = np.copy(X)
X_gbest = X_lbest[0].copy()
# Initialize fitness values for the current particle positions
fitness_X = np.zeros(n_particles)
count = 0
# Define PSO parameters
weight = 0.5
C1 = 0.3
C2 = 0.2
def iteration(b):
    global count
    global weight, C1, C2
    global X, X_lbest, X_gbest, V
    display.clear_output(wait=True)
    display.display(button)
    count += 1

# Update the particle velocities and positions
for i in range(n_particles):
    for j in range(n_dimensions):
        R1 = np.random.rand()
        R2 = np.random.rand()
        V[i][j] = (weight * V[i][j] + C1 * R1 * (X_lbest[i][j] - X[i][j]) + C2 * R2 * (X_gbest[j] - X[i][j]))
        X[i][j] = X[i][j] + V[i][j]

    # Calculate the fitness of the new position
    fitness_X[i] = rosenbrock(X[i][0], X[i][1], X[i][2])

    # Update local best position if necessary
    if fitness_X[i] < fitness_lbest[i]:
        X_lbest[i] = X[i].copy()
        fitness_lbest[i] = fitness_X[i]
    # Update global best position if necessary
    if fitness_X[i] < rosenbrock(X_gbest[0], X_gbest[1], X_gbest[2]):
        X_gbest = X_lbest[i].copy()
    print(count, "Best particle in:", X_gbest, " gbest: ", rosenbrock(X_gbest[0], X_gbest[1], X_gbest[2]))

# Create the "Next Iteration" button
button = create_button()
button.on_click(iteration)
display.display(button)
