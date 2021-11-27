import numpy as np
import matplotlib.pyplot as plt

def lorenz(x, y, z, sigma, rho, beta):
    differentialX = sigma*(y - x)
    differentialY = rho*x - y - x*z
    differentialZ = x*y - beta*z
    return differentialX, differentialY, differentialZ

# Need one more for the  values 
differentialT = 0.01
numberSteps = 10000
X = np.empty(numberSteps + 1)
Y = np.empty(numberSteps + 1)
Z = np.empty(numberSteps + 1)
T= range(1, 10000)
# Set  values
X[0], Y[0], Z[0] = (1, 0, 20)

# Step through "time", calculating the partial derivatives at the current point and using them to estimate the next point
for i in range(numberSteps):    
    differentialX, differentialY, differentialZ = lorenz(X[i], Y[i], Z[i], sigma=10, rho=28, beta=8/3)
    X[i + 1] = X[i] + (differentialX * differentialT)
    Y[i + 1] = Y[i] + (differentialY * differentialT)
    Z[i + 1] = Z[i] + (differentialZ * differentialT)

# Plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(X, Y, Z, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")
plt.show()