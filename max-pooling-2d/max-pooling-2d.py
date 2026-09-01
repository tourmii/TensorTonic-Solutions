import numpy as np

def max_pooling_2d(X: list, pool_size: int) -> list:
    """
    Returns non-overlapping maximum-pooled windows.
    """
    X = np.array(X)
    h, w = X.shape
    h_out = h // pool_size
    w_out = w // pool_size

    output = X.reshape(h_out, pool_size, w_out, pool_size).max(axis=(1,3))
    
    return output.tolist()