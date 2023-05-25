#!/usr/bin/env python
# coding: utf-8

# # Creating a Chess Board with Python

#    I. To create a chessboard with the python programming language, I have used two Python Libraries are Matplotlib and NumPy.
#    
#    II. Matplotlib for Visualization and NumPy for building an algorithm which will help us to create and visualize a chessboard.

# In[1]:


#importing Libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
#LogNorm class is used to normalize a value to the range of 0-1 on a log scale.


# In[2]:


dx, dy = 0.015, 0.05
x = np.arange(-4.0, 4.0, dx)
y = np.arange(-4.0, 4.0, dy)
X, Y =np.meshgrid(x, y)
extent = np.min(x), np.max(x),np.min(y), np.max(y)
z1 = np.add.outer(range(8), range(8)) % 2
plt.imshow(z1, cmap="binary_r", interpolation="nearest",extent=extent, alpha=1)


# In[3]:


dx, dy = 0.015, 0.05
x = np.arange(-4.0, 4.0, dx)
y = np.arange(-4.0, 4.0, dy)
X, Y =np.meshgrid(x, y)
extent = np.min(x), np.max(x),np.min(y), np.max(y)
z1 = np.add.outer(range(8), range(8)) % 2
plt.imshow(z1, cmap="binary_r", interpolation="nearest",extent=extent, alpha=1)
def chess(x, y):
    return(1-x/2+x**5+y**6)*np.exp(-(x**2+y**2))
z2 = chess(X, Y)
plt.imshow(z2, alpha=0.7, interpolation="bilinear",extent=extent)
plt.title("Chess Board with Python")
plt.show()


# In[ ]:




