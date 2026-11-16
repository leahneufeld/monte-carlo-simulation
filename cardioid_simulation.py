import numpy as np
import matplotlib.pyplot as plt
import random

# QUESTION 1 – SIMPLE VERSION

n = 100
xdata = []
ydata = []
inside = 0

# Bounding box for cardioid r = 1 - cos(theta)
xmin, xmax = -2, 1
ymin, ymax = -1.5, 1.5
box_area = (xmax - xmin) * (ymax - ymin)

for i in range(n):
    x = xmin + (xmax - xmin) * random.random()
    y = ymin + (ymax - ymin) * random.random()

    xdata.append(x)
    ydata.append(y)

    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    r_card = 1 - np.cos(theta)

    if r <= r_card and r_card >= 0:
        inside += 1

area_est = box_area * inside / n

# Plot the random points
plt.plot(xdata, ydata, ".", label="Random points")

# Plot the cardioid
theta_vals = np.linspace(0, 2*np.pi, 500)
r_vals = 1 - np.cos(theta_vals)
x_card = r_vals * np.cos(theta_vals)
y_card = r_vals * np.sin(theta_vals)
plt.plot(x_card, y_card, "r", label="Cardioid boundary")

plt.axis("equal")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Monte Carlo Approximation of Cardioid Area")
plt.legend()
plt.show()

print("Hits =", inside)
print("Trials =", n)
print("Estimated area =", area_est)
