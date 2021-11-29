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

# Set  values
X[0], Y[0], Z[0] = (1, 0, 20)
sigma=10
rho=28
beta=8/3

# Predictor-Corrector
for i in range(numberSteps):    
    differentialX, differentialY, differentialZ = lorenz(X[i], Y[i], Z[i], sigma, rho, beta) 
    X[i + 1] = X[i] + (differentialX * (differentialT/2))
    Y[i + 1] = Y[i] + (differentialY * (differentialT/2))
    Z[i + 1] = Z[i] + (differentialZ * (differentialT/2))
    
    differentialXM, differentialYM, differentialZM = lorenz(X[i + 1], Y[i + 1], Z[i + 1], sigma, rho, beta)     
    X[i + 1] = X[i] + (differentialXM * differentialT)
    Y[i + 1] = Y[i] + (differentialYM * differentialT)
    Z[i + 1] = Z[i] + (differentialZM * differentialT)
    
# 2D Plot
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Eular Method for Lorez Equations')
ax1.plot(X,Z,lw=0.5)
ax1.set_title('Z(X)')
ax1.set_xlabel('X')
ax1.set_ylabel('Z')
ax2.plot(Y,Z,lw=0.5)
ax2.set_title('Z(Y)')
ax2.set_xlabel('Y')
ax2.set_ylabel('Z')
plt.show()

# 3D Plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(X,Y,Z, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor for Predictor-Corrector Method")
plt.show()