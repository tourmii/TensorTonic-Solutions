import numpy as np

def kl_divergence(mu: np.ndarray, log_var: np.ndarray) -> float:
    """
    Returns: float scalar KL divergence averaged over the batch
    """
    # Your implementation here
    var = np.exp(log_var)
    kl = -0.5 * np.sum(1 + log_var - (mu ** 2) - var, axis=1).mean(axis=0)
    return kl