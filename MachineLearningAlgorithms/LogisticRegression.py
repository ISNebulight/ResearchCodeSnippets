"""
Script By Nebulight
nebulight.info.gf
"""

import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        """
        Initializes the LogisticRegression class.

        Parameters:
        - learning_rate: float specifying the learning rate for gradient descent (default: 0.01)
        - num_iterations: int specifying the number of iterations for gradient descent (default: 1000)
        """
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None

    def _sigmoid(self, z):
        """
        Calculates the sigmoid function.

        Parameters:
        - z: numpy array or float

        Returns:
        - numpy array or float
        """
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        """
        Fits the logistic regression model to the training data.

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
            z = np.dot(X, self.weights) + self.bias
            predictions = self._sigmoid(z)

            # Calculate gradients
            dw = (1 / num_samples) * np.dot(X.T, (predictions - y))
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
        z = np.dot(X, self.weights) + self.bias
        predictions = self._sigmoid(z)
        return predictions