# Suppose you're given a matrix of 1s and 0s that represents a map of rivers. You can assume that the grid cells in your map are only connected horizontally and vertically (e.g. no diagonal connections). You can assume that 1 represents water (your river) and 0 represents land/your river bank. Each cell has a length of 1 and is square in your map. Given this, write code to determine the perimeter of your river.

# Examples:

# Input: [[1,0]] 
# Output: 4

# Input: [[1,0,1],
#         [1,1,1]] 
# Output: 12

def checkio(river):
    answer = 0
    for i in range(len(river)):
        for j in range(len(river[i])):
            print(i,j)
            if river[i][j] == 1:
                answer += 4
                try:
                    print(i,j,river[i][j+1])
                    if river[i][j+1] == 1:
                        answer -= 1
                except:
                    pass
                print(answer)
                try:
                    print(i,j,river[i][j-1])
                    if river[i][j-1] == 1:
                        answer -= 1
                except:
                    pass
                print(answer)
                try:
                    print(i,j,river[i+1][j])
                    if river[i+1][j] == 1:
                        answer -= 1
                except:
                    pass
                print(answer)
                try:
                    print(i,j,river[i-1][j])
                    if river[i-1][j] == 1:
                        answer -= 1
                except:
                    pass
                print(answer)
            
    return answer


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[1,0]]) == 4
    assert checkio([[1,1],[1,1]]) == 8
    assert checkio([[1,0,1],[1,1,1]]) == 12
    assert checkio([[0]]) == 0
    assert checkio([[1]]) == 4
    assert checkio([[0,1,0]]) == 4
    
