## HW1 BusinessAnalysis
## Shengya Zhang
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import spline


iris = pd.read_csv('Iris.csv')
iris.columns = ['SL','SW','PL','PW','SP']
print(iris)

plt.scatter(iris.PL,
            iris.PW,
            s = 30,
            c = 'steelblue',
            marker = 's',
            alpha = 0.9,
            linewidths = 0.3,
            edgecolors = 'red'
            )
plt.title('Scatter Plot of Iris')
plt.xlabel('PL')
plt.ylabel('PW')
plt.show()



