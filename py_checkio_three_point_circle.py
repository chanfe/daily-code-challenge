# Nicola discovered a calliper inside a set of drafting tools he received as a gift. Seeing the caliper, he has decided to learn how to use it.
#
# Through any three points that do not exist on the same line, there lies a unique circle. The points of this circle are represented in a string with the coordinates like so:
#
#     "(x1,y1),(x2,y2),(x3,y3)"
#
# Where x1,y1,x2,y2,x3,y3 are digits.
#
# You should find the circle for three given points, such that the circle lies through these point and return the result as a string with the equation of the circle. In a Cartesian coordinate system (with an X and Y axis), the circle with central coordinates of (x0,y0) and radius of r can be described with the following equation:
#
#     "(x-x0)^2+(y-y0)^2=r^2"
#
# where x0,y0,r are decimal numbers rounded to two decimal points. Remove extraneous zeros and all decimal points, they are not necessary. For rounding, use the standard mathematical rules.
#
# three_points_circle
# Input: Coordinates as a string..
#
# Output: The equation of the circle as a string.
#
# Example:
#
# checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
# checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
#
# How it is used: This equation, also known as Equation of the Circle, comes from the Pythagorean theorem when applied to any point on a circle: the radius is the hypotenuse of a right-angled triangle whose other sides are of length x − a and y − b. Of course you can use this concept for you mathematics software, but we just want to remind about how awesome circles are.
#
# Precondition: All three given points do not lie on one line.
# 0 < xi, yi, r < 10
import math
import re
def checkio(data):

    #replace this for solution
    coornate = data.split(',')
    x1 = float(coornate[0].strip('()'))
    y1 = float(coornate[1].strip('()'))
    x2 = float(coornate[2].strip('()'))
    y2 = float(coornate[3].strip('()'))
    x3 = float(coornate[4].strip('()'))
    y3 = float(coornate[5].strip('()'))
    try:
        ma = (y2 - y1) / (x2 - x1)
        mb = (y3 - y2) / (x3 - x2)
    except:
        x1 = float(coornate[2].strip('()'))
        y1 = float(coornate[3].strip('()'))
        x2 = float(coornate[4].strip('()'))
        y2 = float(coornate[5].strip('()'))
        x3 = float(coornate[0].strip('()'))
        y3 = float(coornate[1].strip('()'))
        try:
            ma = (y2 - y1) / (x2 - x1)
            mb = (y3 - y2) / (x3 - x2)
        except:
            x1 = float(coornate[4].strip('()'))
            y1 = float(coornate[5].strip('()'))
            x2 = float(coornate[0].strip('()'))
            y2 = float(coornate[1].strip('()'))
            x3 = float(coornate[2].strip('()'))
            y3 = float(coornate[3].strip('()'))
            ma = (y2 - y1) / (x2 - x1)
            mb = (y3 - y2) / (x3 - x2)

    x = (ma*mb*(y1 - y3) + mb*(x1 + x2) - ma*(x2 + x3)) / (2*(mb - ma))
    try:
        y = (-(1/mb)) * (x-(x2 + x3)/2) + (y2 + y3)/2
    except:
        y = (-(1/ma)) * (x-(x1 + x2)/2) + (y1 + y2)/2
    r = math.sqrt((x - x1)**2 + (y - y1)**2)
    return "(x-" + '{0:g}'.format(round(x, 2)) + ")^2+(y-" + '{0:g}'.format(round(y, 2)) + ")^2=" + '{0:g}'.format(round(r, 2)) + "^2"

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
