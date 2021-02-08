# You have a histogram. Try to find size of the biggest rectangle you can build out of the histogram bars.
#
#
#
# Input: List of all rectangles heights in histogram
#
# Output: Area of the biggest rectangle
#
# Example:
#
# largest_histogram([5]) == 5
# largest_histogram([5, 3]) == 6
# largest_histogram([1, 1, 4, 1]) == 4
# largest_histogram([1, 1, 3, 1]) == 4
# largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8
# 1
# 2
# 3
# 4
# 5
# How it is used: There is no way the solution you come up with will be any useful in a real life. Just have some fun here.
#
# Precondition:
# 0 < len(data) < 1000

def largest_histogram(histogram):
    max_length = len(histogram)
    num_couple = 1
    largest = 0
    while True:
        for i in range(max_length):
            if i + num_couple > max_length:
                break

            newlist = histogram[i:i + num_couple]
            if (min(newlist)*num_couple) > largest:
                largest = min(newlist)*num_couple
        if num_couple >= max_length:
            return largest
        else:
            num_couple += 1

    return max(histogram)


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
