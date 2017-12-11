#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Assignment: CW12
###

import numpy as np
import nose
import dduffing as df

def test_rk_1():
    # Known value
    desired = 1
    # Implementing function
    t,x,y = df.rk(a = 0, b = 2, x0 = 1, y0 = 0, nu = 0, F = 0)
    actual = x[len(x)-1]
    # error message
    print("We expected x = ",desired,", but we got ",actual)
    # Checking values
    nose.tools.assert_almost_equal(desired,actual,4)

def test_rk_2():
    # Known value
    desired = 0
    # Implementing function
    t,x,y = df.rk(a = 0, b = 2, x0 = 0, y0 = 0, nu = 0, F = 0)
    actual = x[len(x)-1]
    # Error message
    print("We were expecting x = ",desired,", but we actually got ",actual)
    # Checking values
    nose.tools.assert_almost_equal(desired,actual,4)

def test_rk_3():
    # Known value
    desired = -1
    # Implementing function
    t,x,y = df.rk(a = 0, b = 10, x0 = -0.1, y0 = -0.2, nu = 10, F = 0.01)
    actual = x[len(x)-1]
    # Error message
    print("We were expecting x = ",desired,", but we actually got ",actual)
    # Checking values
    nose.tools.assert_almost_equal(desired,actual,3)