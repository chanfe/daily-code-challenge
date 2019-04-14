# There are four substring missions that were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
#
# A very similar to the first is the second mission of the series with only one distinction is that you should look in a completely different way. You need to find the first longest substring with all unique letters. For example, in substring "abca" we have two substrings with unique letters "abc" and "bca", but we should take the first one, so the answer is "abc".
#
# Input: String.
#
# Output: String.
#
# Example:
#
# non_repeat('aaaaa') == 'a'
# non_repeat('abdjwawk') == 'abdjw'
# non_repeat('abcabcffab') == 'abcf'

from collections import deque
def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    # your code here
    queue = deque()
    temp = ""
    answer = ""
    for i in line:
        print(queue, i)
        if i in queue:
            while True:
                if queue.popleft() == i:
                    break
            queue.append(i)
        else:
            queue.append(i)

        for j in queue:
                temp += j

        if len(temp) > len(answer):
            answer = temp[:]
        temp = ""
    return answer

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')
