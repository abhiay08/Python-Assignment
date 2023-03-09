'''10.B.1: ASSIGNMENT
PROBLEM STATEMENT
Matplotlib

- Import data (data_1.csv, data_2.csv) in pandas dataframes

- Plot them in same graph window With respective lables on axis(x/y)
END OF ASSESSMENT
data_1.csv data_1.csv
data_2.csv data_2.csv'''
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

v1=pd.read_csv("F:/pythonProject1/data_1.csv")
#print(v1)
v2=pd.read_csv("F:/pythonProject1/data_2.csv")
#print(v2)
#plt.scatter(v1,v2)
#plt.show()
x=v1.value
y=v2.value
#plt.scatter(x,y)
#plt.show()

#plt.scatter(x,y,marker="*")
#plt.show()
#plotting x and y points
#plt.plot(v1,v2)
#plt.show()

# plt.plot(v1,v2,"o")
# print(plt.show())

# plt.plot(v1)
#plt.show()

# plt.plot(v2)
#plt.show()

# plt.plot(v1, marker="o")
# plt.show()

# plt.plot(v2, marker="o")
# plt.show()

# plt.plot(v1, v2, marker="*" )
# plt.show()

# plt.plot(v1,v2, marker="D")
# plt.show()

# plt.plot(v1, marker="o", ms=20)
# plt.show()

# plt.plot(v1, marker="o", ms=20, mec="r")
# plt.show()

# plt.plot(v1, marker="o", ms=20, mfc="g")
# plt.show()

# plt.plot(v1,marker="o", ms=20, mfc="b")
# plt.show()

# plt.plot(v1, marker="o", ms=20, mec='r',mfc="r")
# plt.show()

# plt.plot(v1, v2, marker="o", ms=15, mec="r",mfc="g")
# plt.show()

# plt.plot(v1,v2,marker="o", ms=15, mec='hotpink', mfc='hotpink')
# plt.show()

# plt.plot(v1, linestyle='dotted')
# plt.show()

# plt.plot(v2, linestyle='dotted')
# plt.show()

# plt.plot(v1,color='r')
# plt.show()

#linewidth
# plt.plot(v1, linewidth='20.5')
# plt.show()

# plt.plot(v2, linewidth='20.5')
# plt.show()

# plt.plot(v1,v2, linewidth='10.5')
# plt.show()

#multiple lines
# plt.plot(v1)
# plt.plot(v2)
# plt.show()

# plt.plot(x,y)
# plt.title("dataset")
# plt.xlabel("value1")
# plt.ylabel("value2")
# plt.show()


# plt.plot(x,y)
# plt.title("dataset")
# plt.xlabel("value1")
# plt.ylabel("value2")
# plt.grid()
# plt.show()

# plt.plot(x,y)
# plt.title("dataset")
# plt.xlabel("value1")
# plt.ylabel("value2")
# plt.grid(color="green", linestyle="--", linewidth=0.5)
# plt.show()


# plt.plot(v1)
# plt.plot(v2)
# plt.subplot(1, 2, 2)
# plt.plot(v1, v2)
# plt.show()

# plt.scatter(x, y, marker="*")
# plt.show()

# plt.scatter(x, y)
# plt.xlabel("value1")
# plt.ylabel("value2")
# plt.show()

# plt.plot(v1)
# plt.plot(v2)
# plt.scatter(v1, v2)
# plt.show()

# plt.scatter(v1, v2, color="hotpink")
# plt.scatter(v1, v2, color='#88c999')
# plt.show()


'''color each dot'''
# colors=np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta","red","green","red","green","blue","yellow","pink"])
# plt.scatter(x, y, c=colors )
# plt.show()

# plt.scatter(x, y, c=colors, cmap='viridis')
# plt.colorbar()
# plt.show()

import matplotlib.pyplot as plt
import  numpy as np
#
x=np.random.randint(100, size=(100))
y=np.random.randint(100, size=(100))
colors=np.random.randint(100, size=(100))
sizes=10 * np.random.randint(100, size=(100))

# plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
# plt.colorbar()
# plt.show()

# plt.scatter(x, y, s=sizes, alpha=0.5)
# plt.show()

# plt.scatter(x, y, c=colors, cmap='viridis')
# plt.show()

# plt.scatter(x, y, s=sizes, alpha=0.5)
# plt.show()


'''matplotlib bars'''

# plt.bar(x, y)
# plt.show()

# plt.barh(x, y)
# plt.show()

# plt.bar(x, y, color="red" )
# plt.show()

# plt.bar(x, y, color="green")
# plt.show()

# plt.bar(x, y, width=0.1)
# plt.show()

# plt.hist(x)
# plt.show()

# plt.hist(y)
# plt.show()

# plt.pie(y)
# plt.show()

# plt.pie(x)
# plt.show()

#notrun
'''seaborn.kdeplot'''
import seaborn as sns
sns.kdeplot(data=v1)

