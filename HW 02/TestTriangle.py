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

    def testRightTriangle1(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle') 

    def testRightTriangle2(self): 
        self.assertEqual(classifyTriangle(6,8,10),'Right','6,8,10 is a Right triangle')
    
    def testRightTriangle3(self): 
        self.assertEqual(classifyTriangle(12, 16, 20),'Right','12, 16, 20 is a Right triangle')
    
    def testRightTriangle4(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    
    def testRightTriangle5(self): 
        self.assertEqual(classifyTriangle(4,3,5),'Right','4,3,5 is a Right triangle')
        
    def testIsoscelesTriangle1(self): 
        self.assertEqual(classifyTriangle(5,5,9),'Isosceles','5,5,9 is a Isosceles triangle')

    def testIsoscelesTriangle2(self): 
        self.assertEqual(classifyTriangle(5,9,5),'Isosceles','5,9,5 is a Isosceles triangle')
    
    def testIsoscelesTriangle3(self): 
        self.assertEqual(classifyTriangle(9,5,5),'Isosceles','9,5,5 is a Isosceles triangle')

    def testIsoscelesTriangle4(self):  
        self.assertEqual(classifyTriangle(6,6,8),'Isosceles','6,6,8 is a Isosceles triangle')
    
    def testIsoscelesTriangle5(self): 
        self.assertEqual(classifyTriangle(40,56,56),'Isosceles','40,56,56 is a Isosceles triangle')
    
    def testIsoscelesTriangle6(self): 
        self.assertEqual(classifyTriangle(33,25,33),'Isosceles','33,25,33 is a Isosceles triangle')
        
    def testEquilateralTriangle1(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is a equilateral triangle')

    def testEquilateralTriangle2(self): 
        self.assertEqual(classifyTriangle(33,33,33),'Equilateral','33,33,33 is a equilateral triangle')
    
    def testScaleneTriangle1(self):
        self.assertEqual(classifyTriangle(4,2,5),'Scalene','4,2,5 is a scalene triangle')

    def testScaleneTriangle2(self):
        self.assertEqual(classifyTriangle(2,4,5),'Scalene','2,4,5 is a scalene triangle')

    def testScaleneTriangle3(self):
        self.assertEqual(classifyTriangle(130,187,200),'Scalene','137,187,200 is a scalene triangle')

    def testInvalidInput1(self):
        self.assertEqual(classifyTriangle(-3,3,4),'InvalidInput','-3,3,4 is an invalid input')

    def testInvalidInput2(self):
        self.assertEqual(classifyTriangle(-3,-3,4),'InvalidInput','-3,-3,4 is an invalid input')

    def testInvalidInput3(self):
        self.assertEqual(classifyTriangle(-3,-3,-4),'InvalidInput','-3,-3,-4 is an invalid input')

    def testInvalidInput4(self):
        self.assertEqual(classifyTriangle(3,-3,4),'InvalidInput','3,-3,4 is an invalid input')

    def testInvalidInput5(self):
        self.assertEqual(classifyTriangle(3,3,-4),'InvalidInput','3,3,-4 is an invalid input')

    def testInvalidInput6(self):
        self.assertEqual(classifyTriangle(0,3,4),'InvalidInput','0,3,10 is an invalid input')

    def testInvalidInput7(self):
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','0,0,0 is an invalid input')

    def testInvalidInput8(self):
        self.assertEqual(classifyTriangle(0,0,10),'InvalidInput','0,0,10 is an invalid input')

    def testInvalidInput9(self):
        self.assertEqual(classifyTriangle(199, 201, 100),'InvalidInput','199,201,100 is an invalid input')

    def testInvalidInput10(self):
        self.assertEqual(classifyTriangle(385, 385, 385),'InvalidInput','385,385,385 is an invalid input')
    
    def testInvalidInput11(self):
        self.assertEqual(classifyTriangle(3.5, 3.5, 3.5),'InvalidInput','385,385,385 is an invalid input')
    
    def testNotATriangle1(self):
        self.assertEqual(classifyTriangle(30, 70, 150), 'NotATriangle', '30, 70, 150 is not a triangle')

    def testNotATriangle2(self):
        self.assertEqual(classifyTriangle(70, 30, 150), 'NotATriangle', '70, 30, 150 is not a triangle')

    def testNotATriangle3(self):
        self.assertEqual(classifyTriangle(150, 30, 70), 'NotATriangle', '150, 30, 70 is not a triangle')

    def testNotATriangle4(self):
        self.assertEqual(classifyTriangle(5, 7, 30), 'NotATriangle', '5, 7, 30 is not a triangle')

    def testNotATriangle5(self):
        self.assertEqual(classifyTriangle(3, 3, 99), 'NotATriangle', '3, 3, 99 is not a triangle')

    def testNotATriangle6(self):
        self.assertEqual(classifyTriangle(3, 7, 99), 'NotATriangle', '3, 7, 99 is not a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

