## HW1 BusinessAnalysis
## Shengya Zhang

import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('Iris.csv')
iris.columns = ['SL','SW','PL','PW','SP']

ax = iris.plot.scatter(x='SL',y='SW',color='DarkBlue',label='Class1')
iris.plot.scatter(x='PL',y='PW',color='LightGreen',label='Class2',ax=ax)
plt.title('Colored Plot of Iris')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()

