"""
Script By Nebulight
nebulight.info.gf
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def split_dataset(features, target, test_size=0.2, random_state=42):
    """
    Splits the dataset into training and testing sets.

    Parameters:
    - features: numpy array or pandas DataFrame containing the features
    - target: numpy array or pandas DataFrame containing the target variable
    - test_size: float or int specifying the proportion of the dataset to include in the test set (default: 0.2)
    - random_state: int specifying the random seed for reproducibility (default: 42)

    Returns:
    - X_train: numpy array or pandas DataFrame containing the training features
    - X_test: numpy array or pandas DataFrame containing the testing features
    - y_train: numpy array or pandas DataFrame containing the training target variable
    - y_test: numpy array or pandas DataFrame containing the testing target variable
    """
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=test_size, random_state=random_state)

    return X_train, X_test, y_train, y_test

# Example usage:
def main():
    # Load dataset from CSV file
    file_path = 'dataset.csv'  # Replace 'dataset.csv' with your actual CSV file path
    df = pd.read_csv(file_path)

    # Extract features and target from the dataset
    features = df.drop(columns=['target']).values
    target = df['target'].values

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = split_dataset(features, target, test_size=0.25, random_state=42)

    print("Training Features:")
    print(X_train)
    print("Testing Features:")
    print(X_test)
    print("Training Target:")
    print(y_train)
    print("Testing Target:")
    print(y_test)

if __name__ == "__main__":
    main()