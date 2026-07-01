# Stationary Covariance Spectra of Discrete-Time Non-Normal Random Recurrent Dynamics

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![ArXiv](https://img.shields.io/badge/arXiv-2606.31944v1-orange)

## Overview

This repository contains an implementation of the research paper **"Stationary covariance spectra of discrete-time non-normal random recurrent dynamics"** by Jacob A. Zavatone-Veth ([arXiv link](https://arxiv.org/pdf/2606.31944v1)). The paper explores the spectral properties of stationary covariance matrices in discrete-time random recurrent neural networks with non-normal synaptic weight matrices. It uses a free-probability approach to derive a closed functional equation for the moment generating function of the limiting stationary covariance spectrum.

The implementation provided here reproduces the main theoretical results of the paper and provides tools to simulate and analyze the stationary covariance spectra of random non-normal recurrent dynamics.

---

## Core Idea

Principal Component Analysis (PCA) is a powerful tool for understanding the structure of dynamics in recurrent neural networks. For stationary noise-driven dynamics, the eigenvalue spectrum of the stationary covariance matrix determines how variance is distributed across principal components.

While the spectral properties of covariance matrices for linear networks with **normal** synaptic weights are well understood, the case for **non-normal** dynamics is less explored. Non-normal matrices are characterized by their non-orthogonal eigenvectors, leading to rich and complex dynamics.

The paper addresses this gap by:
1. Deriving a **closed functional equation** for the moment generating function of the stationary covariance spectrum in discrete-time dynamics with random non-normal Gaussian weights.
2. Analyzing the behavior of tail eigenvalues in critical regimes.
3. Comparing the discrete-time case to continuous-time dynamics, where the latter results in an infinite hierarchy of Schwinger-Dyson equations.

This implementation focuses on the discrete-time case, providing numerical tools to simulate random recurrent networks and compute their stationary covariance spectra.

---

## How It Works

This implementation follows the theoretical framework outlined in the paper. The key steps are:

1. **Random Weight Matrix Generation**:
   - A random synaptic weight matrix \( W \) is generated with Gaussian-distributed entries.
   - The matrix is non-normal, meaning \( W W^T \neq W^T W \).

2. **Dynamics Simulation**:
   - The discrete-time dynamics are modeled as:
     \[
     x_{t+1} = W x_t + \eta_t
     \]
     where \( x_t \) is the state vector at time \( t \), and \( \eta_t \) is Gaussian noise.

3. **Stationary Covariance Matrix**:
   - The stationary covariance matrix \( C \) is computed as:
     \[
     C = \mathbb{E}[x_t x_t^T]
     \]

4. **Spectrum Analysis**:
   - The eigenvalue spectrum of \( C \) is analyzed to understand the distribution of variance among the principal components.
   - The moment generating function (MGF) of the spectrum is computed using the closed functional equation derived in the paper.

5. **Visualization**:
   - The eigenvalue spectrum and MGF are visualized to provide insights into the behavior of the system.

---

## Installation

To use this implementation, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/non-normal-recurrent-dynamics.git
cd non-normal-recurrent-dynamics
pip install -r requirements.txt
```

---

## Usage

The main implementation is provided in the `implementation.py` script. Below is an example of how to use the script to simulate and analyze the stationary covariance spectra.

### Example Usage

```bash
python implementation.py --matrix_size 100 --time_steps 1000 --noise_std 0.1 --plot_spectrum
```

### Command-Line Arguments

| Argument           | Description                                                                 | Default Value |
|--------------------|-----------------------------------------------------------------------------|---------------|
| `--matrix_size`    | Size of the random synaptic weight matrix \( W \).                         | `100`         |
| `--time_steps`     | Number of time steps for simulating the dynamics.                          | `1000`        |
| `--noise_std`      | Standard deviation of the Gaussian noise \( \eta_t \).                     | `0.1`         |
| `--plot_spectrum`  | Whether to plot the eigenvalue spectrum of the stationary covariance matrix.| `False`       |

### Output

- **Eigenvalue Spectrum Plot**: If `--plot_spectrum` is enabled, the script generates a plot of the eigenvalue spectrum of the stationary covariance matrix.
- **Numerical Results**: The script prints the eigenvalues and key statistics (e.g., mean, variance) of the spectrum to the console.

---

## Example Workflow

Here’s a step-by-step example of how to use the repository:

1. **Generate a random non-normal weight matrix**:
   ```bash
   python implementation.py --matrix_size 200 --time_steps 2000 --noise_std 0.2
   ```

2. **Analyze the stationary covariance spectrum**:
   ```bash
   python implementation.py --matrix_size 150 --time_steps 1500 --noise_std 0.05 --plot_spectrum
   ```

3. **Compare results for different noise levels**:
   Run the script with varying `--noise_std` values to observe how noise affects the spectrum.

---

## Results

The implementation reproduces the key findings of the paper, including:
- The shape of the stationary covariance spectrum for random non-normal dynamics.
- The behavior of tail eigenvalues in critical regimes.
- Insights into the role of non-normality in shaping the dynamics of recurrent networks.

---

## Contributing

Contributions are welcome! If you find a bug or have ideas for improvements, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## References

- Jacob A. Zavatone-Veth, *Stationary covariance spectra of discrete-time non-normal random recurrent dynamics*. [arXiv:2606.31944v1](https://arxiv.org/pdf/2606.31944v1)

---

Happy coding! 😊