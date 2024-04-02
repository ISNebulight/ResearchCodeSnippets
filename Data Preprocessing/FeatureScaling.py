"""
Script By Nebulight
nebulight.info.gf
"""

import numpy as np

def scale_features(features, target, scale_range=(0, 1)):
    """
    Scales the numerical features in the given dataset to a specified range.

    Parameters:
    - features: numpy array or pandas DataFrame containing the numerical features
    - target: numpy array or pandas DataFrame containing the target variable
    - scale_range: tuple specifying the range to scale the features to (default: (0, 1))

    Returns:
    - scaled_features: numpy array or pandas DataFrame containing the scaled features
    - scaled_target: numpy array or pandas DataFrame containing the scaled target variable
    """
    # Calculate the minimum and maximum values of the features
    min_val = np.min(features)
    max_val = np.max(features)

    # Calculate the range of the scaled features
    scaled_range = scale_range[1] - scale_range[0]

    # Scale the features to the specified range
    scaled_features = (features - min_val) / (max_val - min_val) * scaled_range + scale_range[0]

    # Scale the target variable if provided
    if target is not None:
        scaled_target = (target - min_val) / (max_val - min_val) * scaled_range + scale_range[0]
        return scaled_features, scaled_target
    else:
        return scaled_features
    
# Example usage:
if __name__ == "__main__":
    # Example usage of the scale_features function
    numerical_features = np.array([1, 2, 3, 4, 5])
    scaled_features = scale_features(numerical_features)
    print("Scaled Features:")
    print(scaled_features)