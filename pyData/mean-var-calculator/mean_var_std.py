import numpy as np # The calculator must be completed using numpy methods

def calculate(arr):
    # Conditional that checks if the list's length is more than nine
    if len(arr) != 9:
        raise ValueError('List must contain nine numbers.')
    # Conditional for verifying whether or not the list is numpy array
    if isinstance(arr, np.ndarray):
        raise TypeError('Input must be a python list.')
    # The matrix which will hold the 3x3 numpy array
    matrix = np.array(arr).reshape(3, 3)
    # The dict which will store the calculated statisitics
    fin = {
        'mean': [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.mean()],
        'variance': [list(matrix.var(axis=0)), list(matrix.var(axis=1)), matrix.var()],
        'standard deviation': [list(matrix.std(axis=0)), list(matrix.std(axis=1)), matrix.std()],
        'max': [list(matrix.max(axis=0)), list(matrix.max(axis=1)), matrix.max()],
        'min': [list(matrix.min(axis=0)), list(matrix.min(axis=1)), matrix.min()],
        'sum': [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), matrix.sum()]
    }

    return fin