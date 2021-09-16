import unittest     # this makes Python unittest module available
from ClassifyTriangle import classify_triangle

def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classify_triangle(',a, ',', b, ',', c, ')=',classify_triangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    def testSet1(self): 
        self.assertEqual(classify_triangle(3,4,5),'This is a right Scalene triangle.','3,4,5 is a Right Scalene triangle')
        self.assertNotEqual(classify_triangle(1, 1, 2), 'This is a right Isosceles triangle.', 'This is not a right triangle but an Isosceles Triangle')
        
    def testMyTestSet2(self): 
        self.assertEqual(classify_triangle(1,1,1),'This is an Equilateral triangle without a right angle.','1,1,1 should be equilateral')
        self.assertNotEqual(classify_triangle(10,10,10),'This is an Isosceles triangle without a right angle.','Should be Equilateral')
        self.assertEqual(classify_triangle(10,15,30),'This is a Scalene triangle without a right angle.','Should be Isoceles')
        
        

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(5,12,13)
    runClassifyTriangle(2,2,5)
    
    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
