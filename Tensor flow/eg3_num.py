import matplotlib.pyplot as plt
import numpy as np

# Create random seed:
np.random.seed(5484849901)

# Create random data:
xdata = np.random.random([2, 8])  

# Create two datasets from the random floats: 
xdata1 = xdata[0, :]  
xdata2 = xdata[1, :]  

# Sort the data in both datasets:
xdata1.sort()  
xdata2.sort()

# Create y data points:  
ydata1 = xdata1 ** 2
ydata2 = 1 - xdata2 ** 4

# Plot the data:  
plt.plot(xdata1, ydata1)  
plt.plot(xdata2, ydata2)  

# Set x,y lower, upper limits:  
plt.xlim([0, 1])  
plt.ylim([0, 1])  

plt.title(“Multiple Datasets in One Plot")
plt.show()