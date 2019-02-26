# "Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.
#
# You should write a function that will receive a positive integer and return:
# "Fizz Buzz" if the number is divisible by 3 and by 5;
# "Fizz" if the number is divisible by 3;
# "Buzz" if the number is divisible by 5;
# The number as a string for other cases.
# Input: A number as an integer.
#
# Output: The answer as a string.
#
# Example:
#
# checkio(15) == "Fizz Buzz"
# checkio(6) == "Fizz"
# checkio(5) == "Buzz"
# checkio(7) == "7"
#
# How it is used: Here you can learn how to write the simplest function and work with if-else statements.
#
# Precondition: 0 < number ≤ 1000

def checkio(number):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.
    answer = ""
    #replace this for solution
    if (number % 3 == 0 and number % 5 == 0):
        answer = "Fizz Buzz"
    elif number % 3 == 0:
        answer = "Fizz"
    elif number % 5 == 0:
        answer = "Buzz"
    else:
        answer = str(number)
    return answer

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
