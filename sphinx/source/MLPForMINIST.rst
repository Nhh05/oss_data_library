MLPForMINIST Module
===================

This module implements a simple multi-layer perceptron (MLP) for the MNIST dataset.

Classes:
--------

.. autoclass:: MLPForMINIST.MLPForMINIST
   :members:
   :undoc-members:
   :show-inheritance:

Details:
--------

- **fit(X_train, y_train, X_test, y_test, epoch, patience)**: Trains the MLP using backpropagation and gradient descent.
- **predict(X)**: Predicts the class labels for input data.
- **save_model(folder_path)**: Saves the model parameters to a specified folder.
- **load_model(folder_path)**: Loads model parameters from a specified folder.
