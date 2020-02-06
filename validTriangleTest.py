import unittest
from validTriangle import triangleType  
 
class TriangleTypeTest(unittest.TestCase):
    def testEquilateral(self):
        triangle = triangleType(6, 6, 6)
        self.assertEquals(triangle, 'Equilateral Triangle')
 
    def testIsosceles(self):
        triangle = triangleType(6, 6, 5)
        self.assertEquals(triangle, 'Isoceles Triangle')

        triangle = triangleType(5, 6, 5)
        self.assertEquals(triangle, 'Isoceles Triangle')

        triangle = triangleType(6, 5, 5)
        self.assertEquals(triangle, 'Isoceles Triangle')

    def testScalene(self):
        triangle = triangleType(4, 5, 6)
        self.assertEquals(triangle, 'Scalene Triangle')

    def testInvalid(self):
        # Use the triangle inequality theorem
        # x >= (y + z) ==> !triangle
        # y >= (x + z) ==> !triangle
        # z >= (x + y) ==> !triangle
        
        triangle = triangleType(10,2,2)
        self.assertEquals(triangle, 'Invalid Triangle')

        triangle = triangletype(2,5,2)
        self.assertEquals(triangle, 'Invalid Triangle')

        triangle = triangletype(2,2,5)
        self.assertEquals(triangle, 'Invalid Triangle')

    def testError(self):
        # Triangle sides should be in (0,10]
        
        with self.assertRaises(ValueError):
            triangleType(25,19,25)

        with self.assertRaises(ValueError):
            triangleType(19,25,25)

        with self.assertRaises(ValueError):
            triangleType(25,25,19)

        with self.assertRaises(ValueError):
            triangleType(-1,5,5)

        with self.assertRaises(ValueError):
            triangleType(5,-1,5)

        with self.assertRaises(ValueError):
            triangleType(5,5,-1)

        with self.assertRaises(ValueError):
            triangleType(0,5,5)

        with self.assertRaises(ValueError):
            triangleType(5,0,5)

        with self.assertRaises(ValueError):
            triangleType(5,5,0)

if __name__ == '__main__':
    unittest.main()
