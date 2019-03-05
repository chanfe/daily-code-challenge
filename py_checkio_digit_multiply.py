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
    answer = 1
    if number < 10:
        return number
    while number != 0:
        if number % 10 != 0:
            answer = answer * (number % 10)
        number = number // 10
    return answer

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
