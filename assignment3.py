## HW1 BusinessAnalysis
## Shengya Zhang

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# install csv file
iris = pd.read_csv('iris.csv')
iris.columns = ['SL','SW','PL','PW','SP']

sns.lmplot(x="PL", y="PW", hue="SP", truncate=True, data=iris)
plt.xlabel('PL')
plt.ylabel('PW')
plt.title('Iris of PW & PL')

plt.show()
