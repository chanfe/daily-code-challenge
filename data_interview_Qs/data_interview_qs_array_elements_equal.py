# Checking whether array elements can be made equal
# Python Data Structures Arrays
# Given an array a, write a function to feed in the array elements and check whether they can all be made equal by only multiplying the numbers by 2 or 7. (you can multiply by these #s as many times as you like)

# If all elements can be made equal, return False, otherwise return True.

# Example:

#Input
a = [128, 4, 2]

#Here, we can turn all elements into 128, by multiplying by 2
#128, 4*2*2*2*2*2 = 128, 2*2*2*2*2*2*2 = 128

#Output:
#True

#Input
a = [65, 4, 2]
#Here, we cannot make all elements equal through multiplication by 2 or 7, 
#so we return false

#Output:
#False

import unittest

def are_equal(arr):
    for i in arr:
        if not helper(i):
            return False
    return True
        
def helper(num):
    if num // 2 == 1 or num // 7 == 1 or num == 0:
        return True
    
    if num < 0:
        return False

    if num % 2 == 0:
        return helper(num/2)

    if num % 7 == 0:
        return helper(num/7)
    
    return False

class TestStringMethods(unittest.TestCase):

    def test_helper(self):
        self.assertTrue(helper(0))
        self.assertTrue(helper(2))
        self.assertTrue(helper(7))
        self.assertTrue(helper(16))
        self.assertTrue(helper(343))
        self.assertTrue(helper(14))
        self.assertTrue(helper(28))
        self.assertFalse(helper(30))

    def test_are_equal(self):
        self.assertTrue(are_equal([128, 4, 2]))
        self.assertFalse(are_equal([65, 4, 2]))


if __name__ == '__main__':
    unittest.main()