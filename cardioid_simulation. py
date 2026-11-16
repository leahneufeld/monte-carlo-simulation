#Final Project Question 2

import numpy as np
import matplotlib.pyplot as plt
import random


# Exact cardioid area (Done by hand-refer to report)
A_exact = 3 * np.pi / 2

# Bounding box:
ymin, ymax = -1.3, 1.3
box_area = (xmax - xmin) * (ymax - ymin)

# Monte Carlo Sampling
n = 100 #number of points
inside = 0

xdata = []
ydata = []

# Monte Carlo loop
for i in range(n):
    x = xmin + (xmax - xmin) * random.random()
    y = ymin + (ymax - ymin) * random.random()

    xdata.append(x)
    ydata.append(y)

    r = np.sqrt(x*x + y*y)
    theta = np.arctan2(y, x)
    r_card = 1 - np.cos(theta)

    if r <= r_card and r_card >= 0:
        inside += 1

# Estimate area
A_est = box_area * inside / n

# Plot
plt.plot(xdata, ydata, '.', label="Random points")

theta_vals = np.linspace(0, 2*np.pi, 500)
r_vals = 1 - np.cos(theta_vals)
x_card = r_vals * np.cos(theta_vals)
y_card = r_vals * np.sin(theta_vals)
plt.plot(x_card, y_card, 'r', label="Cardioid")

plt.axis("equal")
plt.title("Monte Carlo Approximation of Cardioid Area")
plt.legend()
plt.show()

print("Hits =", inside)
print("Trials =", n)
print("Bounding box area =", box_area)
print("Estimated cardioid area =", A_est)
print("Exact area =", A_exact)

