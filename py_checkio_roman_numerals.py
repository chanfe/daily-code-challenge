# Roman numerals come from the ancient Roman numbering system. They are based on specific letters of the alphabet which are combined to signify the sum (or, in some cases, the difference) of their values. The first ten Roman numerals are:
#
# I, II, III, IV, V, VI, VII, VIII, IX, and X.
#
# The Roman numeral system is decimal based but not directly positional and does not include a zero. Roman numerals are based on combinations of these seven symbols:
#
# Numeral	Value
# I	1 (unus)
# V	5 (quinque)
# X	10 (decem)
# L	50 (quinquaginta)
# C	100 (centum)
# D	500 (quingenti)
# M	1,000 (mille)
# More additional information about roman numerals can be found on the Wikipedia article.
#
# For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.
#
# Input: A number as an integer.
#
# Output: The Roman numeral as a string.
#
# Example:
#
# checkio(6) == 'VI'
# checkio(76) == 'LXXVI'
# checkio(13) == 'XIII'
# checkio(44) == 'XLIV'
# checkio(3999) == 'MMMCMXCIX'
# How it is used: This is an educational task that allows you to explore different numbering systems. Since roman numerals are often used in the typography, it can alternatively be used for text generation. The year of construction on building faces and cornerstones is most often written by Roman numerals. These numerals have many other uses in the modern world and you read about it here... Or maybe you will have a customer from Ancient Rome ;-)
#
# Precondition: 0 < number < 4000

def checkio(data):
    #my_dict.keys()[0]     -> key of "first" element
    #my_dict.values()[0]   -> value of "first" element
    #my_dict.items()[0]    -> (key, value) tuple of "first" element

    remainding_number = data
    test = {1000 : 'M', 900 : 'CM', 500 : 'D', 400 : 'CD', 100 : 'C', 90 : 'XC', 50 : 'L', 40 : 'XL', 10 : 'X', 9 : 'IX', 5 : 'V', 4 : 'IV', 1 : 'I'}
    roman_numeral = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    answer = ""
    count = 0
    while (remainding_number != 0):
        num_times = (remainding_number // roman_numeral[count])
        for x in range(num_times):
            answer = answer + test[roman_numeral[count]]
        remainding_number = remainding_number % roman_numeral[count]
        count = count + 1

    return answer

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
