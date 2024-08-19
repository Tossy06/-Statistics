# Import all libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
from scipy.stats import norm
'''
data_example = pd.DataFrame([1,2,3,3,5,6,7,9])
data_example.plot(kind='box')
print('Media: ', data_example.mean())
print('Desvio: ', data_example.std())
print('Q3: ', np.percentile(data_example, [75]))
print('Q3 - Q1: ', np.percentile(data_example, [75, 25]))
print('Rango intercuartil: ', 6.25-2.75)
'''
#Metodo para saber todo lo anterior de una vez
#print('Data example describe: ', data_example.describe())

x_norm = np.arange(-3,3,0.001)
plt.plot(x_norm,norm.pdf(x_norm,0,1))
plt.axvline(x = 0, color= 'red', linestyle='-' )
plt.show()