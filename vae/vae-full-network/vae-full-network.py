import numpy as np

def vae_forward(x: np.ndarray, epsilon: np.ndarray,
                W_mu: np.ndarray, b_mu: np.ndarray,
                W_logvar: np.ndarray, b_logvar: np.ndarray,
                W_dec: np.ndarray, b_dec: np.ndarray) -> dict:
    """
    Returns reconstruction, mu, log_var, and z as float64 arrays.
    """
    mu = x @ W_mu + b_mu
    logvar = x @ W_logvar + b_logvar
    z = mu + np.exp(0.5 * logvar)* epsilon
    reconstruction =  1/(1 + np.exp(-(z @ W_dec + b_dec)))
    return {
        "reconstruction": reconstruction,
        "mu": mu,
        "log_var": logvar,
        "z": z
    }