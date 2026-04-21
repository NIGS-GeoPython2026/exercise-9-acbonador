"""Functions used in Exercise 8 of Geol 197 GDAM"""

# Import any modules needed in your functions here
import math

import numpy as np

# Define your new functions below
def gaussian_first(mean, stddev, x):
  return (1 / (stddev * np.sqrt(2 * np.pi)))* (np.exp(-((x - mean)**2) / (2 * stddev**2)))
def gaussian(mean, stddev, x_array):
  prob = np.zeros(len(x_array))
  for i in range(len(x_array)):
    x = x_array[i]
    prob[i] = (1 / (stddev * np.sqrt(2 * np.pi)))* (np.exp(-((x - mean)**2) / (2 * stddev**2)))
  return prob

import numpy as np
#Define new function linregress
def linregress(x,y):
    delta  = (len(x) * (x**2).sum()) - (x.sum()**2)
    A = (((x**2).sum() * y.sum()) - (x.sum() * (x*y).sum()))/delta
    B = ((len(x) * (x*y).sum()) - (x.sum() * y.sum()))/delta
    return A, B

def pearson(x,y):
    x = np.array(x)
    y = np.array(y)
    numerator = np.sum((x-x.mean()) * (y - y.mean()))
    denominator = np.sqrt(np.sum((x - x.mean())**2) * np.sum((y -y.mean())**2))
    r = numerator / denominator
    return r

from numpy import mean
def chi_squared(observed, expected, stdev):
    observed = np.array (observed)
    expected = np.array (expected)
    stdev = np.array(stdev)
    N = len(observed)
    chi = (np.sum(((observed - expected)**2) / (stdev**2)))/ (N)
    return chi