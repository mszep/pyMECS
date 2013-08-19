#!/usr/bin/python

import scipy
from scipy import sqrt
from scipy.optimize import fmin_slsqp
from numpy import array

k0 = 1.0
kp = 0.9
v = 0.5 * (k0**2 - kp**2)
A0 = sqrt(2) / 2
D0 = 0.0

def energy(args):
    [A, B, C, D] = args
    psiHpsi = (A**2 + B**2) * 0.5 * k0**2 + (C**2 + D**2) * ((0.5 * kp**2) + v)
    psipsi  = A**2 + B**2 + C**2 + D**2
    return psiHpsi / psipsi

def constr_WF_left(A, B, C, D):
    return (A**2 - A0**2)

def constr_WF_right(A, B, C, D):
    return (D**2 - D0**2)

def constr_current(A, B, C, D):
    return k0 * (A**2 - B**2) - kp * (C**2 - D**2)

def constr_cont(A, B, C, D):
    return A + B - C - D

def constr_all(args):
    [A, B, C, D] = args
  # return array([constr_norm(A, B, C, D), constr_WF_left(A, B, C, D),         \
  #               constr_WF_right(A, B, C, D), constr_current(A, B, C, D)])
    return array([constr_WF_left(A, B, C, D), constr_WF_right(A, B, C, D),     \
                  constr_current(A, B, C, D), constr_cont(A, B, C, D)])

def main():
    startvals = [0.1, 0.0, 0.0, 0.0]
    [out, fx, its, imode, smode] = \
    fmin_slsqp(energy, startvals, f_eqcons=constr_all, iprint=2, full_output=1)
    print "Results: "
    print "A = ", out[0]
    print "B = ", out[1]
    print "C = ", out[2]
    print "D = ", out[3]

if __name__ == "__main__":
    main()

