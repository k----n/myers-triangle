import unittest
from validTriangle import triangleType  
 
class TriangleTypeTest(unittest.TestCase):
    def testEquilateral(self):
        triangle = triangleType(5, 5, 5)
        self.assertEquals(triangle, 'Equilateral Triangle')
 
    def testIsosceles(self):
        #Call to your function to test a valid Isosceles Triangle
 
    def testScalene(self):
        #Call to your function to test a valid Scalene Triangle 

    def testInvalidIsoceles(self):
        triangle = triangleType(3, 3, 10)
        self.assertEquals(triangle, 'Invalid Triangle')
 
    def testInvalidScalene(self):
        #Call to your function to test an invalid Scalene Triangle = triangleType(4, 5, 8)

if __name__ == '__main__':
    unittest.main()