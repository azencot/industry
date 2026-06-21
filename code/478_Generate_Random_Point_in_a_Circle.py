# Given the radius and the position of the center of a circle, implement the function randPoint which generates a uniform random point inside the circle.

# Implement the Solution class:

# Solution(double radius, double x_center, double y_center) initializes the object with the radius of the circle radius and the position of the center (x_center, y_center).
# randPoint() returns a random point inside the circle. A point on the circumference of the circle is considered to be in the circle. The answer is returned as an array [x, y].
import random 
import math

class Solution(object):
    # idea: trick is based on polar coordinates (x, y) = (r * cos(theta), r * sin(theta))
    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center


    def randPoint(self):
        """
        :rtype: List[float]
        """
        r = math.sqrt(random.uniform(0, 1)) * self.radius
        theta = random.uniform(0, 2 * math.pi)

        x0, y0 = r * math.cos(theta), r * math.sin(theta)

        return [self.x_center + x0, self.y_center + y0]
        
