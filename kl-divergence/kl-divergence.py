import numpy as np

def kl_divergence(p: list, q: list, eps: float = 1e-12) -> float:
    """
    Returns the divergence as a float.
    """
    # Write code here
    p_arr = np.array(p)
    q_arr = np.array(q)

    positive = p_arr > 0
    p_pos = p_arr[positive]
    q_pos = np.clip(q_arr[positive], eps, None)

    res = np.sum(p_pos * np.log(p_pos / q_pos))

    return float(res)