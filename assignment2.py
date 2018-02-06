## HW1 BusinessAnalysis
## Shengya Zhang

import pandas as pd
import matplotlib.pyplot as plt

# install csv file
iris = pd.read_csv('iris.csv')
iris.columns = ['SL','SW','PL','PW','SP']

# print data of files, make sure it has been installed
print(iris)

iris.plot(kind='box')
plt.title('BoxPlot of Iris')
plt.xlabel('Label')
plt.ylabel('Value')
plt.show()
