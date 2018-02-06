## HW1 BusinessAnalysis
## Shengya Zhang

import pandas as pd
import matplotlib.pyplot as plt

# install csv file
iris = pd.read_csv('iris.csv')
iris.columns = ['SL','SW','PL','PW','SP']

# print data of files, make sure it has been installed
print(iris)

# bar chart
X = iris.PW
Y1 = iris.PL

plt.bar(X, Y1,width = 0.1,facecolor='#87CEFA')
plt.xlabel('PW')
plt.ylabel('PL')
plt.title('BarChart of PW & PL')

plt.show()
