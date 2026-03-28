import pytest
# TODO: add necessary import
import numpy as np
from ml.model import train_model, compute_model_metrics, inference
# TODO: implement the first test. Change the function name and input as needed
def test_train_model():
    """
    Test that model is trained and returned successfully.
    """
    X = np.array([[1, 2], [3, 4]])
    y = np.array([0, 1])
    model = train_model(X, y)
    assert model is not None


# TODO: implement the second test. Change the function name and input as needed
def test_inference():
    """
    Test that inference returns predictions of correct length.
    """
    X = np.array([[1, 2], [3, 4]])
    y = np.array([0, 1])
    model = train_model(X, y)
    preds = inference(model, X)
    assert len(preds) == len(y)



# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Test that precision, recall, and F1 score are correct for a known example.
    """
    y = np.array([1, 1, 0, 0])
    preds = np.array([1, 0, 0, 0])

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert precision == 1.0
    assert recall == 0.5
    assert round(fbeta, 4) == 0.6667
