cindy_coding_notes

# -*- coding: utf-8 -*-
"""
Authors: Cindy Pino
Date: 3/27/2020
Description: Notes and things I  use a lot when coding.
"""

###Generating random numbers with NumPy 
import numpy as np 

###To generate a random number from the normal distribution 
np.random.normal()
np.random.normal(size = 4) #generate an array with 4 random numbers 

###To generate integeres between 1 to 100
np.random.randint(low = 1, high = 100, size = 4) #generates an array with four random numbers 

### plotting using python
 matplotlib.pyplot.subplots()