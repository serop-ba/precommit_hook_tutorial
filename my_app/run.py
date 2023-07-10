"""
This module contains the main execution logic for the project.
"""
import numpy as np
import pandas as pd
from numpy import ndarray
from sklearn.linear_model import LinearRegression


def get_predictions() -> ndarray:
    """Computes the predictions for dummy data using linear regression model..

    Returns
    -------
    ndarray
        predictions
    """
    # Generate Dummy data
    dummy_data = pd.DataFrame(
        {
            "dummy1": np.random.rand(100),
            "dummy2": np.random.rand(100),
            "dummy3": np.random.rand(100),
        }
    )
    true_label = np.random.rand(100)

    # Initialize the LinearRegression model
    model = LinearRegression()

    # Fit the model to the training data
    model.fit(dummy_data, true_label)

    # Make predictions using the trained model
    predictions = model.predict(dummy_data)

    # Print the predictions
    print(predictions)
    return predictions
