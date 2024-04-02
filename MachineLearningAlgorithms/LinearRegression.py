"""
Script By Nebulight
nebulight.info.gf
"""

import numpy as np

class LinearRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        """
        Initializes the LinearRegression class.

        Parameters:
        - learning_rate: float specifying the learning rate for gradient descent (default: 0.01)
        - num_iterations: int specifying the number of iterations for gradient descent (default: 1000)
        """
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        """
        Fits the linear regression model to the training data.

        Parameters:
        - X: numpy array or pandas DataFrame containing the features
        - y: numpy array or pandas DataFrame containing the target variable
        """
        num_samples, num_features = X.shape

        # Initialize weights and bias
        self.weights = np.zeros(num_features)
        self.bias = 0

        # Gradient descent
        for _ in range(self.num_iterations):
            # Calculate predictions
            predictions = np.dot(X, self.weights) + self.bias

            # Calculate gradients
            dw = (1 / num_samples) * np.dot(X.T, predictions - y)
            db = (1 / num_samples) * np.sum(predictions - y)

            # Update weights and bias
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        """
        Predicts the target variable for the given features.

        Parameters:
        - X: numpy array or pandas DataFrame containing the features

        Returns:
        - numpy array containing the predicted target variable
        """
        predictions = np.dot(X, self.weights) + self.bias
        return predictions