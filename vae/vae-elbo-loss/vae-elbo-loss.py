import numpy as np

def vae_loss(x: np.ndarray, reconstruction: np.ndarray,
             mu: np.ndarray, log_var: np.ndarray) -> dict:
    """
    Returns total_loss, reconstruction_loss, and kl_loss as Python floats.
    """
    B = len(x)
    reconstruction_loss = (1/B) * np.sum((x-reconstruction)**2)
    kl_loss = (-1/(2*B)) * np.sum(1 + log_var - mu ** 2 - np.exp(log_var))

    total_loss = reconstruction_loss + kl_loss

    return {
        'total_loss': float(total_loss),
        'reconstruction_loss': float(reconstruction_loss),
        'kl_loss': float(kl_loss)
    }