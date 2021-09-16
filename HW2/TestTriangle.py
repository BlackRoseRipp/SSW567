# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):
        self.assertNotEqual(classifyTriangle(5,5,9),'Equilateral','5,5,9 should not be equilateral')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Scalene','3,4,5 should be scalene')

    def testScaleneTriangleB(self):
        self.assertNotEqual(classifyTriangle(3,4,3),'Scalene','3,4,3 should not be scalene')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,3),'Isosceles','3,4,3 should be isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(3,3,5),'Isosceles','3,4,3 should be isosceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

