import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler

# Load the MNIST dataset
print("Fetching MNIST data...")
mnist = fetch_openml('mnist_784', version=1)
X, y = mnist.data, mnist.target.astype(int)

# Standardize the data
print("Standardizing data...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform t-SNE
print("Performing t-SNE...")
tsne = TSNE(n_components=2, random_state=42, n_iter=1000, verbose=1, perplexity=30)
X_tsne = tsne.fit_transform(X_scaled)

# Visualize the result
print("Visualizing t-SNE result...")
plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='tab10', s=1, alpha=0.6)
plt.colorbar(scatter, ticks=range(10), label='Digit Label')
plt.title('t-SNE Visualization of MNIST Dataset')
plt.xlabel('t-SNE Feature 1')
plt.ylabel('t-SNE Feature 2')
plt.show()
