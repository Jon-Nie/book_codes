import numpy as np
from scipy.stats import norm, cauchy, gaussian_kde
import matplotlib.pyplot as plt

normal_distribution = []
cauchy_distribution = []
mixed_distribution = []

for _ in range(1_000_000):
    random_number = np.random.random()
    if random_number < 0.05:
        mixed_distribution.append(np.random.normal(0, 16))
    else:
        mixed_distribution.append(np.random.normal(0, 1))

mixed_density = gaussian_kde(mixed_distribution)

for x in np.linspace(-4,4,1_000):
    normal_distribution.append(norm(0, 1).pdf(x))
    cauchy_distribution.append(cauchy(0, 1).pdf(x))

plt.plot(np.linspace(-4,4,1_000), normal_distribution, label="Normal", linewidth=0.8)
plt.plot(np.linspace(-4,4,1_000), cauchy_distribution, label="Cauchy", linewidth=0.8)
plt.plot(np.linspace(-4,4,1_000), mixed_density(np.linspace(-4,4,1_000)), label="Mixture", linewidth=0.8)
plt.title("Comparison of standard normal, cauchy and mixture distribution")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()