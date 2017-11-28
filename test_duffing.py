#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Assignment: CW12
###

import numpy as np
import nose
import dduffing as df

"""This module constains three test functions for three simple cases of the system"""

def test_rk_1():
    """This test function tests for the case where the ball starts at rest in the potential well at
    x = 1, with no driving force and no damping constant.  We expect the ball to stay at x = 1 indefinitely."""

    # Setting the known end value
    desired = 1
    # Implementing the function
    t,x,y = df.rk(a = 0, b = 2, x0 = 1, y0 = 0, nu = 0, F = 0)
    actual = x[len(x)-1]
    # Debug message
    print("We expected x = ",desired,", but we got ",actual)
    # Asserting the values
    nose.tools.assert_almost_equal(desired,actual,4)

def test_rk_2():
    """This test function tests for the case where the ball starts at rest in the potential well at
    x = 0, with no driving force and no damping constant.  We expect the ball to stay at x = 0 indefinitely."""

    # Setting the known end value
    desired = 0
    # Implementing the function
    t,x,y = df.rk(a = 0, b = 2, x0 = 0, y0 = 0, nu = 0, F = 0)
    actual = x[len(x)-1]
    # Debug message
    print("We expected x = ",desired,", but we got ",actual)
    # Asserting the values
    nose.tools.assert_almost_equal(desired,actual,4)

def test_rk_3():
    """This test function tests for the case where the ball starts at x = -0.1 with initial velocity
    y = -0.2, driving force amplitude F = 0.01, and damping coefficient nu = 10.  In this case, we expect the
    damping force to dominate, and the ball to end up at rest in the left potential well at x = -1."""

    # Setting the known end value
    desired = -1
    # Implementing the function
    t,x,y = df.rk(a = 0, b = 10, x0 = -0.1, y0 = -0.2, nu = 10, F = 0.01)
    actual = x[len(x)-1]
    # Debug message
    print("We expected x = ",desired,", but we got ",actual)
    # Asserting the values
    nose.tools.assert_almost_equal(desired,actual,3)