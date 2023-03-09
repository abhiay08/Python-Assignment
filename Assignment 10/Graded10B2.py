'''10.B.2: ASSIGNMENT
PROBLEM STATEMENT
Seaborn
- Plot density plot of data_1.csv
END OF ASSESSMENT
data_1.csv data_1.csv'''
import  pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

v1=pd.read_csv('F:/pythonProject1/data_1.csv')
#print(v1)

#run
plt.plot(v1)
# pplt.show()

#not run

print(sns.displot(data=v1))

#not run
print(sns.pairplot(data=v1,size=2.5))

#run
# print(v1.info())
# print(v1.shape)
#print(v1.describe())
#print(v1.dtypes)

plot=sns.displot(v1,color='purple')
plt.show()

