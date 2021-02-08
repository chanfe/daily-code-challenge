# In mathematics, particularly in linear algebra, a skew-symmetric matrix(also known as an antisymmetric or antimetric) is a square matrix A whose transpose is also its negative. This means it satisfies the equation A = −AT. If the entry in the i-th row and j-th column is aij, i.e. A = (aij) then the symmetric condition becomes aij = −aji.
#
# You should determine whether the specified square matrix is skew-symmetric or not.
#
# You can find more details on Skew-symmetric matrices on its Wikipedia page.
#
# Input: A square matrix as a list of lists with integers.
#
# Output: If the matrix is skew-symmetric or not as a boolean.
#
# Example:
#
# checkio([
#     [ 0,  1,  2],
#     [-1,  0,  1],
#     [-2, -1,  0]]) == True
# checkio([
#     [ 0,  1, 2],
#     [-1,  1, 1],
#     [-2, -1, 0]]) == False
# checkio([
#     [ 0,  1, 2],
#     [-1,  0, 1],
#     [-3, -1, 0]]) == False
#
# How it is used: Skew-symmetric matrices can be useful for the cross product, an operation in mathematics used in the calculation of movement of forces. Matrixes are basis for the linear algebra and vector graphics.
#
# Precondition: 0 < N < 5

def checkio(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != -matrix[j][i]:
                return False
    return True


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
