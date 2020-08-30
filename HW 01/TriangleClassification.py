import unittest

def classify_triangle(a, b, c):
    if (a == b  and b == c and a == c):
        return 'Equilateral'
    elif (a == b or a == c or b == c):
        return "Isosceles"
    elif (a != b and a != c and b != c):
        #will  lead to  errors b/c not  all unequal 3 sided objects make a triangle
        return 'Scalene'
    elif (a**2 + b**2 == c**2):
        #will never be identified b/c isosceles and scalene are identified first
        return 'Right Triangle'
    else:
        #will never be identified b/c scalene is identified before validating triangle
        return  'Not a Triangle'

def runClassifyTraingle(a, b, c):
    print('classify_triangle(',a, ',', b, ',', c, ') = ',classify_triangle(a,b,c),sep="")



class TestClassifyTriangle(unittest.TestCase):
    def testEquilateral(self):
        self.assertEqual(classify_triangle(3,3,3),'Equilateral','3,3,3 is a Equilateral Triangle')
        self.assertNotEqual(classify_triangle(0, 0, 0),'Equilateral','0, 0, 0 is Not a Triangle')
        self.assertEqual(classify_triangle(5, 5, 5),'Equilateral','5, 5, 5 is a Equilateral triangle')
        self.assertEqual(classify_triangle(100, 100, 100),'Equilateral','100, 100, 100 is a Equilateral triangle')
    def testIsosceles(self):
        self.assertEqual(classify_triangle(5, 5, 9),'Isosceles','5, 5, 9 is a Isosceles Triangle')
        self.assertNotEqual(classify_triangle(5, 5, 100),'Isosceles','5,  5, 100 is Not a Triangle')
        self.assertEqual(classify_triangle(20, 20, 10),'Isosceles','20, 20, 10 is a Isosceles triangle')
        self.assertEqual(classify_triangle(100, 100, 50),'Isosceles','100, 100, 50 is a Isosceles triangle')
    def testScalene(self):
        self.assertEqual(classify_triangle(7, 8, 13),'Scalene','7, 8, 13 is a Scalene Triangle')
        self.assertNotEqual(classify_triangle(9, 10, 91),'Scalene','9, 10, 91 is Not a Triangle')
        self.assertEqual(classify_triangle(10, 15, 20),'Scalene','10, 15, 20 is a Scalene triangle')
        self.assertEqual(classify_triangle(9, 13, 14),'Scalene','9, 13, 14 is a Scalene triangle')
    def testRight(self):
        self.assertEqual(classify_triangle(3, 4, 5),'Right','3, 4, 5 is a Right Triangle')
        self.assertNotEqual(classify_triangle(5, 7, 30),'Right','5, 7, 30 is Not a Triangle')
        self.assertEqual(classify_triangle(6, 8, 10),'Right','6, 8, 10 is a Right triangle')
        self.assertEqual(classify_triangle(12, 16, 20),'Right','12, 16, 20 is a Right triangle')
    def testNoTriangle(self):
        self.assertEqual(classify_triangle(3, 3, 20),'Not a Triangle','3, 4, 5 is a Not a Triangle Triangle')
        self.assertNotEqual(classify_triangle(8, 15, 17),'Not a Triangle','5, 7, 30 is Right Triangle')
        self.assertEqual(classify_triangle(15, 14, 49),'Not a Triangle','6, 8, 10 is a Not a Triangle triangle')
        self.assertEqual(classify_triangle(49, 50, 1000),'Not a Triangle','12, 16, 20 is a Not a Triangle triangle')


if __name__ == '__main__':
    unittest.main(exit  = False)
