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
PCX = np.empty(numberSteps + 1)
PCY = np.empty(numberSteps + 1)
PCZ = np.empty(numberSteps + 1)

# Set  values
X[0], Y[0], Z[0] = (1, 0, 20)
PCX[0], PCY[0], PCZ[0] = (1, 0, 20)
sigma=10
rho=28
beta=8/3

# Forward Euler Method
for i in range(numberSteps):    
    differentialX, differentialY, differentialZ = lorenz(X[i], Y[i], Z[i], sigma, rho, beta)   
    X[i + 1] = X[i] + (differentialX * differentialT)
    Y[i + 1] = Y[i] + (differentialY * differentialT)
    Z[i + 1] = Z[i] + (differentialZ * differentialT)
    
# Predictor-Corrector Method
for i in range(numberSteps):    
    differentialPCX, differentialPCY, differentialPCZ = lorenz(PCX[i], PCY[i], PCZ[i], sigma, rho, beta) 
    PCX[i + 1] = PCX[i] + (differentialPCX * (differentialT/2))
    PCY[i + 1] = PCY[i] + (differentialPCY * (differentialT/2))
    PCZ[i + 1] = PCZ[i] + (differentialPCZ * (differentialT/2))
    
    differentialPCXM, differentialPCYM, differentialPCZM = lorenz(PCX[i + 1], PCY[i + 1], PCZ[i + 1], sigma, rho, beta)     
    PCX[i + 1] = PCX[i] + (differentialPCXM * differentialT)
    PCY[i + 1] = PCY[i] + (differentialPCYM * differentialT)
    PCZ[i + 1] = PCZ[i] + (differentialPCZM * differentialT)
    
#2D Plot
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
# fig.suptitle('Lorenz Equations')
# ax1.plot(X, Z, lw=0.5)
# ax1.set_title('Euler Forward Method Z(X)')
# ax1.set_xlabel('X')
# ax1.set_ylabel('Z')
# ax2.plot(Y, Z, lw=0.5)
# ax2.set_title('Euler Forward Method Z(Y)')
# ax2.set_xlabel('Y')
# ax2.set_ylabel('Z')
# ax3.plot(PCX, PCZ, lw=0.5)
# ax3.set_title('Predictor-Corrector Method Z(X))')
# ax3.set_xlabel('X')
# ax3.set_ylabel('Z')
# ax4.plot(PCY, PCZ, lw=0.5)
# ax4.set_title('Predictor-Corrector Method Z(Y)')
# ax4.set_xlabel('Y')
# ax4.set_ylabel('Z')

#3D Plot
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot(X, Y, Z, lw=0.5)
# ax.set_xlabel("X Axis")
# ax.set_ylabel("Y Axis")
# ax.set_zlabel("Z Axis")
# ax.set_title("Lorenz Attractor for Euler Method")
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot(PCX, PCY, PCZ, lw=0.5)
# ax.set_xlabel("X Axis")
# ax.set_ylabel("Y Axis")
# ax.set_zlabel("Z Axis")
# ax.set_title("Lorenz Attractor for Predictor-Corrector Method")
    
plt.show()

