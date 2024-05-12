import csv
import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV file
def load_data(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            data.append([float(row[0]), float(row[1]), float(row[2])])
    return np.array(data)

# Logistic function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Cost function
def compute_cost(X, y, w):
    m = len(y)
    h = sigmoid(np.dot(X, w))
    epsilon = 1e-5  # small value to prevent log(0)
    cost = -1/m * np.sum(y * np.log(h + epsilon) + (1 - y) * np.log(1 - h + epsilon))
    return cost

# Gradient descent to optimize weights
def gradient_descent(X, y, w, learning_rate, iterations, print_step):
    m = len(y)
    costs = []
    for i in range(iterations):
        h = sigmoid(np.dot(X, w))
        gradient = 1/m * np.dot(X.T, (h - y))
        w -= learning_rate * gradient
        cost = compute_cost(X, y, w)
        costs.append(cost)
        if (i+1) % print_step == 0:
            print(f"Iteration {i+1}: Cost = {cost}")
    return w, costs

# Load data (change the path to your file if necessary)
filename = "data.csv"  # Change this path as per your file location
data = load_data(filename)

# Add a column of ones for the bias term (w0)
X = np.c_[np.ones(data.shape[0]), data[:, :2]]
y = data[:, 2]

# Initialize weights
np.random.seed(0)
w = np.random.rand(X.shape[1])

# Set hyperparameters
learning_rate = 0.01
iterations = 1000
print_step = 10

# Run gradient descent
w_optimized, costs = gradient_descent(X, y, w, learning_rate, iterations, print_step)

# Plot cost function convergence
plt.plot(range(1, iterations+1), costs)
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.title('Cost Function Convergence')
plt.grid(True)
plt.show()

# Print optimized weights
print("Optimized weights:")
print("w0 =", w_optimized[0])
print("w1 =", w_optimized[1])
print("w2 =", w_optimized[2])
