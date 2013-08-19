#!/usr/bin/python

import scipy
from scipy.optimize import fmin

k0 = 1.0
kp = 0.8
l  = 1.0
A0 = scipy.sqrt(2) / 2

def scattering_functional(args):
    A = args[0]
    B = args[1]
    C = args[2]
    D = args[3]
    mu = args[4]
    ll = args[5]
    lr = args[6]
    alpha = args[7]
    v = 0.5 * (k0**2 - kp**2)
    return (A**2 + B**2) * 0.5 * k0**2            \
      + (C**2 + D**2) * ((0.5 * kp**2) + v)       \
      - mu * (A**2 + B**2 + C**2 + D**2 -1.0)     \
      + ll * (A**2 - A0**2) + lr * D**2           \
      + alpha * (k0 * (A**2 - B **2) - kp * (C**2 - D**2))

def main():
	startvals = [1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
	results = fmin(scattering_functional, startvals)
	print results
	print scattering_functional(results)


if __name__ == "__main__":
	main()
