# Import all libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
from scipy.stats import norm

medals= pd.read_csv('data/medals.csv')
meanmedals = statistics.mean(medals['Total'])
varmedals = statistics.variance(medals['Total'])
print(meanmedals, " ",  varmedals)

fig_1, ax_1 = plt.subplots()
ax_1.bar(medals['Country'],medals['Total'],color='skyblue')
ax_1.axhline(y = meanmedals, color='red', linestyle="-")
plt.show()