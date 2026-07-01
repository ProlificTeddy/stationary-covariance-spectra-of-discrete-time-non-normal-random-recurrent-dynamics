import numpy as np
import torch

def generate_random_weights(n, mean=0.0, std=1.0):
    """
    Generate a random non-normal Gaussian weight matrix.
    """
    W = np.random.normal(mean, std, (n, n))
    return W

def stationary_covariance_spectrum(W, noise_std=1.0, num_samples=1000):
    """
    Compute the stationary covariance spectrum for a discrete-time random non-normal system.
    """
    n = W.shape[0]
    noise = np.random.normal(0, noise_std, (n, num_samples))
    x = np.zeros((n, num_samples))
    
    # Simulate the dynamics
    for t in range(1, num_samples):
        x[:, t] = W @ x[:, t-1] + noise[:, t]
    
    # Compute the stationary covariance matrix
    cov_matrix = np.cov(x)
    
    # Compute the eigenvalues (spectrum) of the covariance matrix
    eigenvalues = np.linalg.eigvalsh(cov_matrix)
    return eigenvalues

def main():
    # Parameters
    n = 50  # Size of the weight matrix
    mean = 0.0
    std = 1.0
    noise_std = 0.1
    num_samples = 1000

    # Generate random non-normal weight matrix
    W = generate_random_weights(n, mean, std)

    # Compute the stationary covariance spectrum
    spectrum = stationary_covariance_spectrum(W, noise_std, num_samples)

    # Print results
    print("Stationary covariance spectrum (eigenvalues):")
    print(spectrum)

if __name__ == '__main__':
    main()