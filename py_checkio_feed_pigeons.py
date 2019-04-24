# I start to feed one of the pigeons. A minute later two more fly by and a minute after that another 3. Then 4, and so on (Ex: 1+2+3+4+...). One portion of food lasts a pigeon for a minute, but in case there's not enough food for all the birds, the pigeons who arrived first ate first. Pigeons are hungry animals and eat without knowing when to stop. If I have N portions of bird feed, how many pigeons will be fed with at least one portion of wheat?
#
# pigeons
# Input: A quantity of portions wheat as a positive integer.
#
# Output: The number of fed pigeons as an integer.
#
# Example:
#
# checkio(1) == 1
# checkio(2) == 1
# checkio(5) == 3
# checkio(10) == 6
#
# How it is used: This task illustrates how we can model various situations. Of course, the model has a limited approximation, but often-times we don't need a perfect model.
#
# Precondition: 0 < N < 105.


def checkio(number):
    num_bird_list = [0]

    while True:
        for i in range(len(num_bird_list)):
            if number > 0:
                number -= 1
                num_bird_list[i] += 1
            else:
                return sum(x > 0 for x in num_bird_list)

        for i in range(num_bird_list[0]+1):
            num_bird_list.append(0)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
