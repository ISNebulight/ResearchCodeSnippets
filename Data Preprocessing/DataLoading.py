"""
Script By Nebulight
nebulight.info.gf
"""

import pandas as pd

def load_csv(file_path):
    """
    Load a CSV dataset into a pandas DataFrame.

    Args:
    - file_path (str): The path to the CSV file.

    Returns:
    - df (pandas.DataFrame): The loaded DataFrame.
    """
    try:
        # Load CSV file into a DataFrame
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    # Example usage
    file_path = 'dataset.csv'  # Replace 'dataset.csv' with your actual CSV file path
    df = load_csv(file_path)
    
    if df is not None:
        print("DataFrame loaded successfully:")
        print(df.head())  # Display the first few rows of the DataFrame
    else:
        print("Failed to load DataFrame.")

if __name__ == "__main__":
    main()
