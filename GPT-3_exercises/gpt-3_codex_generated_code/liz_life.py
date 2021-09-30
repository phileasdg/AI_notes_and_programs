"""
When is Liz gonna die?
"""

import numpy as np
import matplotlib.pyplot as plt

# constants
liz_age = 73
liz_lifespan = 85

# create a list of ages
ages = np.arange(0, liz_lifespan)

# create a list of survival probabilities
survival_probabilities = [1 - (liz_age - age) / liz_lifespan for age in ages]

# plot the survival probabilities
plt.plot(ages, survival_probabilities)
plt.xlabel('Age')
plt.ylabel('Probability of Survival')
plt.show()s