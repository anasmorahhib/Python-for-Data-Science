#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pi, exp


# In[2]:


domaine = range(-100,100)
mu = 0  # The mean
sigma = 20 # the standard deviation

# Representation of the Gaussian distribution
f = lambda x : 1/(sqrt(2*pi*pow(sigma,2))) * exp(-pow((x-mu),2)/(2*pow(sigma,2)))
y = [f(x) for x in domaine]
plot = plt.plot(domaine, y)


# In[3]:


# We will consider 100 random variables, each with 200 samples.
matrice_aleatoire = np.random.rand(100,200)
sommes = np.sum(matrice_aleatoire,0)


# In[4]:


print("The shape of the variable sums is {}.".format(sommes.shape))


# In[6]:


# Plotting data
plot = plt.scatter(range(200), sommes)


# In[120]:


# Histogram
plot = plt.hist(sommes)


# In[11]:


# use more data
matrice_aleatoire = np.random.rand(10000, 10000)
sommes = np.sum(matrice_aleatoire,0)
plot = plt.hist(sommes, bins=100)


# In[12]:


print("The empirical mean of our distribution is {}."
      .format(np.mean(sommes)))
print("The empirical mean of the variable generated by the rand function is {}."
      .format(np.mean(np.random.rand(100000))))
print("The empirical variance of our distribution is {}."
      .format(np.var(sommes)))
print("The empirical variance of the variable generated by the rand function is {}."
      .format(np.var(np.random.rand(100000))))


# The average of our distribution is equal to the sum of the averages of the distributions that compose it. Variance is the sum of the variances of the distributions that make up our distribution. Be careful, these properties are valid only because our distributions are independent.

# In[ ]:




