import numpy as np

def max_pooling_2d(X: list, pool_size: int) -> list:
    """
    Returns non-overlapping maximum-pooled windows.
    """
    X = np.array(X)
    h, w = X.shape
    h_out = h // pool_size
    w_out = w // pool_size

    output = np.zeros((h_out, w_out))

    for i in range(h_out):
        for j in range(w_out):
            output[i, j] = np.max(X[i*pool_size:(i+1)*pool_size, j*pool_size:(j+1)*pool_size])

    return output.tolist()