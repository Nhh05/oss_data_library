DataPreProcessor Module
=======================

This module contains utilities for preprocessing and transforming datasets.

Classes:
--------

.. autoclass:: oss_png_transfer.DataPreProcessor.DataPreProcessor
   :members:
   :undoc-members:
   :show-inheritance:

Details:
--------

- **shuffle_train_test_data(X_data, y_data, train_ratio, seed)**: Shuffles and splits data into training and testing sets.
- **flatten(data)**: Flattens multi-dimensional arrays into 1D arrays.
- **encode(labels)**: Encodes labels using one-hot encoding.
- **scale_data(data_bundle)**: Scales data to a range of 0 to 1.

