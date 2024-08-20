import numpy as np
from matplotlib import pyplot as plt
from numpy import loadtxt

file_267 = open("267.data", "r")
file_360 = open("360.data", "r")

data267 = file_267.read().split('\n')
#print(data267)

data = loadtxt('267.data', dtype='int')
print(data)

index = np.arange(1,len(data)+1,1)
print(index)

max_data = max(data)
min_data = min(data)

print("max data: ", max_data, "min data: ",  min_data)

fig, ax = plt.subplots()
ax.stackplot(index,data)

# Add relevant y and x labels and text to the plot
plt.title('Cumulative Flow Diagram')
plt.show()


