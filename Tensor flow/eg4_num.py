import matplotlib.pyplot as plt
import numpy as np


# Create a Figure with 2 rows and 2 columns of subplots:
fig, ax = plt.subplots(2, 2)

x = np.linspace(0, 5, 100)

# Index 4 Axes arrays in 4 subplots within 1 Figure: 
ax[0, 0].plot(x, np.sin(x), 'g') #row=0, column=0
ax[1, 0].plot(range(100), 'b') #row=1, column=0
ax[0, 1].plot(x, np.cos(x), 'r') #row=0, column=1
ax[1, 1].plot(x, np.tan(x), 'k') #row=1, column=1

plt.show()
