"""
plotty mcplotty amirite
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_style('whitegrid')

plt.plot(np.arange(10))
plt.show()

plt.plot(np.random.randn(100))
plt.show()

plt.plot(np.random.randn(100).cumsum())
plt.show()