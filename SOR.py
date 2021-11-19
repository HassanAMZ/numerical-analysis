import numpy as np

lengthArrayBase = [5] * 50 #Array of 50 element where each entry is 5
solutionArrayBase = [2]*50 #Array of 50 element where each entry is 2
solutionArrayBase[0]=1 #Updating the first entry to 1
solutionArrayBase[49]=1 #Updating the last entry to 1
initialConditionArray=[0]*50 #Array of 50 element where each entry is 0

#Diagnalizing the matrix by 5
np.diag(lengthArrayBase)
QuestionMatrix = [[0] * len(lengthArrayBase) for _ in range(len(lengthArrayBase))]
for i, e in enumerate(lengthArrayBase):
  QuestionMatrix[i][i] = e
  
#Updating the secondary and tertiary diagonals to -1
for i in range(len(QuestionMatrix)):
  for j in range(len(QuestionMatrix)):
    if not i==j:
      if i-3<j < i+3:
        QuestionMatrix[i][j] = -1

#SOR algorithem
def sor_solver(A, b, omega, initial_guess, convergence_criteria):
  step = 0
  phi = initial_guess[:]
  residual = np.linalg.norm(np.matmul(A, phi) - b) 
  while residual > convergence_criteria:
      for i in range(A.shape[0]):
          sigma = 0
          for j in range(A.shape[1]):
              if j != i:
                  sigma += A[i, j] * phi[j]
          phi[i] = (1 - omega) * phi[i] + (omega / A[i, i]) * (b[i] - sigma)
      residual = np.linalg.norm(np.matmul(A, phi) - b)
      step += 1
      print("Step {} Residual: {:10.6g}".format(step, residual))
  return phi

#Assiging the values to a function
residual_convergence = 1e-5
omega = 1.7 
A = np.array(QuestionMatrix)
print("Matrix A: ",A)
b = np.array(solutionArrayBase)
print("Solution Matrix B: ",b)
initial_guess = np.zeros(50)
print("Initial Conditions: ",initial_guess)
phi = sor_solver(A, b, omega, initial_guess, residual_convergence)
print("Solution Set of the Matrix A for omega ",omega, " = ",phi)