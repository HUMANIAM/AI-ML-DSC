
import numpy as np 
import matplotlib.pyplot as plt

"""
EXE1: fit a model to predict data based on city population and the profit of a food truck in that city.
"""

# load and visualize the data.
data = np.genfromtxt('ex1data1.txt', delimiter=',');
m, n = data.shape


# apply gd as optimization algorithm.
X, Y = data[:, 0].reshape((-1,1)), data[:, 1].reshape((-1,1))
X = np.column_stack((np.ones((m, 1)), X))
theta = np.zeros((2, 1))

iterations = 15000
alpha = 0.01
predicted_y, costs = [], []

# compute mean square error
def compute_mse(actual_y, predicted_y):
    return np.mean(np.square(actual_y - predicted_y))/2
    pass

def predict():
    return np.dot(X, theta)
    pass

def update_params(PY, AY):
    #th_j = th_j - (alpha/m) * mean((PY - AY)*X_j)
    return theta - (alpha/m) * np.mean((PY-AY) * X)
    pass

for i in range(iterations):
    predicted_y = predict()
    costs.append(compute_mse(Y, predicted_y))
    theta = update_params(predicted_y, Y)
    
print(costs[-1])
# plt.plot(range(1500), costs)
plt.plot(X, Y, 'rx')
plt.plot(X, predicted_y)
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000s')
plt.show()