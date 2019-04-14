# From a set of ints you have to create a list of closed intervals as tuples, so the intervals are covering all the values found in the set.
#
# A closed interval includes its endpoints! The interval 1..5, for example, includes each value x that satifies the condition 1 <= x <= 5.
#
# Values can only be in the same interval if the difference between a value and the next smaller value in the set equals one, otherwise a new interval begins. Of course, the start value of an interval is excluded from this rule.
# A single value, that does not fit into an existing interval becomes the start- and endpoint of a new interval.
#
# Input: A set of ints.
#
# Output: A list of tuples of two ints, indicating the endpoints of the interval. The Array should be sorted by start point of each interval
#
# Examples:
#
# create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)]
# create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)]

def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    # your code here
    interval = []
    if not data:
        return interval
    counter = 0
    min_start = min(data)
    largest_int = min_start
    while(data):
        if (min_start + counter) in data:
            largest_int = min_start + counter
            data.remove(largest_int)
            if not data:
                interval.append((min_start, largest_int))
            counter += 1
        else:
            interval.append((min_start, largest_int))
            min_start = min(data)
            largest_int = min_start
            counter = 0
    return interval

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
