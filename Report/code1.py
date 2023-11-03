import numpy as np
import matplotlib . pyplot as plt
from sklearn . datasets import make_circles
# Generate data with make_circles
np. random . seed (5)
X, y = make_circles ( n_samples =500 , factor =0.3 , noise =0.1)

# Plot data

plt.scatter (X [:, 0], X [:, 1], c=y, cmap=plt.cm.Paired)
plt.show()