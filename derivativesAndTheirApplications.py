
import numpy as np
import matplotlib.pyplot as plt

# Generate some fake data
t = np.linspace(0, 10, num=1000)  # 1000 points in time
x = np.sin(t)  # Distance data generated as sine of time

# Estimate the velocity using the central difference method
def compute_velocity_with_fd(x):
    v = []
    for i in range(len(x)-1):
        v.append((x[i+1] - x[i]) / (t[i+1] - t[i]))
    v.append((x[-1] - x[-2]) / (t[-1] - t[-2]))
    return v

v = compute_velocity_with_fd(x)

# Estimate the acceleration using central differences
def compute_acceleration_with_fd(v):
    a = []
    for i in range(1, len(v)-1):
        a.append((v[i+1] - v[i]) / (t[i+1] - t[i]))
    a.append((v[-1] - v[-2]) / (t[-1] - t[-2]))
    return a

a = compute_acceleration_with_fd(v)

# plotting on separate subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 50))

# plot1(distance)
axs[0].plot(t[::10], x[::10], 'bo', label='Distance')
axs[0].set_ylabel('Distance')
axs[0].legend(loc='upper center')

#plot2(velocity)
axs[1].plot(t[::10], v[::10], 'ro', label='Velocity')
axs[1].set_ylabel('Velocity')
axs[1].legend()

# plot3(acceleration)
axs[2].plot(t[::10], a[::10], 'go', label='Acceleration')
axs[2].set_xlabel('Time')
axs[2].set_ylabel('Acceleration')
axs[2].legend(loc='lower center')

plt.show()
