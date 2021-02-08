# On the chest keypad is a grid of numbered dots. The grid is comprised of a square shaped array of dots and contains lines that connect some pairs of adjacent dots. The answer to the code is the number of squares that are formed by these lines. For example, in the figure shown below, there are 3 squares: 2 small squares and 1 medium square.
#
# The dots are marked by the numbers 1 through 16. The endpoints of the lines are represented by lists of two numbers.
#
# Input: A list of lines as a list of list. Each list consists of the two integers.
#
# Output: The quantity of squares formed as an integer.
#
# Example:
#
# checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
#      [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
#      [10, 14], [12, 16], [14, 15], [15, 16]]) == 3
# checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
#      [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
#      [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2
#
# How it is used: This is a simple puzzle that illustrates pattern searching. For complex cases you can improve your program and use it to search for more complex patterns, shapes and objects.
#
# Precondition:
# 0 < len(lines) ≤ 32

def checkio(lines_list):
    """Return the quantity of squares"""
    MAX = 16
    size = 1
    pos = 1
    bol = True
    answer = 0
    for i in lines_list:
        i.sort()
    while size <=3:
        for i in range(size):
            if not ([pos+i, pos+i+1] in lines_list and
            [pos+i*4, pos+i*4+4] in lines_list and
            [pos+size+i*4, pos+size+4+i*4] in lines_list and
            [pos+size*4+i, pos+size*4+i+1] in lines_list):
                bol = False
        if bol == True:
            answer += 1
        else:
            bol = True

        pos += 1
        if pos+4*size+size > MAX:
            size += 1
            pos = 1
    return answer


if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                    [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
    assert (checkio([[16,15],[16,12],[15,11],[11,12],[11,10],[10,14],[9,10],[14,13],[13,9],[15,14]]) == 3), "kaka"
